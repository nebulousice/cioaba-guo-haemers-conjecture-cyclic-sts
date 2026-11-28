# Reproducing the computations

The proof of the Cioabă–Guo–Haemers conjecture for cyclic Steiner triple systems of order v ≡ 1 (mod 12) has **one** computational step: the 17-window table of Lemma G (section 1 below). Everything else here is corroboration, and no proof step depends on it.

All scripts are deterministic, use integers only and need no random seed.

## Environment

| Tool | Version used | Needed for |
| --- | --- | --- |
| Python | 3.12.10 | all Python scripts |
| Node.js | v24.20.0 | `cert/CG/cg_graph_x.js` (no packages) |
| networkx | 3.7 | `cert/C-G/cg_graph_b.py` only |
| python-sat | 1.9.dev25 (Glucose4) | `cert/C-G/cg_graph_b.py` only |
| Lean | 4.37.0-rc1 (`leanprover/lean4:v4.37.0-rc1`) | `lean/Pipeline/CioabaGuoHaemers/Main.lean` (no imports, no Mathlib needed) |
| `bash`, `sha256sum`, `grep`, `git` | any (Git Bash on Windows was used) | the runner scripts |
| OS | Windows 11 (Windows-11-10.0.26200) | — |
| Tectonic | the build in use on 2026-11-27 | `paper.pdf` only |

All other Python scripts use the standard library only.

```
pip install networkx==3.7 python-sat==1.9.dev25
```

**Line endings.** Clone with `core.autocrlf=false`. With `core.autocrlf=true`, Git on Windows converts some files to CRLF, and their sha256 then differs from the hashes in the archived output headers (the git blobs are unaffected):

```
git -c core.autocrlf=false clone https://github.com/nebulousice/cioaba-guo-haemers-conjecture-cyclic-sts.git
cd cioaba-guo-haemers-conjecture-cyclic-sts
```

## Quick route: everything in this folder

From the root of this folder:

```
bash reproduce-check/run_standalone.sh python
```

It runs both primary certificate programs on this folder's [`PROOF.md`](PROOF.md), the SAT cross-check, the four corroboration scripts and [`scripts/orders.py`](scripts/orders.py), and writes `reproduce-check/out/*.out`. Total runtime about 2.5 minutes (most of it `verify_N1.py`). Expected summary:

```
cg_windows.out: exit 0; PASS cg_windows: (a) common prefix 321 123; (b) 17 of 17 windows good; PROOF.md table identical; 18 junction windows covered; 102 of 102 mutations rejected
cg_graph_x.out: exit 0; PASS cg_graph_x: X Y Z^j proper on explicit G(11+6j,2) for j = 0..2000; all 3276 cyclic {X,Y,Z}-words with 2 <= r <= 7 proper; n = 11 strings match PROOF.md; controls detected
cg_graph_b.out: exit 0; PASS
verify_gn2.out: exit 0; RESULT verify_gn2: PASS
verify_misc.out: exit 0; RESULT verify_misc: PASS
verify_small.out: exit 0; RESULT verify_small: PASS
verify_N1.out: exit 0; RESULT verify_N1: PASS
orders.out: exit 0; RESULT orders: PASS (385, 85, 5005 as stated in the write-up)
```

The archived run of 2026-11-27 is in [`reproduce-check/out/`](reproduce-check/out/). Each output header records the sha256 of `PROOF.md` and of its 22 *certified lines*.

## 1. The certified step: Lemma G's 17-window table

### What the certificate reads

The certificate programs read the proof file and check that the words and the table printed there are the ones they recompute. The archived runs of record read the proof file of the private research repository. This folder's `PROOF.md` is a cleaned public copy: it differs from that file only outside the 22 certified lines (the three word rows of the Lemma G word table, the *Inputs* line of §11, the 17 table rows and the n = 11 colour-string line). Check that these lines are byte-identical:

```
grep -E '^\| \$[XYZ](\^\+)?\$ \||\*Inputs\.\*|\*Smallest case \(\$n=11\$' PROOF.md | sha256sum
```

Expected: `cf86be4f636b4f9429ff0cd1d4445a30f5ab9071c760fb6491a68b700c1b060f` (the same hash as at the reviewed commits, recorded in [`cert/CG/README.md`](cert/CG/README.md)).

### Pair 1: `cert/CG/` (primary)

