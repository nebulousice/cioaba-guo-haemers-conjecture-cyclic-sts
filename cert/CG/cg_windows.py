#!/usr/bin/env python3
"""Certificate C-G (primary): the 17-window table of Lemma G, PROOF.md section 6 / section 11.

Exact integer checks only (Python standard library, no floats anywhere).

Checks
  (P0) The three words X, Y, Z hard-coded here equal the words printed in PROOF.md
       (section 6 word table and section 11 'Inputs' line), parsed from the file.
  (P1) Every symbol is a triple in {1,2,3}^3; |X|,|Y|,|Z| = 7,4,6 and are >= 4
       (the concatenation argument needs each word to have length >= 2; the text says >= 4).
  (a)  X, Y, Z share the first two symbols pi = 321, rho = 123.
  (b)  For each W in {X,Y,Z} and each 0-based index i with 2 <= i <= |W|+1 of W+ = W pi rho:
       {O_{i-1}, O_i, S_i} pairwise distinct and {S_i, I_i, I_{i-2}} pairwise distinct.
       Exactly 7+4+6 = 17 windows.
  (T)  The 17-row table printed in PROOF.md section 6 (columns t_{i-2}, t_{i-1}, t_i and the two
       colour triples) agrees row by row with the windows recomputed here.
  (J)  Junction coverage of the concatenation argument, made explicit: for every ordered pair
       (A, B) of words, the windows of A.B at the offsets c = 0, 1 of B coincide with the
       windows at indices |A|, |A|+1 of A+ (which are among the 17). This is the step
       'Since W_s begins with pi rho, this is the window at index |W_{s-1}|+c of W_{s-1}^+'.
  (C)  Controls: every single-entry mutation of every symbol (each of 17*3 entries changed to
       each of the other two colours, 102 mutations) must be rejected by (a) or (b); a checker
       that accepts everything would fail here.

Usage: python cg_windows.py PATH/TO/PROOF.md
"""
import re
import sys

X = ["321", "123", "232", "312", "213", "313", "121"]
Y = ["321", "123", "323", "121"]
Z = ["321", "123", "232", "312", "213", "131"]
WORDS = {"X": X, "Y": Y, "Z": Z}
PI, RHO = "321", "123"

failures = []


def fail(msg):
    failures.append(msg)
    print("  FAIL:", msg)


def sym(s):
    # symbol string 'OSI' -> (O, S, I) as ints
    return (int(s[0]), int(s[1]), int(s[2]))


def pairwise_distinct(a, b, c):
    return a != b and b != c and a != c


def window_triples(Wp, i):
    """Return ((O_{i-1},O_i,S_i), (S_i,I_i,I_{i-2})) for the word Wp (list of int triples)."""
    O1 = Wp[i - 1][0]
    O0, S0, I0 = Wp[i]
    I2 = Wp[i - 2][2]
    return (O1, O0, S0), (S0, I0, I2)


def window_good(Wp, i):
    w, x = window_triples(Wp, i)
    return pairwise_distinct(*w) and pairwise_distinct(*x)


def check_words(words):
    """Return list of (name, i, good) for all windows; words: dict name->list of strings."""
    res = []
    for name, W in words.items():
        Wp = [sym(s) for s in W + [PI, RHO]]
        for i in range(2, len(W) + 2):
            res.append((name, i, window_good(Wp, i)))
    return res


