"""Check of Lemma G in PROOF.md: G(11 + 6j, 2) is 3-edge-colourable for every j >= 0.

Integer arithmetic only.  Two independent parts:

 (1) the finite window check that the proof relies on (17 windows);
 (2) for j = 0..JMAX, build G(n,2), n = 11 + 6j, as an explicit simple graph,
     colour it with the word X Y Z^j and check that the colouring is proper.

Symbols: position i carries (O_i, S_i, I_i) = colours of w_i w_{i+1}, w_i x_i, x_i x_{i+2}.
Vertex names follow PROOF.md section 2 item 6 (w = outer rim, x = inner rim); Bonvicini-Pisanski call them v and u.
The window table below is printed with the word names X^+, Y^+, Z^+ used in PROOF.md (W^+ = W pi rho).
"""
import sys

X = ("3123231", "2231112", "1322331")   # length 7: rows O, S, I
Y = ("3131", "2222", "1331")            # length 4
Z = ("312321", "223113", "132231")      # length 6

def word(rows):
    o, s, i = rows
    assert len(o) == len(s) == len(i)
    return [(int(a), int(b), int(c)) for a, b, c in zip(o, s, i)]

def good(a, b, c):
    """window (t_{i-2}, t_{i-1}, t_i) = (a, b, c): vertex w_i and vertex x_i see 3 distinct colours"""
    return len({b[0], c[0], c[1]}) == 3 and len({c[1], c[2], a[2]}) == 3

def part1(verbose=True):
    ok = True
    ws = {"X": word(X), "Y": word(Y), "Z": word(Z)}
    heads = {k: tuple(w[:2]) for k, w in ws.items()}
    if len(set(heads.values())) != 1:
        ok = False
    p, q = ws["X"][0], ws["X"][1]
    if verbose:
        print("common first two symbols (O,S,I):", p, q, "equal for X,Y,Z:", len(set(heads.values())) == 1)
        print("| word | i | t_{i-2} | t_{i-1} | t_i | at w_i: O_{i-1},O_i,S_i | at x_i: S_i,I_i,I_{i-2} | ok |")
        print("| --- | --- | --- | --- | --- | --- | --- | --- |")
    nwin = 0
    for name in ("X", "Y", "Z"):
        e = ws[name] + [p, q]
        for i in range(2, len(e)):
            a, b, c = e[i - 2], e[i - 1], e[i]
            g = good(a, b, c)
            ok &= g
            nwin += 1
            if verbose:
                f = lambda t: "".join(map(str, t))
                print(f"| {name}^+ | {i} | {f(a)} | {f(b)} | {f(c)} | {b[0]},{c[0]},{c[1]} | {c[1]},{c[2]},{a[2]} | {'yes' if g else 'NO'} |")
    print("PART 1: windows checked", nwin, "all good:", ok)
    return ok

def gp2(n):
    """explicit G(n,2): vertices ('w',i), ('x',i); returns a list of (edge, (kind, i))"""
    E = []
    for i in range(n):
        E.append((frozenset([("w", i), ("w", (i + 1) % n)]), ("O", i)))
        E.append((frozenset([("w", i), ("x", i)]), ("S", i)))
        E.append((frozenset([("x", i), ("x", (i + 2) % n)]), ("I", i)))
    return E

def part2(jmax):
    ok = True
    for j in range(jmax + 1):
        w = word(X) + word(Y) + word(Z) * j
        n = len(w)
        assert n == 11 + 6 * j
        E = gp2(n)
        assert len({e for e, _ in E}) == 3 * n and all(len(e) == 2 for e, _ in E)   # simple, 3n edges
        seen = {}
        for e, (kind, i) in E:
            col = w[i]["OSI".index(kind)]
            assert col in (1, 2, 3)
            for x in e:
                seen.setdefault(x, []).append(col)
        good_n = len(seen) == 2 * n and all(sorted(c) == [1, 2, 3] for c in seen.values())
        ok &= good_n
        if not good_n:
            print("FAIL n =", n)
    print(f"PART 2: G(n,2), n = 11 + 6j, j = 0..{jmax}: proper 3-edge-colouring from X Y Z^j in every case: {ok}")
    return ok

def control():
    """negative control: the checker must reject a corrupted word, and G(5,2) must have no colouring at all"""
    import itertools
    w = word(X) + word(Y)
    w[3] = (w[3][0], w[3][1] % 3 + 1, w[3][2])
    n = len(w)
    bad = not all(good(w[(i - 2) % n], w[(i - 1) % n], w[i]) for i in range(n))
    syms = [(a, b, c) for a in (1, 2, 3) for b in (1, 2, 3) for c in (1, 2, 3)]
    cnt = 0
    for t in itertools.product(syms, repeat=5):
        if all(good(t[(i - 2) % 5], t[(i - 1) % 5], t[i]) for i in range(5)):
            cnt += 1
    print("CONTROL: corrupted word rejected:", bad, "; number of 3-edge-colourings of G(5,2) by exhaustive enumeration of 27^5 words:", cnt)
    return bad and cnt == 0

if __name__ == "__main__":
    import platform
    print("verify_gn2.py; Python", platform.python_version(), "(", platform.python_implementation(), ")", platform.system(), platform.release(), "; standard library only")
    jmax = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    r = part1() and part2(jmax) and control()
    print("RESULT verify_gn2:", "PASS" if r else "FAIL")
