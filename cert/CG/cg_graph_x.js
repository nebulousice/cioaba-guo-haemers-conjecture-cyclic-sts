// Certificate C-G, independent cross-check (Node.js, no dependencies, integers only).
//
// Method: different from the window check. For each n we build the generalised Petersen graph
// G(n,2) explicitly as a vertex/edge list (outer vertices w_i = i, inner vertices x_i = n + i;
// edges w_i w_{i+1}, w_i x_i, x_i x_{i+2}, indices mod n), confirm it is a simple cubic graph
// with 2n vertices and 3n distinct edges, colour edge w_i w_{i+1} by O_i, w_i x_i by S_i and
// x_i x_{i+2} by I_i where (O_i S_i I_i) is the i-th symbol of the cyclic word, and check that
// the three edges at every vertex carry three different colours from {1,2,3}.
//
//   Part 1: T = X Y Z^j for j = 0..JMAX (n = 11 + 6j), the colouring used in Lemma G.
//   Part 2: every cyclic word W_1...W_r with W_s in {X,Y,Z} and 2 <= r <= RMAX
//           (the general concatenation claim of Lemma G, finite range).
//   Part 3: n = 11 colour strings O, S, I agree with the 'Smallest case' line of PROOF.md.
//   Part 4: controls: recolouring any single edge of the n = 11 and n = 17 colourings to
//           either other colour must be detected (all 2 * 3n recolourings).
// Finite ranges only corroborate; the all-j statement is the concatenation argument.
//
// Usage: node cg_graph_x.js PATH/TO/PROOF.md [JMAX=2000] [RMAX=7]
'use strict';
const fs = require('fs');

const WORD = {
  X: ['321', '123', '232', '312', '213', '313', '121'],
  Y: ['321', '123', '323', '121'],
  Z: ['321', '123', '232', '312', '213', '131'],
};

let failures = 0;
function bad(msg) { failures++; console.log('  FAIL: ' + msg); }

function buildGraph(n) {
  // returns array of edges [u, v, kind, i]; kind 0 = outer (O), 1 = spoke (S), 2 = inner (I)
  const E = [];
  for (let i = 0; i < n; i++) {
    E.push([i, (i + 1) % n, 0, i]);
    E.push([i, n + i, 1, i]);
    E.push([n + i, n + ((i + 2) % n), 2, i]);
  }
  return E;
}

function checkSimpleCubic(n, E) {
  const seen = new Set();
  const deg = new Int32Array(2 * n);
  for (const [u, v] of E) {
    if (u === v) return 'loop';
    const key = u < v ? u * 4 * n + v : v * 4 * n + u;
    if (seen.has(key)) return 'multi-edge';
    seen.add(key);
    deg[u]++; deg[v]++;
  }
  if (E.length !== 3 * n) return 'edge count';
  for (let x = 0; x < 2 * n; x++) if (deg[x] !== 3) return 'degree ' + deg[x] + ' at ' + x;
  return null;
}

function colourEdges(E, seq) {
  // seq: array of symbol strings, length n
  return E.map(([, , kind, i]) => Number(seq[i][kind]));
}

function isProper(n, E, col) {
  // bitmask of colours seen at each vertex
  const mask = new Int32Array(2 * n);
  for (let k = 0; k < E.length; k++) {
    const c = col[k];
    if (c !== 1 && c !== 2 && c !== 3) return false;
    const b = 1 << c;
    const [u, v] = E[k];
    if (mask[u] & b || mask[v] & b) return false;
    mask[u] |= b; mask[v] |= b;
  }
  for (let x = 0; x < 2 * n; x++) if (mask[x] !== 14) return false;
  return true;
}

function seqOf(names) {
  const s = [];
  for (const nm of names) for (const t of WORD[nm]) s.push(t);
  return s;
}

