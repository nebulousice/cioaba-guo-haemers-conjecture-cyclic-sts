# Certificate C-G: Lemma G window table (claim CGH-2)

Source: [`PROOF.md`](../../PROOF.md) Lemma G (§6) and §11, at commit `db574df` (the round-3 commit; PROOF.md sha256 with LF line endings `48e768cf8b4f777995c862599ad2ba6e9f7c374e79481913e52127263116e143`).

The certified lines (the word rows of §11, the *Inputs* line, the 17 table rows of Lemma G and the *Smallest case ($n=11$, $j=0$)* line; 22 lines in all) are byte-identical at `cd1c38a` (PROOF.md sha256 `f6167c7225fc92a3754e18cba9d93e23d63b455928e931e9fbc5961b0fc81fa2`), `f2bfa65` and `db574df`: the lines matching `^\| \$[XYZ](\^\+)?\$ \||\*Inputs\.\*|\*Smallest case \(\$n=11\$` in `git show <c>:targets/cioaba-guo-haemers/PROOF.md` have sha256 `cf86be4f636b4f9429ff0cd1d4445a30f5ab9071c760fb6491a68b700c1b060f` at all three. The run against `db574df` is archived in [`out/run_db574df/`](out/run_db574df/); the earlier run against `cd1c38a` (the `.out` files at the top of this folder) is kept.

## Claim certified

The three words (symbols `O S I`)

| Word | Symbols |
| --- | --- |
| X | 321 123 232 312 213 313 121 |
| Y | 321 123 323 121 |
| Z | 321 123 232 312 213 131 |

(a) all begin with `321 123`; (b) for each word W and each 0-based index i with 2 ≤ i ≤ |W|+1 of W⁺ = W·321·123, the colours O_{i-1}, O_i, S_i are pairwise distinct and S_i, I_i, I_{i-2} are pairwise distinct. That is 7 + 4 + 6 = 17 windows, all good. The 17-row table printed in PROOF.md §6 is identical to the recomputed one.

The step from the table to "X Y Z^j is a proper 3-edge-colouring of G(11+6j, 2) for every j ≥ 0" is the concatenation argument of Lemma G, which is by hand and is not certified here. Part (J) of the primary and Part 2 of the cross-check test it on finite ranges only.

## Files

| File | Method | Result |
| --- | --- | --- |
| [`cg_windows.py`](cg_windows.py) → [`cg_windows.out`](cg_windows.out) | Primary. Python 3.12.10, standard library only, exact integers. Words parsed from PROOF.md and compared; (a), (b); PROOF.md table compared row by row; the 18 junction windows of every ordered pair of words shown equal to table rows; 102 single-entry mutations all rejected | PASS |
| [`cg_graph_x.js`](cg_graph_x.js) → [`cg_graph_x.out`](cg_graph_x.out) | Cross-check. Node.js v24.20.0, no packages, different method: builds G(n,2) as an explicit edge list, checks it is simple cubic, colours it, checks the three colours at every vertex. X Y Z^j for j = 0..2000 (n = 11..12011); all 3276 cyclic words W_1…W_r over {X,Y,Z} with 2 ≤ r ≤ 7; n = 11 colour strings equal PROOF.md "Smallest case"; every single-edge recolouring at n = 11, 17 detected | PASS |
| [`../../../../lean/Pipeline/CioabaGuoHaemers/Main.lean`](../../../../lean/Pipeline/CioabaGuoHaemers/Main.lean) → [`lean_check.out`](lean_check.out) | Lean 4.37.0-rc1 kernel, `decide +kernel` (no `native_decide`, no Mathlib import). `lemmaG_table`: alphabet, lengths 7/4/6, common prefix, all 17 windows good. `lemmaG_small_cases` (corroboration): all cyclic windows of X Y Z^j good for j = 0..8. Axioms: propext, Classical.choice. A mutated copy (last symbol of X changed to 122) fails both theorems | PASS |
| [`run_cg.sh`](run_cg.sh) | Runs both scripts and writes the two `.out` files with headers | |

The two programs share no code. The primary checks the windows of the definition; the cross-check never forms windows and checks vertex colours on the built graph.

## Reproduce

From a clean clone (`git clone -c core.autocrlf=false …`, checkout of the commit that archived `out/run_db574df/`):

```
bash targets/cioaba-guo-haemers/cert/CG/run_cg.sh
bash scripts/lean_check.sh CioabaGuoHaemers
```

Expected final lines: `FINAL: PASS (C-G primary, cg_windows.py)`, `FINAL: PASS (C-G cross-check, cg_graph_x.js)`, `PASS lean_check CioabaGuoHaemers (...)`.

The two top-level `.out` files were produced 2026-11-27 in a fresh clone of commit `cd1c38a` (scratch directory, core.autocrlf=false) with these scripts copied in, and copied here unchanged. `lean_check.out` was produced in the main working tree (its `lean/.lake` holds the Mathlib build; the new Lean file is uncommitted). Runtimes: primary under 1 s, cross-check about 3 s, Lean file about 4 s (the full `lake build` of the shared project about 2 min).

## Certified constants

- Words X, Y, Z as above; common prefix π ρ = 321 123; lengths 7, 4, 6.
- 17 of 17 windows good; table in PROOF.md §6 identical to recomputation.
- n = 11 colouring: O = 3 1 2 3 2 3 1 3 1 3 1, S = 2 2 3 1 1 1 2 2 2 2 2, I = 1 3 2 2 3 3 1 1 3 3 1 (matches PROOF.md).
- Corroboration: X Y Z^j proper on G(11+6j, 2) for 0 ≤ j ≤ 2000; all {X,Y,Z}-concatenations with 2 ≤ r ≤ 7 proper.

## Notes for reviewers and the Formaliser

- The text's index range 2 ≤ i ≤ |W|+1 and the count 17 match the scripts.
- The concatenation argument needs r ≥ 2 and each word of length ≥ 2 (true: minimum 4); for T = X Y Z^j, r = 2 + j ≥ 2.
- Formaliser: the remaining hand steps (windows good ⇔ proper colouring of G(n,2); table ⇒ every cyclic window of X Y Z^j good, for all j) are good candidates for a full Lean proof of Lemma G; the finite part is already kernel-checked here.

## Archived run against db574df (2026-11-27, current)

Fresh clone (`git clone -c core.autocrlf=false` of the local repo) at commit `203d4e0`, where PROOF.md is the `db574df` file (the header line `PROOF.md sha256` reads `48e768cf8b4f777995c862599ad2ba6e9f7c374e79481913e52127263116e143`), `bash targets/cioaba-guo-haemers/cert/CG/run_cg.sh`; the two outputs copied unedited into [`out/run_db574df/`](out/run_db574df/). Scripts unchanged (sha256 `cg_windows.py` 0effc69f…, `cg_graph_x.js` 764a380c…, full values in the headers).

| Output | Result | Versions |
| --- | --- | --- |
| `out/run_db574df/cg_windows.out` | FINAL: PASS (17 of 17 windows; PROOF.md table identical; 102 of 102 mutations rejected) | Python 3.12.10, stdlib |
| `out/run_db574df/cg_graph_x.out` | FINAL: PASS (j = 0..2000; 3276 cyclic words; n = 11 strings match; controls detected) | Node.js v24.20.0, no packages |

Runtimes: about 2 s and 4 s. `lean_check.out` was not rerun (the Lean file is unchanged and does not read PROOF.md).
