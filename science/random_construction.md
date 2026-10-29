# A simultaneous exact-yield construction

The code ensemble is established in covariant quantum coding: choose independent Haar vectors in adjacent total-charge sectors. The additional estimate needed for exact conclusive recovery is a **relative operator lower bound**, uniformly over every charge block and every erasure pattern. A trace-norm estimate on typical blocks would not by itself establish this property.

## Ensemble and charge blocks

Take odd $n=2w+1$ and $1\le k\le w$. Set

```math
N=n-k,\qquad r=w-k,\qquad
D_0=\binom nw=\binom n{w+1},\qquad
\mathcal B_{n,k}=\binom{2r}{r}.
```

Choose $|\psi_0\rangle$ and $|\psi_1\rangle$ independently and uniformly on the unit spheres of charges $w$ and $w+1$. For any erased subset $E$, form $T_E$ and $G_E$ as in [Exact recovery](exact_recovery.md).

A column indexed by logical $i$ and erased charge $a$ lies in survivor charge $b=w+i-a$. Thus $T_E$ is a direct sum of rectangular blocks. For $b=w-k,\ldots,w+1$, the row and column dimensions are

```math
m_b=\binom Nb,
\qquad
\ell_b=\binom{k}{w-b}+\binom{k}{w+1-b}
=\binom{k+1}{w+1-b}.
```

The columns include both logical values where available. Their joint Gram matrix therefore retains the logical coherences.

## Uniform dimension surplus, including rare sectors

**Lemma 2.** Every occupied block satisfies

```math
m_b\ge\mathcal B_{n,k}\,\ell_b.
```

To prove it, write $N=(k+1)+2r$ and $c=w+1-b$. In the Vandermonde sum for $\binom Nb$, retain the term that chooses $r$ of the last $2r$ sites and $k+1-c$ of the first $k+1$ sites. Since $b=r+(k+1-c)$, this term is

```math
\binom{2r}{r}\binom{k+1}{k+1-c}
=\mathcal B_{n,k}\ell_b.
```

There are no omitted tail blocks. At a fixed loss fraction below one half, $r$ is linear in $n$, and this ratio is exponentially large even in the least populated sectors.

## Relative Gaussian concentration

Generate unnormalized codewords as independent complex Gaussian coefficient vectors divided by $\sqrt{D_0}$. Before normalizing the two words, each block is $\widetilde T_b=Z_b/\sqrt{D_0}$, where $Z_b$ is an $m_b\times\ell_b$ standard complex Gaussian matrix. Entries in each such matrix are independent, including columns from different logical words. Independence between different erasure patterns is neither assumed nor needed.

Define the diagonal mean Gram matrix

```math
\overline G
=\bigoplus_{i=0}^1\bigoplus_{a=0}^k
\lambda_{i,a}I_{\binom ka},
\qquad
\lambda_{i,a}=\frac{\binom N{w+i-a}}{D_0}.
```

In each survivor-charge block this mean is $(m_b/D_0)I_{\ell_b}$.

For completeness, a net argument gives explicit constants. For fixed unit $x\in\mathbb C^\ell$, $\|Zx\|^2$ is a sum of $m$ independent mean-one exponential variables. Exponential moments and Chernoff's bound give, for $0<u\le1$,

```math
\Pr\left[\left|\frac{\|Zx\|^2}{m}-1\right|>u\right]
\le2e^{-mu^2/4}.
```

For the upper tail use $u-\log(1+u)\ge u^2/4$; for the lower tail use $-u-\log(1-u)\ge u^2/2$. A $1/4$-net of the complex unit sphere has at most $9^{2\ell}$ points, by the usual disjoint-ball volume argument in real dimension $2\ell$. For Hermitian $A$, choosing a net point within $1/4$ of a norm-attaining vector gives $\|A\|\le2\max_x|x^\dagger Ax|$. Consequently, for $0<\delta<1$,

```math
\Pr\left[\left\|\frac{Z^\dagger Z}{m}-I\right\|>\delta\right]
\le2\exp\left(2\ell\log9-\frac{m\delta^2}{16}\right).
```

Choose

```math
\delta_{n,k}=8\sqrt{\frac{n+\log9}{\mathcal B_{n,k}}}.
```

Whenever $\delta_{n,k}<1$, Lemma 2 makes the exponent at most $-4n\ell-2\ell\log9\le-4n$. There are $k+2$ blocks per pattern. A union bound proves that, with probability at least

```math
1-2(k+2)\binom nk e^{-4n},
```

all patterns simultaneously obey

```math
(1-\delta)\overline G
\preceq\widetilde G_E
\preceq(1+\delta)\overline G,
\qquad\delta=\delta_{n,k}.
```

## Normalization preserves a relative lower bound

Let $s_i$ be the squared norm of the unnormalized word $i$. The trace of its diagonal Gram block is $s_i$, while $\sum_a\binom ka\lambda_{i,a}=1$ by Vandermonde. The same event implies $1-\delta\le s_i\le1+\delta$. If $S=\operatorname{diag}(s_0^{-1/2}I,s_1^{-1/2}I)$, the normalized Gram matrix is $G_E=S\widetilde G_ES$. Since $S$ commutes with $\overline G$,

```math
G_E\succeq c_{n,k}\overline G,
\qquad c_{n,k}=\frac{1-\delta_{n,k}}{1+\delta_{n,k}}.
```

Normalization maps the Gaussian ensemble to the independent Haar ensemble, so the same lower probability bound applies to the normalized codes with this property.

## Exact accepted map and finite bound

For every pattern choose, in its computational erased basis,

```math
X_E=c_{n,k}\bigoplus_{a=0}^k
\min\{\lambda_{0,a},\lambda_{1,a}\}I_{\binom ka}.
```

Then $I_2\otimes X_E\preceq c_{n,k}\overline G\preceq G_E$. Proposition 1 constructs a decoder with **exact** success probability

```math
p_E=\operatorname{Tr}X_E
=c_{n,k}\sum_a\min\{P_w(a),P_{w+1}(a)\}
=c_{n,k}\bigl(1-d_{n,k}(w)\bigr).
```

This value is independent of the logical input and, for these chosen decoders, the erased pattern. The matrix of the decoder itself may depend on the pattern. Thus

```math
1-p_E
\le d_{n,k}(w)+\frac{2\delta_{n,k}}{1+\delta_{n,k}}
\le d_{n,k}(w)+2\delta_{n,k}
```

simultaneously for every $k$-subset. This is a finite sufficient bound whenever $\delta_{n,k}<1$. It is not claimed to be numerically tight for small blocks; explicit small-code checks use the actual relative minimum eigenvalue instead of this conservative concentration estimate.

For $k=\lfloor\alpha n\rfloor$ with fixed $\alpha<1/2$, Stirling's formula for the central binomial coefficient gives

```math
\delta_{n,k}=O\left(n^{3/4}2^{-(n-2k-1)/2}\right)
=\exp[-\Omega_\alpha(n)].
```

The exceptional probability also vanishes exponentially, since $\binom nk\le2^n$. The resulting failure probability matches the universal central-offset obstruction up to an exponentially small additive term. [Asymptotic optimization](asymptotic_optimum.md) proves that no other offset improves its leading constant.
