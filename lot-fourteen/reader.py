#!/usr/bin/env python3
"""
Lot Fourteen, Lesefassungen als HTML.

Aufruf:  python3 reader.py chapters/chNN_vX_Y_en.md ziel.html

Laeuft normalerweise nicht von Hand, sondern aus build.py: der schreibt
read/ neu, ein Kapitel je Datei und einmal das ganze Buch.

Wozu das gut ist: eine md-Datei im Chat ist eine Datei zum Herunterladen.
Eine HTML-Seite kann man aufmachen und lesen. Der Ordner read/ ist deshalb
kein zweiter Kanon, sondern nur die Fassung zum Anschauen.

Der Kopf ist als Katalogeintrag gesetzt, weil das Buch aus einem Katalog
kommt: Los, Nummer, Tag, Fassung, Umfang.
"""
import io
import os
import re
import sys

NAME = re.compile(r"^ch(\d{2})_v(\d+)[._](\d+)_en\.md$")
ORD = ("Null One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve "
       "Thirteen Fourteen Fifteen Sixteen Seventeen").split()

CSS = """
:root{
  --paper:#E7E9EC; --sheet:#FBFBFC; --ink:#15171B; --muted:#5F6773;
  --rule:#C8CCD3; --accent:#2F5D62; --accent-soft:#2F5D6222;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --paper:#0E1013; --sheet:#161A1F; --ink:#DCE0E5; --muted:#8C949F;
    --rule:#272C34; --accent:#7FB2AB; --accent-soft:#7FB2AB22;
  }
}
:root[data-theme="dark"]{
  --paper:#0E1013; --sheet:#161A1F; --ink:#DCE0E5; --muted:#8C949F;
  --rule:#272C34; --accent:#7FB2AB; --accent-soft:#7FB2AB22;
}
*{ box-sizing:border-box; }
body{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:"Source Serif 4", Georgia, "Times New Roman", serif;
  font-size:clamp(1.02rem, 0.96rem + 0.3vw, 1.14rem); line-height:1.72;
  -webkit-font-smoothing:antialiased;
}
.sheet{
  max-width:41rem; margin:0 auto; background:var(--sheet); min-height:100vh;
  padding:clamp(1.6rem, 1rem + 3vw, 4.2rem) clamp(1.2rem, 0.6rem + 3.4vw, 3.6rem);
  border-left:1px solid var(--rule); border-right:1px solid var(--rule);
}
header{ margin-bottom:clamp(2rem, 1rem + 3vw, 3.4rem); }
.card{
  border-top:2px solid var(--ink); border-bottom:1px solid var(--rule);
  padding:0.85rem 0 1.1rem;
}
.eyebrow, .meta, footer, .toc, h2{
  font-family:"IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  font-variant-numeric:tabular-nums;
}
.eyebrow, .meta, footer{
  font-size:0.7rem; letter-spacing:0.14em; text-transform:uppercase;
  color:var(--muted);
}
.eyebrow{ display:block; margin-bottom:0.9rem; }
h1{
  font-family:"Cormorant Garamond", Georgia, serif; font-weight:600;
  font-size:clamp(2rem, 1.3rem + 3.4vw, 3.15rem); line-height:1.06;
  margin:0; letter-spacing:-0.005em; text-wrap:balance; color:var(--ink);
}
.meta{ display:flex; flex-wrap:wrap; gap:0.5rem 1.4rem; margin-top:1.1rem; }
.meta b{ font-weight:500; color:var(--accent); }
h2{
  font-weight:500; font-size:0.74rem; letter-spacing:0.16em;
  text-transform:uppercase; color:var(--accent); margin:3rem 0 1.4rem;
  padding-bottom:0.5rem; border-bottom:1px solid var(--rule);
}
p{ margin:0 0 1.15rem; }
blockquote{
  margin:1.6rem 0 1.9rem; padding:0.2rem 0 0.2rem 1.4rem;
  border-left:2px solid var(--accent); color:var(--ink);
}
blockquote p{ margin:0 0 0.85rem; }
blockquote p:last-child{ margin-bottom:0; }
em{ font-style:italic; }
hr{ border:0; height:1.9rem; margin:2rem 0 2.1rem; position:relative; }
hr.scene{ height:0; border-top:1px solid var(--rule); margin:2.6rem auto 2.7rem;
  width:38%; }
hr.scene::after{ content:none; }
hr::after{
  content:"\\00B7 \\00B7 \\00B7"; position:absolute; inset:0; display:flex;
  align-items:center; justify-content:center; letter-spacing:0.75em;
  color:var(--rule); font-size:0.9rem; text-indent:0.75em;
}
footer{
  margin-top:clamp(2.4rem, 1.4rem + 3vw, 4rem); padding-top:1rem;
  border-top:1px solid var(--rule); display:flex; flex-wrap:wrap;
  gap:0.4rem 1.4rem; justify-content:space-between;
}
a{ color:var(--accent); text-decoration-thickness:1px; text-underline-offset:0.2em; }
a:focus-visible{ outline:2px solid var(--accent); outline-offset:3px; }
::selection{ background:var(--accent-soft); }

/* Nur im Sammelband */
.toc{ margin:0 0 1rem; padding:0; list-style:none; font-size:0.82rem; }
.toc li{
  display:grid; grid-template-columns:2.6rem 1fr auto; gap:0.9rem;
  align-items:baseline; padding:0.42rem 0; border-bottom:1px solid var(--rule);
}
.toc .n{ color:var(--accent); letter-spacing:0.1em; }
.toc .t{
  font-family:"Source Serif 4", Georgia, serif; font-size:1.02rem;
  letter-spacing:0; text-transform:none;
}
.toc .d{ color:var(--muted); font-size:0.68rem; letter-spacing:0.1em;
  text-transform:uppercase; text-align:right; }
.chapter{ padding-top:clamp(2.4rem, 1.4rem + 4vw, 5rem); }
.chapter + .chapter{ border-top:1px solid var(--rule); }
.chapter .card{ border-top-width:1px; }
.chapter h1{ font-size:clamp(1.65rem, 1.1rem + 2.4vw, 2.4rem); }
.top{ font-size:0.68rem; letter-spacing:0.14em; text-transform:uppercase;
  font-family:"IBM Plex Mono", ui-monospace, monospace; }
@media (max-width:640px){
  .sheet{ border-left:0; border-right:0; }
  .toc li{ grid-template-columns:2.2rem 1fr; }
  .toc .d{ grid-column:2; text-align:left; }
}
"""

