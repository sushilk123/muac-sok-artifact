"""Build an IEEEtran two-column LaTeX/PDF version of the paper from paper.md.

Pipeline: paper.md -> preprocess (headers, refs, tables, figures) -> pandoc LaTeX body
-> postprocess (citations, symbols) -> main.tex + refs_ieee.bib -> tectonic -> main.pdf
"""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "paper" / "latex"
NBSP = "\u00a0"


def pandoc_latex(md):
    r = subprocess.run(["pandoc", "-f", "markdown", "-t", "latex", "--natbib", "--wrap=none"],
                       input=md, capture_output=True, text=True, check=True)
    return r.stdout


# ------------------------------------------------------------------ bibliography

def parse_bib(text):
    entries = {}
    for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", text, re.S):
        entries[m.group(2).strip()] = (m.group(1), m.group(3), m.group(0))
    return entries


def field(body, name):
    m = re.search(r"\b" + name + r"\s*=\s*", body, re.I)
    if not m:
        return None
    i = m.end()
    if body[i] == "{":
        depth, j = 0, i
        while j < len(body):
            depth += {"{": 1, "}": -1}.get(body[j], 0)
            if depth == 0:
                return body[i + 1:j]
            j += 1
    m2 = re.match(r'"([^"]*)"|(\w+)', body[i:])
    return m2.group(1) or m2.group(2) if m2 else None


def surname(author):
    author = author.strip()
    if author.startswith("{") and author.endswith("}"):
        return author[1:-1]
    author = author.replace("{", "").replace("}", "")
    if "," in author:
        return author.split(",")[0].strip()
    return author.split()[-1]


def narrative_name(entries, key):
    typ, body, _ = entries[key]
    a = field(body, "author") or key
    authors = [x for x in re.split(r"\s+and\s+", a) if x.strip()]
    names = [surname(x) for x in authors]
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return f"{names[0]} et al."


def ieee_bib(entries):
    out = []
    for key, (typ, body, raw) in entries.items():
        eprint = field(body, "eprint")
        if eprint and not re.search(r"\b(howpublished|journal|booktitle)\s*=", body, re.I):
            raw = raw[:-1].rstrip().rstrip(",") + f",\n  howpublished = {{arXiv preprint arXiv:{eprint}}}\n}}"
        if (eprint or field(body, "doi") or "researchgate" in (field(body, "url") or "")) and typ.lower() != "online":
            raw = re.sub(r"\n\s*url\s*=\s*\{[^}]*\},?", "", raw)
        out.append(raw)
    return "\n\n".join(out) + "\n"


# ------------------------------------------------------------------ tables

def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def cells_to_latex(cells):
    """Convert a list of markdown cell strings to LaTeX in one pandoc call."""
    sep = "\n\nZZCELLSEPZZ\n\n"
    tex = pandoc_latex(sep.join(c if c else "~" for c in cells))
    parts = [p.strip() for p in tex.split("ZZCELLSEPZZ")]
    assert len(parts) == len(cells), (len(parts), len(cells))
    return [p.replace("\\textasciitilde{}", "") if p == "\\textasciitilde{}" else p for p in parts]


def is_short_col(col):
    return all(len(re.sub(r"\[.*?\]", "", c)) <= 6 for c in col)


