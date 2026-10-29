# Charge leakage and the universal converse

Fix any offset $w$, any admissible isometric encoder, and any accepted decoders in the [model](model.md). The erased charge carries information about which logical charge sector was supplied. The accepted branch must remove this information exactly.

## Averaging the known erased subset

Let $p_{i,E}(a)$ be the probability of measuring charge $a$ in the erased subsystem for logical input $i$. By the environmental bound in [Proposition 1](exact_recovery.md) and measurement data processing,

```math
1-p_E\ge\frac12\|\rho_E^0-\rho_E^1\|_1
\ge\operatorname{TV}(p_{0,E},p_{1,E}).
```

Average over all $k$-subsets. For every computational string of weight $w+i$, the number of selected occupied sites is hypergeometric. The charge measurement is diagonal, so coherences of the codeword do not change this average. Therefore

```math
\mathbb E_E p_{i,E}(a)=P_{w+i}(a)
=\frac{\binom ka\binom{n-k}{w+i-a}}{\binom n{w+i}}.
```

Convexity of total variation gives

```math
\max_{|E|=k}(1-p_E)
\ge\mathbb E_E(1-p_E)
\ge\mathbb E_E\operatorname{TV}(p_{0,E},p_{1,E})
\ge d_{n,k}(w).
```

In particular,

```math
f^*_{n,k}\ge\min_{0\le w\le n-1}d_{n,k}(w).
```

This is a universal **worst-pattern** bound. It does not say that each particular erased subset of an arbitrary asymmetric code has failure at least $d_{n,k}(w)$.

## Exact finite identity

For $1\le k\le n$ and $0\le w\le n-1$, the adjacent distance has the useful form

```math
\boxed{
d_{n,k}(w)=\frac{k}{n}\max_a
\frac{\binom wa\binom{n-1-w}{k-1-a}}{\binom{n-1}{k-1}}.
}
```

The expression maximized is the mass function of a hypergeometric variable with population $n-1$, $w$ occupied positions, and sample size $k-1$.

### Coupling and the cumulative difference

Generate a uniform occupied $w$-subset, then add one uniformly chosen unoccupied site. The resulting occupied $(w+1)$-subset is uniform. For a fixed erased $k$-subset, let $J$ count the initially selected occupied sites. Conditional on $J=a$, the count increases by one with probability $(k-a)/(n-w)$. Thus the cumulative distribution functions obey

```math
F_w(a)-F_{w+1}(a)=P_w(a)\frac{k-a}{n-w}.
```

On their common support, the likelihood ratio is

```math
\frac{P_{w+1}(a)}{P_w(a)}
=\frac{(w+1)(n-k-w+a)}{(n-w)(w+1-a)}.
```

It crosses one only once, at $a=k(w+1)/(n+1)$. The endpoint masses have the same single-crossing order. Therefore total variation equals the maximum cumulative difference. Finally, counting factorials gives

```math
P_w(a)\frac{k-a}{n-w}
=\frac{k}{n}\frac{\binom wa\binom{n-1-w}{k-1-a}}{\binom{n-1}{k-1}},
```

which proves the identity. A mode is

```math
a_* =\left\lfloor\frac{k(w+1)}{n+1}\right\rfloor;
```

when two adjacent modes tie, either gives the same mass. Degenerate endpoint distributions are covered by the binomial-zero convention. At $k=0$, $d_{n,0}(w)=0$ separately.

## Finite offsets need not be central

Central adjacent sectors optimize the leading extensive-erasure constant, not necessarily this finite bound. For example,

```math
d_{11,3}(5)=\frac5{33},
\qquad
d_{11,3}(3)=\frac7{55}<\frac5{33}.
```

This is a comparison of converse values, not an assertion that a finite encoder saturates either value. The [asymptotic proof](asymptotic_optimum.md) handles the optimization over all offsets without assuming finite-size central optimality.
