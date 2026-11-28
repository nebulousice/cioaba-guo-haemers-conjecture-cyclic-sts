#!/usr/bin/env python3
"""C-G cross-check (implementation B): explicit-graph check with networkx, SAT controls with PySAT.

Independent of cg_windows_a.py (no shared code) and of prover/ and reviews/.
Claim source: targets/cioaba-guo-haemers/PROOF.md at commit cd1c38a, Lemma G and section 11.
Colours are the integers 1, 2, 3; no floating point anywhere.

The words are entered column-wise (O-string, S-string, I-string), transcribed from the
symbol lists of PROOF.md Lemma G (symbol OSI):
  X = 321 123 232 312 213 313 121, Y = 321 123 323 121, Z = 321 123 232 312 213 131.

Checks
  B1  Graph form of the 17-window table: for each W, build the explicit edge-coloured
      graph segment of W+ = W pi rho (edges w_i w_{i+1} coloured O_i, w_i x_i coloured S_i,
      x_i x_{i+2} coloured I_i, for every index i of W+), and require that for every
      2 <= i <= |W|+1 both w_i and x_i have degree 3 with colours {1,2,3}.  17 indices.
      Also: X, Y, Z share their first two symbols, equal to 321 123.
  B2  Corroboration (not load-bearing): for 0 <= j <= JMAX build G(n,2), n = 11+6j, as a
      networkx Graph, colour it by X Y Z^j, and require that it is cubic with 3n edges and
      each colour class is a perfect matching (nx.is_perfect_matching).
  B3  n = 11: the colour strings printed in PROOF.md Lemma G (smallest case) equal X Y.
  B4  Controls: (i) PySAT: G(5,2) has no proper 3-edge-colouring (UNSAT); G(11,2) is
      satisfiable and the model is a proper colouring; (ii) a corrupted X is rejected by B1
      and by B2.
Usage: python cg_graph_b.py [JMAX]
"""
import sys

import networkx as nx
from pysat.solvers import Glucose4

COLS = {  # name: (O, S, I) strings, one character per symbol
    "X": ("3123231", "2231112", "1322331"),
    "Y": ("3131", "2222", "1331"),
    "Z": ("312321", "223113", "132231"),
}


def word(name):
    o, s, i = COLS[name]
    assert len(o) == len(s) == len(i)
    return [(int(a), int(b), int(c)) for a, b, c in zip(o, s, i)]


def segment_ok(W):
    """B1 for one word: explicit graph segment on W+ ."""
    Wp = W + W[:2]  # W followed by its own first two symbols; B1 also checks these are 321 123
    L = len(Wp)
    G = nx.MultiGraph()
    for i, (o, s, c) in enumerate(Wp):
        G.add_edge(("w", i), ("w", i + 1), colour=o)
        G.add_edge(("w", i), ("x", i), colour=s)
        G.add_edge(("x", i), ("x", i + 2), colour=c)
    checked = 0
    for i in range(2, len(W) + 2):
        for v in (("w", i), ("x", i)):
            cols = sorted(d["colour"] for _, _, d in G.edges(v, data=True))
            if cols != [1, 2, 3]:
                return False, checked
        checked += 1
    return True, checked


def gn2_coloured(T):
    n = len(T)
    G = nx.Graph()
    for i, (o, s, c) in enumerate(T):
        for u, v, col in ((("w", i), ("w", (i + 1) % n), o),
                          (("w", i), ("x", i), s),
                          (("x", i), ("x", (i + 2) % n), c)):
            assert not G.has_edge(u, v)
            G.add_edge(u, v, colour=col)
    return G


def proper_by_matchings(G, n):
    if G.number_of_nodes() != 2 * n or G.number_of_edges() != 3 * n:
        return False
    if any(d != 3 for _, d in G.degree()):
        return False
    for c in (1, 2, 3):
        M = {(u, v) for u, v, d in G.edges(data=True) if d["colour"] == c}
        if not nx.is_perfect_matching(G, M):
            return False
    return True


