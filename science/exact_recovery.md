# Exact recovery from a Gram inequality

This page gives a fixed-isometric-encoder form of the established generalized Knill–Laflamme conditions for probabilistic correction. Its role is to make the accepted map explicit and to identify the operator inequality needed by the random construction. The general criterion is not claimed as a new probabilistic-correction framework; [Kukulski, Pawela, and Puchała](../references/RELATED_WORK.md#probabilistic-correction) supply that framework.

## Synthesis matrix

Fix an erasure pattern and an orthonormal basis $\{|e\rangle\}$ of the erased space. Expand

```math
|\psi_i\rangle=\sum_e |b_{i,e}\rangle_B\otimes|e\rangle_E,
\qquad
T|i,e\rangle=|b_{i,e}\rangle,
\qquad G=T^\dagger T.
```

The columns of $T:L\otimes E\to B$ need not be independent. The channel has Kraus matrices $A_e|i\rangle=|b_{i,e}\rangle$. The tensor factor labeled $E$ in the synthesis matrix is a mathematical index; the decoder constructed below acts on $B$ alone.

## Fixed-encoder optimum

**Proposition 1.** For this encoder and erased subset, the optimal exact accepted probability is

```math
p_E^{\max}=\max_{X\succeq0}
\left\{\operatorname{Tr}X:\ I_2\otimes X\preceq G\right\}.
```

The feasible set is compact: its diagonal blocks imply $X\preceq G_{00}$ and $\operatorname{Tr}X\le1$. Thus the maximum is attained.

### Necessity

Let $K_a$ be the accepted recovery Kraus matrices. The composite channel has Kraus matrices $K_a A_e$. Since its Choi matrix equals $p_E|I\rangle\!\rangle\langle\!\langle I|$ and has rank one, every Kraus matrix belongs to that one-dimensional span:

```math
K_a A_e=c_{ae}I_2.
```

Stacking the $K_a$ gives a contraction $D:B\to L\otimes F$, with matrix elements $D|b\rangle=\sum_a K_a|b\rangle\otimes|a\rangle$. Let $C:E\to F$ have entries $c_{ae}$. Then

```math
DT=I_2\otimes C,
\qquad
I_2\otimes C^\dagger C=T^\dagger D^\dagger DT\preceq G.
```

The choice $X=C^\dagger C$ is feasible and has trace $p_E=\sum_{a,e}|c_{ae}|^2$.

### Sufficiency, including singular matrices

Let $X$ be feasible, set $H=I_2\otimes\sqrt X$, and use the Moore–Penrose inverse:

```math
D=HT^+=HG^+T^\dagger.
```

From $H^\dagger H\preceq G$ follows $\ker G\subseteq\ker H$, hence $DT=H$. To check contractivity, write the polar decomposition $T=U\sqrt G$. On $\operatorname{supp}G$,

```math
G^{+1/2}H^\dagger HG^{+1/2}\preceq\Pi_{\operatorname{supp}G}.
```

Consequently $D^\dagger D\preceq I_B$. Taking the second output factor of $D$ as discarded garbage gives recovery Kraus matrices $K_a=(I_L\otimes\langle a|)D$, and

```math
K_aA_e=(\sqrt X)_{ae}I_2,
\qquad
\sum_{a,e}K_aA_e\rho A_e^\dagger K_a^\dagger
=(\operatorname{Tr}X)\rho.
```

A complementary failure operation with effect $I_B-D^\dagger D$ completes the instrument. No postulated inverse of a singular channel or access to the erased subsystem is used. For the full-rank random construction, $G^+$ is simply $G^{-1}$.

## A common environmental substate

The physical erased states for logical basis inputs are

```math
\rho_E^i=G_{ii}^{\mathsf T},
```

where transposition is in the chosen erased basis. A feasible $X$ therefore gives $X^{\mathsf T}\preceq\rho_E^0,\rho_E^1$. The two residuals are positive and both have trace $1-p_E$, so

```math
\frac12\|\rho_E^0-\rho_E^1\|_1
\le\frac12\bigl(\operatorname{Tr}(\rho_E^0-X^{\mathsf T})
+\operatorname{Tr}(\rho_E^1-X^{\mathsf T})\bigr)
=1-p_E.
```

This inequality supplies the converse. A common diagonal substate alone does not supply sufficiency: the full constraint $I_2\otimes X\preceq G$, including logical off-diagonal blocks, is essential. The [construction](random_construction.md) controls that entire matrix.

## Why approximate correction is not enough

For any $0<\varepsilon\le1$, the qubit channel

```math
\mathcal D_\varepsilon(\rho)=(1-\varepsilon)\rho+\varepsilon I_2/2
```

has a Kraus representation with nonzero multiples of both $I$ and the Pauli $X$. If it admitted nonzero exact conclusive recovery, the rank-one argument would force each recovery Kraus matrix, multiplied by $I$, to be proportional to $I$. Multiplication by $X$ would then also have to be proportional to $I$, forcing that recovery Kraus matrix to vanish. Thus its exact accepted probability is zero for every positive $\varepsilon$, even as the channel approaches the identity.

This elementary specialization of the general correction condition rules out inferring exact yield from a small approximate error alone. The distinction motivates the relative positive-semidefinite estimate used here.
