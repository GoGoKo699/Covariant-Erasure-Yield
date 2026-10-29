# From Watrous to exact covariant erasure recovery

A quantum memory can report that a carrier was lost without knowing the state that carrier held. The remaining carriers must reconstruct an unknown qubit, including its phase and its correlations with systems outside the laboratory. This project allows the decoder to report failure. The accepted output must be exact, rather than merely close to the input.

The single educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018)**. Section references use the author's posted prepublication manuscript, with preface dated January 2018. The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the manuscript and errata; its [contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf) identifies the sections below. The book is linked at its source, not redistributed here.

Watrous supplies the state, channel, operator, distinguishability, and random-vector foundations. It is not a textbook treatment of quantum error correction or fault tolerance. The covariance model, conclusive-correction argument, hypergeometric calculation, and explicit relative concentration estimate are supplied in this repository with separate primary attribution. The [30-milestone map](MILESTONES.md) organizes that bridge, while the [scientific account](../science/README.md) owns the complete general proofs.

## Targeted reading

Use these sections as their objects arise; reading the complete book first is unnecessary.

| Purpose | Watrous manuscript section | Project connection |
| --- | --- | --- |
| Operators, spectra, polar decomposition, and norms | §§1.1.2–1.1.3 | Gram matrices, contractions, pseudoinverses, and positive order |
| Probability and convex optimization | §§1.2.1–1.2.3 | Subset averaging, union bounds, and the fixed-encoder optimization |
| States and inaccessible subsystems | §§2.1.2–2.1.3 | Logical coherence, erasure, and reference-entangled inputs |
| Quantum channels and their representations | §§2.2.1–2.2.2 | Isometries, Kraus operators, Choi matrices, and exact accepted maps |
| Measurements | §§2.3.1–2.3.2 | Success/failure records and completion of an accepted operation |
| Pairwise state discrimination | §3.1.1 | Trace-distance leakage and the classical charge witness |
| Uniform spherical and Haar measures | §7.2.1 | Normalized Gaussian vectors inside each charge sector |

Chapter 7's concentration discussion is optional context, not the cited source of this project's explicit net inequality. Likewise, a charge eigenspace is not the permutation-invariant subspace discussed in §7.1. The construction samples the entire charge eigenspace. These distinctions prevent importing a theorem under the wrong symmetry or norm.

## Notation and normalization

Watrous writes an adjoint as a star; this repository usually writes a dagger. A column vector $u$ corresponds to a ket, and $uu^*$ to its pure-state density operator. A partial trace removes a subsystem without conditioning on a measurement result. Here $L$ is the logical qubit, $E$ the erased subsystem, and $B$ the survivors. The letter $R$ denotes an inaccessible reference only when one is explicitly introduced.

A Kraus representation is

```math
\Phi(Z)=\sum_a K_a ZK_a^\dagger.
```

Trace preservation means $\sum_aK_a^\dagger K_a=I$; an accepted operation instead has $\sum_aK_a^\dagger K_a\preceq I$. Its output trace is the acceptance probability.

We use the **unnormalized** Choi convention

```math
J(\Phi)=\sum_{i,j=0}^1\Phi(|i\rangle\langle j|)\otimes|i\rangle\langle j|,
\qquad
J(\operatorname{id}_2)=|I\rangle\!\rangle\langle\!\langle I|,
\qquad
|I\rangle\!\rangle=|00\rangle+|11\rangle.
```

Thus $\operatorname{Tr}J(\operatorname{id}_2)=2$. Dividing by two gives a normalized reference-input state, but changing that normalization in a success calculation would introduce an erroneous factor of two. A superscript $\mathsf T$ means matrix transposition in the specified basis; it is not a physical transpose operation.

Quantum trace distance and classical total variation both contain a factor of one half. The symbol $A\preceq B$ means that every quadratic form of $B-A$ is nonnegative. It is stronger than an upper bound on a single norm or on selected diagonal entries.

## The complete experiment

An isometry $V:L\to(\mathbb C^2)^{\otimes n}$ maps the logical basis to orthogonal codewords $|\psi_0\rangle$ and $|\psi_1\rangle$. A known subset $E$ of size $k$ is erased. The receiver obtains

```math
\mathcal N_E(\rho)=\operatorname{Tr}_E(V\rho V^\dagger).
```

A success operation $\mathcal R_E$ must satisfy

