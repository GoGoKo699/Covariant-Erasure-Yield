# Physical meaning and boundaries

## What heralding changes

The code continuously implements logical phase rotations by transversal physical rotations. Its erased qubits nevertheless carry a small amount of information about the logical charge. Deterministic exact recovery would have to eliminate that information in every branch. The present recovery instead accepts only a component whose environmental state is independent of the logical input, preserving the complete logical coherence exactly, and assigns the remaining component to a declared failure.

The failure probability measures the cost of that selection. At every fixed loss fraction below one half, the best worst-pattern cost vanishes as $n^{-1/2}$ with the coefficient in the [main theorem](model.md). This statement does not contradict finite-dimensional obstructions to deterministic exact covariant correction: the failure probability is nonzero at finite size.

## Why the relative operator bound matters

A small complementary-channel trace distance implies an approximate recovery statement, not necessarily any positive probability of exact recovery. The depolarizing example in [Exact recovery](exact_recovery.md) demonstrates the discontinuity. The random construction controls the full Gram matrix from below by a full-support reference matrix, including rare charge sectors and logical off-diagonal entries. Its explicit inverse filter then removes the residual distortion exactly at a controlled probability cost.

Thus the distinction from prior approximate-decoupling work is operational, not just a change in a norm coefficient. The charge-Haar ensemble and the inverse-square-root extensive-erasure scale are inherited; the [related-work comparison](../references/RELATED_WORK.md) identifies the additional exact-yield conclusion.

## The role of one half

Below one half at fixed separation, every occupied survivor-charge block has an exponentially large row-to-column surplus. This permits simultaneous relative concentration. The proof does not assert a uniform estimate in a shrinking neighborhood of one half.

A separate no-cloning argument rules out near-unit uniform success whenever $k\ge\lceil n/2\rceil$. There are then two disjoint surviving subsets of size $n-k$. Their exact decoders can be applied simultaneously. If both accepted, they would produce two exact copies of every unknown pure logical state. Linearity of a successful Kraus operator forbids nonzero universal exact probabilistic cloning: its action on two basis states and their superpositions cannot have two identical pure output factors. The joint acceptance probability is therefore zero. The two success events are disjoint, so their input-independent probabilities obey

```math
p_A+p_B\le1.
```

At least one pattern has success at most one half. This is the standard exact-recovery no-cloning constraint, not a determination of the optimal yield at or above the threshold. In particular, no precise critical crossover law is claimed here.

## Fixed labels and asymptotic rates

The decoder knows the physical erasure positions. Averaging subsets in the converse is a proof device, not an unrecorded permutation twirl. This distinction prevents transferring capacity statements for unlabeled carriers directly to this task.

Only one logical qubit is stored in a growing block. Near-unit accepted success therefore does not establish a nonzero asymptotic rate. Nor is the result a capacity formula for independent erasure noise, a scheme for amplification above the anti-degradable threshold, or a retry protocol for the same unknown input after failure.

## What remains outside the optimization

The leading law is proved for exactly covariant isometric encoders and ordinary unit-spaced physical qubit charges. Mixed encoding channels, other charge spectra, multiple logical qubits, efficient circuit synthesis, and geometrically local formation time are different optimizations. A finite random code tested numerically need not optimize its own success probability; the verifier constructs a feasible decoder and checks its entire accepted channel. Small-block modal fluctuations also mean that central offsets need not minimize the finite converse.

These boundaries distinguish the established information-theoretic statement from implementation and generalization questions. They are not prerequisites for using the exact law in its stated model.
