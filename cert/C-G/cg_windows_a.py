#!/usr/bin/env python3
"""C-G primary certificate (implementation A): exact window check of Lemma G.

Source of the claim: targets/cioaba-guo-haemers/PROOF.md at commit db574df (certified lines byte-identical to cd1c38a),
Lemma G (section 6) and section 11.  Integers only; standard library only.

Checks
  A1  X, Y, Z are over {1,2,3}^3 and have lengths 7, 4, 6.
  A2  X, Y, Z begin with the same two symbols pi rho = 321 123.
  A3  For W in {X,Y,Z}, W+ = W pi rho, every index 2 <= i <= |W|+1 (0-based):
      O_{i-1}, O_i, S_i pairwise distinct and S_i, I_i, I_{i-2} pairwise distinct.
      Exactly 7 + 4 + 6 = 17 windows.
  A4  The 17-row table printed in PROOF.md (db574df) equals the recomputed table
      (all six columns, row order).  Read with `git show db574df:...`.
  A5  Corroboration (not load-bearing): every cyclic window of X Y Z^j is good,
      for 0 <= j <= JMAX, by direct cyclic indexing (no use of A3).
  A6  Corroboration: every cyclic {X,Y,Z}-word with 2 <= r <= RMAX words has all
      cyclic windows good (the concatenation claim, finitely).
  A7  Negative controls: each single-digit corruption of each word that changes
      a symbol makes A3 fail for that word or is reported as still good (counted);
      and a fixed corrupted word is rejected.
Usage: python cg_windows_a.py [JMAX] [RMAX]
"""
import itertools
import subprocess
import sys

COMMIT = "db574df"
PROOF_PATH = "targets/cioaba-guo-haemers/PROOF.md"


def parse_word(s):
    return [tuple(int(ch) for ch in tok) for tok in s.split()]


X = parse_word("321 123 232 312 213 313 121")
Y = parse_word("321 123 323 121")
Z = parse_word("321 123 232 312 213 131")
PI, RHO = (3, 2, 1), (1, 2, 3)
WORDS = {"X": X, "Y": Y, "Z": Z}


def pairwise_distinct(a, b, c):
    return len({a, b, c}) == 3


def window_triples(seq, i):
    """seq indexed by integers via seq(i); returns ((O_{i-1},O_i,S_i),(S_i,I_i,I_{i-2}))."""
    O_prev = seq(i - 1)[0]
    O_i, S_i, I_i = seq(i)
    I_prev2 = seq(i - 2)[2]
    return (O_prev, O_i, S_i), (S_i, I_i, I_prev2)


def good(tw):
    return pairwise_distinct(*tw[0]) and pairwise_distinct(*tw[1])


def table_rows(name, W):
    Wp = W + [PI, RHO]
    rows = []
    for i in range(2, len(W) + 2):
        tw = window_triples(lambda k: Wp[k], i)
        rows.append((name, i, Wp[i - 2], Wp[i - 1], Wp[i], tw[0], tw[1], good(tw)))
    return rows


def sym(t):
    return "".join(map(str, t))


def parse_proof_table():
    txt = subprocess.run(["git", "show", f"{COMMIT}:{PROOF_PATH}"], capture_output=True,
                         check=True).stdout.decode("utf-8")
    rows = []
    for line in txt.splitlines():
        if not line.startswith("| $") or "^+$" not in line.split("|")[1]:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 7:
            continue
        name = cells[0].replace("$", "").replace("^+", "")
        rows.append((name, int(cells[1]), cells[2], cells[3], cells[4],
                     tuple(int(x) for x in cells[5].split(",")),
                     tuple(int(x) for x in cells[6].split(","))))
    return rows


def cyclic_all_good(T):
    n = len(T)
    return all(good(window_triples(lambda k: T[k % n], i)) for i in range(n))