On this folder's `PROOF.md`:

```
cd cert/CG
python -I cg_windows.py ../../PROOF.md
node cg_graph_x.js ../../PROOF.md 2000 7
```

Last lines: `PASS cg_windows: ...` and `PASS cg_graph_x: ...` as in the quick route above. Runtimes about 1 s and about 3 s.

In the research repository, from its root (this is the runner that wrote the archived outputs; it locates `targets/cioaba-guo-haemers/PROOF.md` relative to itself, so it does not run inside this folder):

```
bash targets/cioaba-guo-haemers/cert/CG/run_cg.sh
```

Expected final lines of `cg_windows.out` and `cg_graph_x.out`:

```
FINAL: PASS (C-G primary, cg_windows.py)
FINAL: PASS (C-G cross-check, cg_graph_x.js)
```

### Pair 2: `cert/C-G/` (second, separately written pair)

In the research repository, from its root:

```
bash targets/cioaba-guo-haemers/cert/C-G/run_cg.sh 500 7 python
```

Expected: both `out/cg_windows_a.out` and `out/cg_graph_b.out` contain a line `PASS` followed by `exit code: 0`. Runtimes about 1 s and 9–13 s.

In this folder, `cg_graph_b.py` runs on its own (its words and strings are built in):

```
python cert/C-G/cg_graph_b.py 500
```

`cg_windows_a.py` compares the table with the proof file **as stored in the research repository's git history** (`git show db574df:targets/cioaba-guo-haemers/PROOF.md`, check A4), so it needs that history and does not run in this folder. Its window computation is independent of the file; the comparison with this folder's file is done by `cg_windows.py` above.

### Archived outputs

| Run | Where | Result |
| --- | --- | --- |
| Run of record (2026-11-27, proof file at commit `db574df`; archived in commit `3b1410d`) | [`cert/CG/out/run_db574df/`](cert/CG/out/run_db574df/), [`cert/C-G/out/run_db574df/`](cert/C-G/out/run_db574df/) | all four PASS |
| Earlier run (proof file at commit `cd1c38a`) | the `.out` files at the top of [`cert/CG/`](cert/CG/) and in [`cert/C-G/out/`](cert/C-G/out/) | all four PASS |
| Final pre-release rerun, fresh clone of release commit `0dcf830` (2026-11-27) | [`final_gate_rerun_0dcf830/CG/`](final_gate_rerun_0dcf830/CG/), [`final_gate_rerun_0dcf830/C-G/`](final_gate_rerun_0dcf830/C-G/) | all four PASS; bodies identical to the run of record apart from date, commit, proof-file hash, modified-file count and runtime lines |
| Standalone rerun on this folder's `PROOF.md` (2026-11-27) | [`reproduce-check/out/`](reproduce-check/out/) | `cg_windows`, `cg_graph_x`, `cg_graph_b` PASS |

### Lean kernel check of the same table

```
cd lean
lean Pipeline/CioabaGuoHaemers/Main.lean
```

Expected output, exit code 0, about 1–2 s:

```
'CioabaGuoHaemers.lemmaG_table' depends on axioms: [propext, Classical.choice]
'CioabaGuoHaemers.lemmaG_small_cases' depends on axioms: [propext, Classical.choice]
```

Archived: [`reproduce-check/out/lean_direct.out`](reproduce-check/out/lean_direct.out) (this folder) and [`final_gate_rerun_0dcf830/lean_direct.out`](final_gate_rerun_0dcf830/lean_direct.out) (fresh clone of the release commit).

In the research repository the full project check is

```
bash scripts/lean_check.sh CioabaGuoHaemers
```

with expected last line `PASS lean_check CioabaGuoHaemers (Lean (version 4.37.0-rc1, ...))`. It builds the whole shared Lake project with Mathlib (about 25 minutes in the final pre-release rerun, `runtime_s: 1473`, with Mathlib prebuilt), although this file imports nothing. Archived: [`cert/CG/lean_check.out`](cert/CG/lean_check.out), [`final_gate_rerun_0dcf830/lean_check.out`](final_gate_rerun_0dcf830/lean_check.out).

## 2. Corroboration (numerical, not used by the proof)

From the `prover/` folder (Python 3.12.10, standard library only):