def make_table(num, caption_md, header, rows, wide=None):
    ncols = len(header)
    flat = cells_to_latex([caption_md] + header + [c for r in rows for c in r])
    cap, flat = flat[0], flat[1:]
    head, body = flat[:ncols], flat[ncols:]
    body = [body[i:i + ncols] for i in range(0, len(body), ncols)]
    cols = list(zip(*([header] + rows)))
    spec = "".join("c" if is_short_col(c[1:]) else ">{\\raggedright\\arraybackslash}X" for c in cols)
    if "X" not in spec:
        spec = ">{\\raggedright\\arraybackslash}X" + spec[1:]
    wide = ncols >= 8 if wide is None else wide
    env, width = ("table*", "\\textwidth") if wide else ("table", "\\columnwidth")
    lines = [f"\\begin{{{env}}}[t]", "\\centering", "\\footnotesize" if wide else "\\scriptsize",
             "\\setlength{\\tabcolsep}{3pt}", f"\\caption{{{cap}}}", f"\\label{{tab-{num}}}",
             f"\\begin{{tabularx}}{{{width}}}{{{spec}}}", "\\toprule",
             " & ".join(f"\\textbf{{{h}}}" for h in head) + " \\\\", "\\midrule"]
    for r in body:
        lines.append(" & ".join(r) + " \\\\")
    lines += ["\\bottomrule", "\\end{tabularx}", f"\\end{{{env}}}"]
    return "\n".join(lines)


def heatmap_table(rows_json):
    comms = {}
    for r in rows_json:
        comms.setdefault(r["comm"], []).append(r)
    order = ["AHT/ZSC", "Negotiation", "LLM-MAS frameworks/benchmarks", "Protocols",
             "Security/identity/delegation", "Governance/CoopAI", "Data ecosystems"]
    label = {"LLM-MAS frameworks/benchmarks": "LLM-MAS frameworks \\& benchmarks",
             "Security/identity/delegation": "Security, identity \\& delegation",
             "Governance/CoopAI": "Governance \\& cooperative AI", "AHT/ZSC": "Ad hoc teamwork / ZSC"}
    lines = ["\\begin{table*}[t]", "\\centering", "\\footnotesize", "\\setlength{\\tabcolsep}{4pt}",
             f"\\caption{{Requirement coverage by community ($n={len(rows_json)}$ coded works). Each cell gives "
             "the number of works coded \\full{} / \\half{}; shading is proportional to "
             "$(\\#\\full + 0.5\\,\\#\\half)/n_{\\text{community}}$. The coordination requirements (R1, R3, R5) and "
             "the security requirements (R2, R4, R7, R8) are covered by disjoint communities.}",
             "\\label{tab-2}", "\\begin{tabular}{l c cccccccc}", "\\toprule",
             "\\textbf{Community} & $n$ & \\textbf{R1} & \\textbf{R2} & \\textbf{R3} & \\textbf{R4} & "
             "\\textbf{R5} & \\textbf{R6} & \\textbf{R7} & \\textbf{R8} \\\\",
             "& & \\scriptsize coord. & \\scriptsize sec. & \\scriptsize coord. & \\scriptsize sec. & "
             "\\scriptsize coord. & \\scriptsize gov. & \\scriptsize sec. & \\scriptsize sec. \\\\", "\\midrule"]
    for c in order:
        rs = comms.get(c, [])
        cells = []
        for i in range(8):
            f = sum(r["R"][i] == "●" for r in rs)
            p = sum(r["R"][i] == "◐" for r in rs)
            score = (f + 0.5 * p) / len(rs) if rs else 0
            shade = int(round(score * 70))
            cells.append(f"\\cellcolor{{cellblue!{shade}}}{f}/{p}")
        lines.append(f"{label.get(c, c)} & {len(rs)} & " + " & ".join(cells) + " \\\\")
    lines += ["\\bottomrule", "\\end{tabular}", "\\end{table*}"]
    return "\n".join(lines)