HEAD = """<title>%(title)s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600&family=IBM+Plex+Mono:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;1,8..60,400&display=swap">
<style>%(css)s</style>
"""


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


def parse(text, fname, band=1, blabel=""):
    """Kapitel in Titel, Datum, Fassung und Absaetze zerlegen.

    Die Datumszeile ist die erste ganz kursive Zeile nach der Kopfzeile und
    nur die: im Fliesstext stehen Saetze wie *It's been handled.*, und die
    sind Absaetze.
    """
    m = NAME.match(fname)
    if not m:
        raise ValueError("Kein Kapiteldateiname: " + fname)
    lines = text.replace("\r\n", "\n").split("\n")

    title = lines[0].lstrip("# ").strip()
    if ":" in title:
        title = title.split(":", 1)[1].strip()
    mv = re.search(r"Version\s+([\d.]+)", lines[1] if len(lines) > 1 else "")

    i, date = 2, ""
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and re.match(r"^\*[^*].*\*$", lines[i].strip()):
        date = lines[i].strip()[1:-1]
        i += 1

    body = []
    quote = []

    def flush_quote():
        """Aufeinanderfolgende Zitatzeilen werden ein Block, kein Absatz."""
        if quote:
            inner = "".join("<p>%s</p>" % inline(q) for q in quote)
            body.append("<blockquote>%s</blockquote>" % inner)
            del quote[:]

    for line in lines[i:]:
        s = line.strip()
        if s.startswith(">"):
            inner_line = s[1:].strip()
            if inner_line:
                quote.append(inner_line)
            continue
        flush_quote()
        if not s:
            continue
        if s == "* * *":
            body.append('<hr class="scene">')
        elif re.match(r"^-{3,}$", s):
            body.append("<hr>")
        elif s.startswith("## "):
            body.append("<h2>%s</h2>" % esc(s[3:].strip()))
        elif s.startswith("# "):
            continue
        else:
            body.append("<p>%s</p>" % inline(s))
    flush_quote()

    return {
        "band": band,
        "blabel": blabel,
        "num": int(m.group(1)),
        "title": title,
        "date": date,
        "version": mv.group(1) if mv else "",
        "words": len(" ".join(lines[i:]).split()),
        "body": body,
        "file": fname,
    }


