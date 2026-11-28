/-!
# Cioabă–Guo–Haemers, Lemma G: the finite window table (checked by the kernel)

Source: `targets/cioaba-guo-haemers/PROOF.md`, Lemma G and §11 (certificate C-G).

An edge colouring of the generalised Petersen graph `G(n,2)` (edges `w_i w_{i+1}`,
`w_i x_i`, `x_i x_{i+2}`) with colours `1,2,3` is a cyclic sequence of symbols
`t_i = (O_i, S_i, I_i)`: `O_i` colours `w_i w_{i+1}`, `S_i` colours `w_i x_i`, `I_i` colours
`x_i x_{i+2}`. The window `(t_{i-2}, t_{i-1}, t_i)` is *good* when `O_{i-1}, O_i, S_i` are
pairwise distinct and `S_i, I_i, I_{i-2}` are pairwise distinct.

Checked here by `decide +kernel` (no `native_decide`):
* `lemmaG_table`: every symbol of `X`, `Y`, `Z` lies in `{1,2,3}^3`; the three words have
  lengths 7, 4, 6 and begin with `π ρ = 321 123`; every window of `W⁺ = W π ρ` at the 0-based
  indices `2 ≤ i ≤ |W|+1` is good (7 + 4 + 6 = 17 windows).
* `lemmaG_small_cases` (corroboration only): the cyclic word `X Y Z^j` has all `11 + 6j`
  cyclic windows good for `j = 0, …, 8`.

Not formalized: the concatenation argument (that the table implies goodness of every cyclic
window of `X Y Z^j` for all `j`) and the translation "all windows good ⇔ proper colouring of
`G(n,2)`"; both are short hand arguments in `PROOF.md` §6.
-/

namespace CioabaGuoHaemers

/-- A symbol `(O, S, I)`. -/
abbrev Sym := Nat × Nat × Nat

def piS : Sym := (3, 2, 1)
def rhoS : Sym := (1, 2, 3)

def X : List Sym := [(3,2,1), (1,2,3), (2,3,2), (3,1,2), (2,1,3), (3,1,3), (1,2,1)]
def Y : List Sym := [(3,2,1), (1,2,3), (3,2,3), (1,2,1)]
def Z : List Sym := [(3,2,1), (1,2,3), (2,3,2), (3,1,2), (2,1,3), (1,3,1)]

def O (t : Sym) : Nat := t.1
def S (t : Sym) : Nat := t.2.1
def I (t : Sym) : Nat := t.2.2

def distinct3 (a b c : Nat) : Bool := a != b && b != c && a != c

def inAlphabet (t : Sym) : Bool :=
  (1 ≤ O t && O t ≤ 3) && (1 ≤ S t && S t ≤ 3) && (1 ≤ I t && I t ≤ 3)

/-- The window `(p, q, r) = (t_{i-2}, t_{i-1}, t_i)` is good. -/
def goodWindow (p q r : Sym) : Bool :=
  distinct3 (O q) (O r) (S r) && distinct3 (S r) (I r) (I p)

def plus (W : List Sym) : List Sym := W ++ [piS, rhoS]

/-- All windows of `W⁺` at indices `i = k + 2`, `0 ≤ k < |W|`, i.e. `2 ≤ i ≤ |W| + 1`. -/
def tableGood (W : List Sym) : Bool :=
  let L := plus W
  (List.range W.length).all fun k =>
    goodWindow (L.getD k (0,0,0)) (L.getD (k+1) (0,0,0)) (L.getD (k+2) (0,0,0))

def startsPiRho (W : List Sym) : Bool := W.take 2 == [piS, rhoS]

theorem lemmaG_table :
    (X.all inAlphabet && Y.all inAlphabet && Z.all inAlphabet) = true ∧
    (X.length = 7 ∧ Y.length = 4 ∧ Z.length = 6) ∧
    (startsPiRho X && startsPiRho Y && startsPiRho Z) = true ∧
    (tableGood X && tableGood Y && tableGood Z) = true ∧
    X.length + Y.length + Z.length = 17 := by
  decide +kernel

/-- `X Y Z^j`. -/
def T (j : Nat) : List Sym := X ++ Y ++ (List.replicate j Z).flatten

/-- Every cyclic window of the word `L` is good. -/
def cyclicGood (L : List Sym) : Bool :=
  let n := L.length
  (List.range n).all fun i =>
    goodWindow (L.getD ((i + n - 2) % n) (0,0,0)) (L.getD ((i + n - 1) % n) (0,0,0))
      (L.getD i (0,0,0))

theorem lemmaG_small_cases :
    ((List.range 9).all fun j => (T j).length == 11 + 6 * j && cyclicGood (T j)) = true := by
  decide +kernel

end CioabaGuoHaemers

#print axioms CioabaGuoHaemers.lemmaG_table
#print axioms CioabaGuoHaemers.lemmaG_small_cases
