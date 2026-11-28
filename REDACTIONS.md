# Redactions

Before publishing, every text file in this folder was scanned on 2026-11-27 for local user paths, the machine's hostname and e-mail addresses.

- **Copied logs and outputs** (`cert/`, `prover/`, `final_gate_rerun_0dcf830/`, `lean/logs/`): none of them contains a local user path, the hostname or an e-mail address, so nothing had to be replaced. Paths in them are relative (for example `targets/cioaba-guo-haemers/cert/C-G/cg_windows_a.py` or `Pipeline\QueensSpectrum\Defs.lean`). Had any been present, they would have been replaced by `<user>` and `<host>`. The files are exactly as written by the tools.
- **New outputs** (`reproduce-check/out/`, `scripts/logs/`): written for this folder by scripts that print relative paths only. Nothing was replaced.
- **Not included.** The shared Lean project's full `build.log` (it covers other projects' files), the LaTeX build log, the referee reports and the working notes of the research repository (`reviews/`, `plans/`), which [`PROOF.md`](PROOF.md) no longer references.
- **Edited copy.** [`PROOF.md`](PROOF.md) is a cleaned copy of the proof at release commit `0dcf830`: the review-process header, the pre-review status labels and references to files outside this folder were removed or replaced. No mathematical step changed, and the 22 certified lines are byte-identical (see [`REPRODUCE.md`](REPRODUCE.md)).
- The only personal name in this folder is the author's, on the title page of the paper.
