# Optimizing the extensive-erasure law

The [charge converse](charge_converse.md) and [random construction](random_construction.md) leave one essential step: optimize over every admissible charge offset, rather than assume the central sectors are always best. The finite mode oscillations make this distinction necessary.

## Interior offsets

Let $k/n\to\alpha\in(0,1)$ and $w/n\to\beta\in(0,1)$. By the exact modal identity,

```math
d_{n,k}(w)=\frac{k}{n}\max_a h_{n,k,w}(a),
\qquad
h_{n,k,w}(a)=
\frac{\binom wa\binom{n-1-w}{k-1-a}}{\binom{n-1}{k-1}}.
```

The mode is $a_*=\lfloor k(w+1)/(n+1)\rfloor$, within $O(1)$ of the mean $(k-1)w/(n-1)$. At the mode, all four entries of the associated $2\times2$ sampling table are linear in $n$. Applying

```math
\log(m!)=(m+\tfrac12)\log m-m+\tfrac12\log(2\pi)+O(m^{-1})
```

to the binomial ratio gives

```math
\max_a h_{n,k,w}(a)
=\frac{1+o(1)}{
\sqrt{2\pi n\alpha(1-\alpha)\beta(1-\beta)}}.
```

One can see the cancellation explicitly by setting $M=n-1$, $s=(k-1)/M$, and $t=w/M$. The mode has $a=Mst+O(1)$; the four factorial arguments are $Mst$, $Mt(1-s)$, $Ms(1-t)$, and $M(1-s)(1-t)$, each up to $O(1)$. Their entropy terms cancel those of the marginals. A bounded displacement from the mean changes the log mass by $O(M^{-1})$, and the remaining square-root factors give $[2\pi M s(1-s)t(1-t)]^{-1/2}(1+o(1))$.

It follows that

```math
\sqrt n\,d_{n,k}(w)
\longrightarrow
\sqrt{\frac{\alpha}{2\pi(1-\alpha)\beta(1-\beta)}}.
```

Among fixed interior fillings, the minimum occurs at $\beta=1/2$, with value $\sqrt{2\alpha/[\pi(1-\alpha)]}$.

## Offsets approaching the edge

The preceding Stirling expansion is not used at vanishing filling. If $w/n\to0$ or $1$, the hypergeometric variance is

```math
\sigma^2=(k-1)\frac{w}{n-1}
\left(1-\frac{w}{n-1}\right)\frac{n-k}{n-2}=o(n).
```

For positive $\sigma$, Chebyshev's inequality places at least three quarters of the probability within distance $2\sigma$ of the mean. That interval contains at most $4\sigma+2$ integers, so

```math
\max_a h_{n,k,w}(a)\ge\frac{3}{4(4\sigma+2)}.
```

For $\sigma=0$, the maximum mass is one. In either case, $\sqrt n\max_a h_{n,k,w}(a)\to\infty$. Thus edge offsets cannot lower the leading constant.

For a minimizing sequence of offsets, choose a subsequence on which $w/n$ converges. Compactness places its limit either in the interior, where the Stirling bound applies, or at an edge, where the scaled bound diverges. This proves

```math
\liminf_{n\to\infty}\sqrt n\min_w d_{n,k}(w)
\ge\sqrt{\frac{2\alpha}{\pi(1-\alpha)}}.
```

This subsequence argument avoids assuming a uniform local central limit theorem up to the charge boundaries.

## Matching upper bound for odd length

For odd $n$, choose $w=(n-1)/2$. The modal formula has variance

```math
\sigma^2=\frac{(k-1)(n-k)}{4(n-2)}.
```

Its asymptotic distance is

```math
d_{n,k}\bigl((n-1)/2\bigr)
=\sqrt{\frac{2\alpha}{\pi(1-\alpha)n}}+o(n^{-1/2}).
```

For fixed $0<\alpha<1/2$, the construction adds only $2\delta_{n,k}=\exp[-\Omega_\alpha(n)]$. With probability tending to one, one sampled code and its explicit decoders attain this bound for every erased subset of size $k$. The existential upper bound therefore matches the universal lower bound.

## Even length and fewer erasures

For even $n$, take the odd-length construction on $n'=n-1$ active qubits and append one fixed $|0\rangle$ spectator. For all sufficiently large $n$, $k=\lfloor\alpha n\rfloor<(n-1)/2$. Choose the active code that handles every $k$-subset of its $n'$ qubits.

If the spectator survives, discard it and apply the active decoder. If it was erased, only $k-1$ active qubits were erased; discard one additional known active survivor and apply the decoder for the resulting $k$-subset. The extra discard is an allowed operation and uses no information about the logical input. Since $k/n'\to\alpha$ and $n'/n\to1$, the leading constant is unchanged.

The same padding of an erased set by voluntarily discarded survivors shows that a code guaranteed for every size-$k$ erased subset also gives that success guarantee for every smaller known erased subset. This does not assume that the originally chosen decoder for a smaller subset has any special optimality property.

Combining the converse and both parity constructions proves the [main theorem](model.md). It is an optimal **leading asymptotic law**, not an exact finite-size formula for $f^*_{n,k}$.
