# Reproduce the finite checks

The analytical results are proved in `science/`. These scripts check exact finite identities and reconstruct explicit accepted channels, including logical coherences. They do not search for globally optimal finite encoders or replace the asymptotic proofs.

## Environment and commands

The recorded run used Python 3.13.5, NumPy 2.3.5, and SciPy 1.17.0. Install the pinned numerical packages from the repository root:

```bash
python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verification/run_all.py
python verification/check_structure.py
```

A fresh JSON report can be written without replacing the reference report:

```bash
python verification/run_all.py --output /tmp/covariant-erasure-yield-results.json
```

`results.json` is a recorded run, not evidence that the current checkout has just been executed. GitHub Actions runs both scripts on pull requests and main. Thread limits reduce avoidable overhead for these small dense matrices. The structural script uses only Python's standard library.

## What is checked

**Exact combinatorics.** Rational arithmetic verifies normalization and the adjacent-hypergeometric total-variation identity for every $2\le n\le29$, every $1\le k\le n$, and every $0\le w<n$: 8,554 cases. Integer arithmetic checks the uniform row-to-column surplus for 5,950 charge blocks through odd $n=61$, together with the conserving-garbage embedding dimensions. The finite $n=11,k=3$ offset example is also checked exactly.

**Complete finite channels.** For one seeded random code at each $(n,k)=(7,1),(9,2),(11,3)$, the script checks every erased subset: 7, 36, and 165 patterns respectively, 208 in total. It builds the physical erasure Kraus matrices and the accepted recovery Kraus matrices, then compares their composite Choi matrix to $p|I\rangle\!\rangle\langle\!\langle I|$. It also checks isometric encoding, the inverse-filter identity, contractivity, charge intertwining, and the environmental trace-distance converse.

These finite decoders use the observed minimum eigenvalue of the relative Gram matrix, with a small numerical safety margin. They are feasible constructions, not semidefinite-program optima. The conservative all-size concentration bound is not expected to be informative at these small block lengths.

The recorded maximum accepted-channel entry residual was below $5\times10^{-16}$; the enforced tolerance is $2\times10^{-10}$. Small differences in floating-point outputs across supported platforms are expected. A tiny residual is numerical evidence for the specified finite matrix calculation, not exact-arithmetic certification of a random complex code.

**Asymptotic coefficient samples.** The exact modal formula is evaluated at loss fractions $0.1,0.25,0.4,0.49$ and block lengths 101, 1,001, and 10,001. These samples illustrate the proved coefficient and test normalization. They do not prove convergence or a uniform critical-window law.

**Structure.** The second script checks required files, local Markdown links and heading anchors, and balanced fenced blocks. It does not inspect the hosting renderer, external-site availability, or visual layout. Hosted mathematical review belongs to the separate final furnishing check.
