#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Konvertor poznámek notes-ipp (Markdown) -> LaTeX fragmenty.

Poznámky Víta Kološe (submodul notes-ipp/statnice/*.md) jsou psané v Markdownu
s odrážkami odsazenými tabulátory a s inline/zobrazenou matematikou v LaTeXu.
Tento skript je převede 1:1 na LaTeX (zachová obsah i strukturu), aby výsledný
PDF dokument byl věrně "postavený na poznámkách".

Pozn.: skript NEMĚNÍ odborný obsah, jen formát. Audit pokrytí řeší ručně
psaný soubor audit.tex a callouty v main.tex.
"""
import re
import sys
import os

NOTES = os.path.join(os.path.dirname(__file__), "..", "notes-ipp", "statnice")
OUT = os.path.join(os.path.dirname(__file__), "parts")

PLACEHOLDER = "\x00{}\x00"

LATEX_ESCAPE = {
    "&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_",
    "{": r"\{", "}": r"\}",
    "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    "\\": r"\textbackslash{}",
}

# Unicode symboly, které se v poznámkách vyskytují MIMO matematiku (prostý text).
# Matematika je v tu chvíli už vytažená do placeholderů, takže je bezpečné mapovat.
# Unicode pomlcky prevadime na obycejny spojovnik dle preferenci uzivatele.
UNICODE_TEXT = {
    "\u2013": "-", "\u2014": "-",
    "…": r"\dots{}",                      # …
    "→": r"$\to$", "←": r"$\leftarrow$", "↔": r"$\leftrightarrow$",
    "×": r"$\times$", "÷": r"$\div$",
    " ": "~",                              # nbsp
    "„": r"\quotedblbase{}", "“": r"\textquotedblleft{}",
    "”": r"\textquotedblright{}", "‚": r"\quotesinglbase{}",
    "ő": r"\H{o}", "Ő": r"\H{O}",   # ő Ő (Erdős)
}

def escape_text(s):
    out = []
    for ch in s:
        if ch in UNICODE_TEXT:
            out.append(UNICODE_TEXT[ch])
        else:
            out.append(LATEX_ESCAPE.get(ch, ch))
    return "".join(out)

# Unicode symboly uvnitř matematiky (math je vytažená doslovně, tady ji ošetříme).
UNICODE_MATH = {
    "×": r"\times ", "÷": r"\div ", "→": r"\to ", "←": r"\leftarrow ",
    "↔": r"\leftrightarrow ", "\u2013": "-", "\u2014": "-", "…": r"\dots ",
    "„": r"\quotedblbase{}", "“": r"\textquotedblleft{}",
    "”": r"\textquotedblright{}", " ": " ", "ő": r"\H{o}",
}

_CZ = set("áčďéěíĺľňóôŕřšťúůýžÁČĎÉĚÍĹĽŇÓÔŔŘŠŤÚŮÝŽ")

def sanitize_math(s):
    # české znaky uvnitř matematiky (např. funkce š(n)) je nutné obalit \text{}
    out = []
    for ch in s:
        if ch in UNICODE_MATH:
            out.append(UNICODE_MATH[ch])
        elif ch in _CZ:
            out.append(r"\text{" + ch + "}")
        else:
            out.append(ch)
    return "".join(out)

def escape_code(s):
    # uvnitř \texttt{}: bezpečně vykreslit i C# snippety s < > | { } atd.
    repl = {
        "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}",
        "$": r"\$", "&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
        "<": r"\textless{}", ">": r"\textgreater{}", "|": r"\textbar{}",
        "…": "...", "\u2013": "-", "\u2014": "-", "→": r"$\to$",
    }
    # povolíme zalomení dlouhých kódových úseků (C# snippety) za vybranými znaky
    breakafter = set(" .,;)>}_(")
    out = []
    for ch in s:
        out.append(repl.get(ch, ch))
        if ch in breakafter:
            out.append(r"\allowbreak{}")
    return "".join(out)

def process_inline(text):
    """Zpracuje jeden řádek textu odrážky -> LaTeX. Matematika a kód zůstávají
    doslovně (chráněné placeholdery), zbytek se escapuje a formátuje."""
    tokens = []  # uložené LaTeX fragmenty, vkládané zpět přes placeholder
    block_tokens = set()  # indexy tokenů, které jsou blokové (obrázky)

    def stash(latex, block=False):
        tokens.append(latex)
        if block:
            block_tokens.add(len(tokens) - 1)
        return PLACEHOLDER.format(len(tokens) - 1)

    # 1) matematika: nejdřív $$...$$ (display), pak $...$ (inline)
    out = []
    i = 0
    n = len(text)
    while i < n:
        if text.startswith("$$", i):
            j = text.find("$$", i + 2)
            if j == -1:
                out.append(text[i:]); break
            out.append(stash(r"\[" + sanitize_math(text[i+2:j]) + r"\]"))
            i = j + 2
        elif text[i] == "$":
            j = text.find("$", i + 1)
            if j == -1:
                out.append(text[i:]); break
            out.append(stash("$" + sanitize_math(text[i+1:j]) + "$"))
            i = j + 1
        else:
            out.append(text[i]); i += 1
    text = "".join(out)

    # 2) inline kód `...`
    def code_sub(m):
        return stash(r"\texttt{" + escape_code(m.group(1)) + "}")
    text = re.sub(r"`([^`]*)`", code_sub, text)

    # 3) obrázky ![alt](url) -- lokální vložíme jako blok, vzdálené jen popisek
    def img_sub(m):
        alt, url = m.group(1), m.group(2)
        if url.startswith("http"):
            return stash("[obr.: " + escape_text(alt) + "]")  # vzdálený nelze stáhnout
        path = "notes-ipp/statnice/" + url  # lokální cesta (přes \graphicspath)
        return stash(r"\begin{center}\includegraphics[max width=0.85\linewidth,max height=8cm]{"
                     + path + r"}\end{center}", block=True)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", img_sub, text)

    # 4) odkazy [text](url)
    sole_ph = re.compile(r"^\x00(\d+)\x00$")
    def link_sub(m):
        label, url = m.group(1), m.group(2)
        mm = sole_ph.match(label)
        # odkaz obalující jen blokový obrázek -> jen obrázek (href nesmí mít blok)
        if mm and int(mm.group(1)) in block_tokens:
            return label
        lab = label if "\x00" in label else escape_text(label)
        return stash(r"\href{" + url + r"}{" + lab + "}")
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_sub, text)

    # 5) markdown escapes \*  \#  \_  -> chraň znak před formátováním/escapováním
    text = re.sub(r"\\([*_#`\[\]()~^])", lambda m: stash(escape_text(m.group(1))), text)

    # 6) escapuj zbylý prostý text
    text = escape_text(text)

    # 7) tučně **...** a kurzíva *...* (po escapu; hvězdičky escape přežijí)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"(?<![\\*])\*([^*\s][^*]*?)\*", r"\\textit{\1}", text)

    # 8) vrať chráněné fragmenty zpět (opakovaně kvůli vnořeným placeholderům)
    def restore(m):
        return tokens[int(m.group(1))]
    for _ in range(5):
        if "\x00" not in text:
            break
        text = re.sub("\x00(\\d+)\x00", restore, text)
    return text

ITEM_RE = re.compile(r"^(\t*)(- |[0-9]+\. )(.*)$")
HEAD_RE = re.compile(r"^(#{1,3}) (.*)$")
MAXDEPTH = 6  # cap, ať nepřekročíme limit zanoření LaTeX seznamů

# Místa, kde poznámky vědomě odkazují na vlastní procvičení (nejde o definiční
# mezeru, ale o výpočetní dovednost, kterou je třeba natrénovat). Označíme je
# přímo v textu žlutým rámečkem, jak požaduje zadání ("incomplete -> CLEARLY mark").
def practice(text):
    return "\\begin{practicebox}\n" + text + "\n\\end{practicebox}"

CALLOUTS = {
    "spolecna-matematika": [
        ("viz libovolnou vhodnou tabulku",
         practice("Poznámky zde derivační pravidla nerozepisují. Natrénuj derivace součinu, podílu a složené funkce na konkrétních příkladech (viz tabulka derivací).")),
        ("substituci a per-partes je nutné nastudovat",
         practice("Výpočetní techniky (substituce, per partes) si projdi na příkladech - v poznámkách je jen vzorec, ne postup.")),
        ("přesný postup pro odhad součtu řady",
         practice("Odhad součtu řady přes integrál je výpočetní dovednost - vyřeš pár konkrétních příkladů.")),
        ("výpočet determinantu je nutné nastudovat",
         practice("Vlastní výpočet determinantu (rozvoj, úprava na trojúhelníkový tvar) si natrénuj na příkladech.")),
    ],
    "spolecna-informatika": [
        ("Implementovat běžné programové konstrukce vyšších jazyků",
         practice("Překlad konstrukcí (přiřazení, podmínka, cyklus, volání funkce) do instrukcí procesoru je dovednost - natrénuj na konkrétní (i fiktivní) instrukční sadě.")),
        ("Zapsat běžnou konstrukci vyššího jazyka",
         practice("Opačný směr (z dané sekvence instrukcí poznat konstrukci vyššího jazyka) je třeba natrénovat na příkladech.")),
        ("implementaci nacvičit",
         practice("Programem řízenou obsluhu zařízení (PIO) pro zadané adresy a porty je potřeba natrénovat na konkrétních zadáních.")),
    ],
}

def convert(md_path, name):
    with open(md_path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    callouts = CALLOUTS.get(name, [])

    body = []
    stack = []  # seznam (depth, kind) otevřených prostředí

    def close_to(pred):
        while stack and pred(stack[-1]):
            d, kind = stack.pop()
            body.append("\\end{%s}" % ("enumerate" if kind == "enum" else "itemize"))

    def close_all():
        close_to(lambda x: True)

    for raw in lines:
        if raw.strip() == "":
            continue
        h = HEAD_RE.match(raw)
        if h:
            close_all()
            level, title = len(h.group(1)), process_inline(h.group(2))
            if level == 1:
                # název souboru -> řešíme v main.tex, sem dáme jako "část" komentář
                body.append("%% (H1) " + title)
            elif level == 2:
                body.append("\\subsection{%s}" % title)
            else:
                body.append("\\subsubsection{%s}" % title)
            continue
        m = ITEM_RE.match(raw)
        if m:
            depth = min(len(m.group(1)), MAXDEPTH)
            kind = "enum" if m.group(2)[0].isdigit() else "item"
            text = process_inline(m.group(3))
            # zavři hlubší nebo neshodný typ na stejné úrovni
            close_to(lambda x, d=depth, k=kind: x[0] > d or (x[0] == d and x[1] != k))
            if not stack or stack[-1][0] < depth:
                body.append("\\begin{%s}" % ("enumerate" if kind == "enum" else "itemize"))
                stack.append((depth, kind))
            body.append("\\item " + text)
            raw_text = m.group(3)
            for anchor, note in callouts:
                if anchor in raw_text:
                    body.append(note)
            continue
        # fallback: odstavec
        close_all()
        body.append(process_inline(raw.strip()) + "\n")

    close_all()
    return "\n".join(body) + "\n"

def main():
    os.makedirs(OUT, exist_ok=True)
    files = ["spolecna-matematika", "spolecna-informatika",
             "zaklady-umele-inteligence", "strojove-uceni"]
    for name in files:
        src = os.path.join(NOTES, name + ".md")
        tex = convert(src, name)
        dst = os.path.join(OUT, name + ".tex")
        with open(dst, "w", encoding="utf-8") as f:
            f.write(tex)
        print("napsáno:", dst, "(%d B)" % len(tex))

if __name__ == "__main__":
    main()
