# The Cioabă–Guo–Haemers conjecture for cyclic Steiner triple systems: the block graph of every cyclic STS(v), v ≡ 1 (mod 12), is class 1

*Public copy of the proof, 2026-11-27. This is the proof text of release commit `0dcf830` of the private research repository. The review-process header and references to files outside this package have been removed, and the pre-review status labels have been replaced by the final ones. No mathematical step has changed. The review record is in [`REVIEWS.md`](REVIEWS.md).*

**Completeness.** The argument is complete: no step failed, and no step is left as a gap. It rests on one published theorem that is not re-proved here: Alspach's 1983 classification of Hamiltonian generalised Petersen graphs, in the form stated as Theorem 1.1 of Bonvicini–Pisanski 2017 (§4.1). It is used only for the cubic pieces whose components are generalised Petersen graphs. The pieces whose components are *proper* I-graphs are 3-edge-coloured by an explicit formula, Lemma N1, proved by hand in this file. Everything else is proved in this file. One lemma (Lemma G) is proved by a finite table of 17 checks, printed in full below; the table is certified by two independent programs and checked by the Lean kernel (§11). Watkins 1969 could not be read (see §4.3) and is **not** used by the main line of the proof.

**Proper I-graph pieces.** With $F_0$ and $\sigma$ arbitrary as in §7, pieces whose components are *proper* I-graphs (connected I-graphs that are not generalised Petersen graphs) can occur only when $v$ has at least two distinct prime divisors; the first such $v\equiv1\pmod{12}$ is $85$ (for example $I(85,5,17)$, §8; see Lemma N1, *Smallest cases*). For prime and prime-power $v$ there are none. Whether they can always be avoided by the choice of $F_0$ and $\sigma$ is not determined here, and it is not needed: Lemma N1 colours them. That every proper I-graph is 3-edge-colourable is already known: Bonvicini and Pisanski record it as a consequence of their Theorem 1.2 (§4.1). Lemma N1 gives an explicit colouring, so that this step does not depend on their case analysis (their Lemma 6.5, drawn in figures). Their route is an independent alternative (§4.1, and Lemma D, Remark (iv)); it is **not** load-bearing.

**Status legend.** Every step carries one of these words.

| Word | Meaning here |
| --- | --- |
| proved | Proved in this file. The whole file passed the project's review rule (AI referees on three models; see [`REVIEWS.md`](REVIEWS.md)). |
| cited | A published theorem, used as stated. The statement was read in the source named, at the place named. Not re-proved here. |
| certified | A finite exact computation, done by two independent programs that agree, with archived output in [`cert/`](cert/). |
| numerical | Finite computer evidence. Corroboration only: no step of the proof depends on it. |

The one computational step, the 17-window table of Lemma G, is **certified** (§11), and the same finite table is checked by the Lean 4 kernel ([`LEAN.md`](LEAN.md)). The theorem as a whole is not formalized.

## 1. The conjecture, and what is claimed

