# Covariant Erasure Yield

**How often can a continuously covariant quantum code recover exactly after losing an extensive number of physical qubits?**

One logical qubit is encoded isometrically into $n$ ordinary excitation-number qubits. Logical phase rotations are implemented by the same phase rotation on every physical qubit. The receiver knows which $k$ qubits were erased and may jointly process the survivors. Recovery announces success or failure; on success, the complete logical channel is exactly the identity, including on inputs entangled with an external reference.

For every fixed loss fraction $0<\alpha<1/2$, with $k=\lfloor\alpha n\rfloor$, the optimal worst-pattern failure probability is

```math
\boxed{
f^*_{n,k}=\sqrt{\frac{2\alpha}{\pi(1-\alpha)n}}+o(n^{-1/2}).
}
```

The optimization includes all charge offsets and all covariant **isometric** encoders. A single encoding attains the law simultaneously for every erased subset of size $k$. Both its encoder and its heralded decoder admit number-conserving implementations without an asymmetric reference. Their circuit complexity and locality are not optimized.

## What establishes the result

| Result | Meaning | Proof |
| --- | --- | --- |
| Exact fixed-encoder recovery criterion | A positive-semidefinite Gram-matrix condition constructs the accepted channel and its physical failure branch | [Exact recovery](science/exact_recovery.md) |
| Universal finite converse | Erased charge distinguishes adjacent logical sectors; averaging over positions gives an exact hypergeometric bound for every encoding | [Charge converse](science/charge_converse.md) |
| Simultaneous construction | Independent Haar codewords in adjacent central sectors satisfy a relative operator bound in **every** charge sector and for every erasure pattern | [Random construction](science/random_construction.md) |
| Optimal leading constant | Optimizing the converse over all charge offsets matches the construction, for odd and even block lengths | [Asymptotic optimum](science/asymptotic_optimum.md) |
| Conserving implementation | The accepted filter and its completion use a neutral flag and conserve excitation number | [Implementation](science/conserving_implementation.md) |

The general probabilistic-recovery conditions and random covariant encoding ensembles are established ingredients. Earlier work also proves the inverse-square-root law for approximate complementary-channel decoupling under extensive erasure. The result here concerns **exact accepted recovery at matched yield**, rather than a new encoding ensemble or a new decoupling exponent. The [source comparison](references/RELATED_WORK.md) makes that distinction explicit.

## Reading routes

Start with the [scientific overview](science/README.md) and [operational model](science/model.md). The proof route proceeds through the recovery criterion, charge converse, random construction, and asymptotic optimization. The [physical interpretation](science/interpretation.md) explains why a small approximate error alone does not guarantee any nonzero exact recovery probability.

For reproduction:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
python verification/check_structure.py
```

The [verification guide](verification/README.md) distinguishes exact combinatorial checks, floating-point channel calculations, and the general analytical arguments.

## Scope

The code stores one logical qubit, so its rate is $1/n$. Erasure locations are known, erased systems are inaccessible, and no protected quantum bypass is supplied. The theorem allows arbitrary collective operations, not efficient or geometrically local circuits. It does not optimize mixed encoders, prove finite-size central-sector optimality, or give a uniform estimate as $\alpha$ approaches one half. Failure is heralded but need not leave the unknown input recoverable for another attempt.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