def main():
    if len(sys.argv) != 2:
        print("usage: python cg_windows.py PROOF.md")
        sys.exit(2)
    text = open(sys.argv[1], encoding="utf-8").read()

    # ---- (P0) words agree with PROOF.md
    print("(P0) words agree with PROOF.md")
    for name, W in WORDS.items():
        m = re.search(r"^\| \$" + name + r"\$ \| (\d+) \| ([0-9, ]+) \|\s*$", text, re.M)
        if not m:
            fail(f"section 6 word table row for {name} not found")
            continue
        parsed = [t.strip() for t in m.group(2).split(",")]
        if parsed != W or int(m.group(1)) != len(W):
            fail(f"section 6 word {name} = {parsed} (len {m.group(1)}) differs from {W}")
        else:
            print(f"  section 6: {name} = {' '.join(parsed)} (length {len(parsed)}) OK")
    m = re.search(r"\*Inputs\.\*(.*)$", text, re.M)
    if not m:
        fail("section 11 Inputs line not found")
    else:
        line = m.group(1)
        for name, W in WORDS.items():
            mm = re.search(r"\$" + name + r"\$ = ([0-9, ]+?)[;.]", line)
            if not mm:
                fail(f"section 11 word {name} not found")
                continue
            parsed = [t.strip() for t in mm.group(1).split(",")]
            if parsed != W:
                fail(f"section 11 word {name} = {parsed} differs from {W}")
            else:
                print(f"  section 11: {name} = {' '.join(parsed)} OK")

    # ---- (P1) alphabet and lengths
    print("(P1) alphabet and lengths")
    for name, W in WORDS.items():
        for s in W:
            if len(s) != 3 or any(ch not in "123" for ch in s):
                fail(f"{name}: symbol {s!r} not in {{1,2,3}}^3")
        if len(W) < 4:
            fail(f"{name}: length {len(W)} < 4")
    lens = tuple(len(WORDS[k]) for k in "XYZ")
    if lens != (7, 4, 6):
        fail(f"lengths {lens} != (7,4,6)")
    print(f"  lengths |X|,|Y|,|Z| = {lens}; 11 + 6j = |X|+|Y|+j|Z| requires (7,4,6): "
          f"{'OK' if lens == (7, 4, 6) else 'MISMATCH'}")

    # ---- (a) common prefix
    print("(a) common prefix pi rho = 321 123")
    for name, W in WORDS.items():
        if W[:2] != [PI, RHO]:
            fail(f"{name} starts {W[:2]}")
        else:
            print(f"  {name}: starts 321 123 OK")

    # ---- (b) the 17 windows
    print("(b) windows of W+ = W pi rho, 2 <= i <= |W|+1")
    print("  word  i  t_{i-2} t_{i-1} t_i   at w_i (O_{i-1},O_i,S_i)   at x_i (S_i,I_i,I_{i-2})   good")
    computed_rows = []
    n_windows = 0
    n_good = 0
    for name, W in WORDS.items():
        Wps = W + [PI, RHO]
        Wp = [sym(s) for s in Wps]
        for i in range(2, len(W) + 2):
            w, x = window_triples(Wp, i)
            g = pairwise_distinct(*w) and pairwise_distinct(*x)
            n_windows += 1
            n_good += g
            computed_rows.append((name + "^+", i, Wps[i - 2], Wps[i - 1], Wps[i], w, x))
            print(f"  {name}+  {i}  {Wps[i-2]}     {Wps[i-1]}     {Wps[i]}   "
                  f"{w[0]},{w[1]},{w[2]}                    {x[0]},{x[1]},{x[2]}                    {g}")
            if not g:
                fail(f"window {name}+ i={i} is bad")
    if n_windows != 17:
        fail(f"number of windows {n_windows} != 17")
    print(f"  windows checked: {n_windows}; good: {n_good}")

    # ---- (T) table in PROOF.md
    print("(T) PROOF.md section 6 table agrees with recomputation")
    rows = re.findall(r"^\| \$([XYZ])\^\+\$ \| (\d+) \| (\d{3}) \| (\d{3}) \| (\d{3}) \| "
                      r"(\d),(\d),(\d) \| (\d),(\d),(\d) \|\s*$", text, re.M)
    if len(rows) != 17:
        fail(f"found {len(rows)} table rows in PROOF.md, expected 17")
    table = []
    for r in rows:
        table.append((r[0] + "^+", int(r[1]), r[2], r[3], r[4],
                      (int(r[5]), int(r[6]), int(r[7])), (int(r[8]), int(r[9]), int(r[10]))))
    if table == computed_rows:
        print("  17 of 17 rows identical (word, i, three symbols, both colour triples)")
    else:
        for a, b in zip(table, computed_rows):
            if a != b:
                fail(f"table row {a} != computed {b}")
        if len(table) != len(computed_rows):
            fail("row count mismatch")

    # ---- (J) junction coverage
    print("(J) junction windows of A.B equal windows |A|, |A|+1 of A+ (all 9 ordered pairs)")
    nj = 0
    for an, A in WORDS.items():
        for bn, B in WORDS.items():
            AB = [sym(s) for s in A + B]
            Ap = [sym(s) for s in A + [PI, RHO]]
            for c in (0, 1):
                pos = len(A) + c  # offset c inside B
                if AB[pos - 2:pos + 1] != Ap[len(A) + c - 2:len(A) + c + 1]:
                    fail(f"junction {an}.{bn} c={c}: symbols differ from {an}+ window")
                if window_triples(AB, pos) != window_triples(Ap, len(A) + c):
                    fail(f"junction {an}.{bn} c={c}: triples differ")
                if not window_good(AB, pos):
                    fail(f"junction {an}.{bn} c={c}: bad window")
                nj += 1
            # interior windows of B inside A.B equal rows c of B+ for 2 <= c <= |B|-1
            Bp = [sym(s) for s in B + [PI, RHO]]
            for c in range(2, len(B)):
                if window_triples(AB, len(A) + c) != window_triples(Bp, c):
                    fail(f"interior {an}.{bn} c={c} differs")
    print(f"  junction windows checked: {nj} (= 9 pairs x 2); interior windows match rows of B+")

    # ---- (C) mutation controls
    print("(C) mutation controls")
    total = 0
    rejected = 0
    for name in "XYZ":
        for pos in range(len(WORDS[name])):
            for comp in range(3):
                orig = WORDS[name][pos]
                for col in "123":
                    if col == orig[comp]:
                        continue
                    mutated = orig[:comp] + col + orig[comp + 1:]
                    mw = {k: list(v) for k, v in WORDS.items()}
                    mw[name][pos] = mutated
                    # keep pi rho fixed as the appended suffix (the original), as in the text
                    res = check_words(mw)
                    prefix_ok = all(v[:2] == [PI, RHO] for v in mw.values())
                    total += 1
                    if not prefix_ok or not all(g for _, _, g in res):
                        rejected += 1
    print(f"  single-entry mutations: {total}; rejected by the window check: {rejected}")
    # A mutation at offset 0 or 1 breaks (a); at offset p >= 2 the entries O_p, S_p, I_p all occur
    # in checked windows (p, p+1, p+2 <= |W|+1), and changing one value of a permutation triple
    # creates a repeat, so (a)+(b) must reject every mutation.
    if rejected != total:
        fail(f"{total - rejected} mutations were not rejected")
    # an all-equal word must be rejected
    if all(g for _, _, g in check_words({"bad": ["111"] * 5})):
        fail("constant word accepted")
    else:
        print("  constant word 111^5 rejected OK")

    print()
    if failures:
        print(f"FAIL cg_windows ({len(failures)} failure(s))")
        sys.exit(1)
    print("PASS cg_windows: (a) common prefix 321 123; (b) 17 of 17 windows good; "
          "PROOF.md table identical; 18 junction windows covered; 102 of 102 mutations rejected")


if __name__ == "__main__":
    main()
