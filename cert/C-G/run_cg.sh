#!/usr/bin/env bash
# Run both C-G implementations and archive their output with provenance.
# Usage (from the repository root of a fresh clone):
#   bash targets/cioaba-guo-haemers/cert/C-G/run_cg.sh [JMAX] [RMAX] [PYTHON]
set -u
JMAX=${1:-500}; RMAX=${2:-7}; PY=${3:-python}
D=targets/cioaba-guo-haemers/cert/C-G
mkdir -p "$D/out"

run() {  # $1 out-name, $2 libraries line, $3 script, rest = script args
  local name="$1" out="$D/out/$1" libs="$2" script="$3"; shift 3
  {
    echo "command: $PY $script $*"
    echo "date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "commit: $(git rev-parse HEAD)"
    echo "tracked files modified: $(git status --porcelain --untracked-files=no | wc -l | tr -d ' ')"
    echo "python: $("$PY" -c 'import sys;print(sys.version.split()[0])')"
    echo "platform: $("$PY" -c 'import platform;print(platform.platform())')"
    echo "$libs"
    echo "sha256: $(sha256sum "$script" | cut -d' ' -f1)  $script"
    echo "---"
  } > "$out"
  local t0 t1 rc
  t0=$(date +%s%N)
  "$PY" "$script" "$@" >> "$out" 2>&1; rc=$?
  t1=$(date +%s%N)
  { echo "---"; echo "exit code: $rc"; echo "runtime_ms: $(( (t1 - t0) / 1000000 ))"; } >> "$out"
  echo "$name: $(grep -E '^(PASS|FAIL)$' "$out" | tail -n 1) (exit $rc)"
}

run cg_windows_a.out "libraries: standard library only (git used to read PROOF.md at db574df)" \
    "$D/cg_windows_a.py" "$JMAX" "$RMAX"
run cg_graph_b.out "libraries: networkx $("$PY" -c 'import networkx;print(networkx.__version__)'), python-sat $("$PY" -c 'import pysat;print(pysat.__version__)') (Glucose4)" \
    "$D/cg_graph_b.py" "$JMAX"
