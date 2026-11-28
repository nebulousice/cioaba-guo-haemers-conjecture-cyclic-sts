"""Check of Lemma N1 in PROOF.md (explicit 3-edge-colouring of I-graphs with coprime rim gcds).

Integer arithmetic only, standard library only.  Numerical corroboration: the proof of Lemma N1 is by hand.

Lemma N1.  Let I(n,p,q) be an I-graph (n >= 3, 1 <= p,q <= n-1, p,q != n/2) with
u = gcd(n,p) >= 2, t = gcd(n,q) >= 2 and gcd(u,t) = 1.  Put x(i) = q^{-1} i mod u, y(i) = p^{-1} i mod t,
eps_L(j) = j mod 2 for 0 <= j < L, except eps_L(L-1) = 2 when L is odd,
r(x) = -eps_u(x-1) - eps_u(x), s(y) = -eps_t(y-1) - eps_t(y)   (all in Z_3), and colour
    outer rim  w_i w_{i+p} : eps_t(y(i)) + r(x(i))
    inner rim  x_i x_{i+q} : eps_u(x(i)) + s(y(i))
    spoke      w_i x_i     : r(x(i)) + s(y(i)).
Then this is a proper 3-edge-colouring.

What is checked here, on the explicitly built graph (edges as unordered vertex pairs):
  (A) every triple (n,p,q) with 3 <= n <= NMAX, 1 <= p,q <= n-1, p,q != n/2, meeting the hypotheses:
      the graph has 3n distinct edges, every vertex has degree 3, each edge gets exactly one colour in {0,1,2},
      and the three edges at every vertex have three different colours;
  (B) the family used in PROOF.md (Lemma D, Case 1): every I(m,a,b), m odd, 3 <= m <= MMAX,
      1 <= a < b <= (m-1)/2, gcd(m,a) >= 2, gcd(m,b) >= 2, gcd(m,a,b) = 1  -- same test;
  (C) negative controls: recolouring any single edge of a few instances is detected; and eps_L really
      satisfies eps_L(j) != eps_L(j-1) for all j, for L = 2..NMAX.

Usage: python verify_N1.py NMAX MMAX
"""
import sys
import platform
from math import gcd


def eps(L):
    e = [j % 2 for j in range(L)]
    if L % 2:
        e[-1] = 2
    return e


def n1_colouring(n, p, q):
    """returns dict {frozenset edge: colour} for the Lemma N1 colouring of I(n,p,q)"""
    u, t = gcd(n, p), gcd(n, q)
    assert u >= 2 and t >= 2 and gcd(u, t) == 1
    eu, et = eps(u), eps(t)
    r = [(-eu[(x - 1) % u] - eu[x]) % 3 for x in range(u)]
    s = [(-et[(y - 1) % t] - et[y]) % 3 for y in range(t)]
    qi, pi = pow(q, -1, u), pow(p, -1, t)
    col = {}
    for i in range(n):
        x, y = (qi * i) % u, (pi * i) % t
        for e, c in ((frozenset([("w", i), ("w", (i + p) % n)]), (et[y] + r[x]) % 3),
                     (frozenset([("x", i), ("x", (i + q) % n)]), (eu[x] + s[y]) % 3),
                     (frozenset([("w", i), ("x", i)]), (r[x] + s[y]) % 3)):
            assert len(e) == 2, "loop"
            assert e not in col, "edge listed twice"
            col[e] = c
    return col


def proper(n, col):
    if len(col) != 3 * n:
        return False
    seen = {}
    for e, c in col.items():
        if c not in (0, 1, 2):
            return False
        for z in e:
            seen.setdefault(z, []).append(c)
    return len(seen) == 2 * n and all(sorted(cs) == [0, 1, 2] for cs in seen.values())


def hyp(n, p, q):
    if not (1 <= p <= n - 1 and 1 <= q <= n - 1) or 2 * p == n or 2 * q == n:
        return False
    u, t = gcd(n, p), gcd(n, q)
    return u >= 2 and t >= 2 and gcd(u, t) == 1


def main():
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    MMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 601
    print("verify_N1.py; Python", platform.python_version(), "(", platform.python_implementation(), ")",
          platform.system(), platform.release(), "; standard library only")
    ok = True

    # (A)
    cnt = odd = 0
    first = None
    for n in range(3, NMAX + 1):
        for p in range(1, n):
            for q in range(1, n):
                if hyp(n, p, q):
                    good = proper(n, n1_colouring(n, p, q))
                    if not good:
                        print("FAIL (A)", (n, p, q))
                    ok &= good
                    cnt += 1
                    odd += n % 2
                    if first is None:
                        first = (n, p, q)
    print(f"(A) all I(n,p,q), 3 <= n <= {NMAX}, meeting the hypotheses of Lemma N1: {cnt} triples "
          f"({odd} with n odd; smallest {first}); proper in every case: {ok}")

    # (B)
    okB = True
    cntB = 0
    smallest = None
    for m in range(3, MMAX + 1, 2):
        for a in range(1, (m - 1) // 2 + 1):
            if gcd(m, a) < 2:
                continue
            for b in range(a + 1, (m - 1) // 2 + 1):
                if gcd(m, b) >= 2 and gcd(m, gcd(a, b)) == 1:
                    assert hyp(m, a, b)
                    good = proper(m, n1_colouring(m, a, b))
                    if not good:
                        print("FAIL (B)", (m, a, b))
                    okB &= good
                    cntB += 1
                    if smallest is None:
                        smallest = (m, a, b)
    print(f"(B) all proper I(m,a,b) with m odd, 3 <= m <= {MMAX}, 1 <= a < b <= (m-1)/2, gcd(m,a,b) = 1: "
          f"{cntB} graphs (smallest {smallest}); proper in every case: {okB}")
    ok &= okB

    # (C)
    okC = all(all(e[j] != e[j - 1] for j in range(L)) for L in range(2, NMAX + 1) for e in [eps(L)])
    det = tot = 0
    for (n, p, q) in ((15, 3, 5), (35, 5, 7), (85, 5, 17), (12, 2, 3), (385, 35, 11)):
        col = n1_colouring(n, p, q)
        assert proper(n, col)
        for e in list(col):
            for d in (1, 2):
                bad = dict(col)
                bad[e] = (col[e] + d) % 3
                tot += 1
                det += not proper(n, bad)
    print(f"(C) eps_L adjacent-distinct for L = 2..{NMAX}: {okC}; single-edge recolourings detected: {det} of {tot}")
    ok &= okC and det == tot

    print("RESULT verify_N1:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
