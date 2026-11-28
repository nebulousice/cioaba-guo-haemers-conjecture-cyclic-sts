# Lean 4: what is formalized and what is not

**Short version.** Lemma G's 17-window table is formalized in Lean. The Theorem (the Cioabă–Guo–Haemers conjecture for cyclic Steiner triple systems of order v ≡ 1 (mod 12)) is **not** formalized.

## What is formalized

File: [`lean/Pipeline/CioabaGuoHaemers/Main.lean`](lean/Pipeline/CioabaGuoHaemers/Main.lean) (84 lines, sha256 `1965fd21c5b54a5ba862a06e7461b318c2a939e87077d89e581b067c9b668be7`). It has **no imports** (not even Mathlib), so it is checked by Lean core alone. Toolchain: `leanprover/lean4:v4.37.0-rc1` ([`lean/lean-toolchain`](lean/lean-toolchain)).

| Theorem | Statement | Proof |
| --- | --- | --- |
| `CioabaGuoHaemers.lemmaG_table` | Every symbol of the words X, Y, Z lies in {1,2,3}³; the words have lengths 7, 4 and 6; all three begin with π ρ = 321 123; every window of W⁺ = W π ρ at the 0-based indices 2 ≤ i ≤ \|W\|+1 is good (7 + 4 + 6 = 17 windows) | `decide +kernel` |
| `CioabaGuoHaemers.lemmaG_small_cases` | For j = 0, …, 8, the cyclic word X Y Z^j has length 11 + 6j and all its cyclic windows are good (corroboration only) | `decide +kernel` |

A window (t_{i−2}, t_{i−1}, t_i) is *good* when O_{i−1}, O_i, S_i are pairwise distinct and S_i, I_i, I_{i−2} are pairwise distinct, exactly as in Lemma G of [`PROOF.md`](PROOF.md). The words X, Y, Z in the Lean file are the same as in the proof.

`decide +kernel` makes the Lean kernel evaluate the decision procedure itself. `native_decide` (which trusts compiled code) is **not** used.

**Axioms.** Both theorems depend on `propext` and `Classical.choice` only ([`lean/logs/axioms.log`](lean/logs/axioms.log)).

**Build output.**

- `bash scripts/lean_check.sh CioabaGuoHaemers` in the research repository (Certifier run, 2026-11-27): `Build completed successfully`, no `sorry` or `admit`, the axioms above, `PASS lean_check CioabaGuoHaemers` ([`cert/CG/lean_check.out`](cert/CG/lean_check.out)).
- The same check from a fresh clone of the release commit `0dcf830` (final pre-release check, 2026-11-27; it reuses the prebuilt Mathlib of the shared project, which this file does not import): `PASS lean_check CioabaGuoHaemers`, exit code 0 ([`final_gate_rerun_0dcf830/lean_check.out`](final_gate_rerun_0dcf830/lean_check.out)). The build warnings in that log concern another project's files, not this one.
- Direct kernel check `lean Pipeline/CioabaGuoHaemers/Main.lean` in the same fresh clone: exit code 0, the axioms above, no `sorry`/`admit` ([`final_gate_rerun_0dcf830/lean_direct.out`](final_gate_rerun_0dcf830/lean_direct.out)).

## What is not formalized, and why

Not formalized:

- the Theorem itself;
- Lemmas A, B, C, D, D′, E, F and N1;
- the concatenation step of Lemma G (that the table makes every cyclic window of X Y Z^j good, for **all** j);
- the translation "all windows good ⇔ proper 3-edge-colouring of G(n, 2)";
- Remark 2, Remark 4 and Corollary 3.

Reasons:

1. The main line uses Alspach's 1983 classification of Hamiltonian generalised Petersen graphs, as cited (in the form of Bonvicini–Pisanski, Theorem 1.1). It is not in Mathlib, and formalizing it is a large project in its own right.
2. Mathlib has no support for block designs or for edge colourings. The orbit, difference and 1-factorization arguments (Lemmas A, B, E and F) are feasible to formalize but costly.
3. Lemma N1 and the concatenation step of Lemma G are elementary and are good next candidates. They were not attempted.

## What you have to trust

For `lemmaG_table`: the Lean kernel, and the reading of the Lean definitions (`goodWindow`, `tableGood`, `plus`, the three words) as the statements of Lemma G. The file is short and documented; the definitions follow the proof line by line. Everything else in the Theorem rests on the hand proof and its review ([`REVIEWS.md`](REVIEWS.md)).

## Reproduce

```
cd lean
lean Pipeline/CioabaGuoHaemers/Main.lean
```

with Lean 4.37.0-rc1 (for example via `elan`, which reads [`lean/lean-toolchain`](lean/lean-toolchain)). Expected output (exit code 0):

```
'CioabaGuoHaemers.lemmaG_table' depends on axioms: [propext, Classical.choice]
'CioabaGuoHaemers.lemmaG_small_cases' depends on axioms: [propext, Classical.choice]
```

Runtime: about 1 second. See also [`REPRODUCE.md`](REPRODUCE.md).
