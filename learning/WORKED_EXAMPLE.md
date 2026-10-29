# Three qubits, one known erasure, and exact acceptance

This finite example applies the [Gram recovery criterion](../science/exact_recovery.md). It makes success, failure, covariance, and logical coherence visible without an asymptotic limit. The [Watrous bridge](WATROUS_BRIDGE.md) provides the channel and operator conventions, and the [milestone map](MILESTONES.md) places the example at M15.

## The encoding

Let $\omega=e^{2\pi i/3}$, so $1+\omega+\omega^2=0$. Encode an unknown logical qubit with

```math
|\psi_0\rangle=\frac{|100\rangle+|010\rangle+|001\rangle}{\sqrt3},
\qquad
|\psi_1\rangle=\frac{|011\rangle+\omega|101\rangle+\omega^2|110\rangle}{\sqrt3}.
```

The two vectors are normalized and occupy charges one and two, respectively. They are orthogonal and give the required exact covariance with offset $w=1$. The encoder can be implemented by a number-conserving unitary with two ancilla qubits in a fixed charge-one state. No phase-coherent external reference is assumed.

## The accepted map for the first erased qubit

Suppose the first physical qubit is lost. Order the two survivors as written, with row basis $00,01,10,11$, and order the synthesis columns as $(i,e)=(0,0),(0,1),(1,0),(1,1)$. Then

```math
T=\frac1{\sqrt3}
\begin{pmatrix}
0&1&0&0\\
1&0&0&\omega\\
1&0&0&\omega^2\\
0&0&1&0
\end{pmatrix},
\qquad
G=T^\dagger T=\frac13
\begin{pmatrix}
2&0&0&-1\\
0&1&0&0\\
0&0&1&0\\
-1&0&0&2
\end{pmatrix}.
```

The eigenvalues of $G$ are $1,1/3,1/3,1/3$, so $G\succeq I_4/3$. Choose $X=I_2/3$. The recovery criterion gives the explicit contraction

```math
D=\frac1{\sqrt3}T^{-1},
\qquad DT=\frac{I_4}{\sqrt3}.
```

For recovery Kraus matrices $K_a=(I_2\otimes\langle a|)D$ and erasure Kraus matrices $A_e$, this identity reads

```math
K_aA_e=\frac{\delta_{ae}}{\sqrt3}I_2.
```

There are two nonzero scalar contributions, and hence

```math
\mathcal R_E\mathcal N_E(\rho)=\frac23\rho.
```

Success has probability $2/3$ on every unknown input. It also preserves every entangled reference exactly on acceptance. The spectrum of $D^\dagger D$ is $1,1,1,1/3$, so the operation is trace-nonincreasing, not an unphysical amplified inverse.

## Every single-erasure pattern

For either other erased position, the two overlapping charge-one survivor columns have an inner product equal to a sum of two distinct cube roots divided by three. Its magnitude is again $1/3$. The remaining two columns each have squared norm $1/3$ and different survivor charges. The Gram spectrum is therefore unchanged, and $X=I_2/3$ is feasible for all three patterns. The decoder uses the known lost position to choose its corresponding $T$.

The erased basis-state distributions are $(2/3,1/3)$ and $(1/3,2/3)$, with total variation $1/3$. The environmental converse gives $p_E\le2/3$ for this code. In addition, the universal modal converse at $n=3,k=1$ is $d_{3,1}(w)=1/3$ for every allowed offset. Thus this example attains the finite **worst-pattern** optimum in this particular three-qubit isometric model. This special case does not assert finite central-offset optimality at general block lengths.

## Success, failure, and number conservation

The output index $e$ of $D$ is locally generated garbage, not the actual erased qubit. Give it charge $1-e$ and identify it with a physical garbage qubit by mapping $e=0$ to charge one and $e=1$ to charge zero. The logical output qubit and this garbage qubit then have the same total charge as the two survivors.

After this embedding, call the contraction $\widehat D$. It preserves number, as does $\sqrt{I-\widehat D^\dagger\widehat D}$. A neutral flag realizes the isometry

```math
|\phi\rangle\longmapsto
\widehat D|\phi\rangle\otimes|\mathrm{s}\rangle
+\sqrt{I-\widehat D^\dagger\widehat D}|\phi\rangle\otimes|\mathrm{f}\rangle.
```

On success, discard the garbage and keep the logical output. The complementary branch occurs with probability $1/3$ for encoded inputs, but no recovery or retry promise is made on that branch. The [general construction](../science/conserving_implementation.md) explains the unitary extension inside charge sectors.

## Why basis-state charge statistics are not enough

Replace $|\psi_1\rangle$ by the equal-phase vector

```math
|\psi_1^{+}\rangle=\frac{|011\rangle+|101\rangle+|110\rangle}{\sqrt3}.
```

The logical basis inputs still have the same erased charge distributions and the same environmental trace distance $1/3$. However, the shared charge-one block now has overlap $2/3$, making the Gram matrix singular. For the first erased qubit, its kernel contains

```math
|v\rangle=\frac{|0,0\rangle-|1,1\rangle}{\sqrt2}.
```

For any positive $X$,

```math
\langle v|(I_2\otimes X)|v\rangle=\frac12\operatorname{Tr}X.
```

The inequality $I_2\otimes X\preceq G$ forces this quantity to vanish. Positivity then implies $X=0$, so the exact accepted probability is zero. Permutation symmetry gives the same conclusion for the other single erasures.

The missing ingredient is not better classical charge overlap. It is the ability to preserve logical coherence while extracting an input-independent accepted environmental component. The relative all-sector bound in the large-block construction controls precisely that stronger requirement.

## Reproduce the matrices

Run `python verification/check_learning.py` from the repository root after installing the existing numerical requirements. It reconstructs all three physical erasure channels and their accepted Kraus maps, checks the Choi matrices, Gram spectra, contractivity, and charge intertwining, and tests the equal-phase kernel obstruction. It also checks the milestone count, phase allocation, required fields, and forward dependency order.

The displayed identities provide the analytic calculation. Floating-point tests check their implementation and do not independently certify the asymptotic theorem.
