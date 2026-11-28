# C-G: certificate for the Lemma G table (target `cioaba-guo-haemers`)

Claim source: `targets/cioaba-guo-haemers/PROOF.md` at commit `db574df` (the round-3 commit; blob sha256 with LF line endings `48e768cf8b4f777995c862599ad2ba6e9f7c374e79481913e52127263116e143`), Lemma G (section 6) and section 11.

The certified lines (the three word rows of the section 11 table, the *Inputs* line, the 17 table rows of Lemma G and the *Smallest case ($n=11$, $j=0$)* line: 22 lines) are byte-identical at `cd1c38a`, `f2bfa65` and `db574df`. Check: extracting the lines matching `^\| \$[XYZ](\^\+)?\$ \||\*Inputs\.\*|\*Smallest case \(\$n=11\$` from `git show <c>:targets/cioaba-guo-haemers/PROOF.md` gives 22 lines with sha256 `cf86be4f636b4f9429ff0cd1d4445a30f5ab9071c760fb6491a68b700c1b060f` for all three commits. Earlier runs were made against `cd1c38a` and are kept in `out/`.

## What is certified (load-bearing)

1. The words X = 321 123 232 312 213 313 121, Y = 321 123 323 121, Z = 321 123 232 312 213 131 (symbols written OSI, over {1,2,3}^3) have lengths 7, 4, 6 and begin with the same two symbols pi rho = 321 123.
2. For each W in {X, Y, Z} and each 0-based index 2 <= i <= |W|+1 of W+ = W pi rho, the window (t_{i-2}, t_{i-1}, t_i) is good: O_{i-1}, O_i, S_i pairwise distinct and S_i, I_i, I_{i-2} pairwise distinct. That is 7 + 4 + 6 = 17 windows.
3. The 17-row table printed in PROOF.md at `db574df` equals the recomputed table, cell by cell (implementation A, check A4).

## Corroboration only (finite; not a substitute for the hand concatenation argument)

- X Y Z^j properly 3-edge-colours G(11+6j, 2) for 0 <= j <= 500 (A5 by cyclic windows; B2 by building the graph and checking three perfect matchings).
- Every cyclic word of r = 2..7 blocks from {X, Y, Z} (3276 words) has all cyclic windows good (A6).
- The n = 11 colour strings printed in PROOF.md equal X Y (B3).
- Controls: every single-entry corruption of X, Y, Z (102 of them) fails the table (A7); a SAT solver finds G(5,2) not 3-edge-colourable and G(11,2) colourable with a model that checks (B4).

The step "the table implies that every cyclic window of X Y Z^j is good, for every j" is the concatenation argument of Lemma G. It is by hand and is not certified here; the ranges above only corroborate it.

## Implementations (no shared code with each other, with `prover/`, `reviews/` or `cert/CG/`)

| File | Method | Libraries |
| --- | --- | --- |
| `cg_windows_a.py` | Symbol-level window check straight from the definition; parses the PROOF table from `git show db574df:...` (constant `COMMIT` in the script) and compares | Python standard library; git |
| `cg_graph_b.py` | Words entered column-wise (O, S, I strings). Builds explicit edge-coloured graph segments of W+ in networkx and checks colours {1,2,3} at w_i and x_i; builds G(n,2) and checks each colour class with `nx.is_perfect_matching`; SAT controls | networkx, python-sat (Glucose4) |

Integers only in both; no floating point in any decision.

## Reproduce

```
git clone -c core.autocrlf=false <repo> cg && cd cg
git checkout <commit>
bash targets/cioaba-guo-haemers/cert/C-G/run_cg.sh 500 7 python
```

Expected last lines: `cg_windows_a.out: PASS (exit 0)` and `cg_graph_b.out: PASS (exit 0)`. Each archived file in `out/` records the command, UTC date, commit, Python version, platform, library versions, the sha256 of the script, the exit code and the runtime. The archived runs, and the versions and runtimes they used, are in `out/` (see the header of each file).

## Lean

The 17-window statement and the cyclic check for j <= 8 are already checked by the Lean kernel (`decide +kernel`) in `lean/Pipeline/CioabaGuoHaemers/Main.lean` (`lemmaG_table`, `lemmaG_small_cases`; ledger CGH-2). Not modified here. The translation "all windows good iff proper colouring of G(n,2)" and the concatenation argument are not formalized; both are short and finite-structured, so the concatenation lemma (any list of blocks from {X,Y,Z} of length >= 2 is cyclically good) is a candidate for a Lean proof by induction over the block list using `lemmaG_table`.

## Archived run against cd1c38a (2026-11-27, superseded in provenance only)

Fresh clone (`git clone -c core.autocrlf=false`) at commit `e69892f`, `bash targets/cioaba-guo-haemers/cert/C-G/run_cg.sh 500 7 python`; outputs copied unedited into `out/` (top level). The script then read PROOF.md at `cd1c38a`.

| Output | Result | Runtime | Versions |
| --- | --- | --- | --- |
| `out/cg_windows_a.out` | PASS (17/17 windows; PROOF table 0 mismatches; j <= 500; 3276 words) | 1.1 s | Python 3.12.10, stdlib |
| `out/cg_graph_b.out` | PASS (17 indices; j <= 500; n = 11 strings; SAT controls) | 9.7 s | Python 3.12.10, networkx 3.7, python-sat 1.9.dev25 |

Script sha256: `cg_windows_a.py` d935b27187b810d9c27510fd3505757587222ca6d37e363e5e135525a368b507, `cg_graph_b.py` 4db2b14d1eb23af855e91d868d8aa40c1ff83dc4d6038780a1bc38fdd07165e3.

## Archived run against db574df (2026-11-27, current)

Fresh clone (`git clone -c core.autocrlf=false` of the local repo) at commit `203d4e0` (scripts pointing at PROOF.md `db574df`; no other change), `bash targets/cioaba-guo-haemers/cert/C-G/run_cg.sh 500 7 python`; outputs copied unedited into `out/run_db574df/`. The header line "tracked files modified" counts only the run's own output files in `out/` (1 for A, 2 for B), which the run overwrites.

| Output | Result | Runtime | Versions |
| --- | --- | --- | --- |
| `out/run_db574df/cg_windows_a.out` | PASS (A4: PROOF.md@db574df 17 rows, 0 mismatches; j <= 500; 3276 words) | 1.0 s | Python 3.12.10, stdlib, git |
| `out/run_db574df/cg_graph_b.out` | PASS | 13.0 s | Python 3.12.10, networkx 3.7, python-sat 1.9.dev25 |

Script sha256: `cg_windows_a.py` a1d8b410186d566c022d7659eb411005f8fab50e90890256ba5658648c800636 (only the `COMMIT` constant and docstring changed), `cg_graph_b.py` 4db2b14d1eb23af855e91d868d8aa40c1ff83dc4d6038780a1bc38fdd07165e3 (unchanged).
