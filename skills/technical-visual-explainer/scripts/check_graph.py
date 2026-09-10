"""Audit a simple directed diagram specification, never the rendered image.

Optional JSON input: nodes (id, role, label), edges (source, target, outcome),
loops (check, work, output, human). This helper does not dictate authoring format.
"""
from __future__ import annotations
import argparse
import json
import re
from collections import deque
from pathlib import Path


def audit(graph: dict) -> list[str]:
    findings = []
    nodes = {n['id']: n for n in graph['nodes']}
    if len(nodes) != len(graph['nodes']):
        findings.append('duplicate node IDs')
    edges = graph['edges']
    for e in edges:
        if e['source'] not in nodes or e['target'] not in nodes:
            findings.append(f"unknown endpoint: {e['source']} -> {e['target']}")
    if findings:
        return findings

    def reachable(start, target, excluded=frozenset(), blocked=frozenset()):
        queue, seen = deque([start]), set()
        while queue:
            current = queue.popleft()
            if current in blocked:
                continue
            if current == target:
                return True
            if current in seen:
                continue
            seen.add(current)
            queue.extend(e['target'] for i, e in enumerate(edges)
                         if i not in excluded and e['source'] == current)
        return False

    for loop in graph.get('loops', []):
        check, work, output, human = (loop[k] for k in ('check','work','output','human'))
        if any(n not in nodes for n in (check, work, output, human)):
            findings.append('loop references an unknown node')
            continue
        outgoing = [(i,e) for i,e in enumerate(edges) if e['source'] == check]
        passes = frozenset(i for i,e in outgoing if e.get('outcome') == 'PASS')
        revisions = [e['target'] for _,e in outgoing if e.get('outcome') == 'REVISE']
        humans = [e['target'] for _,e in outgoing if e.get('outcome') == 'HUMAN']
        if not passes or not reachable(check, output):
            findings.append(f'{check}: no passing output path')
        if reachable(work, output, passes):
            findings.append(f'{check}: accepted output reachable without PASS')
        if not revisions or any(not reachable(r, work) for r in revisions):
            findings.append(f'{check}: revision does not return to rework')
        if any(reachable(r, check, blocked={work}) for r in revisions):
            findings.append(f'{check}: revision can bypass declared rework')
        if not reachable(work, check):
            findings.append(f'{check}: rework does not return through checking')
        if humans != [human]:
            findings.append(f'{check}: human branch target mismatch')
        # Follow escalation until a recheck or an explicitly named terminal.
        # A separate WAIT node is valid; a word such as "stopwatch" is not STOP.
        queue, pending = deque([human]), set()
        while queue:
            current = queue.popleft()
            if current == check or current in pending:
                continue
            pending.add(current)
            queue.extend(e['target'] for e in edges if e['source'] == current)
        terminals = {n for n in pending
                     if not any(e['source'] == n for e in edges)
                     and re.match(r'^(WAIT|STOP|UNRESOLVED)\b', nodes[n]['label'].strip(), re.I)}
        for n in pending:
            if not any(e['source'] == n for e in edges) and n not in terminals:
                findings.append(f'{n}: unlabeled human dead end')
        if any(not reachable(n, check) and not any(reachable(n, t) for t in terminals)
               for n in pending):
            findings.append(f'{human}: resumption bypasses checking or lacks a waiting terminal')
    return findings


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('specification', type=Path)
    args=parser.parse_args()
    result=audit(json.loads(args.specification.read_text(encoding='utf8')))
    print(json.dumps({'scope':'specification only; actual-image review required','findings':result},indent=2))
    raise SystemExit(bool(result))