function main() {
  const proofPath = process.argv[2];
  if (!proofPath) { console.log('usage: node cg_graph_x.js PROOF.md [JMAX] [RMAX]'); process.exit(2); }
  const JMAX = Number(process.argv[3] || 2000);
  const RMAX = Number(process.argv[4] || 7);
  const text = fs.readFileSync(proofPath, 'utf8');

  // Part 0: the words in this file equal those in PROOF.md section 11 'Inputs'.
  console.log('Part 0: words equal PROOF.md section 11 Inputs');
  const inp = text.split('\n').find((l) => l.includes('*Inputs.*'));
  if (!inp) bad('Inputs line not found');
  else {
    for (const nm of ['X', 'Y', 'Z']) {
      const m = inp.match(new RegExp('\\$' + nm + '\\$ = ([0-9, ]+?)[;.]'));
      const got = m ? m[1].split(',').map((t) => t.trim()) : null;
      if (!got || got.join(' ') !== WORD[nm].join(' ')) bad('word ' + nm + ' differs: ' + got);
      else console.log('  ' + nm + ' = ' + got.join(' ') + ' OK');
    }
  }

  // Part 1
  console.log('Part 1: T = X Y Z^j on explicit G(11+6j, 2), j = 0..' + JMAX);
  let ok1 = 0;
  for (let j = 0; j <= JMAX; j++) {
    const names = ['X', 'Y'];
    for (let t = 0; t < j; t++) names.push('Z');
    const seq = seqOf(names);
    const n = seq.length;
    if (n !== 11 + 6 * j) { bad('length ' + n + ' != 11+6j at j=' + j); continue; }
    const E = buildGraph(n);
    const sc = checkSimpleCubic(n, E);
    if (sc) { bad('G(' + n + ',2) not simple cubic: ' + sc); continue; }
    if (isProper(n, E, colourEdges(E, seq))) ok1++;
    else bad('X Y Z^' + j + ' not proper on G(' + n + ',2)');
  }
  console.log('  proper: ' + ok1 + ' of ' + (JMAX + 1) + ' (n = 11 .. ' + (11 + 6 * JMAX) + ')');

  // Part 2
  console.log('Part 2: all cyclic words W_1..W_r over {X,Y,Z}, 2 <= r <= ' + RMAX);
  let tot2 = 0, ok2 = 0;
  for (let r = 2; r <= RMAX; r++) {
    const count = 3 ** r;
    for (let code = 0; code < count; code++) {
      const names = [];
      let c = code;
      for (let s = 0; s < r; s++) { names.push('XYZ'[c % 3]); c = Math.floor(c / 3); }
      const seq = seqOf(names);
      const n = seq.length;
      const E = buildGraph(n);
      const sc = checkSimpleCubic(n, E);
      tot2++;
      if (sc) { bad(names.join('') + ': not simple cubic ' + sc); continue; }
      if (isProper(n, E, colourEdges(E, seq))) ok2++;
      else bad(names.join('') + ' not proper on G(' + n + ',2)');
    }
  }
  console.log('  proper: ' + ok2 + ' of ' + tot2);

  // Part 3
  console.log('Part 3: n = 11 colour strings versus PROOF.md Smallest case');
  const seq11 = seqOf(['X', 'Y']);
  const O = seq11.map((s) => s[0]).join(' ');
  const S = seq11.map((s) => s[1]).join(' ');
  const I = seq11.map((s) => s[2]).join(' ');
  const sm = text.split('\n').find((l) => l.includes('*Smallest case ($n=11$'));
  const grab = (lbl) => {
    const m = sm && sm.match(new RegExp('\\$' + lbl + '_i\\$ = `([0-9 ]+)`'));
    return m ? m[1] : null;
  };
  for (const [lbl, val] of [['O', O], ['S', S], ['I', I]]) {
    const g = grab(lbl);
    if (g !== val) bad(lbl + ' string: PROOF.md ' + g + ' vs computed ' + val);
    else console.log('  ' + lbl + ' = ' + val + ' OK');
  }

  // Part 4
  console.log('Part 4: controls (every single-edge recolouring must be detected)');
  for (const names of [['X', 'Y'], ['X', 'Y', 'Z']]) {
    const seq = seqOf(names);
    const n = seq.length;
    const E = buildGraph(n);
    const col = colourEdges(E, seq);
    let tried = 0, caught = 0;
    for (let k = 0; k < E.length; k++) {
      for (const c of [1, 2, 3]) {
        if (c === col[k]) continue;
        const m = col.slice(); m[k] = c; tried++;
        if (!isProper(n, E, m)) caught++;
      }
    }
    if (caught !== tried) bad('n=' + n + ': ' + (tried - caught) + ' recolourings undetected');
    console.log('  n = ' + n + ': ' + caught + ' of ' + tried + ' recolourings detected');
  }
  // informative control: X rotated by one symbol breaks the common-prefix rule; report the result.
  {
    const rot = WORD.X.slice(1).concat(WORD.X.slice(0, 1)).concat(WORD.Y);
    const n = rot.length;
    const E = buildGraph(n);
    const p = isProper(n, E, colourEdges(E, rot));
    console.log('  rotated-X control (n = ' + n + '): ' + (p ? 'proper (not a failure; informative only)' : 'improper, detected'));
  }

  console.log('');
  if (failures) { console.log('FAIL cg_graph_x (' + failures + ' failure(s))'); process.exit(1); }
  console.log('PASS cg_graph_x: X Y Z^j proper on explicit G(11+6j,2) for j = 0..' + JMAX +
    '; all ' + tot2 + ' cyclic {X,Y,Z}-words with 2 <= r <= ' + RMAX + ' proper; n = 11 strings match PROOF.md; controls detected');
}

main();
