"""Smallest-case checks for PROOF.md (cioaba-guo-haemers, claim CGH-1).  Integer arithmetic only.

For each v on the command line (default 13 25), for EVERY cyclic STS(v) on Z_v that is invariant
under x -> x+1 (all unions of N full translation orbits that cover each pair once):

  Lemma A  orbit lengths, |D(B_P)| = 3, the D(B_P) partition {1..h}; inside an orbit the block
           graph is the circulant on D(B_P); |S_PQ| = 9 and the cross edges are exactly the 9
           shift matchings; degree k.  All compared with the block graph computed directly from
           block intersections.
  Lemma B  each piece R_P(d) u mu_s u R_Q(e) is the image of I(v,d,e) under w_i -> B_P+i,
           x_i -> B_Q+i+s  (edge sets compared).
  Lemma E  v/5 and 2v/5 never lie in one D(B_P).
  Theorem  the colouring of Section 7 is assembled for every admissible bijection sigma (first
           three shifts), and at v = 13 also for the first admissible sigma with every ordered
           choice of 3 shifts, and checked to be a partition of E(G) into k perfect matchings.

Independent of v:
  Lemma C  component structure of I(n,p,q), n odd <= 45.
  Lemma D  (sanity only) connected I(m,a,b), m odd <= 25: exhaustive backtracking.

The 3-edge-colourings of the pieces come from a plain backtracking search (the proof takes
them from Lemma D); each is checked to be proper before use.
"""
import sys
import itertools
from math import gcd


def orbit_data(v):
    """all translation orbits of triples: (base block (0,a,b), set of ordered differences, orbit length, #distinct differences)"""
    seen, out = set(), []
    for a in range(1, v):
        for b in range(a + 1, v):
            B = frozenset([0, a, b])
            if B in seen:
                continue
            orb = {frozenset((x + i) % v for x in B) for i in range(v)}
            seen |= orb
            diffs = [(x - y) % v for x in B for y in B if x != y]
            out.append(((0, a, b), frozenset(diffs), len(orb), len(set(diffs))))
    return out


def all_cyclic_sts(v):
    """exact covers of Z_v minus {0} by the ordered-difference sets of orbits"""
    orbs = [(B, D) for (B, D, L, nd) in orbit_data(v) if L == v and nd == 6]
    by_min = {}
    for B, D in orbs:
        by_min.setdefault(min(D), []).append((B, D))
    res = []

    def rec(used, chosen):
        if len(used) == v - 1:
            res.append(list(chosen))
            return
        t = min(x for x in range(1, v) if x not in used)
        for B, D in by_min.get(t, []):
            if not (D & used):
                chosen.append(B)
                rec(used | D, chosen)
                chosen.pop()

    rec(frozenset(), [])
    return res


def bar(t, v):
    t %= v
    return min(t, v - t)


def igraph_edges(n, p, q):
    E = set()
    for i in range(n):
        E.add(frozenset([("w", i), ("w", (i + p) % n)]))
        E.add(frozenset([("w", i), ("x", i)]))
        E.add(frozenset([("x", i), ("x", (i + q) % n)]))
    return E


def components(V, E):
    adj = {x: [] for x in V}
    for e in E:
        a, b = tuple(e)
        adj[a].append(b)
        adj[b].append(a)
    comp, out = {}, []
    for s in V:
        if s in comp:
            continue
        stack, cur = [s], []
        comp[s] = len(out)
        while stack:
            x = stack.pop()
            cur.append(x)
            for y in adj[x]:
                if y not in comp:
                    comp[y] = len(out)
                    stack.append(y)
        out.append(cur)
    return out, adj


def three_edge_colour(V, E):
    """backtracking; returns dict edge -> colour in {0,1,2}, or None if some component has none"""
    comps, adj = components(V, E)
    col = {}
    sys.setrecursionlimit(20000)
    for comp in comps:
        order, seenv, queue, seene = [], {comp[0]}, [comp[0]], set()
        while queue:
            x = queue.pop(0)
            for y in adj[x]:
                e = frozenset([x, y])
                if e not in seene:
                    seene.add(e)
                    order.append(e)
                if y not in seenv:
                    seenv.add(y)
                    queue.append(y)
        used = {x: set() for x in comp}

        def rec(k):
            if k == len(order):
                return True
            e = order[k]
            a, b = tuple(e)
            for c in (0, 1, 2):
                if c not in used[a] and c not in used[b]:
                    used[a].add(c)
                    used[b].add(c)
                    col[e] = c
                    if rec(k + 1):
                        return True
                    used[a].discard(c)
                    used[b].discard(c)
                    del col[e]
            return False

        if not rec(0):
            return None
    return col


_cache = {}


def igraph_colouring(v, d, e):
    key = (v, d, e)
    if key not in _cache:
        V = [(t, i) for t in "wx" for i in range(v)]
        E = igraph_edges(v, d, e)
        c = three_edge_colour(V, E)
        if c is not None:
            deg = {x: set() for x in V}
            for ed, cc in c.items():
                for x in ed:
                    deg[x].add(cc)
            assert len(c) == 3 * v and all(len(s) == 3 for s in deg.values())
        _cache[key] = c
    return _cache[key]


