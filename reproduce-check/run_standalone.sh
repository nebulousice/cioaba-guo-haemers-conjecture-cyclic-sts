#!/usr/bin/env bash
# Rerun the certificates and the corroboration scripts on the files of THIS folder
# (the public PROOF.md), without the private research repository.
# Usage, from the root of this folder:  bash reproduce-check/run_standalone.sh [PYTHON]
# Writes reproduce-check/out/*.out. Each output starts with a provenance header and
# ends with the program's exit code and runtime. Outputs are never edited by hand.
set -u
PY=${1:-python}
OUT=reproduce-check/out
mkdir -p "$OUT"

run() {  # $1 output name, $2 working dir, rest = command
  local name="$1" dir="$2"; shift 2
  local out="$OUT/$name"
  {
    echo "command (in $dir): $*"
    echo "date (UTC): $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "PROOF.md sha256: $(sha256sum PROOF.md | cut -d' ' -f1)"
    echo "certified lines sha256: $(grep -E '^\| \$[XYZ](\^\+)?\$ \||\*Inputs\.\*|\*Smallest case \(\$n=11\$' PROOF.md | sha256sum | cut -d' ' -f1)"
    echo "python: $("$PY" -c 'import sys;print(sys.version.split()[0])'); node: $(node --version 2>/dev/null || echo none)"
    echo "platform: $("$PY" -c 'import platform;print(platform.platform())')"
    echo "---"
  } > "$out"
  local t0 rc
  t0=$(date +%s)
  ( cd "$dir" && "$@" ) >> "$out" 2>&1; rc=$?
  { echo "---"; echo "exit code: $rc"; echo "runtime_s: $(( $(date +%s) - t0 ))"; } >> "$out"
  echo "$name: exit $rc; $(grep -E 'PASS|FAIL' "$out" | tail -n 1)"
}

run cg_windows.out   cert/CG  "$PY" -I cg_windows.py ../../PROOF.md
run cg_graph_x.out   cert/CG  node cg_graph_x.js ../../PROOF.md 2000 7
run cg_graph_b.out   .        "$PY" cert/C-G/cg_graph_b.py 500
run verify_gn2.out   prover   "$PY" -I verify_gn2.py 200
run verify_misc.out  prover   "$PY" -I verify_misc.py 60 100000
run verify_small.out prover   "$PY" -I verify_small.py 13 25
run verify_N1.out    prover   "$PY" -I verify_N1.py 200 601
run orders.out       .        "$PY" -I scripts/orders.py 200000