def master_longtable(rows_json):
    order = {"AHT/ZSC": 0, "Negotiation": 1, "LLM-MAS frameworks/benchmarks": 2, "Protocols": 3,
             "Security/identity/delegation": 4, "Governance/CoopAI": 5, "Data ecosystems": 6}
    rows = sorted(rows_json, key=lambda r: (order.get(r["comm"], 9), r["year"], r["work"]))
    md_cells = []
    for r in rows:
        cap = lambda x: x[:1].upper() + x[1:] if x else x
        md_cells += [f"{r['work']} [@{r['key']}]", cap(r["B"]), cap(r["D"])]
    tex = cells_to_latex(md_cells)
    lines = ["\\onecolumn", "{\\scriptsize", "\\setlength{\\LTleft}{0pt plus 1fill}\\setlength{\\LTright}{0pt plus 1fill}", "\\setlength{\\tabcolsep}{2.5pt}",
             "\\begin{longtable}{>{\\raggedright\\arraybackslash}p{4.2cm} c cccccccc "
             ">{\\raggedright\\arraybackslash}p{3.6cm} >{\\raggedright\\arraybackslash}p{4.4cm}}",
             f"\\caption{{Full coding of the {len(rows)} works against R1--R8 (\\full{{}} full, \\half{{}} partial, "
             "\\none{} not addressed), with trust assumption (Axis B) and evaluation regime (Axis D).}"
             "\\label{tab-master}\\\\",
             "\\toprule", "\\textbf{Work} & \\textbf{Year} & R1 & R2 & R3 & R4 & R5 & R6 & R7 & R8 & "
             "\\textbf{Trust assumption} & \\textbf{Evaluation} \\\\", "\\midrule", "\\endfirsthead",
             "\\toprule", "\\textbf{Work} & \\textbf{Year} & R1 & R2 & R3 & R4 & R5 & R6 & R7 & R8 & "
             "\\textbf{Trust assumption} & \\textbf{Evaluation} \\\\", "\\midrule", "\\endhead",
             "\\bottomrule", "\\endfoot"]
    current = None
    for i, r in enumerate(rows):
        if r["comm"] != current:
            current = r["comm"]
            lines.append(f"\\multicolumn{{12}}{{l}}{{\\textit{{{current.replace('&', '\\&')}}}}} \\\\")
        work, b, d = tex[3 * i:3 * i + 3]
        lines.append(" & ".join([work, r["year"]] + r["R"] + [b, d]) + " \\\\")
    lines += ["\\end{longtable}", "}"]
    return "\n".join(lines)


# ------------------------------------------------------------------ figures

FIG_SETTING = r"""
\begin{figure}[t]
\centering
\begin{tikzpicture}[font=\scriptsize, >=Stealth, node distance=4mm,
  org/.style={draw=black!60, rounded corners=2pt, fill=gray!7, text width=2.95cm, align=center, inner sep=3pt},
  agent/.style={draw=black!70, rounded corners=2pt, fill=white, text width=2.6cm, align=center, inner sep=2.5pt}]
\node[agent] (aA) {\textbf{Agent} $a_A$\\[-1pt]{\tiny vendor X model}};
\node[agent, right=1.75cm of aA] (aB) {\textbf{Agent} $a_B$\\[-1pt]{\tiny vendor Y model}};
\node[above=1.5mm of aA, align=center] (pA) {\textbf{Principal} $p_A$ (Org.\ A)\\[-1pt]{\tiny policy $\Phi_A$, credentials $C_A$}};
\node[above=1.5mm of aB, align=center] (pB) {\textbf{Principal} $p_B$ (Org.\ B)\\[-1pt]{\tiny objective $u_{p_B}$, credentials $C_B$}};
\begin{scope}[on background layer]
\node[org, fit=(aA)(pA), inner sep=2.5pt] (OA) {};
\node[org, fit=(aB)(pB), inner sep=2.5pt] (OB) {};
\end{scope}
\draw[<->, thick] (aA.east) -- node[above=1pt, font=\tiny, align=center] {protocol $\mathcal{P}$} node[below=1pt, font=\tiny, align=center] {discover\\negotiate\\delegate\\resolve} (aB.west);
\node[draw=cellblue!80!black, fill=cellblue!25, rounded corners=2pt, minimum height=5mm, text width=7.3cm, align=center,
  below=7mm of $(aA.south)!0.5!(aB.south)$] (G) {\textbf{Trusted access-control layer} $\mathcal{G}$: identity, authorization, audit};
\node[draw=black!50, fill=cellblue!8, rounded corners=2pt, minimum height=5mm, text width=7.3cm, align=center,
  below=0.8mm of G] (E) {\textbf{Shared environment} $\mathcal{E}$: resources $R$ under policies $\Phi$};
\draw[->] (aA.south) -- (aA.south |- G.north) node[pos=0.45, left, font=\tiny] {act};
\draw[->] (aB.south) -- (aB.south |- G.north) node[pos=0.45, right, font=\tiny] {act};
\node[above=1mm of $(OA.north)!0.5!(OB.north)$, font=\tiny, text=red!65!black, align=center]
  {untrusted peers may be malicious, subverted, misrepresenting,\\colluding, or curious (T1--T5)};
\end{tikzpicture}
\caption{The MUAC setting. Independently developed agents acting for distinct principals interact only through a protocol $\mathcal{P}$ and act on shared resources only through a trusted access-control layer $\mathcal{G}$; no agent's model, claims, or messages are trusted.}
\label{fig-setting}
\end{figure}
"""

