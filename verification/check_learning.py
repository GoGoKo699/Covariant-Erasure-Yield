#!/usr/bin/env python3
"""Check the learning map and the complete three-qubit accepted channels.

Finite numerical checks support the worked example, not the asymptotic proof.
This script does not test GitHub's hosted mathematical rendering.
"""
from __future__ import annotations

import argparse
from itertools import combinations
import json
from pathlib import Path
import re

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
TOL = 2e-12


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_map(root: Path) -> dict:
    text = (root / 'learning/MILESTONES.md').read_text(encoding='utf-8')
    headings = list(re.finditer(r'^### M(\d{2}) (.+)$', text, re.M))
    require([int(h[1]) for h in headings] == list(range(1, 31)),
            'Expected exactly M01 through M30, in order.')
    phase1 = text.index('## Phase I: background and preliminaries')
    phase2 = text.index('## Phase II: narrative and innovation')
    require(phase1 < headings[0].start() and
            headings[11].start() < phase2 < headings[12].start(),
            'Expected 12 background and 18 narrative milestones.')
    labels = ('Central question.', 'Understanding target.',
              'Dependencies and story role.', 'Conceptual connection.',
              'Source pointers.')
    dependency_edges = 0
    for index, heading in enumerate(headings):
        end = headings[index+1].start() if index+1 < len(headings) else len(text)
        block = text[heading.end():end]
        for label in labels:
            require(block.count(f'**{label}**') == 1,
                    f'M{index+1:02d}: missing or repeated {label}')
        dep = block.split('**Dependencies and story role.**', 1)[1]
        dep = dep.split('**Conceptual connection.**', 1)[0]
        numbers = [int(x) for x in re.findall(r'\bM(\d{2})\b', dep)]
        require(all(1 <= number < index+1 for number in numbers),
                f'M{index+1:02d}: nonpreceding dependency')
        dependency_edges += len(numbers)
    for path in ('learning/WATROUS_BRIDGE.md', 'learning/WORKED_EXAMPLE.md'):
        require((root/path).is_file(), f'Missing {path}')
    return {'milestones': 30, 'background': 12, 'narrative': 18,
            'required_fields_per_milestone': len(labels),
            'preceding_dependency_edges': dependency_edges}


def synthesis(V: np.ndarray, erased: tuple[int, ...]) -> np.ndarray:
    survivors = tuple(j for j in range(3) if j not in erased)
    return np.concatenate([
        V[:,i].reshape((2,)*3).transpose(survivors+erased).reshape(4,2)
        for i in range(2)], axis=1)


def check_example() -> list[dict]:
    omega = np.exp(2j*np.pi/3)
    V = np.zeros((8,2), dtype=complex)
    V[[4,2,1],0] = 1/np.sqrt(3)
    V[[3,5,6],1] = np.array([1,omega,omega**2])/np.sqrt(3)
    symmetric = V.copy()
    symmetric[[3,5,6],1] = 1/np.sqrt(3)
    require(np.max(np.abs(V.conj().T@V-np.eye(2))) < TOL, 'Encoding isometry')
    charges = np.array([j.bit_count() for j in range(8)])
    require(np.max(np.abs(charges[:,None]*V-V*np.array([1,2]))) < TOL,
            'Encoding charge sectors')
    results = []
    for E in combinations(range(3),1):
        T = synthesis(V,E)
        G = T.conj().T@T
        require(np.max(np.abs(np.linalg.eigvalsh(G)-np.array([1/3]*3+[1]))) < TOL,
                f'{E}: Gram spectrum')
        D = np.linalg.solve(T,np.eye(4))/np.sqrt(3)
        A = [T[:,[e,2+e]] for e in range(2)]
        K = [D[[a,2+a],:] for a in range(2)]
        vectors = np.array([(ka@ae).ravel() for ka in K for ae in A])
        J = vectors.T@vectors.conj()
        vecI = np.eye(2).ravel()
        residual = float(np.max(np.abs(J-(2/3)*np.outer(vecI,vecI))))
        require(residual < TOL, f'{E}: complete accepted Choi channel')
        norm_squared = float(np.linalg.eigvalsh(D.conj().T@D)[-1])
        require(norm_squared <= 1+TOL, f'{E}: contractivity')
        qout, qin = np.array([1,0,2,1]), np.array([0,1,1,2])
        covariance = float(np.max(np.abs(qout[:,None]*D-D*qin[None,:])))
        require(covariance < TOL, f'{E}: charge intertwining')
        A_failure = np.eye(4)-D.conj().T@D
        require(np.linalg.eigvalsh(A_failure)[0] >= -TOL, f'{E}: failure positivity')
        effect = sum(ae.conj().T@A_failure@ae for ae in A)
        require(np.max(np.abs(effect-np.eye(2)/3)) < TOL,
                f'{E}: input-independent failure probability')
        T_plus = synthesis(symmetric,E)
        G_plus = T_plus.conj().T@T_plus
        kernel = np.array([1,0,0,-1])/np.sqrt(2)
        require(np.max(np.abs(G_plus@kernel)) < TOL, f'{E}: equal-phase kernel')
        require(np.max(np.abs(G[:2,:2]-G_plus[:2,:2])) < TOL and
                np.max(np.abs(G[2:,2:]-G_plus[2:,2:])) < TOL,
                f'{E}: unchanged environmental basis-state blocks')
        results.append({'erased_site_zero_based': E[0], 'success': 2/3,
                        'choi_entry_residual': residual,
                        'contraction_norm_squared': norm_squared,
                        'covariance_residual': covariance,
                        'equal_phase_obstruction': 'kernel verified'})
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--examples-only', action='store_true',
                        help='check only the matrices, without a repository learning map')
    args = parser.parse_args()
    report = {'status': 'passed', 'worked_example': check_example(),
              'scope': 'finite matrices and source structure, not hosted rendering or proof certification'}
    if not args.examples_only:
        report['learning_map'] = check_map(ROOT)
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