| Command | Runtime | Expected last line | Archived |
| --- | --- | --- | --- |
| `python -I verify_gn2.py 200` | about 10 s | `RESULT verify_gn2: PASS` | [`prover/out_verify_gn2.log`](prover/out_verify_gn2.log), [`final_gate_rerun_0dcf830/prover/out_verify_gn2.log`](final_gate_rerun_0dcf830/prover/out_verify_gn2.log) |
| `python -I verify_misc.py 60 100000` | about 1 s | `RESULT verify_misc: PASS` | [`prover/out_verify_misc.log`](prover/out_verify_misc.log), [`final_gate_rerun_0dcf830/prover/out_verify_misc.log`](final_gate_rerun_0dcf830/prover/out_verify_misc.log) |
| `python -I verify_small.py 13 25` | about 6 s | `RESULT verify_small: PASS` | [`prover/out_verify_small.log`](prover/out_verify_small.log), [`final_gate_rerun_0dcf830/prover/out_verify_small.log`](final_gate_rerun_0dcf830/prover/out_verify_small.log) |
| `python -I verify_N1.py 200 601` | about 2 min | `RESULT verify_N1: PASS` | [`prover/out_verify_N1.log`](prover/out_verify_N1.log), [`final_gate_rerun_0dcf830/prover/out_verify_N1.log`](final_gate_rerun_0dcf830/prover/out_verify_N1.log) |

The logs in `prover/` are the original runs (CRLF line endings, no provenance header). The reruns in `final_gate_rerun_0dcf830/prover/` carry a header (command, date, commit, script sha256) and have byte-identical bodies after removing CR.

Key lines to compare:

- `verify_gn2`: `PART 1: windows checked 17 all good: True`; `PART 2: G(n,2), n = 11 + 6j, j = 0..200: proper 3-edge-colouring from X Y Z^j in every case: True`; `number of 3-edge-colourings of G(5,2) by exhaustive enumeration of 27^5 words: 0`.
- `verify_N1`: `119208 triples (21744 with n odd; smallest (12, 2, 3)); proper in every case: True`; `66141 graphs (smallest (15, 3, 5)); proper in every case: True`; `single-edge recolourings detected: 3192 of 3192`.
- `verify_small`: `1771 I-graphs, all as stated`; `281 graphs; not 3-edge-colourable: [(5, 1, 2)]`; at v = 85, `45 {'proper': 16, 'disconnected': 29} ; not 3-edge-colourable: [(17, 34)]`; `v=13: ... cyclic STS on Z_v: 4; ... full colourings assembled and checked: 2040`; `v=25: ... cyclic STS on Z_v: 240; ... full colourings assembled and checked: 1440`.
- `verify_misc`: Lemma F for every even N in 4..60, and the colour count for every v ≡ 1 (mod 12), 13 ≤ v ≤ 100000: both `True`.

### Orders quoted in the write-up

```
python -I scripts/orders.py 200000
```

About 1 s. Expected (archived in [`scripts/logs/orders.log`](scripts/logs/orders.log)):

```
(1) v = 1 (mod 12), 13 <= v <= 200000, with phi(v)/(v-1) < 2/3: 199 orders
    smallest: 385; first ten: 385, 805, 3325, 4165, 5005, 5425, 7105, 9625, 10465, 11305
    every v = 1 (mod 12) with 13 <= v < 385 satisfies phi(v)/(v-1) >= 2/3: True
(2) smallest v = 1 (mod 12) with >= 2 distinct prime divisors: 85 = 5 * 17
(3) smallest v = 1 (mod 12) with >= 4 distinct prime divisors: 5005 = 5 * 7 * 11 * 13
RESULT orders: PASS (385, 85, 5005 as stated in the write-up)
```

This script was written for the write-up. It is a single implementation (status numerical) and gives context only.

## 3. The paper

```
tectonic -X compile paper.tex
```

Produces `paper.pdf` (amsart; pdfLaTeX-compatible packages only). Expected: no errors, no undefined references or citations, no overfull boxes.


**Note (2026-11-28).** After an independent audit, the page reference to Bonvicini–Pisanski's remark in `PROOF.md` was corrected from p. 21 to p. 20 (journal pagination; arXiv v1 §7, p. 23). This changes the SHA-256 of `PROOF.md` from the value recorded in the archived reproduce-check outputs; the 22 certified lines (the Lemma G table, the Inputs line and the n = 11 strings) are unchanged, so the certificate results still apply.
