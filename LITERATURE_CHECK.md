# Literature and priority check

For the Cioabă–Guo–Haemers conjecture for cyclic Steiner triple systems of order v ≡ 1 (mod 12). Summarised from the project's priority gate (2026-11-27, first run and a re-gate about 16:10–16:45Z UTC) and the delta re-check at the final pre-release check (2026-11-27, 18:19–18:29Z UTC). These are dated search results, not a priority claim. No novelty or priority claim is made.

## Timeline of the problem

| Date | Event | Source |
| --- | --- | --- |
| 1972 | Castagna and Prins: every generalised Petersen graph except the Petersen graph has a Tait colouring (proper 3-edge-colouring); some cases referred to Watkins 1969 | [Pacific J. Math. 40 (1972) 53–58](https://msp.org/pjm/1972/40-1/p07.xhtml) |
| 1983 | Alspach: classification of Hamiltonian generalised Petersen graphs | [J. Combin. Theory Ser. B 34 (1983) 293–312](https://doi.org/10.1016/0095-8956(83)90042-4) |
| 2005 | Boben, Pisanski, Žitnik: I-graphs (connectedness, isomorphism) | [J. Combin. Des. 13 (2005) 406–424](https://doi.org/10.1002/jcd.20054) |
| 2016-03 (online); 2017 | Bonvicini and Pisanski, *A novel characterization of cubic Hamiltonian graphs via the associated quartic graphs*: every connected I-graph other than G(n,2), n ≡ 5 (mod 6), is Hamiltonian (Theorem 1.2); §7, p. 20 (arXiv v1, §7, p. 23) notes that proper I-graphs are therefore 3-edge-colourable | [Ars Math. Contemp. 12 (2017) 1–24](https://doi.org/10.26493/1855-3974.921.b14), [arXiv:1508.01865](https://arxiv.org/abs/1508.01865) |
| 2017 | Darijani, Pike and Poulin: Conjecture 1.3 (every STS(v), v ≡ 1 or 9 (mod 12), has a class 1 block intersection graph); Theorem 3.1 (cyclic, v ≡ 1 (mod 12), with φ(v)/(v−1) ≥ 2/3); Theorem 4.1 (cyclic, v ≡ 9 (mod 12)); Kirkman triple systems | [Australas. J. Combin. 69 (2017) 145–158](https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p145.pdf) |
| 2018-10-15 (v1); 2020-09-16 (v2); 2021 | Cioabă, Guo and Haemers: Conjecture 1.2 (except for the Petersen graph, every connected SRG of even order is class 1); many partial results | [arXiv:1810.06660](https://arxiv.org/abs/1810.06660), [Ars Math. Contemp. 20 (2021) 187–194](https://doi.org/10.26493/1855-3974.2435.ec9) |
| 2020-08 | Darijani's PhD thesis, Ch. 5 (p. 76): proving the conjecture "for the remaining cyclic STS(v) with v ≡ 1 (mod 12)" is listed as future work | [thesis (archived copy)](https://web.archive.org/web/20240606190328/https://www.math.mun.ca/~dapike/publications/Theses/IrenDarijani_PhD.pdf) |
| 2026-11-27 | This work (release commit `0dcf830`, private research repository) | this repository |

## Comparison with the closest prior work

- **Darijani–Pike–Poulin, Theorem 3.1.** Same conclusion, same method (orbits, a 1-factorization of K_N pairing the orbits, cubic pieces, colour count), under φ(v)/(v−1) ≥ 2/3. That hypothesis lets them arrange that every piece is a generalised Petersen graph. It holds for every v ≡ 1 (mod 12) below 385; up to 200000 it fails at 199 orders, beginning 385, 805, 3325, 4165, 5005, … ([`scripts/logs/orders.log`](scripts/logs/orders.log)). They report 37182145 as the smallest order at which their method must fail.
- **This work.** Treats every piece as an I-graph: generalised Petersen pieces by Alspach's theorem (cited, through Bonvicini–Pisanski Theorem 1.1) and an explicit colouring of G(n,2), n ≡ 5 (mod 6) (Lemma G); proper I-graph pieces by an explicit colouring (Lemma N1); and avoids the Petersen pieces I(v, v/5, 2v/5) (Lemma E).
- **Bonvicini–Pisanski, §7, p. 20 (arXiv v1, §7, p. 23).** The conclusion of Lemma N1 (every proper I-graph is 3-edge-colourable, equivalently 1-factorizable) is stated there, as a consequence of their Theorem 1.2. No explicit edge-colouring formula for I-graphs was found in the sources read, so the explicit formula appears to be this project's own construction; it proves a known statement and is included for self-containment, not as a new result. Proper pieces can occur only when v has at least two distinct prime divisors; the first such v ≡ 1 (mod 12) is 85, inside Darijani–Pike–Poulin's range.
- **Castagna–Prins.** An independent published source for the generalised Petersen pieces (the route Darijani–Pike–Poulin use). Not used in the main line, because part of its proof (including all G(n,2)) is referred to Watkins 1969, which could not be read.
- **Cioabă–Guo–Haemers.** Their partial results include block graphs of Steiner 2-designs with a parallelism with an even number of classes, and an asymptotic result for primitive SRGs that excludes Steiner block graphs. None covers the cyclic STS(v), v ≡ 1 (mod 12), case in general.
- **Ferber–Frederickson–Mao–Yepremyan–Zhu** ([arXiv:2410.12981](https://arxiv.org/abs/2410.12981)) and the Overfull Conjecture paper arXiv:2611.32763: general asymptotic edge-colouring results; neither covers STS block graphs, whose degree is a vanishing fraction of the order.

## Priority searches (2026-11-27)

| Source | Searched | Finding |
| --- | --- | --- |
| arXiv | "block intersection graph"; "Steiner triple" with chromatic index, class 1, edge colo(u)ring; "cyclic Steiner triple"; "I-graphs"; author listings for Cioabă, Haemers, K. Guo, Pike, Darijani, Bonvicini, Pisanski; math.CO sweep 2026-11-01 to 2026-11-27 | No paper on the chromatic index of STS block graphs, and none removing the totient condition. Nothing relevant posted on 2026-11-26 or 2026-11-27. The November 2026 papers under "Darijani" are on Gaussian mixtures and appear to be by a different author. Watch item: an active Bonvicini–Pisanski–Žitnik programme on Hamiltonicity of bicirculants (arXiv:2510.23420, 2604.21607, 2611.05531), full texts grepped, no STS or edge-colouring content |
| Citers | Citers of DPP (OpenAlex, Semantic Scholar, zbMATH): only CGH and an unrelated 2024 paper. Citers of CGH: 8 works, none on Steiner block graphs. Citers of Bonvicini–Pisanski and Boben–Pisanski–Žitnik: none on edge colouring of I-graphs | No follow-up on cyclic STS |
| Pike's and Darijani's later work | OpenAlex, zbMATH, arXiv, a saved copy of Pike's publication list | No later paper on the chromatic index of block intersection graphs |
| Crossref, OpenAlex, zbMATH | Keyword and full-text searches (chromatic index, class 1, edge colouring, 1-factorization, Hamilton decomposition with block intersection graph / STS) | No hit. (Colbourn–Colbourn 1982 is about colouring the blocks, not the block graph.) |
| GitHub | Issues, branches and code of AI-mathematics repositories (including the-omega-institute/trureturing, 1337isnot1337/solved-conjectures, PerAlexandersson/RealRooted, formal-conjectures, graph-theory-AI and others); global issue and code search for "block intersection graph", "Darijani", "cyclic Steiner triple" | No relevant match (6/clank-lab #218/#219 concern point bicolourings of an STS(39), unrelated) |
| Catalogs and forums | MathDB #340747 (the CGH conjecture: no progress recorded, 0 solutions), MathOverflow, Open Problem Garden, Hexagon, Prove2Me (public pages), Crab Research, eulersolve, Zenodo | No claim, attempt or announcement |
| Web search | DPP follow-ups, removal of the totient condition, I-graph and generalised Petersen decompositions of cyclic STS, recent Memorial theses | Only DPP, the thesis, CGH and unrelated work |

## Not reachable on 2026-11-27 (to retry before any public release)

- Google Scholar (redirected to an interstitial);
- the Semantic Scholar search endpoint (HTTP 429; OpenAlex used instead);
- UnsolvedMath (HTTP 429 bot check);
- Pike's live publications page (connection refused; his arXiv listing and a saved copy used instead);
- the full text of Boben–Pisanski–Žitnik 2005 (HTTP 403; abstract only);
- the Prove2Me mission search (needs a login).

None of these is expected to change the result of the check.

## Citation notes

- The Bonvicini–Pisanski paper in Ars Math. Contemp. 12 (2017) 1–24 is titled *A novel characterization of cubic Hamiltonian graphs via the associated quartic graphs* (checked on Crossref, DOI 10.26493/1855-3974.921.b14, and on arXiv). *Hamiltonian cycles in I-graphs* is the same authors' 2013 extended abstract in Electron. Notes Discrete Math. 40, 43–47, a different item.
- Theorem numbers of Bonvicini–Pisanski are those of the journal version. In arXiv:1508.01865v1, Theorem 1.1 is "Theorem 1" and Theorem 1.2 is "Theorem 2"; [`PROOF.md`](PROOF.md) §4.1 has the full table.
- The Cioabă–Guo–Haemers statement is identical in arXiv v1, v2 and the journal. Some secondary paraphrases omit "connected", which makes the statement false (2K₃).