def card(c, level=1):
    label = ORD[c["num"]] if c["num"] < len(ORD) else str(c["num"])
    meta = []
    if c["date"]:
        meta.append("<span>%s</span>" % esc(c["date"]))
    if c["version"]:
        meta.append("<span>Fassung <b>%s</b></span>" % esc(c["version"]))
    meta.append("<span>%d Woerter</span>" % c["words"])
    tag = "header" if level == 1 else "div"
    sep = " &nbsp;&#183;&nbsp; "
    brow = sep.join(x for x in ("Lot Fourteen", esc(c.get("blabel") or ""),
                                "Chapter %s" % label) if x)
    return ('<%s><div class="card">'
            '<span class="eyebrow">%s</span>'
            "<h1>%s</h1></div>"
            '<div class="meta">%s</div></%s>'
            % (tag, brow, esc(c["title"]), "".join(meta), tag))


def render(text, fname, blabel="", band=1):
    """Eine Seite fuer ein Kapitel."""
    c = parse(text, fname, band, blabel)
    return "\n".join([
        HEAD % {"title": esc(c["title"]), "css": CSS},
        '<div class="sheet">',
        card(c),
        "\n".join(c["body"]),
        '<footer><span>%s</span><span>Kanon: %s</span></footer>'
        % (esc(fname), esc(c["blabel"] or "chapters/")),
        "</div>",
    ])


def render_book(quads):
    """Eine Seite fuer alle Kapitel aller Baende, mit Inhaltsverzeichnis.

    quads: Liste von (dateiname, text, band, bandtitel), in Reihenfolge.
    Die Anker tragen die Bandnummer, sonst zeigen in einem zweiten Band
    alle Verweise auf Kapitel 1 des ersten.
    """
    ch = [parse(t, f, b, bl) for f, t, b, bl in quads]
    total = sum(c["words"] for c in ch)
    toc, seen = ["<ul class='toc'>"], None
    for c in ch:
        if c["band"] != seen and c["blabel"]:
            toc.append('<li class="band"><span class="n"></span>'
                       '<span class="t"><b>%s</b></span>'
                       '<span class="d"></span></li>' % esc(c["blabel"]))
            seen = c["band"]
        toc.append(
            '<li><span class="n">%02d</span>'
            '<a class="t" href="#b%dch%02d">%s</a>'
            '<span class="d">%s</span></li>'
            % (c["num"], c["band"], c["num"], esc(c["title"]),
               esc(c["date"] or "")))
    toc.append("</ul>")

    out = [HEAD % {"title": "Lot Fourteen", "css": CSS}, '<div class="sheet" id="top">']
    out.append('<header><div class="card">'
               '<span class="eyebrow">Sammelband &nbsp;&#183;&nbsp; Lesefassung</span>'
               "<h1>Lot Fourteen</h1></div>"
               '<div class="meta"><span>%d Kapitel</span>'
               "<span><b>%s</b> Woerter</span>"
               "<span>%s</span></div></header>"
               % (len(ch), format(total, ",").replace(",", "."),
                  esc(", ".join(dict.fromkeys(
                      c["blabel"] for c in ch if c["blabel"])) or "chapters/")))
    out.append("\n".join(toc))
    for c in ch:
        out.append('<article class="chapter" id="b%dch%02d">'
                   % (c["band"], c["num"]))
        out.append(card(c, level=2))
        out.append("\n".join(c["body"]))
        out.append('<p class="top"><a href="#top">&#8593; Inhalt</a></p>')
        out.append("</article>")
    out.append("</div>")
    return "\n".join(out)


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    src, dst = sys.argv[1], sys.argv[2]
    text = io.open(src, encoding="utf-8").read()
    html = render(text, os.path.basename(src))
    io.open(dst, "w", encoding="utf-8", newline="\n").write(html)
    print("%s, %d Zeichen." % (dst, len(html)))


if __name__ == "__main__":
    main()
