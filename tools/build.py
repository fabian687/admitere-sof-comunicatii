#!/usr/bin/env python3
"""
Generează din sursele tools/intrebari/*.txt:
  - grile/<ID>.md          (grile pe capitole, cu răspunsuri ascunse)
  - simulari/simulare-NN.md (teste complete 20 legislație + 25 specialitate)
  - quiz/index.html        (quiz interactiv, funcționează offline)

Format sursă (blocuri separate prin linie goală):
    # titlu: Constituția României
    ? Textul întrebării
    + răspunsul corect
    - variantă greșită
    - variantă greșită
    - variantă greșită
    = explicație scurtă (articolul / formula)

Rulare:  python3 tools/build.py
"""
import hashlib
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "intrebari"
LETTERS = "abcd"


def parse(path):
    title = path.stem
    qs = []
    cur = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.startswith("# titlu:"):
            title = line.split(":", 1)[1].strip()
            continue
        if not line.strip():
            if cur:
                qs.append(cur)
                cur = None
            continue
        tag, text = line[0], line[1:].strip()
        if tag == "?":
            if cur:
                qs.append(cur)
            cur = {"q": text, "ok": None, "bad": [], "ex": ""}
        elif cur is None:
            continue
        elif tag == "+":
            cur["ok"] = text
        elif tag == "-":
            cur["bad"].append(text)
        elif tag == "=":
            cur["ex"] = (cur["ex"] + " " + text).strip()
        else:  # continuare a întrebării pe rândul următor
            cur["q"] += " " + line.strip()
    if cur:
        qs.append(cur)
    for i, q in enumerate(qs):
        if q["ok"] is None or len(q["bad"]) != 3:
            raise SystemExit(f"{path.name}: întrebarea {i+1} nu are 1 corect + 3 greșite: {q['q'][:60]}")
    return title, qs


def shuffle(q, qid):
    """Amestecă determinist variantele, ca litera corectă să fie distribuită echilibrat."""
    seed = int(hashlib.sha1(qid.encode()).hexdigest(), 16)
    rnd = random.Random(seed)
    opts = [q["ok"]] + q["bad"]
    order = list(range(4))
    rnd.shuffle(order)
    opts = [opts[i] for i in order]
    return opts, LETTERS[order.index(0)]


def md_escape(s):
    return s.replace("|", "\\|")