FIG_PILOT = r"""
\begin{figure}[t]
\centering
\begin{tikzpicture}
\begin{axis}[ybar, width=\columnwidth, height=4.6cm, bar width=9pt, ymin=0, ymax=105,
  ylabel={Agreement rate (\%)}, ylabel style={font=\scriptsize}, tick label style={font=\scriptsize},
  symbolic x coords={Free-form, Structured, Gated}, xtick=data, enlarge x limits=0.25,
  legend style={font=\scriptsize, at={(0.5,1.02)}, anchor=south, legend columns=2, draw=none},
  nodes near coords, every node near coord/.append style={font=\tiny, yshift=5pt},
  error bars/y dir=both, error bars/y explicit]
\addplot[fill=cellblue!55, draw=cellblue!80!black] coordinates {
  (Free-form,91) += (0,4) -= (0,8)
  (Structured,98) += (0,1) -= (0,6)
  (Gated,78) += (0,7) -= (0,10)};
\addplot[fill=red!45, draw=red!60!black] coordinates {
  (Free-form,86) += (0,5) -= (0,9)
  (Structured,59) += (0,9) -= (0,10)
  (Gated,72) += (0,8) -= (0,10)};
\legend{Benign, Adversarial (forged notice)}
\end{axis}
\end{tikzpicture}
\caption{Pilot agreement rates by protocol and condition (Wilson 95\% CIs; $n=90$ per bar). Structured messaging eliminated violations but collapsed under attack through walk-aways; the gate guaranteed compliance at a substantial benign cost.}
\label{fig-pilot}
\end{figure}
"""


# ------------------------------------------------------------------ main

