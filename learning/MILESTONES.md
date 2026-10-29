# Project understanding map

This is the common **30-milestone** route through Covariant Erasure Yield. The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018), using the author's January 2018 prepublication manuscript. The [Watrous bridge](WATROUS_BRIDGE.md) identifies the exact sections, translates notation, and develops the steps that are supplied by this project rather than by the textbook.

The allocation is **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. The background connects individual states, channels, charge sectors, distinguishability, and random vectors into the complete experiment. The narrative joins a fixed-encoder recovery criterion to a universal charge obstruction and a simultaneous construction, then integrates implementation, attribution, and scope. This map expresses the project's conceptual dependencies, not any particular reader's progress. Full proofs remain in [science](../science/README.md).

## Phase I: background and preliminaries

### M01 States and logical coherence

**Central question.** What must be preserved when an unknown qubit is recovered?

**Understanding target.** Interpret a density operator as positive and trace one, and distinguish a coherent superposition from a classical mixture with the same basis populations. Understand why checking only the two computational basis states leaves the off-diagonal part of a quantum channel untested.

**Dependencies and story role.** None. This supplies the local object whose recovery defines the task.

**Conceptual connection.** Exact recovery must preserve both populations and coherences, rather than merely predict a classical bit.

**Source pointers.** Watrous §2.1.2; [bridge notation](WATROUS_BRIDGE.md#notation-and-normalization); [operational model](../science/model.md).

### M02 An inaccessible reference and erasure

**Central question.** Why is recovery tested on a system that may already be entangled?

**Understanding target.** Use tensor products and partial trace to describe a logical qubit entangled with an inaccessible reference, an isometric encoding, and the loss of a specified physical subsystem. Distinguish knowing the lost positions from possessing the lost qubits.

**Dependencies and story role.** M01. The single-qubit task becomes a task on correlations with other systems.

**Conceptual connection.** Equality of quantum channels preserves every reference-entangled input; a basis-state test does not establish that guarantee.

**Source pointers.** Watrous §§2.1.2–2.1.3; [model](../science/model.md); [bridge experiment](WATROUS_BRIDGE.md#the-complete-experiment).

### M03 Channels and Kraus operators

**Central question.** How is the inaccessible loss represented without measuring it?

**Understanding target.** Read a completely positive map as a sum of Kraus terms. Expand each codeword in an erased-subsystem basis and identify the associated operators from the logical input to the survivors. Understand that the erased-basis index is a mathematical description, not a record available to the decoder.

**Dependencies and story role.** M01, M02. This supplies the operator representation used in the proof.

**Conceptual connection.** A coherent codeword becomes a channel after partial trace; a recovery operation must correct all of its Kraus contributions consistently.

**Source pointers.** Watrous §§2.2.1–2.2.2; [synthesis matrix](../science/exact_recovery.md#synthesis-matrix).

### M04 A heralded quantum instrument

**Central question.** What does an exact answer with a possible failure mean physically?

**Understanding target.** Distinguish a trace-preserving channel from a trace-nonincreasing accepted operation. Interpret the equality $\mathcal R_E\mathcal N_E=p_E\operatorname{id}$ as an input-independent success probability and an exact conditional output. Include a complementary failure operation and a classical flag.

**Dependencies and story role.** M02, M03. This fixes the operational objective before optimizing it.

**Conceptual connection.** Heralded failure, conditional infidelity, and disturbance after a failed attempt are different quantities. Failure does not promise that the input can be tried again.

**Source pointers.** Watrous §§2.2.2 and 2.3.1–2.3.2; [model](../science/model.md); [bridge experiment](WATROUS_BRIDGE.md#the-complete-experiment).

### M05 The Choi representation

**Central question.** How can one matrix encode the action on every logical input?

**Understanding target.** Relate a completely positive map to its Choi matrix and its Kraus vectors. Fix the unnormalized convention in which the identity channel has Choi matrix $|I\rangle\!\rangle\langle\!\langle I|$ and trace two. Explain why an accepted identity channel has rank one.

**Dependencies and story role.** M02, M03, M04. This turns exactness into a usable algebraic constraint.

**Conceptual connection.** Positivity prevents different Kraus contributions from canceling outside a rank-one Choi support. The argument checks logical coherence automatically.

**Source pointers.** Watrous §2.2.2; [exact-recovery necessity](../science/exact_recovery.md#necessity); [bridge](WATROUS_BRIDGE.md#from-an-accepted-channel-to-a-gram-inequality).

### M06 Gram matrices and positive order

**Central question.** Which matrix condition permits a physical inverse filter?

**Understanding target.** Interpret a synthesis matrix as a list of survivor vectors and its Gram matrix as all their overlaps. Read $A\preceq B$ as a quadratic-form inequality. Connect a contraction to a valid accepted operation, and distinguish an inverse on the support from an inverse on the entire space.

**Dependencies and story role.** M03, M05. This introduces the geometric objects used for both feasibility and construction.

**Conceptual connection.** The Gram matrix contains overlaps between logical values as well as within them; controlling only its diagonal blocks can miss a coherence obstruction.

**Source pointers.** Watrous §§1.1.2–1.1.3 and 1.2.3; [exact recovery](../science/exact_recovery.md).

### M07 Charge eigenspaces and degeneracy

**Central question.** What freedom remains when the total excitation number is fixed?

**Understanding target.** Count the charge-$w$ computational basis states as $\binom nw$ and recognize their span as an eigenspace of the physical number operator. Distinguish an arbitrary superposition inside that space from the single equal-amplitude permutation-symmetric vector.

**Dependencies and story role.** M01, M02. This adds the physical symmetry to the channel description.

**Conceptual connection.** Number conservation permits complicated operations within a degenerate charge space. It does not force permutation invariance or simple circuits.

**Source pointers.** Watrous §1.1.2 for spectral foundations; [model](../science/model.md#encoding-and-charge); [bridge covariance](WATROUS_BRIDGE.md#covariance-without-a-phase-reference).

### M08 Exact covariance and the charge offset

**Central question.** How does the same phase rotation on every carrier act as a logical rotation?

**Understanding target.** Explain why codewords of charges $w$ and $w+1$ intertwine the physical and logical rotations, up to an irrelevant common phase. Keep the physical charge spacing fixed and include every allowed integer offset in the optimization.

**Dependencies and story role.** M03, M07. The symmetry becomes an exact input/output relation rather than a qualitative label.

**Conceptual connection.** Covariance restricts the encoding isometry but leaves a large choice of vectors inside each charge sector. General mixed encoding channels are not included in the theorem.

**Source pointers.** Watrous §2.2.2 for isometries; [model](../science/model.md); [bridge covariance](WATROUS_BRIDGE.md#covariance-without-a-phase-reference).

### M09 Distinguishability and information leakage

**Central question.** How does the erased subsystem reveal something about the logical input?

**Understanding target.** Use half trace norm for quantum trace distance and half the sum of absolute probability differences for total variation. Explain why measuring the erased charge cannot increase distinguishability, and why distinguishable erased states obstruct an identical accepted environmental component.

**Dependencies and story role.** M02, M04, M06. This introduces the converse's information measure.

**Conceptual connection.** The converse limits success by information that has left the receiver, not by the difficulty of computing a decoder.

**Source pointers.** Watrous §§1.1.3 and 3.1.1; [common substate](../science/exact_recovery.md#a-common-environmental-substate); [bridge obstruction](WATROUS_BRIDGE.md#why-erased-charge-limits-success).

### M10 Sampling without replacement

**Central question.** Why does a hypergeometric distribution appear for an arbitrary codeword?

**Understanding target.** Count occupied sites in a uniformly selected erased subset of a fixed-weight string. Derive the normalization and meaning of $P_w(a)$. Understand why averaging the subset removes dependence on the particular string, while a fixed subset of an arbitrary code need not have that distribution.

**Dependencies and story role.** M07, M09. This connects the symmetry to an explicit classical obstruction.

**Conceptual connection.** The random subset is used in a proof of a worst-pattern bound. No physical permutation twirl or random-erasure assumption is introduced.

**Source pointers.** Watrous §1.2.2 for probability foundations; [charge converse](../science/charge_converse.md); [bridge obstruction](WATROUS_BRIDGE.md#why-erased-charge-limits-success).

### M11 Uniform random vectors and concentration

**Central question.** What can a random construction establish about a single usable code?

**Understanding target.** Interpret Haar-distributed unit vectors within a specified charge sector and obtain them by normalizing isotropic complex Gaussian vectors. Distinguish a statement for one erasure pattern from an event controlling all patterns. Understand how a union bound can combine dependent events.

**Dependencies and story role.** M06, M07, M10. This supplies the constructive method without presuming independent erasure-pattern tests.

**Conceptual connection.** A high-probability construction implies existence of one common encoder. It does not imply efficient preparation or an optimal finite numerical sample.

**Source pointers.** Watrous §7.2.1 and §1.2.2; [random construction](../science/random_construction.md); [bridge construction](WATROUS_BRIDGE.md#from-random-vectors-to-an-exact-filter).

### M12 The complete optimization

**Central question.** Which experiment, resources, and error convention does the theorem optimize?

**Understanding target.** Assemble one logical qubit, a covariant isometry into $n$ ordinary number qubits, a known erased subset, and an exact accepted identity channel with unrestricted joint decoding. Explain the infimum over offsets, encoders, and decoders, followed by the maximum failure over erased subsets of the specified size.

**Dependencies and story role.** M04, M08, M09, M10, M11. This integrates the background into one operational question.

**Conceptual connection.** The fixed-fraction large-$n$ limit differs from finite-size optimality, coding capacity, mixed-encoder optimization, and efficient circuit synthesis.

**Source pointers.** [Model and main theorem](../science/model.md); [bridge experiment](WATROUS_BRIDGE.md#the-complete-experiment); Watrous §§2.2.1–2.2.2 for the channel language.

## Phase II: narrative and innovation

### M13 Exactness forces scalar composite Kraus operators

**Central question.** What must every accepted recovery Kraus operator do to every loss Kraus operator?

**Understanding target.** Apply rank-one Choi support to derive $K_aA_e=c_{ae}I_2$. Stack the recovery Kraus operators into a contraction and collect the scalar coefficients into a matrix. Interpret the coefficient indices without granting access to the erased subsystem.

**Dependencies and story role.** M03, M05, M06, M12. This is the local algebraic entry into the recovery theorem.

**Conceptual connection.** The general probabilistic-correction condition is inherited. Its role here is to expose the operator constraint that the charge-sector construction must satisfy.

**Source pointers.** Watrous §2.2.2; [necessity proof](../science/exact_recovery.md#necessity); [attribution](../references/RELATED_WORK.md#probabilistic-correction).

### M14 A feasible matrix gives an actual recovery

**Central question.** Does a Gram inequality describe a physical instrument or only a formal bound?

**Understanding target.** Connect $I_2\otimes X\preceq T^\dagger T$ to the contraction $D=(I_2\otimes\sqrt X)T^+$. Explain the kernel condition, the exact composite channel, success probability $\operatorname{Tr}X$, and the positive failure effect completing the operation.

**Dependencies and story role.** M04, M06, M13. This turns necessity into a complete construction, including singular matrices.

**Conceptual connection.** The inverse filter is paid for by a reduced success probability. Mathematical invertibility alone does not establish contractivity.

**Source pointers.** Watrous §1.1.3; [sufficiency proof](../science/exact_recovery.md#sufficiency-including-singular-matrices); [bridge](WATROUS_BRIDGE.md#from-an-accepted-channel-to-a-gram-inequality).

### M15 A complete three-qubit illustration

**Central question.** Can exact accepted recovery and the importance of coherence be seen in a small matrix?

**Understanding target.** Follow the explicit charge-one/charge-two code in the worked example. Verify its Gram spectrum and accepted success $2/3$ for each single erasure. Contrast it with the equal-phase pair, whose erased basis-state statistics are the same but whose exact accepted probability is zero.

**Dependencies and story role.** M07, M08, M14. This makes the recovery condition concrete before the asymptotic argument.

**Conceptual connection.** Logical off-diagonal overlaps can decide feasibility even when the charge distributions are unchanged. The example is an application of the criterion, not the random-code asymptotic proof.

**Source pointers.** [Worked example](WORKED_EXAMPLE.md); [exact recovery](../science/exact_recovery.md); Watrous §§2.2.2 and 1.1.3.

### M16 The accepted environmental component

**Central question.** Why must the failure probability cover the environmental distinguishability?

**Understanding target.** Identify $X^{\mathsf T}$ as a common positive substate of the two erased states. Subtract it, use the positive residual traces, and derive $1-p_E\ge\tfrac12\|\rho_E^0-\rho_E^1\|_1$. Retain the transpose convention and the direction of the inequality.

**Dependencies and story role.** M09, M13, M14. This extracts the converse from the same recovery condition.

**Conceptual connection.** The common-substate bound is necessary, but the three-qubit contrast shows why it is not sufficient without coherence control.

**Source pointers.** Watrous §3.1.1; [environmental bound](../science/exact_recovery.md#a-common-environmental-substate); [worked example](WORKED_EXAMPLE.md).

### M17 From individual patterns to a universal obstruction

**Central question.** How can an averaged charge law constrain every proposed encoder's worst case?

**Understanding target.** Apply erased-charge measurement, average over fixed-size subsets, and use convexity of total variation. Follow the chain from the maximum failure to the adjacent hypergeometric distance. Explain why the final bound is worst-pattern rather than a bound on each subset separately.

**Dependencies and story role.** M10, M12, M16. This makes the converse independent of the codeword amplitudes.

**Conceptual connection.** The obstruction permits arbitrary recovery resources and every charge offset. It comes from inaccessible information, not a restricted decoder baseline.

**Source pointers.** Watrous §§1.2.1–1.2.2; [averaging proof](../science/charge_converse.md#averaging-the-known-erased-subset).

### M18 The adjacent-charge modal identity

**Central question.** How can the distance between two distributions be reduced to a single peak probability?

**Understanding target.** Couple a uniform weight-$w$ string to weight $w+1$ by adding one occupied site. Relate the cumulative-distribution difference to the chance of adding an erased excitation. Use the single likelihood-ratio crossing to identify total variation with the largest cumulative difference and hence a hypergeometric mode.

**Dependencies and story role.** M10, M17. This gives an exact finite formula suited to asymptotics and verification.

**Conceptual connection.** The modal formula measures the overlap cost of shifting the conserved logical charge by one unit.

**Source pointers.** [Exact finite identity](../science/charge_converse.md#exact-finite-identity); Watrous §1.2.2 for the probability language; [bridge obstruction](WATROUS_BRIDGE.md#why-erased-charge-limits-success).

### M19 Finite offsets and the meaning of optimality

**Central question.** Why can central sectors be asymptotically optimal without minimizing every finite bound?

**Understanding target.** Compare the exact $n=11,k=3$ modal distances at offsets five and three. Distinguish optimizing a converse from finding an attaining finite code. Recognize that discrete modes can change finite coefficients without changing the leading large-block conclusion.

**Dependencies and story role.** M12, M18. This prevents a stronger finite claim from entering the main result implicitly.

**Conceptual connection.** A useful asymptotic construction need not solve the full finite-size optimization, and finite numerical minima cannot substitute for the all-offset proof.

**Source pointers.** [Finite offset example](../science/charge_converse.md#finite-offsets-need-not-be-central); [verification](../verification/README.md); Watrous §1.2.2 for probability conventions.

### M20 The optimal leading charge coefficient

**Central question.** Why does no noncentral or edge filling improve the leading converse?

**Understanding target.** Use Stirling's formula at the hypergeometric mode for interior filling and identify the factor $\beta(1-\beta)$. Separately exclude filling fractions approaching zero or one by a variance bound on the peak mass. Combine subsequences to cover every possible offset sequence.

**Dependencies and story role.** M18, M19. This closes the universal asymptotic optimization rather than only analyzing the proposed construction.

**Conceptual connection.** The central coefficient is a conclusion of the optimization, not an assumption that finite central sectors always win.

**Source pointers.** [Asymptotic optimum](../science/asymptotic_optimum.md); Watrous §§1.2.1–1.2.2 for limit and probability foundations; the asymptotic calculation is supplied locally.

### M21 Survivor-charge blocks

**Central question.** Which rectangular matrices contain all the loss-channel coherences?

**Understanding target.** Group the synthesis columns by survivor charge $b=w+i-a$. Count the rows as $\binom{n-k}{b}$ and combine the columns from both logical values using Pascal's identity. Keep the logical off-diagonal Gram entries within each shared block.

**Dependencies and story role.** M06, M07, M11, M14. This begins the matching construction at the level of one block.

**Conceptual connection.** Charge conservation organizes the matrix but does not remove the need to control overlaps between logical codewords.

**Source pointers.** [Ensemble and blocks](../science/random_construction.md#ensemble-and-charge-blocks); [bridge construction](WATROUS_BRIDGE.md#from-random-vectors-to-an-exact-filter); Watrous §7.2.1 for the random-vector ensemble.

### M22 A dimension surplus in every sector

**Central question.** Why do even rare charge sectors have enough survivor space below half erasure?

**Understanding target.** Retain one term in Vandermonde's identity to bound every row-to-column ratio by a central binomial coefficient. Explain why the ratio is exponentially large at a fixed loss fraction below one half and why no tail sector has been discarded.

**Dependencies and story role.** M07, M21. This provides the uniform parameter needed by the operator estimate.

**Conceptual connection.** Exact acceptance cannot tolerate an uncontrolled sector merely because that sector is unlikely. A uniform dimension inequality supplies the missing protection.

**Source pointers.** [Dimension-surplus lemma](../science/random_construction.md#uniform-dimension-surplus-including-rare-sectors); [bridge construction](WATROUS_BRIDGE.md#from-random-vectors-to-an-exact-filter).

### M23 Relative concentration for all patterns

**Central question.** How does a Gaussian block estimate produce one encoder that works for every erasure pattern?

**Understanding target.** Connect exponential tails for a fixed vector to a finite-net operator-norm bound, then apply the dimension surplus and a union bound over blocks and erased subsets. Distinguish relative positive-semidefinite control from an additive trace-norm estimate.

**Dependencies and story role.** M06, M11, M22. This upgrades local random geometry to the simultaneous construction event.

**Conceptual connection.** Independence of distinct erased patterns is unnecessary. The small exceptional probability proves common-code existence rather than a different code for each pattern.

**Source pointers.** [Relative Gaussian concentration](../science/random_construction.md#relative-gaussian-concentration); Watrous §7.2.1 for the ensemble; the explicit net proof is local, not an application attributed to §7.3.

### M24 Normalizing the sampled codewords

**Central question.** Does turning Gaussian vectors into unit vectors destroy the relative matrix bound?

**Understanding target.** Use diagonal-block traces to bound each sampled norm, apply the corresponding block-diagonal rescaling, and obtain the factor $(1-\delta)/(1+\delta)$. Explain why this rescaling commutes with the mean Gram matrix.

**Dependencies and story role.** M11, M21, M23. This converts an estimate for unnormalized arrays into a statement about actual encoding isometries.

**Conceptual connection.** A normalized code is a physical input map; ignoring its normalization would alter both the probability accounting and the feasibility condition.

**Source pointers.** [Normalization proof](../science/random_construction.md#normalization-preserves-a-relative-lower-bound); Watrous §§1.1.2 and 7.2.1.

### M25 Exact yield from the common overlap

**Central question.** Where do the charge converse and the conclusive decoder meet?

**Understanding target.** Choose each diagonal entry of $X$ as the smaller of the two mean-sector weights times the normalization factor. Verify the full Gram inequality and sum the entries to obtain $p=c(1-d)$. Distinguish the exact accepted-channel equality from the asymptotic estimate on its probability.

**Dependencies and story role.** M14, M18, M20, M24. This joins the inverse filter, charge overlap, and concentration estimate into matching leading bounds.

**Conceptual connection.** Random fluctuations cost only an exponentially small additional failure probability in the fixed-fraction regime; accepted outputs themselves have no residual error.

**Source pointers.** [Exact accepted map](../science/random_construction.md#exact-accepted-map-and-finite-bound); [main theorem](../science/model.md); [bridge synthesis](WATROUS_BRIDGE.md#what-the-matching-law-says).

### M26 Even length and fewer erased qubits

**Central question.** Why do parity and a smaller known loss set not invalidate the guarantee?

**Understanding target.** Append one ground-state spectator to an odd-length code. Condition on whether it was erased, voluntarily discard an additional active survivor when needed, and use the appropriate guaranteed decoder. Explain why this operation preserves the leading coefficient and provides a guarantee for smaller known erased sets.

**Dependencies and story role.** M02, M08, M25. This completes the theorem's block-length and loss-set quantifiers.

**Conceptual connection.** Deliberately discarding a known survivor is an allowed channel, not access to an erased qubit or a free protected register.

**Source pointers.** [Parity and fewer erasures](../science/asymptotic_optimum.md#even-length-and-fewer-erasures); Watrous §2.2.1.

### M27 A conserving success instrument

**Central question.** Can the mathematical filter be implemented without a hidden phase reference?

**Understanding target.** Assign charges to its auxiliary output indices, embed their multiplicities into ordinary survivor-qubit sectors, and verify charge intertwining. Complete the contraction with a square-root failure branch and a neutral flag, then extend the isometry within charge sectors.

**Dependencies and story role.** M04, M07, M08, M14, M22, M25. This closes the implementation and resource-accounting requirements.

**Conceptual connection.** The garbage index is produced locally. Number conservation is established, but a small or local circuit is not.

**Source pointers.** [Conserving implementation](../science/conserving_implementation.md); Watrous §§1.1.3 and 2.2.2; [worked example](WORKED_EXAMPLE.md#success-failure-and-number-conservation).

### M28 Half erasure, rate, and physical boundaries

**Central question.** Which conclusions survive when the loss regime or resource question changes?

**Understanding target.** Explain the disjoint-decoder no-cloning obstruction at and above half erasure. Separate this from the fixed-fraction dimension-surplus proof below half. Recognize the vanishing code rate, unrestricted collective control, and lack of a uniform critical-window estimate.

**Dependencies and story role.** M12, M22, M25, M26, M27. This places the achieved capability inside its physical boundaries.

**Conceptual connection.** Near-unit accepted transmission of one qubit is neither an independent-erasure capacity formula nor an efficient fault-tolerant architecture.

**Source pointers.** [Interpretation](../science/interpretation.md); [model](../science/model.md); Watrous §8.2.1 only for the contrasting capacity notion, not an additional prerequisite.

### M29 Attribution and the strength of evidence

**Central question.** Which ingredients are inherited, and which operational conclusion is established here?

**Understanding target.** Identify the general probabilistic-recovery condition, charge-Haar ensemble, and approximate extensive-erasure law in their primary sources. Locate the relative all-sector estimate and exact accepted-channel construction supplying the distinct yield conclusion. Separate rational identities, floating-point channel checks, analytical proofs, and independent review.

**Dependencies and story role.** M15, M20, M23, M25, M27, M28. This connects the complete contribution to the evidence that actually supports it.

**Conceptual connection.** One educational anchor does not replace research attribution, and passing finite tests is not a novelty or universal-proof certificate.

**Source pointers.** [Related work](../references/RELATED_WORK.md); [verification guide](../verification/README.md); [Watrous reading route](WATROUS_BRIDGE.md#targeted-reading).

### M30 The complete exact-yield story

**Central question.** Why can an exactly covariant code recover exactly on acceptance despite unavoidable charge leakage?

**Understanding target.** Connect the accepted-channel criterion, common environmental component, all-offset charge converse, uniform relative random-matrix bound, and conserving instrument to the optimal leading failure law. State the full assumptions and explain what changes when exactness, labels, charge spectrum, encoding type, or implementation cost is changed.

**Dependencies and story role.** M12, M20, M25, M26, M27, M28, M29. This integrates both phases into one account of necessity, attainability, and physical meaning.

**Conceptual connection.** Exact conditional quality is obtained by sacrificing a quantitatively optimal fraction of attempts, not by eliminating charge leakage from the unconditional experiment.

**Source pointers.** [Scientific account](../science/README.md); [main theorem](../science/model.md); [bridge synthesis](WATROUS_BRIDGE.md#what-the-matching-law-says); [worked example](WORKED_EXAMPLE.md).
