#!/usr/bin/env bash
# Run both C-G certificates and write cg_windows.out and cg_graph_x.out next to this script.
# Usage (from any directory): bash targets/cioaba-guo-haemers/cert/CG/run_cg.sh
# Each output begins with the command, UTC date, commit, tool versions and script sha256,
# and ends with the program's own PASS or FAIL line. Outputs are never edited by hand.
set -uo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
root="$(cd "$here/../../../.." && pwd)"
proof="$root/targets/cioaba-guo-haemers/PROOF.md"
cd "$here"

header() {
  echo "command: $1"
  echo "date (UTC): $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "repo commit: $(git -C "$root" rev-parse HEAD)"
  echo "working tree: $(git -C "$root" status --porcelain -- targets/cioaba-guo-haemers/PROOF.md | wc -l | tr -d ' ') local change(s) to PROOF.md"
  echo "PROOF.md sha256: $(sha256sum "$proof" | cut -d' ' -f1)"
  echo "script sha256: $(sha256sum "$2" | cut -d' ' -f1)  $2"
  echo "platform: $(uname -s -r -m)"
}

{
  header "python -I cg_windows.py ../../PROOF.md" cg_windows.py
  echo "python: $(python -c 'import sys; print(sys.version.replace(chr(10), " "))') (standard library only: re, sys)"
  echo "----"
  python -I cg_windows.py "$proof"; rc=$?
  echo "exit code: $rc"
  [ $rc -eq 0 ] && echo "FINAL: PASS (C-G primary, cg_windows.py)" || echo "FINAL: FAIL (C-G primary, cg_windows.py)"
} > cg_windows.out 2>&1

{
  header "node cg_graph_x.js ../../PROOF.md 2000 7" cg_graph_x.js
  echo "node: $(node --version) (no packages; built-in fs only)"
  echo "----"
  node cg_graph_x.js "$proof" 2000 7; rc=$?
  echo "exit code: $rc"
  [ $rc -eq 0 ] && echo "FINAL: PASS (C-G cross-check, cg_graph_x.js)" || echo "FINAL: FAIL (C-G cross-check, cg_graph_x.js)"
} > cg_graph_x.out 2>&1

tail -n 1 cg_windows.out
tail -n 1 cg_graph_x.out