Source: S. M. Cioabă, K. Guo, W. H. Haemers, *The chromatic index of strongly regular graphs*, [arXiv:1810.06660](https://arxiv.org/abs/1810.06660); Ars Math. Contemp. 20 (2021) 187–194, [doi:10.26493/1855-3974.2435.ec9](https://doi.org/10.26493/1855-3974.2435.ec9). Verbatim (identical in arXiv v1, v2 and the journal; see [`LITERATURE_CHECK.md`](LITERATURE_CHECK.md)):

> **Conjecture 1.2.** Except for the Petersen graph, every connected SRG of even order is class 1.

For Steiner triple systems this was posed earlier: Darijani, Pike and Poulin (DPP), *The chromatic index of block intersection graphs of Kirkman triple systems and cyclic Steiner triple systems*, [Australas. J. Combin. 69 (2017) 145–158](https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p145.pdf), Conjecture 1.3: every STS($v$) with $v\equiv 1$ or $9 \pmod{12}$ has a class 1 block intersection graph.

**Claimed here (Theorem 1, §3):** the block graph of every cyclic STS($v$) with $v\equiv 1\pmod{12}$ is class 1, where *cyclic* means the normal form of §2 item 4. This is the conclusion of DPP's Theorem 3.1, for cyclic systems in the normal form that DPP assume in their §3, without the hypothesis $\varphi(v)/(v-1)\ge 2/3$. DPP's own definition of *cyclic* (p. 147) is a priori weaker. Remark 4 shows that the two notions give the same systems whenever $v$ has at most three distinct prime divisors, in particular for every $v<5005$. Theorem 1 does not depend on Remark 4. It is a special case of both conjectures; neither conjecture is proved. §9 lists what is not covered.

## 2. Definitions and conventions

1. **Class 1.** A graph $G$ is class 1 if its chromatic index equals its maximum degree. For a $k$-regular graph this holds if and only if $E(G)$ is a disjoint union of $k$ perfect matchings (a *1-factorization*): in a proper edge colouring with $k$ colours every vertex sees all $k$ colours, so every colour class is a perfect matching, and conversely. This is the convention of the source (§1).
2. **STS.** A Steiner triple system STS($v$) is a set $V$ of $v$ points with a set $\mathcal B$ of 3-subsets (blocks) such that every pair of points lies in exactly one block. Two distinct blocks share at most one point. There are $v(v-1)/6$ blocks, and every point lies in $(v-1)/2$ blocks.
3. **Block graph** (block intersection graph). Vertices are the blocks; two distinct blocks are adjacent when they share a point. It is a simple graph.
4. **Cyclic.** In this file an STS($v$) is *cyclic* if it has an automorphism that permutes the points in a single cycle of length $v$. Relabelling the points gives $V=\mathbb Z_v$ and $\mathcal B+1=\mathcal B$, where $B+i=\{x+i : x\in B\}$ (the *normal form*). Theorem 1 is proved for this notion.

   The DPP journal paper itself (p. 147) defines an STS($v$) to be cyclic when its automorphism group contains a cyclic subgroup of order $v$. At the start of its §3 it then assumes the normal form without loss of generality. Darijani's thesis has the same wording (p. 6) and the same assumption (§2.2). (Two AI referees independently confirmed the p. 147 wording in the journal PDF.) Every system that is cyclic in our sense is cyclic in DPP's sense. The converse holds when $v$ has at most three distinct prime divisors (Remark 4); for other $v$ we do not know. See §12, note 1.
5. **Notation.** Throughout, $v\equiv 1\pmod{12}$, $v\ge 13$, and

```math
h=\frac{v-1}{2},\qquad N=\frac{v-1}{6},\qquad k=\frac{3(v-3)}{2}.
```

   For $t\in\mathbb Z_v$ let $\lVert t\rVert=\min(t \bmod v,\ (-t) \bmod v)\in\{0,1,\dots,h\}$. So $\lVert t\rVert=\lVert -t\rVert$, and $\lVert t\rVert=0$ only for $t=0$.
6. **I-graphs** (definition of Bonvicini–Pisanski, §1). Let $n\ge 3$ and $1\le p,q\le n-1$ with $p,q\ne n/2$. The graph $I(n,p,q)$ has vertices $w_i,x_i$ ($i\in\mathbb Z_n$) and edges

```math
w_iw_{i+p}\ \ (\text{outer rim}),\qquad w_ix_i\ \ (\text{spokes}),\qquad x_ix_{i+q}\ \ (\text{inner rim}),\qquad i\in\mathbb Z_n .
```

   It is a simple cubic graph with $2n$ vertices and $3n$ edges (the conditions on $p,q$ make each rim a 2-regular graph on $n$ vertices). The *generalised Petersen graph* is $G(n,q)=I(n,1,q)$. The Petersen graph is $G(5,2)$.
7. **3-edge-colourable** means: has a proper edge colouring with 3 colours. For a cubic graph each colour class is then a perfect matching.

## 3. Statements

**Theorem 1.** Let $v\equiv 1\pmod{12}$, $v\ge 13$, and let $(\mathbb Z_v,\mathcal B)$ be a cyclic STS($v$). Then its block graph $G$ is class 1: $E(G)$ is a disjoint union of $k=3(v-3)/2$ perfect matchings. **Status: proved** (depends on one cited theorem, Alspach's theorem as stated in Bonvicini–Pisanski, §4.1).

**Remark 2 (relation to Conjecture 1.2).** $G$ is a connected strongly regular graph with parameters $(v(v-1)/6,\ 3(v-3)/2,\ (v+3)/2,\ 9)$ of even order, and it is not the Petersen graph (it has at least 26 vertices). So Theorem 1 confirms Conjecture 1.2 for these graphs. Proof of the parameters, for completeness (classical; **proved**): the degree is computed in Lemma A(5). If two blocks $B,B'$ share the point $x$, a common neighbour either contains $x$, or meets $B$ in a point $a\ne x$ and $B'$ in a point $a'\ne x$ and is then the block through $a$ and $a'$. There are $(v-1)/2-2$ of the first kind. The 4 blocks of the second kind are pairwise distinct and miss $x$, because a block containing two points of $B$ is $B$ and a block containing two points of $B'$ is $B'$. That gives $(v-5)/2+4=(v+3)/2$. If $B\cap B'=\emptyset$, the common neighbours are exactly the 9 blocks through one point of $B$ and one of $B'$, pairwise distinct for the same reason. Since any two non-adjacent vertices have a common neighbour, $G$ is connected. The order $v(v-1)/6=vN$ is even because $N$ is even.

**Corollary 3.** Every cyclic STS($v$) with $v\equiv 1$ or $9\pmod{12}$ has a class 1 block graph. **Status: proved for $v\equiv1$ (Theorem 1); cited for $v\equiv9$** (DPP Theorem 4.1 = Darijani's thesis, Theorem 2.3.1; statement read in the thesis, proof not checked here).

**Remark 4 (the two readings of "cyclic"). Status: proved; not used in the proof of Theorem 1.** Let $v$ have at most three distinct prime divisors. If the automorphism group of an STS($v$) contains an element $g$ of order $v$, then $g$ is a $v$-cycle on the points. So for such $v$ the systems that are cyclic in DPP's sense (p. 147) are exactly those that are cyclic in the sense of §2 item 4, and Theorem 1 covers them all. The smallest $v\equiv1\pmod{12}$ with four distinct prime divisors is $5005=5\cdot7\cdot11\cdot13$ (a $v\equiv1\pmod{12}$ is prime to 6, and $5005=12\cdot417+1$). In particular it holds at $v=385=5\cdot7\cdot11$, which DPP report as the smallest $v\equiv1\pmod{12}$ where the hypothesis of their Theorem 3.1 fails (§9).

*Proof.* (a) *Fixed points.* Let $\varphi\ne\mathrm{id}$ be an automorphism and $F$ its set of fixed points. If $a,b\in F$, the third point of the block through $a,b$ is fixed too. So $F$ is closed: a block with two points in $F$ lies in $F$. Suppose $|F|\ge2$ and take $z\notin F$ (possible since $\varphi\ne\mathrm{id}$). For $a\in F$ let $c_a$ be the third point of the block through $z$ and $a$. Then $c_a\notin F$ (else $z\in F$ by closure), $c_a\ne z$, and $c_a\ne c_b$ for $a\ne b$ (the block through $z$ and $c_a$ is unique). So $v\ge|F|+1+|F|$, that is $|F|\le(v-1)/2$. This also holds when $|F|\le1$, as $v\ge3$.

(b) Let $g$ have order $v$ and suppose $g$ has no cycle of length $v$. The cycle lengths divide $v$, so each is a proper divisor of $v$, and each point $x$ lies in a cycle whose length divides $v/p$ for some prime $p\mid v$; then $x$ is fixed by $g^{v/p}$, which is not the identity. Write $F_p$ for the fixed set of $g^{v/p}$. The sets $F_p$ ($p\mid v$ prime) cover the points, each has at most $(v-1)/2$ points by (a), and each is a union of cycles of $g$.

- One prime: $v\le(v-1)/2$, impossible.
- Two primes: $v\le(v-1)/2+(v-1)/2$, impossible.
- Three primes $p,q,r$, with $v=p^aq^br^c$: put $A=F_p$, $B=F_q$, $C=F_r$, and let $A_0$ be the points in $A$ only, and so on. Since $|A\cup B|\le v-1$, some point lies in $C$ only, so $C_0\ne\emptyset$; likewise $A_0,B_0\ne\emptyset$. Take $x\in A_0$ and $z\in B_0$, and let $y$ be the third point of their block. If $y\in A$ then $z\in A$ by closure of $A$, which is false; so $y\notin A$, likewise $y\notin B$, and $y\in C_0$. For fixed $x$ the map $z\mapsto y$ is injective (the block through $x$ and $y$ is unique), so $|B_0|\le|C_0|$. By symmetry $|A_0|=|B_0|=|C_0|=:n_0>0$. A point of $A_0$ lies in a cycle whose length $\ell$ divides $v/p$ but neither $v/q$ nor $v/r$; hence $q^b\mid\ell$ and $r^c\mid\ell$. $A_0$ is a union of such cycles, so $q^br^c\mid n_0$. Symmetrically $p^ar^c\mid n_0$ and $p^aq^b\mid n_0$, so $v\mid n_0$. But $3n_0\le v$, a contradiction. $\square$

*Credit.* The argument was suggested by an AI referee in this project's review process (2026-11-27) and was written out and checked.

## 4. Results used from the literature

### 4.1 Bonvicini–Pisanski: Theorem 1.1 (Alspach's theorem; the only external theorem in the main line) and Theorem 1.2 (alternative route, not load-bearing). Status: cited

S. Bonvicini, T. Pisanski, *A novel characterization of cubic Hamiltonian graphs via the associated quartic graphs*, Ars Math. Contemp. 12 (2017) 1–24, [doi:10.26493/1855-3974.921.b14](https://doi.org/10.26493/1855-3974.921.b14); [arXiv:1508.01865](https://arxiv.org/abs/1508.01865). Read: the journal galley and arXiv v1, both at §1 (definitions and the two theorems below), the proposition on I-graph parameters, and §7 (proof of the main theorem and the paragraph after it). The statements quoted here agree word for word in the two versions.

**Numbering.** All theorem numbers in this file are those of the journal version (AMC 12 (2017) 1–24). arXiv:1508.01865v1 numbers the same results consecutively:

| Journal (AMC 2017) | arXiv v1 |
| --- | --- |
| Theorem 1.1 (Alspach) | Theorem 1 |
| Theorem 1.2 (main theorem) | Theorem 2 |
| Theorem 2.2 | Theorem 4 |
| Proposition 3.4 | Proposition 10 |
| Lemma 3.5 | Lemma 11 |
| Lemma 5.1 | Lemma 24 |
| Lemmas 6.1, 6.2 | Lemmas 27, 28 |
| Proposition 6.4 | Proposition 30 |
| Lemma 6.5 | Lemma 31 |

- **Definition there (§1).** $I(n,p,q)$ exactly as in §2 item 6, with the outer rim called $v_i$ and the inner rim $u_i$ there (our $w_i$ and $x_i$): $n\ge3$, $1\le p,q\le n-1$, $p,q\ne n/2$; $G(n,q)=I(n,1,q)$.
- **Theorem 1.1 there (Alspach).** A generalised Petersen graph $G(n,q)$ is Hamiltonian if and only if it is not isomorphic to $G(n,2)$ when $n\equiv 5\pmod 6$. It is cited there from B. Alspach, J. Combin. Theory Ser. B 34 (1983) 293–312, [doi:10.1016/0095-8956(83)90042-4](https://doi.org/10.1016/0095-8956(83)90042-4). **Alspach's paper was not read by us**; we use the statement as printed in Bonvicini–Pisanski.
- **What we use (main line).** Only this: if $1\le\kappa\le m-1$, $\kappa\ne m/2$, and $G(m,\kappa)$ has no Hamilton cycle, then $m\equiv 5\pmod 6$ and $G(m,\kappa)\cong G(m,2)$.
- **Hypotheses in our use.** We apply it in Lemma D, Case 2, to $G(m,\kappa)$ with $m\ge3$, $1\le\kappa\le m-1$ and $\kappa\ne m/2$. These are exactly the conditions of the definition there, so the hypotheses hold. (In the application to Theorem 1, $m$ is odd and $m\ge5$; see Lemma D′. Only $m\ge3$ is needed here.)
- **Theorem 1.2 there (not load-bearing).** A connected I-graph is Hamiltonian if and only if it is not isomorphic to $G(n,2)$ when $n\equiv 5\pmod 6$. For generalised Petersen graphs the proof there is Theorem 1.1. For the remaining connected I-graphs ("proper" I-graphs) Hamiltonicity is proved in the paper itself (§7 there, from its Theorem 2.2 and Lemmas 3.5, 5.1 and 6.5). The load there falls on Lemma 6.5, whose case analysis is drawn in figures. After the proof the authors note that a proper I-graph is therefore 3-edge-colourable, equivalently 1-factorizable (journal §7, p. 20; arXiv v1 §7, p. 23, where the theorem is "Theorem 2"). This is exactly the conclusion of Lemma N1 (§6). Their route is an independent alternative to Lemma N1 (Lemma D, Remark (iv)), and no step of the main line uses it.

### 4.2 Castagna–Prins (independent second source for the generalised Petersen pieces). Status: cited; not needed for the main line

F. Castagna, G. Prins, *Every generalized Petersen graph has a Tait coloring*, Pacific J. Math. 40 (1972) 53–58, [msp.org/pjm/1972/40-1/p07.xhtml](https://msp.org/pjm/1972/40-1/p07.xhtml). Read in full.

- **Definition there.** $n,k$ positive integers, $k\le n-1$, $n\ne 2k$; $G(n,k)$ has rims $(i,i+1)$ and $(i',(i+k)')$ and spokes $(i,i')$. This is $I(n,1,k)$ of §2.
- **Result there** (title and abstract): every generalised Petersen graph other than the Petersen graph $G(5,2)$ has a Tait colouring (a proper 3-edge-colouring).
- **Division of the proof.** The paper itself proves the cases $n$ odd, $n>7$, $\gcd(n,k)=1$, $2<k<(n-1)/2$, and states that all other cases were dealt with by Watkins.

### 4.3 Watkins 1969. Status: not read; not used

M. E. Watkins, *A theorem on Tait colorings with an application to the generalized Petersen graphs*, J. Combin. Theory 6 (1969) 152–164, [doi:10.1016/S0021-9800(69)80116-X](https://doi.org/10.1016/S0021-9800(69)80116-X). On 2026-11-27 the publisher page and its PDF link returned HTTP 403, and no other full text was reached. No statement from this paper is quoted, because none could be checked. The cases that Castagna–Prins delegate to Watkins include $k\le 2$, which is exactly the family $G(n,2)$ that the main line needs. For that reason the main line does **not** go through Castagna–Prins: it uses Theorem 1.1 of §4.1 and a direct colouring of $G(n,2)$ (Lemma G). §4.2 is kept as an independent published confirmation for the generalised Petersen pieces, and it is the result DPP themselves use.

### 4.4 Not needed

The Boben–Pisanski–Žitnik criteria (J. Combin. Des. 13 (2005), [doi:10.1002/jcd.20054](https://doi.org/10.1002/jcd.20054)) — an I-graph is connected iff $\gcd(n,p,q)=1$; it is a generalised Petersen graph iff $\gcd(n,p)=1$ or $\gcd(n,q)=1$ — are **not** used. The one direction needed (connectedness when the gcd is 1) is proved in Lemma C.

## 5. Structure of the block graph

Fix a cyclic STS $(\mathbb Z_v,\mathcal B)$ with $v\equiv1\pmod{12}$, $v\ge13$, and its block graph $G$. The *orbit* of a block $B$ is $\{B+i : i\in\mathbb Z_v\}$. Choose one *base block* $B_P$ in each orbit $O_P$.

### Lemma A (orbits, differences, edges). Status: proved

1. Every orbit has exactly $v$ blocks, the blocks $B_P+i$ ($i\in\mathbb Z_v$) are pairwise distinct, and there are exactly $N$ orbits $O_1,\dots,O_N$. $N$ is even.
2. For a block $B$ let $\Delta(B)$ be the list of its six ordered differences $a-b$ ($a,b\in B$, $a\ne b$), and $D(B)=\{\lVert t\rVert : t\in\Delta(B)\}$. Then every non-zero element of $\mathbb Z_v$ occurs exactly once in the concatenated list $\Delta(B_1),\dots,\Delta(B_N)$. Consequently each $D_P:=D(B_P)$ has exactly 3 elements, and $D_1,\dots,D_N$ partition $\{1,\dots,h\}$.
3. (Inside an orbit.) For $i\ne j$: $B_P+i$ and $B_P+j$ are adjacent if and only if $\lVert j-i\rVert\in D_P$. For $d\in D_P$ put

```math
R_P(d)=\{\ \{B_P+i,\ B_P+i+d\} : i\in\mathbb Z_v\ \}.
```

   Each $R_P(d)$ is a set of $v$ edges forming a 2-regular spanning subgraph of $G[O_P]$; the three sets $R_P(d)$, $d\in D_P$, are pairwise disjoint and their union is $E(G[O_P])$.
4. (Between orbits.) For $P\ne Q$ put $S_{PQ}=\{a-b : a\in B_P,\ b\in B_Q\}\subseteq\mathbb Z_v$. Then $|S_{PQ}|=9$, and $B_P+i$ is adjacent to $B_Q+j$ if and only if $j-i\in S_{PQ}$. For $s\in S_{PQ}$ put

```math
\mu^{PQ}_s=\{\ \{B_P+i,\ B_Q+i+s\} : i\in\mathbb Z_v\ \}.
```

   Each $\mu^{PQ}_s$ is a perfect matching of $O_P\cup O_Q$; the nine sets are pairwise disjoint and their union is the set of all edges of $G$ between $O_P$ and $O_Q$.
5. $G$ is regular of degree $6+9(N-1)=k$, and $E(G)$ is the disjoint union of all $R_P(d)$ and all $\mu^{PQ}_s$ ($P<Q$).

*Proof.* (1) Suppose $B+t=B$ with $t\ne0$. Then $x\mapsto x+t$ permutes the three points of $B$ without a fixed point, so it is a 3-cycle on $B$, and $x+3t=x$ for $x\in B$. Hence $3t=0$ in $\mathbb Z_v$; as $\gcd(3,v)=1$, $t=0$, a contradiction. So every orbit has $v$ distinct blocks. There are $v(v-1)/6$ blocks, hence $(v-1)/6=N$ orbits. Writing $v=12m+1$ gives $N=2m$.

(2) Let $t\ne0$. The pair $\{0,t\}$ lies in a block, which is $B_P+i$ for some $P$ and $i$. Then $-i$ and $t-i$ lie in $B_P$, and their difference is $t$. So every one of the $v-1$ non-zero elements occurs at least once in a list of total length $6N=v-1$. Hence each occurs exactly once. In particular the six elements of $\Delta(B_P)$ are distinct. $\Delta(B_P)$ is closed under $t\mapsto -t$, and $t\ne -t$ because $v$ is odd, so the six elements form three pairs $\{t,-t\}$ and $|D_P|=3$. Every $d\in\{1,\dots,h\}$ lies in exactly one $\Delta(B_P)$, hence in exactly one $D_P$.

(3) $B_P+i$ and $B_P+j$ share a point iff $a+i=b+j$ for some $a,b\in B_P$, i.e. iff $i-j=b-a$; here $a\ne b$ because $i\ne j$. That is: iff $i-j\in\Delta(B_P)$, iff $\lVert j-i\rVert\in D_P$. Now fix $d\in D_P$. The edges $\{B_P+i,B_P+i+d\}$, $i\in\mathbb Z_v$, are pairwise distinct: if $\{i,i+d\}=\{j,j+d\}$ with $i\ne j$ then $i=j+d$ and $i+d=j$, so $2d=0$ and $d=0$ ($v$ odd), impossible. The vertex $B_P+i$ lies in exactly two of them (indices $i$ and $i-d$). An edge $\{B_P+i,B_P+j\}$ of $G[O_P]$ lies in $R_P(d)$ exactly for $d=\lVert j-i\rVert$, which gives disjointness and the union.

(4) $B_P+i$ and $B_Q+j$ share a point iff $a+i=b+j$ for some $a\in B_P$, $b\in B_Q$, i.e. iff $j-i=a-b\in S_{PQ}$. Suppose $a-b=a'-b'$ with $(a,b)\ne(a',b')$. If $a=a'$ then $b=b'$; so $a\ne a'$, and likewise $b\ne b'$. Then $a-a'=b-b'$ is a non-zero element lying in both $\Delta(B_P)$ and $\Delta(B_Q)$, contradicting (2). So the nine differences are distinct. For fixed $s$, the map $B_P+i\mapsto B_Q+i+s$ is a bijection $O_P\to O_Q$ by (1), so $\mu^{PQ}_s$ is a perfect matching of $O_P\cup O_Q$. The edge $\{B_P+i,B_Q+j\}$ lies in $\mu^{PQ}_s$ exactly for $s=j-i$.

(5) By (3) a vertex has 6 neighbours in its own orbit, and by (4) it has 9 in each of the other $N-1$ orbits. $6+9(N-1)=9N-3=\tfrac{3(v-1)}{2}-3=k$. The decomposition of $E(G)$ is (3) and (4) together. $\square$

*Smallest case, by hand ($v=13$).* Base blocks $\{0,1,4\}$ and $\{0,2,7\}$ (the system used as the example in DPP). $\Delta=\{1,12,4,9,3,10\}$ and $\{2,11,7,6,5,8\}$: all twelve non-zero residues once. $D_1=\{1,3,4\}$, $D_2=\{2,5,6\}$. $S_{12}=\{0,11,6,1,12,7,4,2,10\}$, nine distinct values. Degree $6+9=15=k$.

### Lemma B (the cubic pieces are I-graphs). Status: proved

Let $P\ne Q$, $d\in D_P$, $e\in D_Q$, $s\in S_{PQ}$. The subgraph of $G$ with vertex set $O_P\cup O_Q$ and edge set

```math
\Gamma=R_P(d)\ \cup\ \mu^{PQ}_s\ \cup\ R_Q(e)
```

is isomorphic to $I(v,d,e)$, and $1\le d,e\le h$, $d\ne e$.

*Proof.* $d,e\in\{1,\dots,h\}$ and $d\ne e$ by Lemma A(2) ($D_P\cap D_Q=\emptyset$). Since $h<v/2$, the triple $(v,d,e)$ satisfies the conditions of §2 item 6. Map $w_i\mapsto B_P+i$ and $x_i\mapsto B_Q+i+s$; this is a bijection onto $O_P\cup O_Q$ by Lemma A(1). It sends the outer rim $\{w_iw_{i+d}\}$ onto $R_P(d)$, the spokes $\{w_ix_i\}$ onto $\mu^{PQ}_s$, and the inner rim edge $x_ix_{i+e}$ to $\{B_Q+(i+s),B_Q+(i+s)+e\}$; as $i$ runs over $\mathbb Z_v$ these are exactly the edges of $R_Q(e)$. $\square$

## 6. Colouring the pieces

### Lemma C (components of an I-graph). Status: proved

Let $I(n,p,q)$ be as in §2 item 6, with $1\le p,q<n/2$, and let $g=\gcd(n,p,q)$. Then $I(n,p,q)$ is the vertex-disjoint union of $g$ subgraphs, each isomorphic to $I(n/g,\ p/g,\ q/g)$, and $I(n/g,p/g,q/g)$ is connected. (So an I-graph with $\gcd(n,p,q)=1$ is connected.)

*Proof.* First, $(n/g,p/g,q/g)$ is admissible: $1\le p/g<(n/g)/2$ gives $n/g>2$, and the same bound holds for $q/g$. Since $g$ divides $n$, the residue $i \bmod g$ of an index $i\in\mathbb Z_n$ is well defined, and since $g$ divides $p$ and $q$, every edge joins two vertices whose indices have the same residue mod $g$. For $r\in\{0,\dots,g-1\}$ the map $w'_t\mapsto w_{r+gt}$, $x'_t\mapsto x_{r+gt}$ ($t\in\mathbb Z_{n/g}$) is well defined, is a bijection onto the vertices with index $\equiv r\pmod g$, and sends the edges $w'_tw'_{t+p/g}$, $w'_tx'_t$, $x'_tx'_{t+q/g}$ of $I(n/g,p/g,q/g)$ onto the edges $w_iw_{i+p}$, $w_ix_i$, $x_ix_{i+q}$ with $i=r+gt$. So the vertices of residue $r$ induce a copy of $I(n/g,p/g,q/g)$, and there are no edges between different residues.

Connectedness when $\gcd(m,a,b)=1$, for $I(m,a,b)$: from $w_i$ one reaches $w_{i+a}$ along the outer rim, and $w_{i+b}$ by the path $w_i,x_i,x_{i+b},w_{i+b}$. So $w_0$ reaches every $w_t$ with $t$ in the subgroup of $\mathbb Z_m$ generated by $a$ and $b$, which is all of $\mathbb Z_m$ because $\gcd(m,a,b)=1$; and every $x_t$ is adjacent to $w_t$. $\square$

*Smallest case.* $I(15,3,6)$: $g=3$, three copies of $I(5,1,2)$. In the range of Theorem 1 the smallest disconnected piece is $I(25,5,10)$: five copies of $I(5,1,2)$.

### Lemma G ($G(n,2)$ for $n\equiv5\pmod 6$, $n\ge11$). Status: proved; the 17-row table is certified and checked by the Lean kernel (§11)

For every integer $j\ge0$ the graph $G(11+6j,2)$ is 3-edge-colourable.

*Proof.* Let $n\ge5$. The edges of $G(n,2)=I(n,1,2)$ are $w_iw_{i+1}$, $w_ix_i$, $x_ix_{i+2}$ ($i\in\mathbb Z_n$), all distinct. An edge colouring with colours $1,2,3$ is the same thing as a cyclic sequence $t_0,\dots,t_{n-1}$ of *symbols* $t_i=(O_i,S_i,I_i)\in\{1,2,3\}^3$, where

```math
O_i=\text{colour of }w_iw_{i+1},\qquad S_i=\text{colour of }w_ix_i,\qquad I_i=\text{colour of }x_ix_{i+2}.
```

The edges at $w_i$ are $w_{i-1}w_i$, $w_iw_{i+1}$, $w_ix_i$, and the edges at $x_i$ are $w_ix_i$, $x_ix_{i+2}$, $x_{i-2}x_i$ (three distinct edges in each case, as $n\ge5$). So the colouring is proper if and only if for every $i\in\mathbb Z_n$ the *window* $(t_{i-2},t_{i-1},t_i)$ is *good*, meaning

```math
O_{i-1},\ O_i,\ S_i\ \text{ pairwise distinct}\qquad\text{and}\qquad S_i,\ I_i,\ I_{i-2}\ \text{ pairwise distinct}.
```

Write a symbol as a 3-digit string $OSI$. Define three words:

| Word | Length | Symbols (each is $O_iS_iI_i$) |
| --- | --- | --- |
| $X$ | 7 | 321, 123, 232, 312, 213, 313, 121 |
| $Y$ | 4 | 321, 123, 323, 121 |
| $Z$ | 6 | 321, 123, 232, 312, 213, 131 |

All three begin with the same two symbols $\pi=321$, $\rho=123$. For a word $W$ let $W^+=W\pi\rho$ (the word followed by these two symbols), indexed from 0.

*Table.* Every window $(t_{i-2},t_{i-1},t_i)$ of $X^+$, $Y^+$, $Z^+$, i.e. $2\le i\le |W|+1$, is good:

| word | $i$ | $t_{i-2}$ | $t_{i-1}$ | $t_i$ | at $w_i$: $O_{i-1},O_i,S_i$ | at $x_i$: $S_i,I_i,I_{i-2}$ |
| --- | --- | --- | --- | --- | --- | --- |
| $X^+$ | 2 | 321 | 123 | 232 | 1,2,3 | 3,2,1 |
| $X^+$ | 3 | 123 | 232 | 312 | 2,3,1 | 1,2,3 |
| $X^+$ | 4 | 232 | 312 | 213 | 3,2,1 | 1,3,2 |
| $X^+$ | 5 | 312 | 213 | 313 | 2,3,1 | 1,3,2 |
| $X^+$ | 6 | 213 | 313 | 121 | 3,1,2 | 2,1,3 |
| $X^+$ | 7 | 313 | 121 | 321 | 1,3,2 | 2,1,3 |
| $X^+$ | 8 | 121 | 321 | 123 | 3,1,2 | 2,3,1 |
| $Y^+$ | 2 | 321 | 123 | 323 | 1,3,2 | 2,3,1 |
| $Y^+$ | 3 | 123 | 323 | 121 | 3,1,2 | 2,1,3 |
| $Y^+$ | 4 | 323 | 121 | 321 | 1,3,2 | 2,1,3 |
| $Y^+$ | 5 | 121 | 321 | 123 | 3,1,2 | 2,3,1 |
| $Z^+$ | 2 | 321 | 123 | 232 | 1,2,3 | 3,2,1 |
| $Z^+$ | 3 | 123 | 232 | 312 | 2,3,1 | 1,2,3 |
| $Z^+$ | 4 | 232 | 312 | 213 | 3,2,1 | 1,3,2 |
| $Z^+$ | 5 | 312 | 213 | 131 | 2,1,3 | 3,1,2 |
| $Z^+$ | 6 | 213 | 131 | 321 | 1,3,2 | 2,1,3 |
| $Z^+$ | 7 | 131 | 321 | 123 | 3,1,2 | 2,3,1 |

(In every row both triples are permutations of 1, 2, 3. The table is a relabelled copy of the output of [`prover/verify_gn2.py`](prover/verify_gn2.py), archived in [`prover/out_verify_gn2.log`](prover/out_verify_gn2.log): the log writes the word as `X^+` without math markup and has an extra `ok` column; the values are the same. It can also be checked by hand.)

*Concatenation.* Let $T=W_1W_2\cdots W_r$ with $r\ge 2$ and each $W_s\in\{X,Y,Z\}$, read cyclically, of total length $n$. We claim every cyclic window of $T$ is good. Take a position $i$ of $T$; it lies in some $W_s$ at offset $c$, $0\le c<|W_s|$. If $c\ge2$, the window $(t_{i-2},t_{i-1},t_i)$ lies inside $W_s$ and is row $c$ of the table for $W_s^+$ (note $c\le |W_s|-1$). If $c\in\{0,1\}$, the window consists of the last $2-c$ symbols of the preceding word $W_{s-1}$ (cyclically; it has length at least 4) followed by the first $c+1$ symbols of $W_s$. Since $W_s$ begins with $\pi\rho$, this is the window at index $|W_{s-1}|+c$ of $W_{s-1}^+$, which is in the table. This proves the claim.

Take $T=XYZ^j$ ($j\ge0$). Its length is $7+4+6j=11+6j=n\ge 11$, and by the claim it defines a proper 3-edge-colouring of $G(n,2)$. $\square$

*Smallest case ($n=11$, $j=0$).* For $i=0,\dots,10$ the colours are: $O_i$ = `3 1 2 3 2 3 1 3 1 3 1`, $S_i$ = `2 2 3 1 1 1 2 2 2 2 2`, $I_i$ = `1 3 2 2 3 3 1 1 3 3 1`. Checked on the explicitly built graph, together with all $n=11+6j$, $j\le200$ (**numerical**, `prover/out_verify_gn2.log`).

### Lemma N1 (an explicit colouring of I-graphs with coprime rim gcds). Status: proved

Let $I(n,p,q)$ be an I-graph (§2 item 6) and put $u=\gcd(n,p)$, $t=\gcd(n,q)$. If $u\ge2$, $t\ge2$ and $\gcd(u,t)=1$, then $I(n,p,q)$ is 3-edge-colourable. In particular, if $\gcd(n,p)\ge2$, $\gcd(n,q)\ge2$ and $\gcd(n,p,q)=1$ (by Bonvicini–Pisanski these are exactly the connected proper I-graphs; only the gcd conditions are used here), then $I(n,p,q)$ is 3-edge-colourable, because $\gcd(u,t)=\gcd(n,p,q)$.

*Credit.* The 3-edge-colourability of every proper I-graph is known: Bonvicini and Pisanski record it (Ars Math. Contemp. 12 (2017), §7, p. 20) as a consequence of their theorem that every connected I-graph other than $G(n,2)$ with $n\equiv 5\pmod 6$ is Hamiltonian. Lemma N1 gives a short explicit 3-edge-colouring of these graphs, so that this step does not depend on their case analysis. The lemma and its colouring were suggested by an AI referee in this project's review process (2026-11-27), and the proof was checked by hand. It is included for self-containment, not as a new result.

*Proof.* Colours are elements of $\mathbb Z_3$.

*Step 1 (two coordinates).* Since $u\mid n$ and $t\mid n$, the residues $i\bmod u$ and $i\bmod t$ of $i\in\mathbb Z_n$ are well defined. Any common divisor of $p$ and $t$ divides $\gcd(n,p)=u$ and $t$, hence divides $\gcd(u,t)=1$; so $p$ is invertible modulo $t$. In the same way $q$ is invertible modulo $u$. Define

```math
x(i)=q^{-1}i \bmod u\ \in\mathbb Z_u,\qquad y(i)=p^{-1}i \bmod t\ \in\mathbb Z_t\qquad(i\in\mathbb Z_n).
```

As $u\mid p$ and $t\mid q$,

```math
x(i+p)=x(i),\qquad y(i+p)=y(i)+1,\qquad x(i+q)=x(i)+1,\qquad y(i+q)=y(i).
```

*Step 2 (proper colourings of the cycles $\mathbb Z_L$).* For $L\ge2$ define $\varepsilon_L:\mathbb Z_L\to\mathbb Z_3$ by $\varepsilon_L(j)=j\bmod2$ for $0\le j\le L-1$, except that $\varepsilon_L(L-1)=2$ when $L$ is odd. Then $\varepsilon_L(j)\ne\varepsilon_L(j-1)$ for every $j\in\mathbb Z_L$. Indeed, for $1\le j\le L-1$ the pair $\varepsilon_L(j-1),\varepsilon_L(j)$ is $(j-1)\bmod 2,\ j\bmod2$, which differ, except when $L$ is odd and $j=L-1$; then the pair is $(L-2)\bmod2=1$ and $2$, which differ. For $j=0$ the pair is $\varepsilon_L(L-1),\varepsilon_L(0)$, which is $1,0$ when $L$ is even and $2,0$ when $L$ is odd. (For $L=2$ the values are $0,1$; for $L=3$ they are $0,1,2$.)

Put, in $\mathbb Z_3$,

```math
r(x)=-\varepsilon_u(x-1)-\varepsilon_u(x)\quad(x\in\mathbb Z_u),\qquad s(y)=-\varepsilon_t(y-1)-\varepsilon_t(y)\quad(y\in\mathbb Z_t).
```

*Step 3 (the colouring).* Each edge of $I(n,p,q)$ has a unique index $i\in\mathbb Z_n$ and type: the outer rim edge $w_iw_{i+p}$, the spoke $w_ix_i$, the inner rim edge $x_ix_{i+q}$. (Uniqueness: $\{w_i,w_{i+p}\}=\{w_j,w_{j+p}\}$ with $i\ne j$ forces $i=j+p$ and $j=i+p$, so $2p\equiv0$ and $p=n/2$, which is excluded; likewise for the inner rim.) With $x=x(i)$, $y=y(i)$, colour

```math
c(w_iw_{i+p})=\varepsilon_t(y)+r(x),\qquad c(x_ix_{i+q})=\varepsilon_u(x)+s(y),\qquad c(w_ix_i)=r(x)+s(y).
```

*Step 4 (an elementary fact).* If $\alpha,\beta\in\mathbb Z_3$ and $\alpha\ne\beta$, then $\alpha$, $\beta$, $-\alpha-\beta$ are pairwise distinct. Indeed $-\alpha-\beta=\alpha$ would give $\beta=-2\alpha=\alpha$, and $-\alpha-\beta=\beta$ would give $\alpha=-2\beta=\beta$.

*Step 5 (vertex $w_i$).* The three edges at $w_i$ are $w_iw_{i+p}$ (index $i$), $w_{i-p}w_i$ (outer rim, index $i-p$) and the spoke $w_ix_i$; they are distinct because the outer rim is 2-regular. Let $x=x(i)$, $y=y(i)$. By Step 1, $x(i-p)=x$ and $y(i-p)=y-1$. With $\alpha=\varepsilon_t(y)$ and $\beta=\varepsilon_t(y-1)$ the three colours are

```math
r(x)+\alpha,\qquad r(x)+\beta,\qquad r(x)+s(y)=r(x)-\beta-\alpha .
```

Since $\alpha\ne\beta$ (Step 2, with $L=t\ge2$), Step 4 shows that they are pairwise distinct.

*Step 6 (vertex $x_i$).* The three edges at $x_i$ are $x_ix_{i+q}$ (index $i$), $x_{i-q}x_i$ (inner rim, index $i-q$) and the spoke $w_ix_i$. By Step 1, $x(i-q)=x-1$ and $y(i-q)=y$. With $\alpha'=\varepsilon_u(x)$ and $\beta'=\varepsilon_u(x-1)$ the three colours are

```math
s(y)+\alpha',\qquad s(y)+\beta',\qquad s(y)+r(x)=s(y)-\beta'-\alpha',
```

pairwise distinct by Step 2 (with $L=u\ge2$) and Step 4.

So every vertex sees three different colours, and $c$ is a proper 3-edge-colouring. $\square$

*Smallest cases.* The smallest $n$ meeting the hypotheses is $n=12$, with $I(12,2,3)$; the smallest odd $n$ is $15$, with $I(15,3,5)$. A proper I-graph $I(m,a,b)$ needs two distinct primes dividing $m$, so in the range of Theorem 1 proper pieces first occur at $v=85=5\cdot17$ (for example the piece $I(85,5,17)$, see §8). The formula was checked on the explicitly built graph for all $119208$ triples $(n,p,q)$ with $n\le200$ meeting the hypotheses, and for all $66141$ connected proper $I(m,a,b)$ with $m$ odd, $m\le601$, $1\le a<b\le(m-1)/2$ (**numerical**, [`prover/verify_N1.py`](prover/verify_N1.py), [`prover/out_verify_N1.log`](prover/out_verify_N1.log)).

### Lemma D (I-graphs with $\gcd(m,a,b)=1$). Status: proved, from Lemma N1, the cited Theorem 1.1 of §4.1 (Alspach) and Lemma G

Let $H=I(m,a,b)$ be an I-graph (so $m\ge3$, $1\le a,b\le m-1$, $a,b\ne m/2$) with $\gcd(m,a,b)=1$. If $m\ne5$, then $H$ is 3-edge-colourable.

*Proof.* Case 1: $\gcd(m,a)\ge2$ and $\gcd(m,b)\ge2$ ($H$ is a proper I-graph). Here $\gcd(\gcd(m,a),\gcd(m,b))=\gcd(m,a,b)=1$, so $H$ is 3-edge-colourable by Lemma N1.

Case 2: $\gcd(m,a)=1$ or $\gcd(m,b)=1$. The map $w_i\leftrightarrow x_i$ is an isomorphism $I(m,a,b)\to I(m,b,a)$ (it exchanges the two rims and fixes the spokes), so we may assume $\gcd(m,a)=1$. Let $c=a^{-1}\bmod m$. The map $w_i\mapsto w_{ci}$, $x_i\mapsto x_{ci}$ is a bijection of the vertex set (as $c$ is a unit) and sends $w_iw_{i+a}$ to $w_{ci}w_{ci+1}$, $w_ix_i$ to $w_{ci}x_{ci}$ and $x_ix_{i+b}$ to $x_{ci}x_{ci+cb}$. So $H\cong G(m,\kappa)=I(m,1,\kappa)$ with $\kappa\equiv cb\pmod m$, $1\le\kappa\le m-1$. Also $\kappa\ne m/2$: otherwise $2cb\equiv0$, so $2b\equiv0\pmod m$ and $b=m/2$, which is excluded. So $G(m,\kappa)$ is a generalised Petersen graph in the sense of §4.1, and Theorem 1.1 of §4.1 applies to it.

- Case 2a: $G(m,\kappa)$ has a Hamilton cycle $C$. It has $2m$ vertices, so $C$ has even length; colour its edges alternately 1 and 2. Every vertex has exactly one edge outside $C$, so the remaining edges form a perfect matching; colour them 3. This is a proper 3-edge-colouring.
- Case 2b: $G(m,\kappa)$ has no Hamilton cycle. By Theorem 1.1 of §4.1, $m\equiv5\pmod 6$ and $G(m,\kappa)\cong G(m,2)$. As $m\ne5$, $m=11+6j$ with $j\ge0$, and $G(m,2)$ is 3-edge-colourable by Lemma G.

In each case the colouring is transported to $H$ by the isomorphism. $\square$

*Remarks.* (i) For $m=5$ the lemma says nothing, and nothing is needed: see Lemma D′. (ii) Independent confirmation for Case 2: $G(m,\kappa)$ is 3-edge-colourable unless it is the Petersen graph, by Castagna–Prins (§4.2). This is the route of DPP. It is not used above (part of its proof is delegated to Watkins 1969, which we could not read). (iii) *Smallest cases.* $m=7$: $I(7,1,2)$, $I(7,1,3)$, $I(7,2,3)$ (all Case 2). The smallest odd $m$ with a Case 1 graph is $m=15$: $I(15,3,5)$. All connected $I(m,a,b)$ with $m$ odd, $m\le25$, $a<b\le(m-1)/2$ (281 graphs) were 3-edge-coloured by exhaustive backtracking except $(5,1,2)$; of these 281, 276 are Case 2 and 5 are Case 1, namely $(15,3,5)$, $(15,5,6)$, $(21,3,7)$, $(21,6,7)$, $(21,7,9)$ (**numerical**, `prover/out_verify_small.log`). (iv) *Alternative route for Case 1, not load-bearing.* A connected proper I-graph is Hamiltonian by Bonvicini–Pisanski Theorem 1.2 (§4.1), and then the argument of Case 2a colours it. It is independent of Lemma N1 and rests on the figure-based Lemma 6.5 there.

### Lemma D′ (which pieces are 3-edge-colourable). Status: proved

Let $v$ be odd, $h=(v-1)/2$, and $1\le d,e\le h$ with $d\ne e$. If $\{d,e\}\ne\{v/5,2v/5\}$ (in particular whenever $5\nmid v$), then $I(v,d,e)$ is 3-edge-colourable.

*Proof.* Let $g=\gcd(v,d,e)$ and $m=v/g$. By Lemma C, $I(v,d,e)$ is a disjoint union of copies of the connected I-graph $I(m,d/g,e/g)$, so it suffices to 3-edge-colour that graph. Here $m$ is odd (it divides $v$), and $a=d/g$, $b=e/g$ satisfy $1\le a,b\le(m-1)/2$ (since $a\le h/g<m/2$) and $a\ne b$. Two distinct integers in $\{1,\dots,(m-1)/2\}$ need $(m-1)/2\ge2$, so $m\ge5$; in particular $m=3$ cannot occur. (Lemma D and §4.1 need only $m\ge3$.) Also $\gcd(m,a,b)=1$ by the choice of $g$. If $m\ne5$, Lemma D applies. Suppose $m=5$. Then $5\mid v$ and $g=v/5=:f$. Both $d$ and $e$ are multiples of $f$ in $\{1,\dots,h\}$, and $h=(5f-1)/2<3f$, so $d,e\in\{f,2f\}$. As $d\ne e$, $\{d,e\}=\{f,2f\}=\{v/5,2v/5\}$, which is excluded. $\square$

*Remark (not used).* The excluded graph $I(v,v/5,2v/5)$ is $v/5$ disjoint copies of $I(5,1,2)$, the Petersen graph, which is not 3-edge-colourable. So this one pair of differences really must be avoided; Lemma E shows it always can be.

### Lemma E ($v/5$ and $2v/5$ lie in different orbits). Status: proved

Suppose $5\mid v$ and put $f=v/5$. Then no base block $B_P$ has both $f\in D_P$ and $2f\in D_P$. (Note $1\le f<2f\le h$, since $2f\le h$ is equivalent to $v\ge5$.)

*Proof.* Let $B_P=\{x,y,z\}$ and $\alpha=y-x$, $\beta=z-y$, $\gamma=x-z$. Then $\alpha+\beta+\gamma=0$ and $D_P=\{\lVert\alpha\rVert,\lVert\beta\rVert,\lVert\gamma\rVert\}$. Suppose $f,2f\in D_P$. The relation $\alpha+\beta+\gamma=0$ is symmetric, so we may assume $\lVert\alpha\rVert=f$ and $\lVert\beta\rVert=2f$, i.e. $\alpha=\pm f$, $\beta=\pm2f$. Then $\gamma=-\alpha-\beta\in\{\pm f,\pm3f\}$. Since $5f=0$ in $\mathbb Z_v$, $\lVert 3f\rVert=\lVert -2f\rVert=2f$. So $\lVert\gamma\rVert\in\{f,2f\}$ and $|D_P|\le2$, contradicting Lemma A(2). $\square$

*Smallest case ($v=25$, $f=5$).* In the cyclic STS(25) with base blocks $\{0,1,3\},\{0,4,11\},\{0,5,13\},\{0,6,15\}$ the sets $D_P$ are $\{1,2,3\},\{4,7,11\},\{5,8,12\},\{6,9,10\}$: 5 and 10 are in different sets. Checked for all 240 cyclic STS(25) on $\mathbb Z_{25}$ (**numerical**, `prover/out_verify_small.log`).

### Lemma F (1-factorization of $K_N$, $N$ even). Status: proved (classical; proof included)

For even $N\ge2$ the edge set of the complete graph $K_N$ is a disjoint union of $N-1$ perfect matchings $F_0,\dots,F_{N-2}$.

*Proof.* For $N=2$ take $F_0$ to be the single edge. Let $N\ge4$ and take the vertex set $\mathbb Z_{N-1}\cup\{\infty\}$. For $j\in\mathbb Z_{N-1}$ let

```math
F_j=\{\{\infty,j\}\}\ \cup\ \{\{j-t,\ j+t\} : 1\le t\le (N-2)/2\}.
```

$N-1$ is odd. For $1\le t,t'\le(N-2)/2$: $j+t=j-t'$ would give $t+t'\equiv0$ with $2\le t+t'\le N-2$, impossible; and $j\pm t\ne j$. So the $N-2$ elements $j\pm t$ are distinct and different from $j$, and $F_j$ is a perfect matching. An edge $\{\infty,a\}$ lies only in $F_a$. An edge $\{a,b\}\subseteq\mathbb Z_{N-1}$ lies in $F_j$ iff $a+b=2j$; since 2 is invertible mod $N-1$ this determines $j$ uniquely, and then $\{a,b\}=\{j-t,j+t\}$ for the unique $t\in\{1,\dots,(N-2)/2\}$ with $t\equiv\pm(b-a)/2$. So every edge lies in exactly one $F_j$. $\square$

## 7. Proof of Theorem 1. Status: proved

Let $O_1,\dots,O_N$, $B_P$, $D_P$, $S_{PQ}$, $R_P(d)$, $\mu^{PQ}_s$ be as in Lemma A. We colour $E(G)$ with the colours $1,\dots,k$ so that every colour class is a perfect matching of $G$.

**Step 0 (pairing the orbits).** $N$ is even (Lemma A(1)). By Lemma F there are perfect matchings $F_0,\dots,F_{N-2}$ of the complete graph on $\{1,\dots,N\}$ that partition its edge set. Write each pair as $\{P,Q\}$ with $P<Q$.

**Step 1 (choices for the pairs of $F_0$).** For each $\{P,Q\}\in F_0$ choose

- a bijection $\sigma:D_P\to D_Q$ such that $\{d,\sigma(d)\}\ne\{v/5,2v/5\}$ for all $d\in D_P$, and
- three distinct elements $s_1,s_2,s_3\in S_{PQ}$ (possible since $|S_{PQ}|=9$, Lemma A(4)).

*Such a $\sigma$ exists.* If $5\nmid v$ there is no condition. Let $5\mid v$, $f=v/5$. If $D_P\cup D_Q$ does not contain both $f$ and $2f$, there is again no condition. Otherwise, by Lemma E one of $f,2f$ lies in $D_P$ and the other in $D_Q$; say $f'\in D_P$ and $f''\in D_Q$ with $\{f',f''\}=\{f,2f\}$. The condition is $\sigma(f')\ne f''$. Of the $3!=6$ bijections exactly 2 have $\sigma(f')=f''$, so 4 are allowed.

**Step 2 (nine colours on three cubic pieces per pair of $F_0$).** Fix $\{P,Q\}\in F_0$ and write $D_P=\{d_1,d_2,d_3\}$. For $t=1,2,3$ let

```math
\Gamma_t=R_P(d_t)\ \cup\ \mu^{PQ}_{s_t}\ \cup\ R_Q(\sigma(d_t)).
```

By Lemma B, $\Gamma_t\cong I(v,d_t,\sigma(d_t))$ with $1\le d_t\ne\sigma(d_t)\le h$, and by the choice of $\sigma$, $\{d_t,\sigma(d_t)\}\ne\{v/5,2v/5\}$. By Lemma D′, $\Gamma_t$ has a proper 3-edge-colouring; use the colours $3t-2,3t-1,3t$. $\Gamma_t$ is cubic with vertex set $O_P\cup O_Q$, so each of these three colour classes is a perfect matching of $O_P\cup O_Q$.

The three pieces $\Gamma_1,\Gamma_2,\Gamma_3$ are pairwise edge-disjoint: they use different $d_t$, different $\sigma(d_t)$ ($\sigma$ is injective) and different $s_t$, and the sets $R_P(\cdot)$, $R_Q(\cdot)$, $\mu^{PQ}_{(\cdot)}$ are pairwise disjoint by Lemma A(3),(4). Together they contain all of $E(G[O_P])$ and $E(G[O_Q])$ (every $d\in D_P$ and, as $\sigma$ is onto, every $e\in D_Q$ is used) and exactly three of the nine matchings $\mu^{PQ}_s$.

**Step 3 (six more colours per pair of $F_0$).** The six remaining matchings $\mu^{PQ}_s$, $s\in S_{PQ}\setminus\{s_1,s_2,s_3\}$, receive the colours $10,\dots,15$, one colour each. Each is a perfect matching of $O_P\cup O_Q$ (Lemma A(4)).

Do Steps 1–3 for every pair of $F_0$, with the same colours $1,\dots,15$ for every pair. The pairs of $F_0$ partition $\{1,\dots,N\}$, so the sets $O_P\cup O_Q$ partition $V(G)$. Hence each colour $c\in\{1,\dots,15\}$ is now a perfect matching of $G$ (the union over the pairs of $F_0$ of one perfect matching of each $O_P\cup O_Q$).

**Step 4 (nine colours for each further matching $F_j$).** For $j=1,\dots,N-2$ and each pair $\{P,Q\}\in F_j$, give the nine matchings $\mu^{PQ}_s$, $s\in S_{PQ}$, the nine colours $15+9(j-1)+1,\dots,15+9j$, one colour each. As before, since the pairs of $F_j$ partition the orbits, each of these colours is a perfect matching of $G$.

**Every edge is coloured exactly once.** By Lemma A(5), $E(G)$ is the disjoint union of the sets $R_P(d)$ ($1\le P\le N$, $d\in D_P$) and $\mu^{PQ}_s$ ($P<Q$, $s\in S_{PQ}$). Each orbit $P$ lies in exactly one pair of $F_0$, and there each $R_P(d)$ lies in exactly one piece $\Gamma_t$ (Step 2). Each pair $\{P,Q\}$ lies in exactly one $F_j$ (Lemma F): if $j=0$ its nine matchings are coloured in Steps 2 and 3 (three inside the pieces, six directly); if $j\ge1$ they are coloured in Step 4. Nothing is coloured twice.

**Colour count.** The colours used are $1,\dots,15+9(N-2)$, and

```math
15+9(N-2)=9N-3=\frac{3(v-1)}{2}-3=\frac{3(v-3)}{2}=k .
```

This agrees with the degree of $G$ (Lemma A(5): $6+9(N-1)=9N-3$). So $E(G)$ is partitioned into $k$ perfect matchings, and $G$ is class 1. $\square$

### The two smallest orders

- **$v=13$.** $N=2$, $k=15$. $F_0$ is the only matching (there are $N-1=1$), Step 4 is empty, and $15+9\cdot0=15=k$. $5\nmid13$, so every bijection $\sigma$ is allowed. Every piece is $I(13,d,e)$ with $\gcd(13,d,e)=1$, connected with $m=13\ne5$, and a generalised Petersen graph since $\gcd(13,d)=1$; Lemma D applies (Case 2, and Case 2a by Theorem 1.1 of §4.1, since $13\not\equiv5\pmod 6$). Example with base blocks $\{0,1,4\},\{0,2,7\}$: $\sigma=(1\mapsto2,\ 3\mapsto5,\ 4\mapsto6)$, $s_t=0,1,2$; pieces $I(13,1,2)$, $I(13,3,5)$, $I(13,4,6)$; the six matchings $\mu_s$, $s\in\{4,6,7,10,11,12\}$, take colours 10–15.
- **$v=25$.** $N=4$, $k=33=15+9\cdot2$. Here $f=5$, $2f=10$. A piece $I(25,d,e)$ is disconnected only if $5\mid d$ and $5\mid e$, i.e. only for $\{d,e\}=\{5,10\}$ (five Petersen graphs); Step 1 forbids exactly this. Every other piece is connected with $m=25\ne5$, and one of $d,e$ is prime to 25, so it is a generalised Petersen graph; Lemma D applies (Case 2, and Case 2a by Theorem 1.1 of §4.1, since $25\not\equiv5\pmod6$). Example: base blocks $\{0,1,3\},\{0,4,11\},\{0,5,13\},\{0,6,15\}$; if $F_0$ pairs the orbits with $D=\{5,8,12\}$ and $\{6,9,10\}$, take $\sigma=(5\mapsto6,\ 8\mapsto9,\ 12\mapsto10)$.

For both orders the whole construction was run on **every** cyclic STS on $\mathbb Z_v$ (4 systems for $v=13$, 240 for $v=25$), for every allowed $\sigma$, and the result was checked to be a partition of the directly computed block graph into $k$ perfect matchings (**numerical**; `prover/out_verify_small.log`).

## 8. Smallest-case checks of each lemma (corroboration; status numerical)

| Lemma | Smallest case(s) checked | Where |
| --- | --- | --- |
| A | $v=13$ by hand (§5); all 4 cyclic STS(13) and all 240 cyclic STS(25): orbit lengths, $\lvert D_P\rvert=3$, partition of $\{1..h\}$, $\lvert S_{PQ}\rvert=9$, and the edge set built from $R_P(d)$, $\mu^{PQ}_s$ equals the edge set computed from block intersections; degree $k$ | `prover/verify_small.py`, `prover/out_verify_small.log` |
| B | Same systems: the image of $I(v,d,e)$ equals $R_P(d)\cup\mu_s\cup R_Q(e)$ for every piece used | same |
| C | All $I(n,p,q)$, $n$ odd $\le45$, $p<q\le(n-1)/2$ (1771 graphs): number of components and the embedding of $I(n/g,p/g,q/g)$ | same |
| G | $n=11$; all $n=11+6j$, $j\le200$, on the explicit graph; negative controls (a corrupted word is rejected; $G(5,2)$ has no proper 3-edge-colouring among all $27^5$ symbol sequences) | `prover/verify_gn2.py`, `prover/out_verify_gn2.log` |
| N1 | The formula on the explicit graph: all 119208 triples $(n,p,q)$, $n\le200$, meeting the hypotheses (smallest $I(12,2,3)$); all 66141 connected proper $I(m,a,b)$, $m$ odd $\le601$, $a<b\le(m-1)/2$ (smallest $I(15,3,5)$); negative controls (every single-edge recolouring of five instances is detected) | `prover/verify_N1.py`, `prover/out_verify_N1.log` |
| D | $m=7$; all connected $I(m,a,b)$, $m$ odd $\le25$: 281 graphs, all 3-edge-coloured by backtracking except $(5,1,2)$. Of the 281, 276 are Case 2 (generalised Petersen) and 5 are Case 1 (proper): $(15,3,5)$, $(15,5,6)$, $(21,3,7)$, $(21,6,7)$, $(21,7,9)$. The formula of Lemma N1 itself is checked in the N1 row | `prover/out_verify_small.log` |
| D′ / E | $v=25$: 5 and 10 never in one $D_P$, 240 systems; the forbidden bijection was rejected 128 times and an allowed one always existed | same |
| D′ | $v=85$, the smallest order in the range of Theorem 1 that has a piece whose components are $G(m,2)$ with $m\equiv5\pmod6$, $m\ge11$ (namely $I(85,5,10)$: five copies of $G(17,2)$, the first use of Lemma G) and that has proper I-graph pieces (for example $I(85,5,17)$). All 45 pieces $I(85,d,e)$ with neither $d$ nor $e$ coprime to 85 (16 proper, 29 disconnected) are 3-edge-colourable except $(17,34)$, which is $\{v/5,2v/5\}$ | same |
| F | $N=2$, $N=4$ (used in the runs above); the formula for every even $N$ from 4 to 60; the identity $15+9(N-2)=k=6+9(N-1)$ for every $v\equiv1\pmod{12}$ up to 100000 | `prover/verify_misc.py`, `prover/out_verify_misc.log` |
| Theorem 1 | $v=13$: 2040 assembled colourings (4 systems; all 6 bijections, and all 504 ordered choices of three shifts for one bijection). $v=25$: 1440 assembled colourings (240 systems; all allowed bijections). All verified | same |

*Coverage of the end-to-end runs.* At $v=13$ and $v=25$ no admissible piece is disconnected or proper, and Lemma G is never reached: `prover/out_verify_small.log` shows `disconnected: 0, proper: 0`. So the runs of `verify_small.py` exercise Lemmas A, B, E, F, the conclusion of Lemma D for connected generalised Petersen pieces (each piece is coloured by exhaustive backtracking, not by the Hamilton-cycle construction of Case 2a) and the assembly of §7. They do not exercise Lemma C with $g>1$, Lemma N1 or Lemma G. Those are exercised separately: Lemma C, and the colourability of the $v=85$ disconnected and proper pieces (again by backtracking), by other parts of `verify_small.py` (rows C and D′ above); Lemma G by `verify_gn2.py`; the formula of Lemma N1 by `verify_N1.py`. An AI referee's own end-to-end runs (orders $85,121,145,205,265,325,385,625$; not part of this package and not relied on) did reach disconnected, proper and $G(m,2)$-type pieces.

Wider exploratory runs (a separate implementation, kept in the private research repository; not part of this package and not relied on): all 36025 connected I-graphs with $n$ odd, $n\le121$, are 3-edge-colourable except $I(5,1,2)$; all 18336 possible pieces $I(385,d,e)$ are 3-edge-colourable except $(77,154)$; full colourings of two random cyclic STS(385) and of samples at $v=37,49,61$ verified. Status **numerical**.

## 9. What this does NOT cover

- **Non-cyclic Steiner triple systems.** The proof uses the translation orbits throughout. DPP's Conjecture 1.3 for general STS($v$) stays open.
- **$v\equiv9\pmod{12}$.** Here $3\mid v$, there is a short orbit, and Lemma A(1) fails. For cyclic systems this case is DPP's Theorem 4.1 (cited in Corollary 3, not re-proved). For Kirkman triple systems it is DPP's Theorem 2.2.
- **$v\equiv3,7\pmod{12}$.** The block graph has odd order, so it is class 2 for the trivial counting reason and lies outside both conjectures.
- **Systems that are "cyclic" only in DPP's weaker sense** (an automorphism of order $v$ that is not a $v$-cycle), if any exist. By Remark 4 (proved, not used by Theorem 1) there are none when $v$ has at most three distinct prime divisors, so this exclusion can matter only for $v\ge5005$. See §12, note 1.
- **Complements** of these block graphs; Steiner 2-designs with block size above 3; all other strongly regular graphs. Conjecture 1.2 itself is not proved.
- **Hamilton decompositions** or any property stronger than class 1.
- No statement is made about which orders are new relative to DPP's *method*. DPP's Theorem 3.1 as stated requires $\varphi(v)/(v-1)\ge2/3$; they report 385 as the smallest order $v\equiv1\pmod{12}$ where this fails and 37182145 as the smallest order where their method must fail. Whether their method (their conditions (2.1), (2.2)) happens to succeed for every cyclic STS(385) was not determined.

## 10. Table of all steps

| Step | Statement (short) | Status | Evidence |
| --- | --- | --- | --- |
| §2.1 | $k$-regular: class 1 iff 1-factorization | proved (elementary) | `PROOF.md` §2 |
| Lemma A | Orbits of length $v$; $N$ even; difference partition; $R_P(d)$ and $\mu^{PQ}_s$ decompose $E(G)$; degree $k$ | proved | `PROOF.md` §5; numerical check `prover/out_verify_small.log` |
| Lemma B | Each piece is $I(v,d,e)$, $d\ne e$ | proved | `PROOF.md` §5; same log |
| Lemma C | $I(n,p,q)$ = $\gcd(n,p,q)$ copies of a connected I-graph | proved | `PROOF.md` §6; same log |
| BP Thm 1.1 (Alspach) | $G(n,q)$ without a Hamilton cycle is isomorphic to $G(n,2)$, $n\equiv5\pmod6$ | cited (main line; Alspach's paper not read, statement as printed in BP) | Bonvicini–Pisanski, [AMC 12 (2017)](https://doi.org/10.26493/1855-3974.921.b14) §1 Theorem 1.1 = [arXiv:1508.01865v1](https://arxiv.org/abs/1508.01865) Theorem 1; `PROOF.md` §4.1 |
| BP Thm 1.2 | Connected I-graph without a Hamilton cycle is $G(n,2)$, $n\equiv5\pmod6$ | cited; **not load-bearing** (alternative route for Case 1 of Lemma D) | Bonvicini–Pisanski, AMC 12 (2017) §1, §7, Theorem 1.2 = arXiv v1 Theorem 2; `PROOF.md` §4.1 |
| Lemma N1 | $I(n,p,q)$ with $\gcd(n,p),\gcd(n,q)\ge2$ coprime is 3-edge-colourable (explicit formula) | proved (hand proof; suggested by an AI referee; the conclusion is known from Bonvicini–Pisanski §7, p. 20) | `PROOF.md` §6; numerical check `prover/verify_N1.py`, `prover/out_verify_N1.log` |
| Lemma G | $G(11+6j,2)$ is 3-edge-colourable | proved; the 17-row table (step C-G, §11) is certified and checked by the Lean kernel | `PROOF.md` §6; `prover/verify_gn2.py`, `prover/out_verify_gn2.log` |
| Lemma D | $I(m,a,b)$ with $\gcd(m,a,b)=1$, $m\ne5$, is 3-edge-colourable | proved (from Lemma N1, BP Thm 1.1 and Lemma G) | `PROOF.md` §6 |
| CP 1972 | Every $G(n,k)$ except the Petersen graph is 3-edge-colourable | cited; not needed for the main line; its proof delegates cases to Watkins 1969, which was not read | [Pacific J. Math. 40 (1972) 53–58](https://msp.org/pjm/1972/40-1/p07.xhtml); `PROOF.md` §4.2–4.3 |
| Lemma D′ | $I(v,d,e)$ is 3-edge-colourable unless $\{d,e\}=\{v/5,2v/5\}$ | proved | `PROOF.md` §6 |
| Lemma E | $v/5$, $2v/5$ are in different $D_P$ | proved | `PROOF.md` §6; `prover/out_verify_small.log` |
| Lemma F | 1-factorization of $K_N$, $N$ even | proved (classical, proof included) | `PROOF.md` §6 |
| Theorem 1 | Cyclic STS($v$), $v\equiv1\pmod{12}$: block graph class 1 | proved | `PROOF.md` §7 |
| Count | $15+9(N-2)=k=6+9(N-1)$ | proved (identity) | `PROOF.md` §7 |
| Remark 2 | $G$ is a connected SRG of even order, not Petersen | proved (classical) | `PROOF.md` §3 |
| Remark 4 | The two readings of "cyclic" agree when $v$ has at most three distinct prime divisors | proved; not used by Theorem 1 (suggested by an AI referee) | `PROOF.md` §3 |
| Corollary 3 | All cyclic STS($v$), $v\equiv1,9\pmod{12}$ | proved for $v\equiv1$; cited for $v\equiv9$ (DPP Thm 4.1, proof not checked here) | `PROOF.md` §3; [DPP](https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p145.pdf) |
| Checks | §8 | numerical | `prover/*.log`, `final_gate_rerun_0dcf830/prover/` |

## 11. The computational step

The proof has **one** computational step.

**C-G (Lemma G, load-bearing).** Exact, integers only; no thresholds or tolerances.

- *Inputs.* The three words over $\{1,2,3\}^3$ (symbols written $OSI$): $X$ = 321, 123, 232, 312, 213, 313, 121; $Y$ = 321, 123, 323, 121; $Z$ = 321, 123, 232, 312, 213, 131.
- *What is checked.* (a) $X$, $Y$, $Z$ have the same first two symbols $\pi\rho$. (b) For each $W\in\{X,Y,Z\}$ and each index $i$ with $2\le i\le|W|+1$ of $W^+=W\pi\rho$ (0-based): the three values $O_{i-1},O_i,S_i$ are pairwise distinct and the three values $S_i,I_i,I_{i-2}$ are pairwise distinct. That is $7+4+6=17$ windows. (c) The table printed in Lemma G equals the recomputed one.
- *Status: certified.* Two independent pairs of programs, archived in [`cert/`](cert/), agree.
  - [`cert/CG/`](cert/CG/): `cg_windows.py` (Python 3.12.10, standard library only) recomputes the 17 windows and compares them with the table in this file; `cg_graph_x.js` (Node.js v24.20.0, no packages) builds $G(11+6j,2)$ explicitly and checks the colouring by $XYZ^j$ vertex by vertex for $j\le2000$, and for every cyclic word of $r$ factors from $\{X,Y,Z\}$ with $2\le r\le7$ (3276 words).
  - [`cert/C-G/`](cert/C-G/): `cg_windows_a.py` (standard library only) and `cg_graph_b.py` (networkx 3.7 and python-sat 1.9.dev25), a second, separately written pair; $XYZ^j$ is proper for $j\le500$, and, as a control, SAT finds no 3-edge-colouring of $G(5,2)$.
  - All four programs end in PASS in the runs of record (`out/run_db574df/` in each folder) and in the rerun from a fresh clone of the release commit (`final_gate_rerun_0dcf830/`).
- *Lean.* The finite statements (a) and (b) are also checked by the Lean 4 kernel (`decide +kernel`, theorem `lemmaG_table` in [`lean/Pipeline/CioabaGuoHaemers/Main.lean`](lean/Pipeline/CioabaGuoHaemers/Main.lean)). The concatenation step of Lemma G, for all $j$, is by hand and is not formalized. See [`LEAN.md`](LEAN.md).
- *A finite range only corroborates.* The checks for $j\le2000$ and $j\le500$ are corroboration; the proof for all $j$ is the concatenation argument in Lemma G.
- *Which file the certificates read.* The archived outputs record the sha256 of the version of this proof that they read in the private research repository. This public copy differs from that version only outside the *certified lines*: the three word rows of the Lemma G word table, the *Inputs* line above, the 17 table rows of Lemma G and the line giving the colour strings for $n=11$, 22 lines in all, selected by the regular expression given in [`cert/CG/README.md`](cert/CG/README.md). These 22 lines are byte-identical here. [`REPRODUCE.md`](REPRODUCE.md) shows how to check this and how to run the certificates on this file.
- *Reproduction.* Check out with `core.autocrlf=false` (for example `git -c core.autocrlf=false clone <repo>`). With `core.autocrlf=true`, Git on Windows converts some files to CRLF, and their sha256 then differs from the hashes recorded in the archived outputs; the git blobs are unaffected.

**Corroboration (not load-bearing).** `python -I prover/verify_gn2.py 200`, `python -I prover/verify_small.py 13 25`, `python -I prover/verify_misc.py 60 100000` and `python -I prover/verify_N1.py 200 601` (Python 3.12.10, standard library only; outputs in `prover/out_verify_*.log`, rerun with provenance headers in `final_gate_rerun_0dcf830/prover/`). Each is a single implementation, so its status is **numerical**. Lemma N1 is proved by hand and has no computational step; `verify_N1.py` only corroborates it.

## 12. Notes

1. **Definition of "cyclic".** Theorem 1 is for the normal form $V=\mathbb Z_v$, $\mathcal B+1=\mathcal B$ (an automorphism that is a single $v$-cycle on the points). The DPP journal paper itself (p. 147) and Darijani's thesis (p. 6) both word the definition as: the automorphism group contains a cyclic subgroup of order $v$; both then assume the normal form without loss of generality (the paper at the start of its §3, the thesis in §2.2). The two readings agree when $v$ has at most three distinct prime divisors (Remark 4, status proved, not used by Theorem 1; the prime-power case is immediate, since an element of order $p^a$ on $p^a$ points with no $p^a$-cycle has order at most $p^{a-1}$). For $v$ with four or more distinct prime divisors (the smallest with $v\equiv1\pmod{12}$ is 5005) we do not know whether they can differ, and Theorem 1 claims only the normal form.
2. **Where the weight is.** Lemmas A–C, N1, D′, E, F and §7 are elementary and self-contained. The whole non-elementary content is Alspach's theorem, used in the form of Bonvicini–Pisanski Theorem 1.1 (§4.1), and only for pieces whose components are generalised Petersen graphs (Lemma D, Case 2). For those pieces there is a second, independent published source, Castagna–Prins (§4.2; part of its proof is in Watkins 1969, not read). Pieces whose components are *proper* I-graphs (neither rim difference coprime to the component's $m$) can occur, with $F_0$ and $\sigma$ arbitrary as in §7, only when $v$ has at least two distinct prime divisors; they first occur at $v=85$ (for example $I(85,5,17)$; see Lemma N1, *Smallest cases*). DPP's sufficient condition for their method, $\varphi(v)/(v-1)\ge2/3$, first fails at $v=385$ (§9). Whether proper pieces can always be avoided by the choice of $F_0$ and $\sigma$ is not determined here and is not needed for Theorem 1, since Lemma N1 colours them. Bonvicini–Pisanski's Theorem 1.2 (through the figure-based Lemma 6.5 there) also colours these pieces, and they say so (§4.1). Here they are coloured by the explicit formula of Lemma N1, proved by hand, and Bonvicini–Pisanski Theorem 1.2 remains an independent alternative (Lemma D, Remark (iv)).
3. **Petersen pieces.** $I(v,v/5,2v/5)$ is the only piece that is not 3-edge-colourable. It is avoided by the choice of $\sigma$, never coloured.
4. **Sign convention.** $S_{PQ}=\{a-b : a\in B_P, b\in B_Q\}$ and $\mu^{PQ}_s$ joins $B_P+i$ to $B_Q+i+s$: the common point is $a+i$. (With $b-a$ instead the matchings are wrong; `verify_small.py` compares against directly computed intersections and catches this.)
5. **Not read.** Watkins 1969 (§4.3); Alspach 1983 (statement taken from Bonvicini–Pisanski Theorem 1.1, arXiv v1 Theorem 1); Boben–Pisanski–Žitnik 2005 (not used). The DPP journal PDF and the corresponding thesis chapter were read (Lemma 2.2.1, Theorem 2.2.1, Theorem 2.3.1 there correspond to the paper's §3–4).
6. **Vertex names in the scripts.** `prover/verify_gn2.py` and `prover/verify_N1.py` use $w_i$ (outer rim) and $x_i$ (inner rim), as in §2 item 6. Bonvicini–Pisanski write $v_i$ for the outer rim and $u_i$ for the inner rim.

## 13. Credits and sources

No claim of priority or novelty is made.

- The conjecture for strongly regular graphs: Cioabă, Guo, Haemers, [arXiv:1810.06660](https://arxiv.org/abs/1810.06660), Ars Math. Contemp. 20 (2021).
- The conjecture for Steiner triple systems, the orbit decomposition, the pairing of orbits by a 1-factorization of $K_N$, the cubic pieces (as generalised Petersen graphs) and the colour count $9+6+9(N-2)$: Darijani, Pike, Poulin, [Australas. J. Combin. 69 (2017) 145–158](https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p145.pdf). §7 follows their proof of Theorem 3.1; the changes are that the pieces are taken as I-graphs for arbitrary differences (Lemmas B, C, D′) and that the pair $\{v/5,2v/5\}$ is avoided (Lemma E).
- I. Darijani, *Colourings of G-designs*, PhD thesis, Memorial University of Newfoundland, 2020 ([archived copy](https://web.archive.org/web/20240606190328/https://www.math.mun.ca/~dapike/publications/Theses/IrenDarijani_PhD.pdf)): Chapter 2 is the DPP paper; Chapter 5 (p. 76) names the remaining cyclic $v\equiv1\pmod{12}$ case and the non-cyclic case as future work.
- Proper I-graph pieces: The 3-edge-colourability of every proper I-graph is known: Bonvicini and Pisanski record it (Ars Math. Contemp. 12 (2017), §7, p. 20) as a consequence of their theorem that every connected I-graph other than $G(n,2)$ with $n\equiv 5\pmod 6$ is Hamiltonian. Lemma N1 gives a short explicit 3-edge-colouring of these graphs, so that this step does not depend on their case analysis. The lemma and its colouring were suggested by an AI referee in this project's review process (2026-11-27), and the proof was checked by hand. It is included for self-containment, not as a new result.
- Remark 4 (two readings of "cyclic"): the argument was suggested by an AI referee in this project's review process (2026-11-27) and was written out and checked.
- Hamiltonicity of I-graphs: Bonvicini, Pisanski, *A novel characterization of cubic Hamiltonian graphs via the associated quartic graphs*, [Ars Math. Contemp. 12 (2017) 1–24](https://doi.org/10.26493/1855-3974.921.b14) ([arXiv:1508.01865](https://arxiv.org/abs/1508.01865)); for generalised Petersen graphs, Alspach, [J. Combin. Theory Ser. B 34 (1983) 293–312](https://doi.org/10.1016/0095-8956(83)90042-4).
- Tait colourings of generalised Petersen graphs: Castagna, Prins, [Pacific J. Math. 40 (1972) 53–58](https://msp.org/pjm/1972/40-1/p07.xhtml); Watkins, [J. Combin. Theory 6 (1969) 152–164](https://doi.org/10.1016/S0021-9800(69)80116-X).
- I-graphs: Bouwer, Chernoff, Monson, Star, *The Foster Census* (1988), and Boben, Pisanski, Žitnik, [J. Combin. Des. 13 (2005) 406–424](https://doi.org/10.1002/jcd.20054), as cited by Bonvicini–Pisanski.
- This work: the proof, certificates and Lean check were produced 2026-11-27 by an AI research pipeline (Claude models: Opus, Fable, Sonnet) under the direction of the repository owner. The release commit is `0dcf830` in the private research repository.