def main():
    files = sorted(SRC.glob("*.txt"))
    chapters = []
    for f in files:
        title, qs = parse(f)
        cid = f.stem
        items = []
        for n, q in enumerate(qs, 1):
            qid = f"{cid}-{n:03d}"
            opts, ans = shuffle(q, qid)
            items.append({"id": qid, "q": q["q"], "o": opts, "a": ans, "e": q["ex"]})
        chapters.append({"id": cid, "title": title, "items": items,
                         "kind": "L" if cid.startswith("L") else "S"})

    # ---------- grile/<ID>.md ----------
    (ROOT / "grile").mkdir(exist_ok=True)
    for ch in chapters:
        folder = "legislatie" if ch["kind"] == "L" else "specialitate"
        out = [f"# Grile — {ch['title']}\n",
               f"{len(ch['items'])} întrebări. Un singur răspuns corect. "
               f"Încearcă singur, apoi deschide „Răspuns”.\n",
               f"[← Înapoi la capitol](../{folder}/{ch['id']}.md) · [Cuprins](../README.md)\n"]
        for n, it in enumerate(ch["items"], 1):
            out.append(f"\n**{n}. {it['q']}**\n")
            for L, o in zip(LETTERS, it["o"]):
                out.append(f"- {L}) {o}")
            ex = f" — {it['e']}" if it["e"] else ""
            out.append(f"\n<details><summary>Răspuns</summary>\n\n**{it['a']})** {it['o'][LETTERS.index(it['a'])]}{ex}\n\n</details>\n")
        (ROOT / "grile" / f"{ch['id']}.md").write_text("\n".join(out), encoding="utf-8")

    # ---------- simulări ----------
    leg = [it for ch in chapters if ch["kind"] == "L" for it in ch["items"]]
    spe = [it for ch in chapters if ch["kind"] == "S" for it in ch["items"]]
    rnd = random.Random(2026)
    leg_pool = leg[:]
    spe_pool = spe[:]
    rnd.shuffle(leg_pool)
    rnd.shuffle(spe_pool)
    nsim = max(1, min(len(leg_pool) // 20, len(spe_pool) // 25))
    nsim = min(nsim, 8)
    (ROOT / "simulari").mkdir(exist_ok=True)
    for old in (ROOT / "simulari").glob("simulare-*.md"):
        old.unlink()
    for s in range(nsim):
        L = leg_pool[s * 20:(s + 1) * 20]
        S = spe_pool[s * 25:(s + 1) * 25]
        test = S + L  # ca la examen: 25 specialitate + 20 legislație
        out = [f"# Simularea {s+1} — test complet (45 de itemi, 90 de minute)\n",
               "Condiții de examen: cronometru 90 min, fără notițe, fără calculator. "
               "Notează răspunsurile pe o foaie, apoi verifică la final.\n",
               "Nota = 1 + 0,20 × (răspunsuri corecte). Minim de admitere: 5,00 (20 corecte).\n",
               "[Cuprins](../README.md)\n",
               "## Partea I — Pregătire de specialitate (25 de itemi)\n"]
        for n, it in enumerate(test, 1):
            if n == 26:
                out.append("\n## Partea a II-a — Legislație (20 de itemi)\n")
            out.append(f"\n**{n}. {it['q']}**\n")
            for Lt, o in zip(LETTERS, it["o"]):
                out.append(f"- {Lt}) {o}")
        out.append("\n---\n\n## Barem\n")
        out.append("| Nr. | Răspuns | Explicație |\n|---|---|---|")
        for n, it in enumerate(test, 1):
            out.append(f"| {n} | **{it['a']}** | {md_escape(it['e'] or '—')} |")
        out.append("\n**Departajare la medii egale:** 1) corecte la specialitate; "
                   "2) corecte la ultimii 10 itemi de legislație (aici 36–45); 3) media la BAC.\n")
        (ROOT / "simulari" / f"simulare-{s+1:02d}.md").write_text("\n".join(out), encoding="utf-8")

    # ---------- quiz/index.html ----------
    data = [{"id": ch["id"], "t": ch["title"], "k": ch["kind"],
             "q": [[it["q"], it["o"], LETTERS.index(it["a"]), it["e"]] for it in ch["items"]]}
            for ch in chapters]
    tpl = (ROOT / "tools" / "quiz_template.html").read_text(encoding="utf-8")
    html = tpl.replace("/*__DATA__*/[]", json.dumps(data, ensure_ascii=False))
    standalone = ('<!doctype html>\n<html lang="ro">\n<head>\n<meta charset="utf-8">\n'
                  '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                  '</head>\n<body>\n' + html + '</body>\n</html>\n')
    (ROOT / "quiz" / "index.html").write_text(standalone, encoding="utf-8")
    # varianta fără schelet, pentru publicare ca pagină web (artifact)
    (ROOT / "tools" / "quiz_fragment.html").write_text(html, encoding="utf-8")

    # ---------- statistici ----------
    from collections import Counter
    allit = leg + spe
    cnt = Counter(it["a"] for it in allit)
    print(f"Capitole: {len(chapters)} | legislație: {len(leg)} | specialitate: {len(spe)} | total: {len(allit)}")
    print("Distribuția literei corecte:", dict(sorted(cnt.items())))
    print(f"Simulări generate: {nsim}")
    for ch in chapters:
        print(f"  {ch['id']:<4} {len(ch['items']):>3}  {ch['title']}")


if __name__ == "__main__":
    main()
