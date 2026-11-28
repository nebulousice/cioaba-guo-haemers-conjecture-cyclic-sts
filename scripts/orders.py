"""Orders v = 1 (mod 12) relevant to the write-up (context only; no proof step uses this output).

Prints, for 13 <= v <= VMAX with v = 1 (mod 12):
  (1) the v where Darijani-Pike-Poulin's hypothesis phi(v)/(v-1) >= 2/3 fails,
      i.e. 3*phi(v) < 2*(v-1) (exact integer comparison);
  (2) the smallest v with at least two distinct prime divisors;
  (3) the smallest v with at least four distinct prime divisors.
Integers only, Python standard library only.  Usage: python -I orders.py [VMAX]
"""
import sys, platform


def prime_factors(n):
    ps, d = [], 2
    while d * d <= n:
        if n % d == 0:
            ps.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ps.append(n)
    return ps


def phi(n, ps):
    r = n
    for p in ps:
        r = r // p * (p - 1)
    return r


def main():
    vmax = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    print(f"orders.py; Python {platform.python_version()}; standard library only; VMAX = {vmax}")
    fails, two, four = [], None, None
    for v in range(13, vmax + 1, 12):
        ps = prime_factors(v)
        if 3 * phi(v, ps) < 2 * (v - 1):
            fails.append(v)
        if two is None and len(ps) >= 2:
            two = v
        if four is None and len(ps) >= 4:
            four = v
    print(f"(1) v = 1 (mod 12), 13 <= v <= {vmax}, with phi(v)/(v-1) < 2/3: {len(fails)} orders")
    print(f"    smallest: {fails[0]}; first ten: {', '.join(map(str, fails[:10]))}")
    print(f"    every v = 1 (mod 12) with 13 <= v < {fails[0]} satisfies phi(v)/(v-1) >= 2/3: True")
    print(f"(2) smallest v = 1 (mod 12) with >= 2 distinct prime divisors: {two} = {' * '.join(map(str, prime_factors(two)))}")
    print(f"(3) smallest v = 1 (mod 12) with >= 4 distinct prime divisors: {four} = {' * '.join(map(str, prime_factors(four)))}")
    ok = fails[0] == 385 and two == 85 and four == 5005
    print("RESULT orders: " + ("PASS (385, 85, 5005 as stated in the write-up)" if ok else "MISMATCH"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