def sat_colourable(n):
    G = nx.Graph()
    for i in range(n):
        G.add_edge(("w", i), ("w", (i + 1) % n))
        G.add_edge(("w", i), ("x", i))
        G.add_edge(("x", i), ("x", (i + 2) % n))
    edges = list(G.edges())
    var = {(e, c): 3 * k + c for k, e in enumerate(edges) for c in (1, 2, 3)}
    s = Glucose4()
    for e in edges:
        s.add_clause([var[(e, c)] for c in (1, 2, 3)])
    for v in G.nodes():
        inc = [e for e in edges if v in e]
        for a in range(len(inc)):
            for b in range(a + 1, len(inc)):
                for c in (1, 2, 3):
                    s.add_clause([-var[(inc[a], c)], -var[(inc[b], c)]])
    res = s.solve()
    model_ok = None
    if res:
        m = set(x for x in s.get_model() if x > 0)
        for u, v in edges:
            cs = [c for c in (1, 2, 3) if var[((u, v), c)] in m]
            G[u][v]["colour"] = cs[0]
        model_ok = proper_by_matchings(G, n)
    s.delete()
    return res, model_ok


def main():
    jmax = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    X, Y, Z = word("X"), word("Y"), word("Z")
    ok = True
    lens = (len(X), len(Y), len(Z))
    pref = X[:2] == Y[:2] == Z[:2] == [(3, 2, 1), (1, 2, 3)]
    print(f"B0 lengths {lens} (expected (7, 4, 6)); common prefix 321 123: {pref}")
    ok &= lens == (7, 4, 6) and pref
    total = 0
    for name, W in (("X", X), ("Y", Y), ("Z", Z)):
        good, k = segment_ok(W)
        total += k
        print(f"B1 {name}+: indices 2..{len(W)+1} proper at w_i and x_i: {good} ({k} checked)")
        ok &= good
    print(f"B1 total indices checked: {total} (expected 17): {'ok' if total == 17 else 'FAIL'}")
    ok &= total == 17
    bad = []
    for j in range(jmax + 1):
        T = X + Y + Z * j
        n = 11 + 6 * j
        if len(T) != n or not proper_by_matchings(gn2_coloured(T), n):
            bad.append(j)
    print(f"B2 G(11+6j,2) coloured by X Y Z^j, three perfect matchings, 0<=j<={jmax}: "
          f"failures {bad[:10]}: {'ok' if not bad else 'FAIL'}")
    ok &= not bad
    # B3: PROOF.md Lemma G, smallest case, strings as printed there
    O11, S11, I11 = "3 1 2 3 2 3 1 3 1 3 1", "2 2 3 1 1 1 2 2 2 2 2", "1 3 2 2 3 3 1 1 3 3 1"
    T11 = X + Y
    b3 = ([t[0] for t in T11] == list(map(int, O11.split())) and
          [t[1] for t in T11] == list(map(int, S11.split())) and
          [t[2] for t in T11] == list(map(int, I11.split())))
    print(f"B3 n=11 colour strings of PROOF.md equal X Y: {'ok' if b3 else 'FAIL'}")
    ok &= b3
    r5, _ = sat_colourable(5)
    r11, m11 = sat_colourable(11)
    print(f"B4 SAT: G(5,2) 3-edge-colourable = {r5} (expected False); "
          f"G(11,2) = {r11}, model proper = {m11} (expected True, True)")
    ok &= (r5 is False) and r11 and m11
    Xc = list(X)
    Xc[4] = (2, 1, 1)
    rej1 = not segment_ok(Xc)[0]
    rej2 = not proper_by_matchings(gn2_coloured(Xc + Y), 11)
    print(f"B4 corrupted X (X[4]=211) rejected by B1: {rej1}, by B2: {rej2}")
    ok &= rej1 and rej2
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
