"""Check interface translations against i18n/source.json.  Usage: python3 tools/check-i18n.py [code ...]"""
import json, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent / "i18n"
src = json.loads((root / "source.json").read_text())
codes = sys.argv[1:] or sorted(p.stem for p in root.glob("*.json") if p.stem != "source")
CATS = {"zero", "one", "two", "few", "many", "other"}
bad = 0
for code in codes:
    f = root / f"{code}.json"
    if not f.exists(): print(code, "MISSING FILE"); bad += 1; continue
    d = json.loads(f.read_text()); errs = []
    for k in src["t"]:
        v = d.get("t", {}).get(k)
        if not isinstance(v, str) or not v.strip(): errs.append(f"t missing: {k!r}")
    for k in src["p"]:
        v = d.get("p", {}).get(k)
        if not isinstance(v, str) or not v.strip(): errs.append(f"p missing: {k!r}"); continue
        need = set(re.findall(r"\{[tL]?(\d)\}", k))
        got = set(re.findall(r"\{(\d)(?::[^}]*)?\}", v))
        if need != got: errs.append(f"p placeholders {sorted(need)} vs {sorted(got)}: {k!r} -> {v!r}")
        for m in re.finditer(r"\{\d:([^}]*)\}", v):
            for part in m.group(1).split(";"):
                cat = part.split("=")[0]
                if "=" not in part or cat not in CATS: errs.append(f"bad plural {m.group(0)!r} in {k!r}")
            if "other=" not in m.group(1): errs.append(f"plural without other= in {k!r}")
    extra = set(d.get("t", {})) - set(src["t"]) | set(d.get("p", {})) - set(src["p"])
    if extra: errs.append(f"unknown keys: {sorted(extra)[:5]}")
    print(code, "OK" if not errs else f"{len(errs)} problems"); [print("   ", e) for e in errs[:15]]
    bad += bool(errs)
sys.exit(1 if bad else 0)