def main():
    jmax = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    rmax = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    ok = True

    # A1
    a1 = all(all(c in (1, 2, 3) for t in W for c in t) for W in WORDS.values()) and \
        [len(X), len(Y), len(Z)] == [7, 4, 6]
    print(f"A1 alphabet and lengths (7,4,6): {'ok' if a1 else 'FAIL'}")
    ok &= a1
    # A2
    a2 = all(W[0] == PI and W[1] == RHO for W in WORDS.values())
    print(f"A2 all begin with pi rho = 321 123: {'ok' if a2 else 'FAIL'}")
    ok &= a2
    # A3
    rows = []
    for name, W in WORDS.items():
        rows += table_rows(name, W)
    print("A3 table (word, i, t_{i-2}, t_{i-1}, t_i, [O_{i-1},O_i,S_i], [S_i,I_i,I_{i-2}], good)")
    for r in rows:
        print(f"   {r[0]}+ {r[1]} {sym(r[2])} {sym(r[3])} {sym(r[4])} "
              f"{','.join(map(str, r[5]))} {','.join(map(str, r[6]))} {r[7]}")
    a3 = len(rows) == 17 and all(r[7] for r in rows)
    print(f"A3 windows good: {sum(r[7] for r in rows)}/{len(rows)} (expected 17/17): "
          f"{'ok' if a3 else 'FAIL'}")
    ok &= a3
    # A4
    prow = parse_proof_table()
    mine = [(r[0], r[1], sym(r[2]), sym(r[3]), sym(r[4]), r[5], r[6]) for r in rows]
    diffs = [(p, m) for p, m in itertools.zip_longest(prow, mine) if p != m]
    a4 = len(prow) == 17 and not diffs
    print(f"A4 PROOF.md@{COMMIT} table rows parsed: {len(prow)}; mismatches: {len(diffs)}: "
          f"{'ok' if a4 else 'FAIL'}")
    for p, m in diffs:
        print(f"   PROOF {p}  vs  recomputed {m}")
    ok &= a4
    # A5
    bad = [j for j in range(jmax + 1)
           if len(X + Y + Z * j) != 11 + 6 * j or not cyclic_all_good(X + Y + Z * j)]
    a5 = not bad
    print(f"A5 X Y Z^j all cyclic windows good, 0<=j<={jmax}: failures {bad[:10]}: "
          f"{'ok' if a5 else 'FAIL'}")
    ok &= a5
    # A6
    cnt = 0
    fails = 0
    for r in range(2, rmax + 1):
        for combo in itertools.product("XYZ", repeat=r):
            T = [t for c in combo for t in WORDS[c]]
            cnt += 1
            if not cyclic_all_good(T):
                fails += 1
    a6 = fails == 0
    print(f"A6 all {{X,Y,Z}}-words, 2<=r<={rmax}: {cnt} words, {fails} failures: "
          f"{'ok' if a6 else 'FAIL'}")
    ok &= a6
    # A7 negative controls
    killed = survived = 0
    for name, W in WORDS.items():
        for pos in range(len(W)):
            for comp in range(3):
                for val in (1, 2, 3):
                    if W[pos][comp] == val:
                        continue
                    W2 = [list(t) for t in W]
                    W2[pos][comp] = val
                    W2 = [tuple(t) for t in W2]
                    # keep the pi rho prefix fixed so the table statement is about W2
                    if all(r[7] for r in table_rows(name, W2)) and W2[:2] == [PI, RHO]:
                        survived += 1
                    else:
                        killed += 1
    Xbad = list(X)
    Xbad[3] = (3, 1, 3)
    neg = not all(r[7] for r in table_rows("Xbad", Xbad)) and not cyclic_all_good(Xbad + Y)
    print(f"A7 single-entry corruptions: {killed} rejected, {survived} still pass; "
          f"fixed corruption X[3]=313 rejected: {'ok' if neg else 'FAIL'}")
    a7 = neg and killed > 0
    ok &= a7
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
