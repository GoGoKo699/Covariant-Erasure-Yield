# Model and main theorem

## Encoding and charge

Let $L\simeq\mathbb C^2$ have charge $Q_L=|1\rangle\langle1|$, and let $n$ distinguishable physical qubits have charge

```math
Q_n=\sum_{j=1}^n |1\rangle\langle1|_j.
```

Charge spacing is fixed to one. An admissible encoder is an isometry $V:L\to(\mathbb C^2)^{\otimes n}$ with

```math
e^{-i\theta Q_n}V=e^{-iw\theta}V e^{-i\theta Q_L}
\qquad(\theta\in\mathbb R).
```

The overall phase has no effect on the encoding channel. The integer offset satisfies $0\le w\le n-1$, and the two normalized codewords $|\psi_i\rangle=V|i\rangle$ occupy total-charge sectors $w+i$. Conversely, any such pair defines an admissible isometry because the two sectors are orthogonal.

The global encoding may be arbitrarily complicated. It can be implemented by a number-conserving unitary on the logical input and $n-1$ ancilla qubits in a fixed computational state of charge $w$: extend the desired map separately in each total-charge sector. All $n$ resulting physical qubits undergo the same erasure model. There is no protected sender register, preshared entanglement, quantum side channel, or asymmetric phase reference.

This optimization concerns **isometric encoders**, not all covariant completely positive trace-preserving encoders. General probabilistic correction can benefit from mixed encodings; see the [source comparison](../references/RELATED_WORK.md).

## Erasure and accepted recovery

For a known erased subset $E\subseteq\{1,\ldots,n\}$ of size $k$, let $B=E^c$ and

```math
\mathcal N_E(\rho)=\operatorname{Tr}_E(V\rho V^\dagger).
```

A successful recovery $\mathcal R_E:\mathcal B(B)\to\mathcal B(L)$ is completely positive and trace-nonincreasing. Exact conclusive recovery with probability $p_E$ means the equality of linear maps

```math
\mathcal R_E\circ\mathcal N_E=p_E\,\operatorname{id}_L.
```

Thus $p_E$ is independent of the logical input, and success preserves entanglement with an arbitrary inaccessible reference. A failure operation completes the instrument and supplies an orthogonal classical flag. There is no preservation promise on failure.

The decoder may depend on $V$ and the full erasure pattern, act jointly on all survivors, and use fresh ancillas. It cannot access the erased qubits. The converse permits unrestricted decoding; the attaining construction also admits a number-conserving realization. A statement about failure probability is not a conditional infidelity or a complementary-channel trace distance.

## Optimized quantity

For $0\le k\le n$, define

```math
f^*_{n,k}=\inf_{w,V,\{\mathcal R_E\}}
\max_{|E|=k}(1-p_E),
```

where the infimum obeys the preceding constraints. The same $V$ serves every erased subset. The definition is worst-pattern, not an average over an independently random erasure channel. At $k=0$, the optimum is zero.

**Main theorem.** For every fixed $0<\alpha<1/2$ and $k=\lfloor\alpha n\rfloor$,

```math
f^*_{n,k}
=\sqrt{\frac{2\alpha}{\pi(1-\alpha)}}\,n^{-1/2}
+o(n^{-1/2}).
```

The lower bound optimizes over every offset $w$. For odd $n$, independent Haar codewords in the two adjacent central sectors attain the leading constant simultaneously for every erased subset. For even $n$, one fixed ground-state spectator reduces the construction to odd length. The [asymptotic proof](asymptotic_optimum.md) gives the complete quantifiers.

The estimate is for fixed $\alpha$. Its remainder and constructive constants are not uniform as $\alpha\uparrow1/2$. A single logical qubit is transmitted; neither a nonzero asymptotic code rate nor efficient encoding or decoding follows.

## Notation

Use $N=n-k$ for the number of survivors, $\binom ab=0$ outside $0\le b\le a$, and $A\preceq B$ for positive-semidefinite order. Total variation is one half of the classical $\ell_1$ distance; quantum trace distance is one half of the trace norm. A Gaussian entry below has independent real and imaginary parts of variance $1/2$, so its squared magnitude has mean one.

For a fixed offset define the erased-charge law and adjacent distance

```math
P_w(a)=\frac{\binom ka\binom{n-k}{w-a}}{\binom nw},
\qquad
d_{n,k}(w)=\frac12\sum_{a=0}^k|P_w(a)-P_{w+1}(a)|.
```

These laws arise after averaging the erased subset, even when a particular codeword is not permutation-invariant. Randomizing the subset in a proof does not impose permutation noise on the physical channel.