```math
\mathcal R_E\circ\mathcal N_E=p_E\operatorname{id}_L.
```

This is a linear-map equality on all operators, including off-diagonal ones. Applying it together with an identity map on an external reference proves exact preservation of entanglement on success. The scalar $p_E$ is independent of the unknown input. Conditioning on success divides the output by $p_E$; it does not change the fact that the unconditional instrument sometimes fails.

The decoder knows the encoding and the erased positions, can process all survivors jointly, and cannot access the lost subsystem. The same encoder must work for every pattern of the stipulated size, although different patterns can use different decoders. The theorem minimizes the largest failure probability over those patterns, not a mean for a chosen random-loss distribution.

## Covariance without a phase reference

Each physical qubit has excitation charge zero or one. With $Q_L=|1\rangle\langle1|$ and $Q_n$ the sum of the physical number operators, the requirement is

```math
e^{-i\theta Q_n}V=e^{-iw\theta}Ve^{-i\theta Q_L}.
```

Consequently the logical-zero codeword has charge $w$ and the logical-one codeword has charge $w+1$. Their common phase is irrelevant to the encoding channel. The adjacent charge spacing is fixed; rescaling it would change the problem.

Within a charge eigenspace, arbitrary complex superpositions are permitted. A number-conserving unitary can map an input qubit and a fixed charge-$w$ computational ancilla state to the two chosen codewords, extending each map inside its own charge sector. This is an implementation existence statement. It does not bound circuit size, depth, locality, or experimental precision.

## From an accepted channel to a Gram inequality

For a fixed pattern, expand the codewords as

```math
|\psi_i\rangle=\sum_e|b_{i,e}\rangle_B\otimes|e\rangle_E,
\qquad
T|i,e\rangle=|b_{i,e}\rangle,
\qquad
G=T^\dagger T.
```

The loss Kraus matrices are $A_e|i\rangle=|b_{i,e}\rangle$. If $K_a$ are accepted recovery Kraus matrices, their composite matrices are $K_aA_e$. A rank-one Choi matrix is a sum of positive outer products only when every contributing vector lies in its one-dimensional support. Exactness therefore forces

```math
K_aA_e=c_{ae}I_2.
```

Stacking the recovery matrices into a contraction gives the necessary condition

```math
I_2\otimes X\preceq G,
\qquad X\succeq0,
\qquad p_E=\operatorname{Tr}X.
```

Conversely, set $H=I_2\otimes\sqrt X$ and $D=HT^+$. Positive order ensures that $H$ vanishes on the kernel of $T$, that $DT=H$, and that $D^\dagger D\preceq I_B$. Taking the second output factor as discarded garbage produces an accepted channel with probability $\operatorname{Tr}X$. A failure branch completes the contraction. The [canonical proof](../science/exact_recovery.md) includes the support argument for singular matrices.

This is a useful form of the established probabilistic-correction framework, not a newly invented recovery principle. Its crucial feature for this project is that the **full** Gram matrix must dominate $I_2\otimes X$. Logical off-diagonal blocks cannot be omitted. The [three-qubit example](WORKED_EXAMPLE.md) shows both a feasible exact filter and a case where identical charge statistics do not suffice.

## Why erased charge limits success

The erased states for basis inputs obey $\rho_E^i=G_{ii}^{\mathsf T}$. Feasibility supplies the same positive substate $X^{\mathsf T}$ inside both. Their remaining positive parts each have trace $1-p_E$, so

```math
1-p_E\ge\frac12\|\rho_E^0-\rho_E^1\|_1.
```

Measuring the erased number can only reduce this distinguishability. After averaging over all $k$-subsets, a weight-$w$ codeword gives the hypergeometric law

```math
P_w(a)=\frac{\binom ka\binom{n-k}{w-a}}{\binom nw}.
```

The numerator counts strings with $a$ occupied erased positions and $w-a$ occupied surviving positions. Coherences do not enter a diagonal charge measurement. Averaging the subset gives the same law for every vector in that charge sector; a particular subset of an arbitrary vector need not have that law.

Convexity then implies a worst-pattern failure of at least $d_{n,k}(w)=\operatorname{TV}(P_w,P_{w+1})$. Adding one uniformly chosen unoccupied site couples the two laws. Their likelihood ratio crosses one once, and the largest cumulative difference gives

