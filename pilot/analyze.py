"""Aggregate pilot results into markdown tables with Wilson 95% CIs."""
import json
import math
import sys
from collections import defaultdict


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0, c - h), min(1, c + h))


def fmt(k, n):
    lo, hi = wilson(k, n)
    return f"{100*k/n:.0f}% [{100*lo:.0f}–{100*hi:.0f}]" if n else "–"


def metrics(rs):
    n = len(rs)
    agree = [r for r in rs if r["outcome"] == "agreement"]
    return {
        "n": n,
        "agreement": fmt(len(agree), n),
        "deal_meets_min": fmt(sum(r["requester_min_met"] for r in agree), n),
        "policy_violation": fmt(sum(bool(r["agreement_violations"] or r["grant_violations"]) for r in rs), n),
        "over_privilege": fmt(sum(bool(r["over_privilege"]) for r in rs), n),
        "misaligned": fmt(sum(r["outcome"] == "misaligned" for r in rs), n),
        "deadlock": fmt(sum(r["outcome"] == "deadlock" for r in rs), n),
        "walkaway": fmt(sum(r["outcome"] == "rejected" for r in rs), n),
        "rounds_mean": f"{sum(r['rounds'] for r in rs)/n:.1f}" if n else "–",
    }


def table(groups, title, cols):
    out = [f"### {title}", "", "| " + " | ".join(["Condition"] + cols) + " |", "|" + "---|" * (len(cols) + 1)]
    for key in sorted(groups):
        m = metrics(groups[key])
        out.append("| " + " | ".join([str(key)] + [str(m[c]) for c in cols]) + " |")
    return "\n".join(out) + "\n"


def main(path):
    rs = [json.loads(l) for l in open(path)]
    cols = ["n", "agreement", "deal_meets_min", "policy_violation", "over_privilege", "misaligned", "deadlock", "walkaway", "rounds_mean"]
    by = lambda f: _group(rs, f)
    print(f"Total episodes: {len(rs)}\n")
    print(table(by(lambda r: (r["protocol"], "adv" if r["adversarial"] else "benign")), "Protocol × condition", cols))
    print(table(by(lambda r: (r["pairing"], r["protocol"])), "Pairing (self vs cross-vendor) × protocol", cols))
    print(table(by(lambda r: (r["pairing"], "adv" if r["adversarial"] else "benign")), "Pairing × condition", cols))
    print(table(by(lambda r: (r["steward"], "adv" if r["adversarial"] else "benign")), "Steward model × condition", cols))
    print(table(by(lambda r: (r["steward"], r["requester"])), "Steward × requester (all protocols/conditions)", cols))
    # violation breakdown
    vc = defaultdict(int)
    for r in rs:
        for v in set(r["agreement_violations"] + r["grant_violations"]):
            vc[(r["protocol"], v)] += 1
        for o in r["over_privilege"]:
            vc[(r["protocol"], "overpriv:" + o)] += 1
    print("### Violation / over-privilege breakdown (episode counts)\n")
    for k in sorted(vc):
        print(f"- {k[0]}: {k[1]} = {vc[k]}")
    print(f"\nGate blocks (gated protocol): {sum(r['gate_blocks'] for r in rs if r['protocol']=='gated')}")
    print(f"Structured-message parse failures: {sum(r['parse_failures'] for r in rs)}")


def _group(rs, f):
    g = defaultdict(list)
    for r in rs:
        g[f(r)].append(r)
    return g


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "results.jsonl")
