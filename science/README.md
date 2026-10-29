# Scientific account

Continuous transversal phase rotations and deterministic exact erasure correction are incompatible for the finite covariant codes considered here. Allowing a declared failure changes the operational question: the accepted quantum channel may be exact even though the probability of failure is nonzero. This account determines the optimal leading failure probability when any fixed fraction below one half of the carriers can be erased.

## Connected proof route

1. [Model](model.md) fixes the isometric encoding, charge normalization, erasure information, and success convention.
2. [Exact recovery](exact_recovery.md) translates the accepted-channel requirement into a Gram-matrix inequality and constructs a completely positive recovery from any feasible matrix.
3. [Charge converse](charge_converse.md) obtains the universal worst-pattern obstruction and an exact finite hypergeometric identity.
4. [Random construction](random_construction.md) proves a simultaneous relative operator estimate, including rare charge sectors, and matches the central-sector obstruction up to an exponentially small additive term.
5. [Asymptotic optimum](asymptotic_optimum.md) optimizes over all charge offsets and treats even block lengths.
6. [Conserving implementation](conserving_implementation.md) realizes the encoder, success filter, and failure completion with number conservation.
7. [Interpretation](interpretation.md) connects exactness, heralding, loss fraction, and physical resources.

The [related-work account](../references/RELATED_WORK.md) identifies the inherited probabilistic-correction framework, random covariant ensemble, and approximate-decoupling results. The [verification guide](../verification/README.md) supplies runnable finite checks. Those checks support their tested identities and channels; the all-size and asymptotic statements rest on the proofs above.
