#!/usr/bin/env python3
"""
Construiește „Manualul candidatului” – un site de o singură pagină (index.html):
  sursa/capitole/*.md   capitolele (fișe, desene, flashcards)
  sursa/desene/*.svg    desenele
  sursa/pagini/*.md     paginile Examenul și Recapitularea
  tools/intrebari/*.txt grilele
  sursa/prioritati.txt  cât de probabilă e fiecare grilă (1–3)

Rulare:  python3 tools/carte.py
"""
import hashlib
import html
import json
import random
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "sursa"
QDIR = ROOT / "tools" / "intrebari"
LET = "abcd"

MD_EXT = ["tables", "sane_lists", "attr_list", "md_in_html"]


# ---------------------------------------------------------------- grile
def parse_questions(path):
    qs, cur = [], None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.startswith("# titlu:"):
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
    if cur:
        qs.append(cur)
    for q in qs:
        assert q["ok"] and len(q["bad"]) == 3, (path.name, q["q"][:60])
    return qs


def load_priorities():
    pr = {}
    for line in (SRC / "prioritati.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        fid, rest = line.split(":", 1)
        d = {}
        for part in rest.split(";"):
            part = part.strip()
            if not part:
                continue
            k, v = part.split("=")
            for n in v.split(","):
                d[int(n)] = int(k.strip()[1])
        pr[fid.strip()] = d
    return pr


def questions_for(fids, pr):
    out = []
    for fid in fids:
        qs = parse_questions(QDIR / f"{fid}.txt")
        for i, q in enumerate(qs, 1):
            qid = f"{fid}-{i:03d}"
            rnd = random.Random(int(hashlib.sha1(qid.encode()).hexdigest(), 16))
            opts = [q["ok"]] + q["bad"]
            order = list(range(4))
            rnd.shuffle(order)
            out.append({
                "id": qid,
                "p": pr.get(fid, {}).get(i, 2),
                "q": q["q"],
                "o": [opts[k] for k in order],
                "a": order.index(0),
                "e": q["ex"],
            })
    out.sort(key=lambda x: x["p"])  # sort stabil: întâi cele foarte probabile
    return out


# ---------------------------------------------------------------- capitole
def svg(name):
    p = SRC / "desene" / f"{name}.svg"
    return p.read_text(encoding="utf-8").strip()


def render_md(text):
    def desen(m):
        name, _, cap = m.group(1).partition("|")
        cap_html = f"<figcaption>{html.escape(cap.strip())}</figcaption>" if cap.strip() else ""
        return f'\n<figure class="dg">{svg(name.strip())}{cap_html}</figure>\n'

    text = re.sub(r"\{\{desen:([^}]+)\}\}", desen, text)
    # liniile de listă/tabel lipite de un paragraf primesc un rând liber înainte
    fixed, prev = [], ""
    for line in text.split("\n"):
        s_ = line.lstrip()
        kind = "ul" if re.match(r"[-*] ", s_) else "ol" if re.match(r"\d+\. ", s_) else "tb" if s_.startswith("|") else "bq" if s_.startswith(">") else "tx" if s_ else ""
        pk = "ul" if re.match(r"[-*] ", prev.lstrip()) else "ol" if re.match(r"\d+\. ", prev.lstrip()) else "tb" if prev.lstrip().startswith("|") else "bq" if prev.lstrip().startswith(">") else "tx" if prev.strip() else ""
        if kind in ("ul", "ol", "tb") and pk == "tx" and not line.startswith(" "):
            fixed.append("")
        fixed.append(line)
        prev = line
    text = "\n".join(fixed)
    out = markdown.markdown(text, extensions=MD_EXT)
    # chenare speciale după primul simbol din citat
    kinds = {"🌍": ("analog", "Ca în viața reală"), "⚠️": ("capcana", "Capcană la grilă"),
             "💡": ("retine", "Ține minte"), "ℹ️": ("info", "Bine de știut"), "🧮": ("calc", "Exemplu rezolvat")}

    syms = "|".join(re.escape(k) for k in kinds)

    def one(body):
        for sym, (cls, label) in kinds.items():
            if body.startswith("<p>" + sym):
                body = body.replace("<p>" + sym, "<p>", 1).replace("<p> ", "<p>", 1)
                return f'<aside class="co co-{cls}"><div class="co-h">{label}</div>{body}</aside>'
        return f"<blockquote>{body}</blockquote>"

    def callout(m):
        body = m.group(1).strip()
        parts = [x.strip() for x in re.split(r"(?=<p>(?:%s))" % syms, body) if x.strip()]
        return "".join(one(x) for x in parts)

    out = re.sub(r"<blockquote>(.*?)</blockquote>", callout, out, flags=re.S)
    out = out.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")
    # linkurile spre vechile fișiere .md devin text simplu
    out = re.sub(r'<a href="[^"]*\.md[^"]*">(.*?)</a>', r"\1", out)
    return out


def parse_chapter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    body = text[m.end():]
    blocks = re.findall(r"^::: *(\w[\w-]*) *(.*?)\n(.*?)^:::\s*$", body, re.S | re.M)
    fise, flash, pescurt = [], [], ""
    for kind, title, content in blocks:
        if kind == "pe-scurt":
            pescurt = render_md(content)
        elif kind == "fisa":
            fise.append({"t": title.strip(), "h": render_md(content)})
        elif kind == "flash":
            for line in content.strip().splitlines():
                if "||" in line:
                    f, b = line.split("||", 1)
                    flash.append([f.strip(), b.strip()])
    return meta, pescurt, fise, flash


def main():
    pr = load_priorities()
    chapters = []
    for path in sorted((SRC / "capitole").glob("*.md")):
        meta, pescurt, fise, flash = parse_chapter(path)
        fids = [x.strip() for x in meta.get("grile", "").split(",") if x.strip()]
        chapters.append({
            "nr": int(meta["nr"]),
            "id": meta["id"],
            "t": meta["titlu"],
            "tema": meta.get("tema", ""),
            "parte": meta.get("parte", "S"),
            "stele": int(meta.get("stele", "2")),
            "itemi": meta.get("itemi", ""),
            "timp": meta.get("timp", ""),
            "sursa": meta.get("sursa", ""),
            "ps": pescurt,
            "fise": fise,
            "flash": flash,
            "q": questions_for(fids, pr),
        })
    chapters.sort(key=lambda c: c["nr"])
    pages = {}
    for p in sorted((SRC / "pagini").glob("*.md")):
        pages[p.stem] = render_md(p.read_text(encoding="utf-8"))

    data = {"ch": chapters, "pg": pages}
    tpl = (ROOT / "tools" / "carte_template.html").read_text(encoding="utf-8")
    frag = tpl.replace("/*__DATA__*/{}", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    (ROOT / "tools" / "carte_fragment.html").write_text(frag, encoding="utf-8")
    full = ('<!doctype html>\n<html lang="ro">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '</head>\n<body>\n' + frag + '\n</body>\n</html>\n')
    (ROOT / "index.html").write_text(full, encoding="utf-8")

    nq = sum(len(c["q"]) for c in chapters)
    nf = sum(len(c["flash"]) for c in chapters)
    nfi = sum(len(c["fise"]) for c in chapters)
    print(f"Capitole: {len(chapters)} | fișe: {nfi} | flashcards: {nf} | grile: {nq} | "
          f"index.html: {len(full)//1024} KB")
    for c in chapters:
        p1 = sum(1 for q in c["q"] if q["p"] == 1)
        print(f"  {c['nr']:>2}. {c['t'][:48]:<48} fișe {len(c['fise']):>2}  flash {len(c['flash']):>3}  grile {len(c['q']):>3} (★ {p1})")


if __name__ == "__main__":
    main()