```math
d_{n,k}(w)=\frac{k}{n}\max_a
\frac{\binom wa\binom{n-1-w}{k-1-a}}{\binom{n-1}{k-1}}.
```

The [charge converse](../science/charge_converse.md) proves this identity exactly. It includes the small-block counterexample to finite central-offset optimality.

For fixed interior filling $w/n\to\beta$, Stirling's formula at this mode yields

```math
\sqrt n\,d_{n,k}(w)\longrightarrow
\sqrt{\frac{\alpha}{2\pi(1-\alpha)\beta(1-\beta)}}.
```

The central filling maximizes $\beta(1-\beta)$ and minimizes this coefficient. The [all-offset argument](../science/asymptotic_optimum.md) separately rules out offsets approaching the charge boundaries, so central filling is not merely an assumed optimum.

## From random vectors to an exact filter

For odd $n=2w+1$, independently choose unit vectors in sectors $w$ and $w+1$. Watrous §7.2.1 supplies the uniform-vector foundations. The following dimension and operator estimates are supplied locally.

A synthesis column with logical value $i$ and erased charge $a$ lies in survivor charge $b=w+i-a$. Its block has

```math
m_b=\binom{n-k}{b}\quad\text{rows},
\qquad
\ell_b=\binom{k+1}{w+1-b}\quad\text{columns}.
```

Writing $r=w-k$, one retained term of Vandermonde's identity proves

```math
m_b\ge\binom{2r}{r}\ell_b
```

for **every** occupied sector. Below half erasure at a fixed separation, this ratio is exponentially large. No rare sector is discarded.

For unnormalized Gaussian codewords, each block is an independent-entry Gaussian rectangle. An exponential tail for one quadratic form, a finite net of the unit sphere, and a union bound produce a relative bound on the entire Gram matrix for every pattern. Pattern-to-pattern independence is not assumed. Bounding the two normalization factors then gives

```math
G_E\succeq c\overline G,
\qquad c=\frac{1-\delta}{1+\delta},
\qquad \delta=\exp[-\Omega_\alpha(n)].
```

Here $\overline G$ is diagonal in the logical and erased-charge indices. Its sector entries are

```math
\lambda_{i,a}=\frac{\binom{n-k}{w+i-a}}{\binom nw}.
```

Take $X$ diagonal, with entry $c\min(\lambda_{0,a},\lambda_{1,a})$ on each erased basis vector of charge $a$. This guarantees the full operator inequality, not just an environmental overlap. The exact accepted probability is

```math
p_E=c\sum_a\min\{P_w(a),P_{w+1}(a)\}
=c(1-d_{n,k}(w)).
```

The decoder removes distortion exactly; random-matrix fluctuations reduce only its acceptance probability. Explicit constants and the finite sufficient bound appear in [Random construction](../science/random_construction.md). The concentration estimate can be conservative for small $n$; it is not a numerical prediction for every sampled finite code.

## What the matching law says

Combining the converse and construction gives

```math
f^*_{n,\lfloor\alpha n\rfloor}
=\sqrt{\frac{2\alpha}{\pi(1-\alpha)n}}+o(n^{-1/2}),
\qquad 0<\alpha<\tfrac12.
```

This law concerns one logical qubit, isometric encoders, known loss positions, and a fixed loss fraction. Even lengths are covered by a ground-state spectator and, when necessary, an additional deliberate discard. Smaller known loss sets can likewise be enlarged by discarding survivors.

The [conserving implementation](../science/conserving_implementation.md) assigns the filter's garbage indices charge $w-a$, embeds them in ordinary survivor-qubit charge spaces, and completes the accepted contraction with a neutral success/failure flag. It introduces no asymmetric reference. It still permits arbitrary collective control.

Exact quality on acceptance is not a statement of high code rate, an efficient circuit, a favorable conditional output after failure, or uniform performance arbitrarily close to half erasure. Nor can an approximate-decoupling result alone establish exact yield: the depolarizing counterexample in [Exact recovery](../science/exact_recovery.md#why-approximate-correction-is-not-enough) has zero exact accepted probability for every positive noise strength.

For a compact physical realization of these distinctions, read the [worked example](WORKED_EXAMPLE.md). For provenance and evidence boundaries, use [Related work](../references/RELATED_WORK.md) and [Verification](../verification/README.md). The book supplies the selected foundations; those research sources remain necessary attribution, not additional assigned educational anchors.
