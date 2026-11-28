# Review history

The proof of the Cioabă–Guo–Haemers conjecture for cyclic Steiner triple systems of order v ≡ 1 (mod 12) ([`PROOF.md`](PROOF.md)) was reviewed on 2026-11-27 by AI referees on three Claude models. The referee reports themselves are kept in the private research repository; this file summarises them.

**Expert verification required.** No review by a human expert, and no review by a model outside the Claude family, has been recorded yet.

## The review rule

- **Round 1.** A line-by-line checker (Claude Opus) and an adversarial referee that assumes the proof is wrong (Claude Fable) review the same commit of the full package (proof, scripts, archived output), blind to each other and to the working notes. If both accept with zero issues, the proof passes.
- **Later rounds.** Otherwise every issue is fixed or rebutted in a new commit. The checker, the adversary and a third referee (Claude Sonnet, fresh and blind, the "arbiter") all review that commit. The proof passes when at least two of the three accept with zero issues and no referee has an unresolved major issue.
- A major issue from any referee always blocks.

## Rounds

| Round | Commit | Checker (Claude Opus) | Adversary (Claude Fable) | Arbiter (Claude Sonnet) | Outcome |
| --- | --- | --- | --- | --- | --- |
| 1 | `cd1c38a` | minor, 4 issues | accept, 0 issues | not run | not a pass |
| 2 | `f2bfa65` | minor, 3 issues | minor, 1 issue | accept, 0 issues | not a pass |
| 3 | `955993e` | accept, 0 issues | accept, 0 issues | minor, 1 wording issue | **pass** |

The release commit `0dcf830` fixed the round-3 wording issue. Its only changes to the proof file since `955993e` are two sentences (the paragraph describing the change of route, and note 2 of §12), both about where proper I-graph pieces can occur. The final pre-release check (2026-11-27) confirmed the new wording and found that it touches no proof step.

No referee reported a major issue or a mathematical gap in any round. No issue changed a step of the proof of the Theorem.

## Issues and fixes

### Round 1 (`cd1c38a`)

Checker, 4 minor issues:

1. *Theorem numbering of Bonvicini–Pisanski.* The proof used the journal's numbers while linking arXiv v1, which numbers the same results differently. **Fix:** all numbers are stated to be the journal's, with a table of arXiv v1 equivalents (§4.1).
2. *Scope of "cyclic".* The Darijani–Pike–Poulin journal paper itself (p. 147) defines "cyclic" by a cyclic subgroup of order v, not only the thesis; the Theorem is proved for the normal form. **Fix:** the claim is restated for systems in normal form, the p. 147 wording is attributed to the paper, and Remark 4 (agreement for at most three prime divisors) was added.
3. *An unproved bound m ≥ 5* in the hypotheses of the cited theorem. **Fix:** only m ≥ 3 is needed there; Lemma D′ now derives m ≥ 5.
4. *The computational step was not yet certified*, and a script named the vertices the other way round from the proof. **Fix:** two independent certificate pairs and a Lean kernel check were built ([`cert/`](cert/), [`lean/`](lean/)); the script now uses the proof's vertex names.

Adversary: accept, 0 issues. Its non-blocking notes suggested the explicit colouring that became Lemma N1 and the argument that became Remark 4; both were written out and checked by hand, and are credited as such.

### Round 2 (`f2bfa65`)

Checker, 3 minor issues:

1. *A false sentence about which small cases were checked* (it said all were generalised Petersen graphs; 5 of the 281 are proper I-graphs). **Fix:** the sentence now gives 276 and 5, with the five triples.
2. *An unsupported sentence* saying that proper I-graph pieces cannot always be avoided for v ≥ 385. **Fix:** replaced by what is known: proper pieces can occur, Lemma N1 colours them, and whether they can always be avoided is not determined and not needed.
3. *Certificates tied to an earlier version of the proof file.* **Fix:** the certificates were rerun and archived against the reviewed file (`cert/*/out/run_db574df/`); the certified lines were shown to be byte-identical across versions.

Adversary, 1 minor issue: the same unsupported sentence as checker issue 2 (the adversary withdrew a round-1 note of its own that had led to it). Same fix.

Arbiter: accept, 0 issues. It independently rechecked Lemma N1, Lemma G, the cited form of Alspach's theorem (Hamilton cycle search for all G(m, κ) with m ≤ 17) and the full assembly on random cyclic systems.

### Round 3 (`955993e`)

Checker: accept, 0 issues (all four certificate programs, the four corroboration scripts and the Lean file rerun; all pass and match their archives).

Adversary: accept, 0 issues.

Arbiter, 1 minor wording issue: a sentence read as saying that proper I-graph pieces occur for every v ≥ 85. They can occur only when v has at least two distinct prime divisors, and the first such v ≡ 1 (mod 12) is 85. **Fix (release commit `0dcf830`):** the sentence now says exactly that, in both places.

## Current status

`proved` under the review rule above (round 3, `955993e`), with the Lemma G table `certified` and `formalized` (finite table only). The theorem as a whole is not formalized; see [`LEAN.md`](LEAN.md).

Still needed: expert verification by a human combinatorialist, in particular of Lemmas A–E, the concatenation argument of Lemma G and the use of Alspach's theorem through Bonvicini–Pisanski Theorem 1.1 (Alspach's paper itself was not read); and a review of the full package by a model outside the Claude family.