def one_factorization_KN(N):
    """round robin on Z_{N-1} and one extra vertex N-1; N-1 perfect matchings of range(N)"""
    if N == 2:
        return [[(0, 1)]]
    m = N - 1
    F = []
    for j in range(m):
        f = [(N - 1, j)] + [((j - t) % m, (j + t) % m) for t in range(1, (N - 2) // 2 + 1)]
        F.append(f)
    return F


def check_system(v, bases, stats):
    h, N, k = (v - 1) // 2, (v - 1) // 6, 3 * (v - 3) // 2
    assert len(bases) == N and N % 2 == 0

    def blk(P, i):
        return frozenset((x + i) % v for x in bases[P])

    verts = [(P, i) for P in range(N) for i in range(v)]
    B = {x: blk(*x) for x in verts}
    assert len(set(B.values())) == N * v == v * (v - 1) // 6  # orbits of length v, all blocks distinct
    cnt = {}
    for b in B.values():
        for pr in itertools.combinations(sorted(b), 2):
            cnt[pr] = cnt.get(pr, 0) + 1
    assert len(cnt) == v * (v - 1) // 2 and set(cnt.values()) == {1}  # STS(v)
    # block graph, directly from intersections
    Edir = {frozenset([x, y]) for x, y in itertools.combinations(verts, 2) if B[x] & B[y]}
    deg = {x: 0 for x in verts}
    for e in Edir:
        for x in e:
            deg[x] += 1
    assert set(deg.values()) == {k}
    # Lemma A
    D = [sorted({bar(x - y, v) for x in bases[P] for y in bases[P] if x != y}) for P in range(N)]
    assert all(len(d) == 3 for d in D)
    assert sorted(x for d in D for x in d) == list(range(1, h + 1))
    S = {}
    Estruct = set()
    for P in range(N):
        for d in D[P]:
            for i in range(v):
                Estruct.add(frozenset([(P, i), (P, (i + d) % v)]))
        for Q in range(P + 1, N):
            S[(P, Q)] = sorted({(x - y) % v for x in bases[P] for y in bases[Q]})
            assert len(S[(P, Q)]) == 9
            for s in S[(P, Q)]:
                for i in range(v):
                    Estruct.add(frozenset([(P, i), (Q, (i + s) % v)]))
    assert Estruct == Edir  # Lemma A(2),(3) against direct adjacency
    assert len(Edir) == N * v * k // 2
    # Lemma E
    if v % 5 == 0:
        f = v // 5
        assert not any(f in d and 2 * f in d for d in D)
    # Theorem: assemble
    F = one_factorization_KN(N)
    assert len(F) == N - 1 and all(sorted(x for pr in f for x in pr) == list(range(N)) for f in F)
    assert len({frozenset(pr) for f in F for pr in f}) == N * (N - 1) // 2
    pairs0 = [tuple(sorted(pr)) for pr in F[0]]

    def admissible(P, Q):
        out = []
        for perm in itertools.permutations(D[Q]):
            sig = list(zip(D[P], perm))
            if v % 5 == 0 and any({d, e} == {v // 5, 2 * v // 5} for d, e in sig):
                stats["rejected"] += 1
                continue
            out.append(sig)
        assert len(out) >= 4
        return out

    choices = []
    for (P, Q) in pairs0:
        adm = admissible(P, Q)
        opts = [(sig, tuple(S[(P, Q)][:3])) for sig in adm]
        if v == 13:
            opts += [(adm[0], sh) for sh in itertools.permutations(S[(P, Q)], 3)]
        choices.append(opts)
    nrun = max(len(o) for o in choices)
    for run in range(nrun):
        colour = {}
        for (P, Q), opts in zip(pairs0, choices):
            sig, shifts = opts[run % len(opts)]
            for t, ((d, e), s) in enumerate(zip(sig, shifts)):
                c = igraph_colouring(v, d, e)
                assert c is not None, (v, d, e)
                stats["pieces"] += 1
                g = gcd(v, gcd(d, e))
                if g > 1:
                    stats["disconnected"] += 1
                elif gcd(v, d) > 1 and gcd(v, e) > 1:
                    stats["proper"] += 1

                def img(z, P=P, Q=Q, s=s):
                    return (P, z[1]) if z[0] == "w" else (Q, (z[1] + s) % v)

                piece = set()
                for ed, cc in c.items():
                    a, b = tuple(ed)
                    ge = frozenset([img(a), img(b)])
                    assert ge not in colour
                    colour[ge] = 3 * t + cc
                    piece.add(ge)
                want = (
                    {frozenset([(P, i), (P, (i + d) % v)]) for i in range(v)}
                    | {frozenset([(P, i), (Q, (i + s) % v)]) for i in range(v)}
                    | {frozenset([(Q, i), (Q, (i + e) % v)]) for i in range(v)}
                )
                assert piece == want and len(piece) == 3 * v  # Lemma B
            rest = [s for s in S[(P, Q)] if s not in shifts]
            assert len(rest) == 6
            for u, s in enumerate(rest):
                for i in range(v):
                    ge = frozenset([(P, i), (Q, (i + s) % v)])
                    assert ge not in colour
                    colour[ge] = 9 + u
        for j in range(1, N - 1):
            for pr in F[j]:
                P, Q = sorted(pr)
                for u, s in enumerate(S[(P, Q)]):
                    for i in range(v):
                        ge = frozenset([(P, i), (Q, (i + s) % v)])
                        assert ge not in colour
                        colour[ge] = 15 + 9 * (j - 1) + u
        # final check against the directly computed block graph
        assert set(colour) == Edir
        assert set(colour.values()) == set(range(k)) and 15 + 9 * (N - 2) == k
        at = {x: [] for x in verts}
        for ge, c in colour.items():
            for x in ge:
                at[x].append(c)
        assert all(sorted(cs) == list(range(k)) for cs in at.values())
        stats["colourings"] += 1


def lemma_C_check(nmax):
    """I(n,p,q), n odd <= nmax, 1 <= p < q <= (n-1)/2: gcd(n,p,q) components, each the image of I(n/g,p/g,q/g)"""
    cnt = 0
    for n in range(5, nmax + 1, 2):
        for p in range(1, (n - 1) // 2 + 1):
            for q in range(p + 1, (n - 1) // 2 + 1):
                g = gcd(n, gcd(p, q))
                V = [(t, i) for t in "wx" for i in range(n)]
                E = igraph_edges(n, p, q)
                assert len(E) == 3 * n
                comps, _ = components(V, E)
                assert len(comps) == g
                small = igraph_edges(n // g, p // g, q // g)
                for r in range(g):
                    img = {frozenset((t, (r + g * i) % n) for (t, i) in e) for e in small}
                    assert img <= E and len(img) == 3 * n // g
                cnt += 1
    return cnt


def lemma_D_small(nmax):
    """exhaustive backtracking: connected I(m,a,b), m odd <= nmax, a < b"""
    bad, cnt = [], 0
    for m in range(5, nmax + 1, 2):
        for a in range(1, (m - 1) // 2 + 1):
            for b in range(a + 1, (m - 1) // 2 + 1):
                if gcd(m, gcd(a, b)) != 1:
                    continue
                cnt += 1
                if igraph_colouring(m, a, b) is None:
                    bad.append((m, a, b))
    return cnt, bad


if __name__ == "__main__":
    vs = [int(x) for x in sys.argv[1:]] or [13, 25]
    print("Lemma C check, n odd <= 45:", lemma_C_check(45), "I-graphs, all as stated")
    cnt, bad = lemma_D_small(25)
    print("Lemma D sanity, connected I(m,a,b), m odd <= 25, a<b:", cnt, "graphs; not 3-edge-colourable:", bad)
    assert bad == [(5, 1, 2)]
    # Lemma D' at v = 85 = 5 * 17: the smallest order in the range of the theorem with a piece whose
    # components are G(m,2), m = 5 (mod 6), m >= 11 (I(85,5,10) = 5 copies of I(17,1,2)), and with
    # proper I-graph pieces (for example I(85,5,17)).
    # Only the pieces with BOTH differences not coprime to 85 are run (plain backtracking is too slow
    # for some of the remaining connected generalised Petersen graphs on 170 vertices).
    v85, bad85, kinds = 85, [], dict(proper=0, disconnected=0)
    for d in range(1, 43):
        for e in range(d + 1, 43):
            if gcd(v85, d) == 1 or gcd(v85, e) == 1:
                continue
            g = gcd(v85, gcd(d, e))
            kinds["disconnected" if g > 1 else "proper"] += 1
            if igraph_colouring(v85, d, e) is None:
                bad85.append((d, e))
    print("Lemma D' at v=85: pieces I(85,d,e), 1<=d<e<=42, gcd(85,d)>1 and gcd(85,e)>1:", sum(kinds.values()), kinds,
          "; not 3-edge-colourable:", bad85)
    assert bad85 == [(17, 34)]
    for v in vs:
        assert v % 12 == 1
        systems = all_cyclic_sts(v)
        stats = dict(pieces=0, disconnected=0, proper=0, rejected=0, colourings=0)
        for bases in systems:
            check_system(v, bases, stats)
        N = (v - 1) // 6
        print(
            f"v={v}: N={N}, k={3 * (v - 3) // 2}, 15+9(N-2)={15 + 9 * (N - 2)}; cyclic STS on Z_v: {len(systems)}; "
            f"Lemma A/B/E assertions hold for all; full colourings assembled and checked: {stats['colourings']}; stats {stats}"
        )
    print("RESULT verify_small: PASS")
