# The Cioabă–Guo–Haemers conjecture for cyclic Steiner triple systems

> **Paper (Zenodo):** [doi:10.5281/zenodo.24613814](https://doi.org/10.5281/zenodo.24613814), author Sukhraj Sachdeva. The PDF is also in this repository ([`paper.pdf`](paper.pdf)).

*The block graphs of cyclic Steiner triple systems of order v ≡ 1 (mod 12) are class 1. Repository: https://github.com/nebulousice/cioaba-guo-haemers-conjecture-cyclic-sts.*

> **In one line:** for every $`v\equiv 1 \pmod{12}`$, the block graph of a cyclic Steiner triple system of order $v$ has a proper edge colouring with as many colours as its degree. Darijani, Pike and Poulin proved this when $`\varphi(v)/(v-1)\ge 2/3`$; this repository removes that condition by following their method, with one cited theorem (Alspach's) and one finite table of 17 checks. This is the Cioabă–Guo–Haemers conjecture for cyclic Steiner triple systems of order $`v\equiv1\pmod{12}`$ (the case $`v\equiv9\pmod{12}`$ is a cited theorem of Darijani, Pike and Poulin). The conjecture for all strongly regular graphs stays open.

Disclosure: Human researcher assisted by AI systems during search, proof drafting, and verification. Internally audited and computationally verified, externally unrefereed.

**Expert verification required.** Verified so far with: two independent AI referee reviews accepting with zero issues on the same commit (Claude Opus checker and Claude Fable adversary, round 3 at 955993e; a third AI referee, Claude Sonnet, reported one minor wording point, since fixed); two independent certificate implementations for the one computational step (the 17-window table of Lemma G); a Lean 4 kernel check of that finite table. The full theorem is not formalized.

## Summary

A graph is **class 1** if its edges can be properly coloured (edges with a common end get different colours) with exactly as many colours as its maximum degree. A **Steiner triple system** of order $v$, written STS($v$), is a set of $v$ points with a family of 3-element subsets (**blocks**) such that every pair of points lies in exactly one block. Its **block graph** has the blocks as vertices, two blocks being adjacent when they share a point. The system is **cyclic** if some permutation of the points that maps blocks to blocks is a single cycle of length $v$. Relabelling the points along that cycle puts the system in **normal form**: the points are the integers modulo $v$, and adding 1 to every point maps blocks to blocks.

**Theorem.** Let $`v\equiv 1\pmod{12}`$, $`v\ge 13`$, and let $`(\mathbb Z_v,\mathcal B)`$ be a cyclic STS($v$) in normal form. Then its block graph $G$ is class 1: its edge set is a disjoint union of

```math
k=\frac{3(v-3)}{2}
```

perfect matchings.

This is the conclusion of Theorem 3.1 of I. Darijani, D. A. Pike and J. Poulin, *The chromatic index of block intersection graphs of Kirkman triple systems and cyclic Steiner triple systems*, [Australas. J. Combin. 69 (2017) 145–158](https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p145.pdf), for cyclic systems in the normal form that they assume in their §3, without their hypothesis $`\varphi(v)/(v-1)\ge 2/3`$ ($`\varphi`$ is Euler's function).

The block graph $G$ is a connected strongly regular graph of even order, with parameters

```math
\Bigl(\frac{v(v-1)}{6},\ \frac{3(v-3)}{2},\ \frac{v+3}{2},\ 9\Bigr),
```

and it is not the Petersen graph. So the Theorem confirms, for these graphs, Conjecture 1.2 of S. M. Cioabă, K. Guo and W. H. Haemers, *The chromatic index of strongly regular graphs* ([arXiv:1810.06660](https://arxiv.org/abs/1810.06660); [Ars Math. Contemp. 20 (2021) 187–194](https://doi.org/10.26493/1855-3974.2435.ec9)): "Except for the Petersen graph, every connected SRG of even order is class 1."

**Two readings of "cyclic".** Darijani, Pike and Poulin (p. 147) call an STS($v$) cyclic when its automorphism group contains a cyclic subgroup of order $v$; at the start of their §3 they assume the normal form. Remark 4 of the proof shows that the two readings agree whenever $v$ has at most three distinct prime divisors, hence for every $v<5005$ ($`5005=5\cdot7\cdot11\cdot13`$ is the smallest $`v\equiv1\pmod{12}`$ with four). For larger $v$ with four or more prime divisors, only the normal form is claimed. The Theorem does not use Remark 4.

**Which orders earlier work already covers.** The hypothesis of Darijani–Pike–Poulin's Theorem 3.1 holds for every $`v\equiv1\pmod{12}`$ below 385. Up to 200000 it fails at 199 orders, beginning 385, 805, 3325, 4165, 5005, 5425, 7105, … ([`scripts/logs/orders.log`](scripts/logs/orders.log)). So the end-to-end computer runs at $v=13$ and $v=25$ (below) lie inside their proved range: they corroborate the argument, they do not test new cases.

**Priority and credit** (credit lines written at the final pre-release check of 2026-11-27 and approved by the repository owner; no novelty or priority claim is made).

- *The conjecture.* Cioabă, Guo and Haemers, [arXiv:1810.06660](https://arxiv.org/abs/1810.06660) (first version 2018-10); Ars Math. Contemp. 20 (2021) 187–194, [doi:10.26493/1855-3974.2435.ec9](https://doi.org/10.26493/1855-3974.2435.ec9). Conjecture 1.2. For Steiner triple systems the question was posed earlier by Darijani, Pike and Poulin, [Australas. J. Combin. 69 (2017) 145–158](https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p145.pdf), Conjecture 1.3.
- *Prior results and method.* Darijani, Pike and Poulin (2017) proved the cyclic case $`v\equiv 1\pmod{12}`$ under $`\varphi(v)/(v-1)\ge 2/3`$ (their Theorem 3.1), and the cyclic case $`v\equiv 9\pmod{12}`$ (Theorem 4.1). The orbit decomposition, the pairing of orbits by a 1-factorization of $`K_N`$, the cubic generalised-Petersen pieces and the colour count are theirs. The argument here follows their proof of Theorem 3.1, treating the pieces as I-graphs and avoiding the Petersen pair $`\{v/5,2v/5\}`$. Darijani's PhD thesis (Memorial University of Newfoundland, 2020; [archived copy](https://web.archive.org/web/20240606190328/https://www.math.mun.ca/~dapike/publications/Theses/IrenDarijani_PhD.pdf)) lists the remaining cyclic $`v\equiv 1\pmod{12}`$ case as future work.
- *Hamiltonicity and colouring of the pieces.* Generalised Petersen pieces: B. Alspach, J. Combin. Theory Ser. B 34 (1983) 293–312, [doi:10.1016/0095-8956(83)90042-4](https://doi.org/10.1016/0095-8956(83)90042-4). It is used as stated in Theorem 1.1 of S. Bonvicini and T. Pisanski, *A novel characterization of cubic Hamiltonian graphs via the associated quartic graphs*, Ars Math. Contemp. 12 (2017) 1–24, [doi:10.26493/1855-3974.921.b14](https://doi.org/10.26493/1855-3974.921.b14) ([arXiv:1508.01865](https://arxiv.org/abs/1508.01865)). Independently, F. Castagna and G. Prins, Pacific J. Math. 40 (1972) 53–58, [link](https://msp.org/pjm/1972/40-1/p07.xhtml), prove that every generalised Petersen graph except the Petersen graph is 3-edge-colourable.
- *Proper I-graph pieces.* "The 3-edge-colourability of every proper I-graph is known: Bonvicini and Pisanski record it (Ars Math. Contemp. 12 (2017), §7, p. 20) as a consequence of their theorem that every connected I-graph other than G(n,2) with n ≡ 5 (mod 6) is Hamiltonian. Lemma N1 gives a short explicit 3-edge-colouring of these graphs, so that this step does not depend on their case analysis. The lemma and its colouring were suggested by an AI referee in this project's review process (2026-11-27), and the proof was checked by hand. It is included for self-containment, not as a new result."
- *Remark 4 (two readings of "cyclic").* The argument was suggested by an AI referee in this project's review process (2026-11-27) and was written out and checked.
- *This work.* The proof, certificates and Lean check were produced 2026-11-27 by an AI research pipeline (Claude models: Opus, Fable, Sonnet) under the direction of the repository owner. The release commit is `0dcf830` in the private research repository. This result's own repository is https://github.com/nebulousice/cioaba-guo-haemers-conjecture-cyclic-sts.

**Method** (following the proof of Darijani–Pike–Poulin's Theorem 3.1).

1. *Orbits.* Adding a constant permutes the blocks in $`N=(v-1)/6`$ orbits of size $v$ (an even number). The differences of points within the base blocks partition $`\{1,\dots,(v-1)/2\}`$ into triples (Lemma A).
2. *Edges.* The edges of $G$ inside an orbit form three "rims" (2-regular graphs, one per difference), and the edges between two orbits form nine perfect matchings, the "spokes" (Lemma A).
3. *Pieces.* One rim of each of two orbits, plus one spoke matching between them, form a cubic graph isomorphic to the I-graph $I(v,d,e)$ (Lemma B; I-graphs are defined below).
4. *Colouring the pieces.* $I(v,d,e)$ is a disjoint union of copies of a connected I-graph (Lemma C). A connected I-graph is 3-edge-colourable unless it is the Petersen graph (Lemma D): proper I-graphs by an explicit formula (Lemma N1); generalised Petersen graphs by a Hamilton cycle, from Alspach's theorem (cited), except $G(n,2)$ with $`n\equiv5\pmod6`$, which get an explicit colouring from a table of 17 finite checks (Lemma G). The only piece with Petersen components is $I(v,v/5,2v/5)$ (Lemma D′), and $v/5$ and $2v/5$ never lie in the same orbit (Lemma E).
5. *Assembly.* Pair the orbits by a 1-factorization of $`K_N`$ (Lemma F). For the pairs of one matching, colour three pieces with 9 colours, choosing the pairing of rims to avoid $I(v,v/5,2v/5)$, and give the 6 remaining spoke matchings one colour each. Every other pair gives its 9 spoke matchings 9 new colours. The count is

```math
15+9(N-2)=\frac{3(v-3)}{2}=k .
```

**Side facts** (proved, not used by the Theorem): the strongly regular parameters above (Remark 2); the agreement of the two readings of "cyclic" for $v$ with at most three prime divisors (Remark 4). **Corollary 3:** every cyclic STS($v$) with $`v\equiv 1`$ or $`9\pmod{12}`$ has a class 1 block graph; the $`v\equiv9`$ half is Darijani–Pike–Poulin's Theorem 4.1, cited, and its proof was not checked here.

**Verification.**

- *Proof:* complete, by hand, except for one cited theorem (Alspach's classification of Hamiltonian generalised Petersen graphs, in the form stated by Bonvicini and Pisanski; Alspach's paper itself was not read) and one finite table (Lemma G). Status: `proved` (passed our review rule; the referees are AI models, see below).
- *The finite table of Lemma G:* `certified`. Two independent pairs of programs agree, with archived output in [`cert/`](cert/): one pair recomputes the 17 windows and compares them with the printed table, the other builds the graphs $G(11+6j,2)$ explicitly and checks the colouring vertex by vertex ($`j\le2000`$ and $`j\le500`$; corroboration beyond the table). Rerun from a fresh clone of the release commit: all PASS.
- *Lean 4:* only the finite table is `formalized`: theorem `lemmaG_table` in [`lean/Pipeline/CioabaGuoHaemers/Main.lean`](lean/Pipeline/CioabaGuoHaemers/Main.lean), proved by `decide +kernel` (no `native_decide`, no imports), axioms `propext` and `Classical.choice` only, Lean 4.37.0-rc1. The Theorem is **not** formalized. Alspach's theorem is not in Mathlib, and Mathlib has no support for designs or edge colourings. See [`LEAN.md`](LEAN.md).
- *Computer checks (corroboration only, single implementations, status `numerical`):* the whole construction on every cyclic STS(13) (4 systems, 2040 assembled colourings) and STS(25) (240 systems, 1440 colourings); the Lemma N1 formula on all 119208 qualifying triples with $`n\le200`$ and all 66141 connected proper I-graphs $I(m,a,b)$ with $m$ odd, $`m\le601`$; Lemma F and the colour count. See [`REPRODUCE.md`](REPRODUCE.md).
- *Reviews (2026-11-27):* three rounds of AI review on three Claude models.
  - Round 1 at `cd1c38a`: checker (Claude Opus) minor, 4 issues; adversary (Claude Fable) accept, 0 issues.
  - Round 2 at `f2bfa65`: arbiter (Claude Sonnet, fresh) accept, 0 issues; checker minor, 3 issues; adversary minor, 1 issue.
  - Round 3 at `955993e`: checker accept, 0 issues; adversary accept, 0 issues; arbiter minor, 1 wording issue. A pass under our rule. The release commit `0dcf830` fixed that wording.
  - No referee reported a major issue. See [`REVIEWS.md`](REVIEWS.md).
- *Not yet done:* expert review by a human combinatorialist; a review by a model outside the Claude family.

**How it was made.** The literature and priority search, the choice of method, the proof, the certificates, the Lean check and the reviews were each done by AI models (Claude, from Anthropic) in separate sessions, directed by the owner of this repository. All computation ran on one Windows 11 machine.

## Where to start

| If you want… | Read |
| --- | --- |
| The proof (self-contained, every step labelled) | [`PROOF.md`](PROOF.md) |
| The paper | [`paper.pdf`](paper.pdf), compiled with Tectonic from [`paper.tex`](paper.tex) (amsart) |
| To rerun the computations | [`REPRODUCE.md`](REPRODUCE.md) |
| Prior work and the priority search | [`LITERATURE_CHECK.md`](LITERATURE_CHECK.md) |
| The review history | [`REVIEWS.md`](REVIEWS.md) |
| What is formalized in Lean, and what is not | [`LEAN.md`](LEAN.md) |
| What was removed from copied logs | [`REDACTIONS.md`](REDACTIONS.md) |

---

## Research log

### Setup

- **I-graphs** (Bonvicini–Pisanski's definition). For $`n\ge3`$ and $`1\le p,q\le n-1`$ with $`p,q\ne n/2`$, the graph $I(n,p,q)$ has vertices $`w_i, x_i`$ ($`i\in\mathbb Z_n`$) and edges $`w_iw_{i+p}`$ (outer rim), $`w_ix_i`$ (spokes) and $`x_ix_{i+q}`$ (inner rim). It is cubic. The **generalised Petersen graph** is $`G(n,q)=I(n,1,q)`$; the Petersen graph is $G(5,2)$. A **proper** I-graph is a connected I-graph that is not a generalised Petersen graph.
- **Class 1 for regular graphs.** A $k$-regular graph is class 1 exactly when its edges split into $k$ perfect matchings.

### Notation

For $`v\equiv1\pmod{12}`$:

```math
h=\frac{v-1}{2},\qquad N=\frac{v-1}{6},\qquad k=\frac{3(v-3)}{2}.
```

For a residue $t$ modulo $v$, $`\lVert t\rVert`$ is the smaller of $`t \bmod v`$ and $`(-t) \bmod v`$.

### Results along the way

Status words are those of the project ledger (`proved`, `certified`, `formalized`, `numerical`).

| # | Statement | Status | Evidence |
| --- | --- | --- | --- |
| 1 | The Theorem: block graphs of cyclic STS($v$), $`v\equiv1\pmod{12}`$, are class 1 | proved (passed review round 3 at `955993e`: checker accept 0, adversary accept 0, arbiter minor 1 wording, no major; wording fixed afterwards); relies on Alspach's theorem as quoted in Bonvicini–Pisanski Thm 1.1; Lemma G table certified (row 2) | [`PROOF.md`](PROOF.md) §7; [`REVIEWS.md`](REVIEWS.md) |
| 2 | Lemma G table: the words $X$, $Y$, $Z$ begin with $`\pi\rho`$ = 321 123, and all 17 windows are good; the printed table equals the recomputation. (The all-$j$ concatenation step is by hand, part of row 1.) | certified (two independent implementations agree, in two independent pairs); formalized for the finite table (Lean 4.37.0-rc1, `decide +kernel`, `lemmaG_table`, axioms propext and Classical.choice) | [`cert/CG/`](cert/CG/), [`cert/C-G/`](cert/C-G/), [`final_gate_rerun_0dcf830/`](final_gate_rerun_0dcf830/), [`lean/`](lean/) |
| 3 | Lemma N1: explicit proper 3-edge-colouring of every connected proper I-graph | proved (part of the package that passed review round 3); the conclusion is already stated in Bonvicini–Pisanski, AMC 12 (2017) §7 p. 20 (arXiv v1, §7, p. 23) | [`PROOF.md`](PROOF.md) §6 |
| 4 | The Lemma N1 colouring is proper on all 119208 qualifying $(n,p,q)$ with $`n\le200`$ and on all 66141 connected proper $I(m,a,b)$ with $m$ odd $`\le601`$ | numerical (single implementation) | [`prover/verify_N1.py`](prover/verify_N1.py), [`prover/out_verify_N1.log`](prover/out_verify_N1.log) |
| 5 | Remark 4: the two readings of "cyclic" agree when $v$ has at most three distinct prime divisors (all $`v\equiv1\pmod{12}`$ below 5005) | proved; not used by the Theorem | [`PROOF.md`](PROOF.md) §3 |
| 6 | Corollary 3: block graphs of cyclic STS($v$) are class 1 for $`v\equiv1`$ (the Theorem) and $`v\equiv9\pmod{12}`$ (Darijani–Pike–Poulin Thm 4.1, cited, proof not checked here) | proved for $`v\equiv1\pmod{12}`$; cited (unchecked) for $`v\equiv9\pmod{12}`$ | [`PROOF.md`](PROOF.md) §3 |
| 7 | End-to-end corroboration: the assembly of §7 verified on every cyclic STS($v$) for $v=13$ and $v=25$ | numerical (small $v$ lie inside Darijani–Pike–Poulin's range $v<385$) | [`prover/out_verify_small.log`](prover/out_verify_small.log), [`prover/out_verify_misc.log`](prover/out_verify_misc.log) |
