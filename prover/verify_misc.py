"""Corroboration for PROOF.md (cioaba-guo-haemers, CGH-1): Lemma F and the colour count.  Integers only.

Lemma F: for even N >= 4, on Z_{N-1} u {inf},
    F_j = {{inf, j}} u {{j-t, j+t} : 1 <= t <= (N-2)/2},  j in Z_{N-1},
are N-1 perfect matchings that partition E(K_N).

Count: for v = 1 (mod 12), with N = (v-1)/6 and k = 3(v-3)/2:
    N is even and 15 + 9(N-2) = k = 6 + 9(N-1).
"""
import sys


def lemma_F(nmax):
    for N in range(4, nmax + 1, 2):
        m = N - 1
        seen = {}
        for j in range(m):
            F = [frozenset(["inf", j])] + [frozenset([(j - t) % m, (j + t) % m]) for t in range(1, (N - 2) // 2 + 1)]
            cover = [x for e in F for x in e]
            assert len(F) == N // 2 and len(set(cover)) == N and all(len(e) == 2 for e in F)
            for e in F:
                assert e not in seen
                seen[e] = j
        assert len(seen) == N * (N - 1) // 2
    return True


def count(vmax):
    for v in range(13, vmax + 1, 12):
        N, k = (v - 1) // 6, 3 * (v - 3) // 2
        assert (v - 1) % 6 == 0 and (3 * (v - 3)) % 2 == 0
        assert N % 2 == 0 and 15 + 9 * (N - 2) == k == 6 + 9 * (N - 1)
    return True


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    vmax = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
    print(f"Lemma F: F_0..F_(N-2) are perfect matchings partitioning E(K_N) for every even N in 4..{nmax}:", lemma_F(nmax))
    print(f"Count: N even and 15+9(N-2) = k = 6+9(N-1) for every v = 1 (mod 12), 13 <= v <= {vmax}:", count(vmax))
    print("RESULT verify_misc: PASS")
