# Reproduce the finite checks

The analytical results are proved in `science/`. These scripts check exact finite identities and reconstruct explicit accepted channels, including logical coherences. They do not search for globally optimal finite encoders or replace the asymptotic proofs.

## Environment and commands

The recorded `results.json` run used Python 3.13.5, NumPy 2.3.5, and SciPy 1.17.0. Install the pinned numerical packages from the repository root:

```bash
python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verification/run_all.py
python verification/check_structure.py
python verification/check_learning.py
```

A fresh main-suite JSON report can be written without replacing the reference report:

```bash
python verification/run_all.py --output /tmp/covariant-erasure-yield-results.json
```

`results.json` is a recorded run, not evidence that the current checkout has just been executed. GitHub Actions runs all three scripts on pull requests and main. Thread limits reduce avoidable overhead for these small dense matrices. The structural script uses only Python's standard library.

## What is checked

**Exact combinatorics.** Rational arithmetic verifies normalization and the adjacent-hypergeometric total-variation identity for every $2\le n\le29$, every $1\le k\le n$, and every $0\le w<n$: 8,554 cases. Integer arithmetic checks the uniform row-to-column surplus for 5,950 charge blocks through odd $n=61$, together with the conserving-garbage embedding dimensions. The finite $n=11,k=3$ offset example is also checked exactly.

**Complete finite channels.** For one seeded random code at each $(n,k)=(7,1),(9,2),(11,3)$, the main script checks every erased subset: 7, 36, and 165 patterns respectively, 208 in total. It builds the physical erasure Kraus matrices and the accepted recovery Kraus matrices, then compares their composite Choi matrix to $p|I\rangle\!\rangle\langle\!\langle I|$. It also checks isometric encoding, the inverse-filter identity, contractivity, charge intertwining, and the environmental trace-distance converse.

These finite decoders use the observed minimum eigenvalue of the relative Gram matrix, with a small numerical safety margin. They are feasible constructions, not semidefinite-program optima. The conservative all-size concentration bound is not expected to be informative at these small block lengths.

The recorded maximum accepted-channel entry residual was below $5\times10^{-16}$; the enforced main-suite tolerance is $2\times10^{-10}$. Small differences in floating-point outputs across supported platforms are expected. A tiny residual is numerical evidence for the specified finite matrix calculation, not exact-arithmetic certification of a random complex code.

**Asymptotic coefficient samples.** The exact modal formula is evaluated at loss fractions $0.1,0.25,0.4,0.49$ and block lengths 101, 1,001, and 10,001. These samples illustrate the proved coefficient and test normalization. They do not prove convergence or a uniform critical-window law.

**Learning map and worked example.** `check_learning.py` requires exactly M01–M30 in order, the 12/18 phase allocation, all five substantive fields, and only preceding milestone dependencies. It reconstructs the three-qubit example for all three single-erasure patterns, checks its full accepted Choi channel of probability $2/3$, the Gram spectrum, contractivity, input-independent failure, and number conservation. The equal-phase comparison checks both unchanged environmental basis-state blocks and the kernel that forces zero exact accepted yield. Its floating-point tolerance is $2\times10^{-12}$. The analytic finite-optimality argument is in the [worked example](../learning/WORKED_EXAMPLE.md); the matrices do not establish the general asymptotic theorem. Use `--examples-only` to run only these matrix checks without inspecting a learning map.

**Structure.** `check_structure.py` checks required scientific files, all local Markdown links and heading anchors, and balanced fenced blocks, including the learning pages. It does not inspect the hosting renderer, external-site availability, or visual layout. Hosted mathematical review is a separate check and must not be inferred from a successful source or numerical test.
