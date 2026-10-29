#!/usr/bin/env python3
"""Finite checks for exact heralded covariant erasure recovery.

These tests check combinatorial identities and explicit finite channels.
They do not replace the all-n proof or establish efficient implementation.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
import json
from math import comb, pi, sqrt
from pathlib import Path
import platform

import numpy as np
from scipy.stats import hypergeom
import scipy


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def exact_law(n: int, w: int, k: int) -> list[Fraction]:
    """Erased-charge law for a uniformly sampled k-subset."""
    return [Fraction(choose(k, a) * choose(n-k, w-a), choose(n, w))
            for a in range(k+1)]


def tv(p: list[Fraction], q: list[Fraction]) -> Fraction:
    return sum((abs(a-b) for a, b in zip(p, q)), Fraction()) / 2


def combinatorial_checks() -> dict:
    adjacent_cases = 0
    sector_cases = 0
    for n in range(2, 30):
        for k in range(1, n+1):
            for w in range(n):
                p, q = exact_law(n, w, k), exact_law(n, w+1, k)
                modal = max(Fraction(choose(w, a)*choose(n-1-w, k-1-a),
                                     choose(n-1, k-1)) for a in range(k))
                if sum(p) != 1 or sum(q) != 1 or tv(p, q) != Fraction(k, n)*modal:
                    raise AssertionError((n, w, k, 'adjacent law'))
                adjacent_cases += 1
    for n in range(3, 62, 2):
        w = (n-1)//2
        for k in range(w+1):
            N, r = n-k, w-k
            B = choose(2*r, r)
            for b in range(w-k, w+2):
                a = w-b
                ell = choose(k, a) + choose(k, a+1)
                if ell != choose(k+1, a+1) or choose(N, b) < B*ell:
                    raise AssertionError((n,k,b,'sector domination'))
                sector_cases += 1
            for a in range(k+1):
                if choose(N-1, w-a) < choose(k,a):
                    raise AssertionError((n,k,a,'number-conserving output embedding'))
    # Small-n modal oscillations prohibit claiming finite central-sector optimality.
    central = tv(exact_law(11,5,3), exact_law(11,6,3))
    offcentre = tv(exact_law(11,3,3), exact_law(11,4,3))
    if not offcentre < central:
        raise AssertionError('finite-size qualification disappeared')
    return {'adjacent_identity_cases': adjacent_cases,
            'all_sector_dimension_cases': sector_cases,
            'finite_size_counterexample': {'n':11,'k':3,
                 'central_TV': str(central), 'offset_3_TV': str(offcentre)}}


def sample_code(n: int, seed: int) -> np.ndarray:
    if n % 2 != 1:
        raise ValueError('This verifier samples the odd-n construction.')
    rng = np.random.default_rng(seed)
    weights = np.array([j.bit_count() for j in range(2**n)])
    V = np.zeros((2**n,2), dtype=complex)
    for i, charge in enumerate(((n-1)//2, (n+1)//2)):
        idx = np.flatnonzero(weights == charge)
        z = rng.normal(size=len(idx)) + 1j*rng.normal(size=len(idx))
        V[idx,i] = z/np.linalg.norm(z)
    return V


def synthesis(V: np.ndarray, n: int, erased: tuple[int,...]) -> np.ndarray:
    surviving = tuple(j for j in range(n) if j not in erased)
    dE, dB = 2**len(erased), 2**len(surviving)
    return np.concatenate([V[:,i].reshape((2,)*n).transpose(surviving+erased)
                           .reshape(dB,dE) for i in range(2)],axis=1)


def channel_check(V: np.ndarray, n: int, E: tuple[int,...]) -> dict[str,float]:
    k, w = len(E), (n-1)//2
    dE, dB = 2**k, 2**(n-k)
    T = synthesis(V,n,E)
    G = T.conj().T @ T
    chargeE = np.array([j.bit_count() for j in range(dE)])
    mean = np.array([[choose(n-k,w+i-int(a))/choose(n,w+i)
                      for a in chargeE] for i in range(2)])
    inv = 1/np.sqrt(mean.ravel())
    relative = inv[:,None]*G*inv[None,:]
    c = min(1.0,float(np.linalg.eigvalsh(relative)[0]))*(1-1e-10)
    if c <= 0:
        raise AssertionError('sampled synthesis is not full column rank')
    x = c*np.minimum(mean[0],mean[1])
    target = np.diag(np.tile(np.sqrt(x),2))
    D = target @ np.linalg.solve(G,T.conj().T)
    p = float(x.sum())
    # Reconstruct physical erasure Kraus matrices and recovery Kraus matrices.
    A = np.stack([np.column_stack((T[:,e],T[:,dE+e])) for e in range(dE)])
    K = np.stack([D[[a,dE+a],:] for a in range(dE)])
    logical_kraus = np.einsum('aob,ebi->aeoi',K,A)
    vectors = logical_kraus.reshape(-1,4)
    choi = vectors.T @ vectors.conj()
    vecI = np.eye(2).ravel()
    residual = float(np.max(np.abs(choi-p*np.outer(vecI,vecI))))
    largest = float(np.linalg.eigvalsh(D @ D.conj().T)[-1])
    qout = np.concatenate((w-chargeE,w+1-chargeE))
    qin = np.array([j.bit_count() for j in range(dB)])
    covariance = float(np.max(np.abs(qout[:,None]*D-D*qin[None,:])))
    inverse_residual = float(np.max(np.abs(D@T-target)))
    # Erased states are transposes of diagonal Gram blocks. Trace norm invariant.
    environment_tv = float(np.abs(np.linalg.eigvalsh(G[:dE,:dE]-G[dE:,dE:])).sum()/2)
    if residual > 2e-10 or inverse_residual > 2e-10 or covariance > 2e-10:
        raise AssertionError((n,E,'channel/covariance',residual,inverse_residual,covariance))
    if largest > 1+2e-10 or p > 1-environment_tv+2e-10:
        raise AssertionError((n,E,'contractivity/converse',largest,p,environment_tv))
    return {'success':p,'choi_residual':residual,'inverse_residual':inverse_residual,
            'covariance_residual':covariance,'contraction_norm_squared':largest,
            'environment_trace_distance':environment_tv}


def finite_channel_checks() -> list[dict]:
    output=[]
    for n,k,seed in ((7,1,20261029),(9,2,20261030),(11,3,20261031)):
        V=sample_code(n,seed)
        if np.max(np.abs(V.conj().T@V-np.eye(2)))>1e-12:
            raise AssertionError('not an isometry')
        rows=[channel_check(V,n,E) for E in combinations(range(n),k)]
        output.append({'n':n,'k':k,'seed':seed,'patterns':len(rows),
                       'minimum_certified_success': min(z['success'] for z in rows),
                       'maximum_choi_residual': max(z['choi_residual'] for z in rows),
                       'maximum_inverse_residual': max(z['inverse_residual'] for z in rows),
                       'maximum_covariance_residual': max(z['covariance_residual'] for z in rows),
                       'maximum_contraction_norm_squared':max(z['contraction_norm_squared'] for z in rows)})
    return output


def asymptotic_checks() -> list[dict]:
    rows=[]
    for alpha in (0.1,0.25,0.4,0.49):
        constant=sqrt(2*alpha/(pi*(1-alpha)))
        for n in (101,1001,10001):
            k=int(alpha*n)
            w=(n-1)//2
            mode=(k*(w+1))//(n+1)
            distance=(k/n)*hypergeom.pmf(mode,n-1,w,k-1)
            scaled=float(sqrt(n)*distance)
            if n==10001 and abs(scaled/constant-1)>0.003:
                raise AssertionError((n,k,'asymptotic coefficient',scaled,constant))
            rows.append({'alpha':alpha,'n':n,'k':k,'sqrt_n_TV':scaled,
                         'limiting_coefficient':constant})
    return rows


def run() -> dict:
    return {'status':'passed','scope':'finite identities and explicit channels; not a universal-proof certificate',
            'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
            'combinatorial':combinatorial_checks(),
            'finite_channels':finite_channel_checks(),
            'asymptotic_samples':asymptotic_checks()}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,help='write the fresh JSON result to this path')
    args=parser.parse_args()
    report=run()
    rendered=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(rendered,encoding='utf-8')
    print(rendered,end='')