def main():
    md = (ROOT / "paper" / "paper.md").read_text()
    entries = parse_bib((ROOT / "paper" / "refs.bib").read_text())
    rows_json = json.loads((ROOT / "coding" / "master.json").read_text())

    # split YAML front matter
    _, yaml, body = md.split("---\n", 2)
    abstract_md = re.search(r"abstract: \|\n(.*)", yaml, re.S).group(1)
    abstract_md = "\n".join(l[2:] if l.startswith("  ") else l for l in abstract_md.splitlines())

    # move end-matter (artifact/AI/acknowledgments) and appendices out of the body
    end_start = body.index("**Artifact availability.**")
    app_start = body.index("# Appendix A.")
    main_md, end_md, app_md = body[:end_start], body[end_start:app_start], body[app_start:]
    main_md = main_md.rstrip().rstrip("-").rstrip()

    # appendices: reorder so the long coding table is last
    appA = app_md[:app_md.index("# Appendix B.")]
    appB = app_md[app_md.index("# Appendix B."):app_md.index("# Appendix C.")]
    appC = app_md[app_md.index("# Appendix C."):]
    appB = appB.replace("# Appendix B. Coding Rubric", "# Coding Rubric {#app-rubric}")
    appC = appC.replace("# Appendix C. Pilot Prompts and Protocol", "# Pilot Prompts and Protocol {#app-pilot}")

    # numbered headers -> labels
    def hdr(m):
        num = m.group(2).rstrip(".")
        return f"{m.group(1)} {m.group(3)} {{#sec-{num.replace('.', '-')}}}"
    main_md = re.sub(r"^(#+) (\d+(?:\.\d+)*\.?) (.+)$", hdr, main_md, flags=re.M)

    # section references
    def secref(num):
        return f"\\ref{{sec-{num.replace('.', '-')}}}"
    def ref_all(text):
        text = re.sub(r"§(\d+(?:\.\d+)?)–§(\d+(?:\.\d+)?)",
                      lambda m: f"Sections{NBSP}{secref(m.group(1))}--{secref(m.group(2))}", text)
        text = re.sub(r"§(\d+(?:\.\d+)?)", lambda m: f"Section{NBSP}{secref(m.group(1))}", text)
        text = re.sub(r"\(Appendix A\)", f"(Appendix{NBSP}\\\\ref{{app-coding}})", text)
        text = text.replace("Appendix A gives", f"Appendix{NBSP}\\ref{{app-coding}} gives")
        return text
    main_md, appB, appC = ref_all(main_md), ref_all(appB), ref_all(appC)

    # tables: caption paragraph + pipe table
    pat = re.compile(r"^\*\*Table (\d)\. (.*?)\*\*(.*?)\n\n((?:\|.*\|\n?)+)", re.M)
    def table_sub(m):
        num, title, rest, tbl = m.group(1), m.group(2), m.group(3).strip(), m.group(4)
        if num == "2":
            return "```{=latex}\n" + heatmap_table(rows_json) + "\n```\n"
        lines = [l for l in tbl.strip().splitlines() if not re.match(r"^\|[-|: ]+\|$", l)]
        header, rows = split_row(lines[0]), [split_row(l) for l in lines[1:]]
        caption = title.rstrip(".") + ((" " if rest.startswith("(") else ". ") + rest if rest else "")
        tex = make_table(num, caption, header, rows, wide={"1": True, "3": True, "4": True, "5": False}[num])
        return "```{=latex}\n" + tex + "\n```\n"
    main_md = pat.sub(table_sub, main_md)
    # table footnote line under Table 3 becomes table note -> keep as text paragraph
    main_md = re.sub(r"(?<![\w{])Table (\d)\b", lambda m: f"Table{NBSP}\\ref{{tab-{m.group(1)}}}", main_md)

    # figures
    main_md = main_md.replace("## Mutually Untrusting Ad Hoc Coordination {#sec-3-1}",
                              "```{=latex}\n" + FIG_SETTING + "\n```\n\n## Mutually Untrusting Ad Hoc Coordination {#sec-3-1}")
    main_md = main_md.replace("A MUAC instance consists of a shared environment",
                              f"Fig.{NBSP}\\ref{{fig-setting}} illustrates the setting. A MUAC instance consists of a shared environment")
    main_md = main_md.replace("## Observations {#sec-8-3}",
                              "```{=latex}\n" + FIG_PILOT + "\n```\n\n## Observations {#sec-8-3}")
    main_md = main_md.replace("**O1 — With explicit acceptance markers",
                              f"Fig.{NBSP}\\ref{{fig-pilot}} summarizes agreement rates.\n\n**O1 — With explicit acceptance markers")

    # end matter
    end_md = end_md.replace("**Artifact availability.**", "# Artifact Availability {.unnumbered}\n\n")
    end_md = end_md.replace("**Use of AI tools.**", "\n\n# Use of AI Tools {.unnumbered}\n\n")
    end_md = end_md.replace("**Acknowledgments and funding.**", "\n\n# Acknowledgment {.unnumbered}\n\n")

    coding_md = ("# Full Coding Table {#app-coding}\n\n"
                 "Table\u00a0\\ref{tab-master} lists every coded work. Codes follow the rubric in Appendix\u00a0\\ref{app-rubric}.\n\n"
                 "```{=latex}\n" + master_longtable(rows_json) + "\n```\n")

    body_tex = pandoc_latex(main_md)
    end_tex = pandoc_latex(end_md)
    app_tex = pandoc_latex(appB + "\n\n" + appC + "\n\n" + coding_md)
    abs_tex = pandoc_latex(abstract_md)

    def post(t):
        t = re.sub(r"\\citep\{([^}]*)\}", r"\\cite{\1}", t)
        t = re.sub(r"\\citet\{([^}]*)\}",
                   lambda m: ", ".join(f"{narrative_name(entries, k.strip())}~\\cite{{{k.strip()}}}"
                                       for k in m.group(1).split(",")), t)
        reps = {"●": "\\full{}", "◐": "\\half{}", "○": "\\none{}", "Φ": "$\\Phi$", "→": "$\\rightarrow$",
                "≤": "$\\le$", "≥": "$\\ge$", "×": "$\\times$", "≈": "$\\approx$", "†": "\\textsuperscript{\\dag}",
                "10⁻¹⁰": "$10^{-10}$", "10⁻³": "$10^{-3}$", "10⁻⁴": "$10^{-4}$", "⊆": "$\\subseteq$", "≠": "$\\neq$",
                "✓": "\\checkmark{}", "−": "$-$", "∈": "$\\in$", "–": "--", "—": "---"}
        for a, b in reps.items():
            t = t.replace(a, b)
        t = t.replace("\\section{", "\\section{").replace("\\hypertarget", "\\relax\\hypertarget")
        return t

    body_tex, end_tex, app_tex, abs_tex = map(post, (body_tex, end_tex, app_tex, abs_tex))
    # end-matter headings should be unnumbered
    end_tex = re.sub(r"\\section\{([^}]*)\}\\label\{[^}]*\}", r"\\section*{\1}", end_tex)
    end_tex = end_tex.replace("\\section*{Acknowledgment}", "\\section*{Acknowledgment}")

    preamble = r"""\documentclass[conference]{IEEEtran}
\IEEEoverridecommandlockouts
\usepackage{amsmath}
\usepackage{newtxmath}
\usepackage[nointegrals]{wasysym}
\usepackage{booktabs,tabularx,longtable,array,multirow}
\usepackage[table]{xcolor}
\definecolor{cellblue}{RGB}{31,94,168}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,fit,backgrounds,calc}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usepackage{cite}
\usepackage[hidelinks]{hyperref}
\usepackage{url}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\newcommand{\full}{{\small\CIRCLE}}
\newcommand{\half}{{\small\LEFTcircle}}
\newcommand{\none}{{\small\Circle}}
\renewcommand{\arraystretch}{1.12}
\begin{document}
\title{SoK: Coordination Among Mutually Untrusting,\\Independently Developed AI Agents\\in Cloud Data Ecosystems}
\author{\IEEEauthorblockN{Sushil Khairnar}
\IEEEauthorblockA{Independent Researcher\\
Email: sushilkhairnar84@gmail.com}}
\maketitle
"""
    keywords = ("\\begin{IEEEkeywords}\nmulti-agent systems, large language model agents, ad hoc teamwork, "
                "zero-shot coordination, automated negotiation, delegation, access control, agent protocols, "
                "cloud data ecosystems, AI security\n\\end{IEEEkeywords}\n")
    doc = (preamble + "\\begin{abstract}\n" + abs_tex.strip() + "\n\\end{abstract}\n\n" + keywords + "\n"
           + body_tex + "\n" + end_tex + "\n\\bibliographystyle{IEEEtran}\n\\bibliography{refs_ieee}\n\n"
           + "\\appendices\n" + app_tex + "\n\\end{document}\n")
    (OUT / "main.tex").write_text(doc)
    (OUT / "refs_ieee.bib").write_text(ieee_bib(entries))
    leftovers = sorted({ch for ch in doc if ord(ch) > 127})
    print("non-ASCII chars remaining:", "".join(leftovers))


if __name__ == "__main__":
    main()
