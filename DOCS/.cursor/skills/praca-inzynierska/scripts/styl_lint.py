#!/usr/bin/env python3
"""Heurystyczna kontrola stylu i formatowania szkiców rozdziałów pracy (Markdown).

Użycie: python3 styl_lint.py <plik.md | katalog> [...]
Poziomy: BŁĄD – narusza zasadę promotora lub wydziału; UWAGA – prawdopodobny problem;
INFO – do oceny przez piszącego. Kod wyjścia 1, gdy wystąpił BŁĄD.
To heurystyka: każde zgłoszenie trzeba ocenić, a nie poprawiać mechanicznie.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

ERROR, WARN, INFO = "BŁĄD", "UWAGA", "INFO"
IC = re.IGNORECASE

PHRASES = [
    (re.compile(pattern, flags), level, message)
    for pattern, flags, level, message in [
        (r"\bw dzisiejszych czasach\b|\bw dobie\b|\bwspółczesny świat\b", IC, WARN,
         "ogólnikowe otwarcie – zacznij od konkretnego problemu albo faktu"),
        (r"\bna dzień dzisiejszy\b", IC, ERROR, "„masło maślane” – pisz „obecnie”"),
        (r"\bwspomnian\w*\s+wcześniej\b|\bwcześniej\s+wspomnian\w*", IC, ERROR,
         "„masło maślane” – wystarczy „wspomniano”"),
        (r"\bnapotka\w*\s+na\b", IC, ERROR, "„napotkać trudności”, bez „na”"),
        (r"\b(?:warto|należy)\s+(?:zauważyć|podkreślić|wspomnieć|zaznaczyć)\b|\bco istotne\b"
         r"|\bnie bez znaczenia\b|\bmając na uwadze\b", IC, WARN,
         "pusty łącznik – usuń, treść zdania wystarczy"),
        (r"\b(?:kluczow|innowacyjn|kompleksow|holistyczn|fundamentaln)\w*|\bniezwykle\b"
         r"|\bszeroko pojęt\w*", IC, WARN, "pusty wzmacniacz – zastąp konkretem albo usuń"),
        (r"\b(?:zaawansowan|nowoczesn)\w*", IC, INFO, "czy przymiotnik coś mówi? podaj konkret zamiast oceny"),
        (r"\bposiad\w*", IC, WARN, "„mieć”, nie „posiadać”"),
        (r"\bilo(?:ść|ści|ścią)\b", IC, INFO, "„liczba” dla rzeczy policzalnych, „ilość” dla niepoliczalnych"),
        (r"\bściąg\w*", IC, WARN, "żargon – pisz „pobrać”"),
        (r"\bdedykowan\w*", IC, WARN, "kalka z angielskiego – „przeznaczony”"),
        (r"\badresow\w*\s+(?:problem|wyzwani|potrzeb)\w*", IC, WARN, "kalka – „rozwiązywać problem”"),
        (r"\bbazuj\w*\s+na\b", IC, INFO, "kalka – „opierać się na”"),
        (r"\bpotencjalnie\b|\bw pewnym stopniu\b", IC, INFO, "asekuracja – podaj przyczynę niepewności albo usuń"),
        (r"\bpodsumowując\b", IC, INFO, "podsumowanie tylko raz, na końcu rozdziału"),
        (r"\b(?:powyżej|poniżej|powyższ\w*|poniższ\w*)\b", IC, INFO,
         "jeśli to odwołanie do rysunku, tabeli albo fragmentu tekstu – podaj numer"),
        (r"\bzostan(?:ie|ą)\b|\bbędzie\b|\bbędą\b", IC, WARN, "czas przyszły? pisz w teraźniejszym albo przeszłym"),
        (r"\bnasz(?:a|e|ego|ej|ym|ych|emu|ą)?\b", IC, WARN, "forma bezosobowa zamiast „nasz”"),
        (r"\b(?:projekt|prac)\w*\s+polega\w*", IC, INFO, "projekt „dotyczy”, a nie „polega”"),
        (r"wikipedi", IC, ERROR, "Wikipedia nie może być źródłem"),
        (r"\bwi\s?fi\b", IC, WARN, "pisownia: „Wi-Fi”"),
        (r"\b(?:heat\s?map|hitmap)\w*", IC, WARN, "termin: „mapa pokrycia”"),
        (r"\b(?:LiDAR|LIDAR)\b", 0, INFO, "termin: „lidar” (nazwę produktu RPLIDAR zostaw)"),
        (r"!", 0, WARN, "wykrzyknik w tekście pracy"),
    ]
]

STARTERS = {"aby", "ponieważ", "więc", "ale", "żeby", "i", "a"}
FIRST_WORD = re.compile(r"^[„\"'(\[]*([^\W\d_]+)(?!\w)")
SENTENCE_END = re.compile(r"(?<=[.!?…])\s+(?=[„\"(\[]?[A-ZĄĆĘŁŃÓŚŹŻ])")
UNIT = re.compile(r"\b\d+(?:[.,]\d+)?(?:mm|cm|km|ms|kHz|MHz|GHz|Hz|mV|mA|dBm|dB|kg|°C|m|s|V|A|W|g)\b")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
CAPTION = re.compile(r"^(Rys\.|Tabela|Fragment kodu)\s+(\d+)\.(\d+)\.\s+(\S.*)$")
CAPTION_LIKE = re.compile(r"^(?:rys\.?|rysunek|tab\.?|tabela|fragment kodu|listing)\s*\d", IC)
IMAGE = re.compile(r"^!\[[^\]]*\]\([^)]*\)$")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)]|[a-z]\))\s+(.*)$")
EQUATION_NUMBER = re.compile(r"\(\d+\.\d+\)")
PLACEHOLDER = re.compile(r"\[(?:DO UZUPEŁNIENIA|DO WERYFIKACJI|RYS:)")
CITE_AFTER_DOT = re.compile(r"[.!?]\s*\[@")
NUMERIC_CITE = re.compile(r"\[\d+(?:\s*[,–-]\s*\d+)*\]")
INLINE_CODE = re.compile(r"`[^`]*`")
GENERIC_TITLE = re.compile(r"\bczęść\s+(?:teoretyczna|praktyczna)\b", IC)
REF_WORD = {"Rys.": r"(?:rys\.|rysun\w*)", "Tabela": r"(?:tab\.|tabel\w*)", "Fragment kodu": r"fragment\w*\s+kodu"}
TEXT_KINDS = {"prose", "list", "heading", "caption", "table", "source"}
LONG_SENTENCE_WORDS = 35
LONG_PARAGRAPH_WORDS = 200


@dataclass
class Finding:
    line: int
    level: str
    message: str
    excerpt: str = ""


def classify(lines: list[str]) -> list[str]:
    kinds: list[str] = []
    in_code = in_math = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            kinds.append("fence")
            in_code = not in_code
            continue
        if in_code:
            kinds.append("code")
            continue
        dollars = stripped.count("$$")
        if in_math or dollars:
            kinds.append("math")
            if dollars % 2:
                in_math = not in_math
            continue
        if not stripped:
            kinds.append("blank")
        elif HEADING.match(stripped):
            kinds.append("heading")
        elif stripped.startswith("|"):
            kinds.append("table")
        elif IMAGE.match(stripped):
            kinds.append("image")
        elif CAPTION.match(stripped):
            kinds.append("caption")
        elif stripped.startswith("Źródło:"):
            kinds.append("source")
        elif stripped.startswith("<!--"):
            kinds.append("comment")
        elif LIST_ITEM.match(line):
            kinds.append("list")
        else:
            kinds.append("prose")
    return kinds


def next_nonblank(kinds: list[str], index: int) -> int | None:
    return next((i for i in range(index + 1, len(kinds)) if kinds[i] != "blank"), None)


def previous_nonblank(kinds: list[str], index: int) -> int | None:
    return next((i for i in range(index - 1, -1, -1) if kinds[i] != "blank"), None)


def check_lines(lines: list[str], kinds: list[str], findings: list[Finding]) -> None:
    for number, (line, kind) in enumerate(zip(lines, kinds), start=1):
        if kind not in TEXT_KINDS:
            continue
        text = INLINE_CODE.sub("", line)
        for pattern, level, message in PHRASES:
            findings.extend(Finding(number, level, message, m.group(0)) for m in pattern.finditer(text))
        findings.extend(
            Finding(number, WARN, "między liczbą a jednostką wstaw spację", m.group(0)) for m in UNIT.finditer(text)
        )
        if kind in ("prose", "list", "caption"):
            if CITE_AFTER_DOT.search(text):
                findings.append(Finding(number, WARN, "cytowanie stawiaj przed kropką: „… [@klucz].”"))
            findings.extend(
                Finding(number, INFO, "w szkicu cytuj kluczem [@klucz]; numery nadaje cytowania.py", m.group(0))
                for m in NUMERIC_CITE.finditer(text)
            )
        stripped = line.strip()
        if kind == "prose" and CAPTION_LIKE.match(stripped) and not stripped.endswith(".") and len(stripped.split()) < 20:
            findings.append(Finding(
                number, WARN,
                "podpis w złym formacie; wzór: „Rys. 4.1. Opis”, „Tabela 3.1. Opis”, „Fragment kodu 5.1. Opis”",
                stripped[:60],
            ))


def check_headings(lines: list[str], kinds: list[str], findings: list[Finding]) -> None:
    headings = [
        (index, len(match.group(1)), match.group(2))
        for index, line in enumerate(lines)
        if kinds[index] == "heading" and (match := HEADING.match(line.strip()))
    ]
    for position, (index, level, title) in enumerate(headings):
        number = index + 1
        if level > 3:
            findings.append(Finding(number, ERROR, "najwyżej trzy poziomy nagłówków", title))
        if title.endswith("."):
            findings.append(Finding(number, ERROR, "bez kropki na końcu tytułu", title))
        if GENERIC_TITLE.search(title):
            findings.append(Finding(number, WARN, "tytuł zbyt ogólny – nazwij treść rozdziału", title))
        following = next_nonblank(kinds, index)
        if following is not None and kinds[following] == "heading":
            if len(HEADING.match(lines[following].strip()).group(1)) > level:
                findings.append(Finding(number, ERROR, "pod tytułem od razu podrozdział – rozdział zaczyna się tekstem", title))
        if level < 3:
            children = 0
            for _, other_level, _ in headings[position + 1:]:
                if other_level <= level:
                    break
                children += other_level == level + 1
            if children == 1:
                findings.append(Finding(number, ERROR, "tylko jeden podrozdział – dodaj drugi albo usuń podział", title))


def check_captions(lines: list[str], kinds: list[str], findings: list[Finding]) -> None:
    last: dict[str, tuple[int, int]] = {}
    for index, line in enumerate(lines):
        if kinds[index] != "caption":
            continue
        number = index + 1
        label, chapter, item, text = CAPTION.match(line.strip()).groups()
        chapter_no, item_no = int(chapter), int(item)
        cited = "[@" in text
        if text.rstrip().endswith("."):
            findings.append(Finding(number, ERROR, "bez kropki na końcu podpisu", line.strip()))
        previous = previous_nonblank(kinds, index)
        following = next_nonblank(kinds, index)
        if label == "Rys.":
            if previous is None or kinds[previous] != "image":
                findings.append(Finding(number, WARN, "podpis rysunku stoi pod rysunkiem – nad podpisem brak obrazu"))
            if not cited and (following is None or kinds[following] != "source"):
                findings.append(Finding(number, WARN, "pod rysunkiem brak linii „Źródło: …”"))
        elif label == "Tabela":
            if following is None or kinds[following] != "table":
                findings.append(Finding(number, WARN, "podpis tabeli stoi nad tabelą – pod podpisem brak tabeli"))
            else:
                end = following
                while end + 1 < len(kinds) and kinds[end + 1] == "table":
                    end += 1
                after = next_nonblank(kinds, end)
                if not cited and (after is None or kinds[after] != "source"):
                    findings.append(Finding(number, WARN, "pod tabelą brak linii „Źródło: …”"))
        elif previous is None or kinds[previous] != "fence":
            findings.append(Finding(number, WARN, "podpis fragmentu kodu stoi pod blokiem kodu"))

        reference = re.compile(
            rf"\b{REF_WORD[label]}\s*(?:\d+\.\d+\.?\s*(?:,|i|oraz|–|-)\s*)*{chapter_no}\.{item_no}(?!\d)", IC
        )
        before = " ".join(text for text, kind in zip(lines[:index], kinds[:index]) if kind in ("prose", "list"))
        if not reference.search(before):
            findings.append(Finding(number, WARN, f"brak odwołania w tekście przed obiektem {label} {chapter_no}.{item_no}"))

        expected = (last[label][0], last[label][1] + 1) if label in last else (chapter_no, 1)
        if (chapter_no, item_no) != expected:
            findings.append(Finding(number, WARN, f"numeracja: oczekiwano {label} {expected[0]}.{expected[1]}"))
        last[label] = (chapter_no, item_no)


def check_equations(lines: list[str], kinds: list[str], findings: list[Finding]) -> None:
    for index, kind in enumerate(kinds):
        if kind != "math" or (index + 1 < len(kinds) and kinds[index + 1] == "math"):
            continue
        following = next_nonblank(kinds, index)
        numbered = EQUATION_NUMBER.search(lines[index]) or (
            following is not None and EQUATION_NUMBER.match(lines[following].strip())
        )
        if not numbered:
            findings.append(Finding(index + 1, WARN, "wzór bez numeru (rozdział.numer), np. (3.1)"))


def check_lists(lines: list[str], kinds: list[str], findings: list[Finding]) -> None:
    index = 0
    while index < len(kinds):
        if kinds[index] != "list":
            index += 1
            continue
        start = index
        while index < len(kinds) and kinds[index] == "list":
            index += 1
        items = [(i, LIST_ITEM.match(lines[i]).group(1).strip()) for i in range(start, index)]
        if len(items) < 2 or not all(text[:1].islower() for _, text in items):
            continue
        for position, (i, text) in enumerate(items):
            if position < len(items) - 1 and not text.endswith(","):
                findings.append(Finding(i + 1, WARN, "pozycja wypunktowania kończy się przecinkiem", text[-40:]))
            if position == len(items) - 1 and not text.endswith("."):
                findings.append(Finding(i + 1, WARN, "ostatnia pozycja wypunktowania kończy się kropką", text[-40:]))


def check_paragraphs(lines: list[str], kinds: list[str], findings: list[Finding]) -> None:
    blocks: list[list[int]] = []
    current: list[int] = []
    for index, kind in enumerate(kinds):
        if kind == "prose":
            current.append(index)
            continue
        if current:
            blocks.append(current)
            current = []
        if kind == "list":
            blocks.append([index])
    if current:
        blocks.append(current)

    for block in blocks:
        parts = [LIST_ITEM.match(lines[i]).group(1) if kinds[i] == "list" else lines[i] for i in block]
        paragraph = INLINE_CODE.sub("", " ".join(part.strip() for part in parts))
        words = len(paragraph.split())
        if kinds[block[0]] == "prose" and words > LONG_PARAGRAPH_WORDS:
            findings.append(Finding(block[0] + 1, INFO, f"akapit ma {words} słów – czy to jedna myśl?"))
        for sentence in (s.strip() for s in SENTENCE_END.split(paragraph)):
            if not sentence:
                continue
            probe = sentence[:20]
            line_no = next((i + 1 for i in block if probe in lines[i]), block[0] + 1)
            first = FIRST_WORD.match(sentence)
            if first and first.group(1)[0].isupper() and first.group(1).lower() in STARTERS:
                findings.append(Finding(line_no, ERROR, f"zdanie zaczyna się od „{first.group(1)}”", sentence[:60]))
            count = len(sentence.split())
            if count > LONG_SENTENCE_WORDS:
                findings.append(Finding(line_no, INFO, f"zdanie ma {count} słów – rozważ podział", sentence[:60]))


def lint(path: Path) -> list[Finding]:
    lines = path.read_text(encoding="utf-8").splitlines()
    kinds = classify(lines)
    findings: list[Finding] = []
    for check in (check_lines, check_headings, check_captions, check_equations, check_lists, check_paragraphs):
        check(lines, kinds, findings)
    placeholders = sum(
        len(PLACEHOLDER.findall(line)) for line, kind in zip(lines, kinds) if kind not in ("code", "fence")
    )
    if placeholders:
        findings.append(Finding(0, INFO, f"miejsc do uzupełnienia lub weryfikacji: {placeholders}"))
    return sorted(findings, key=lambda finding: finding.line)


def collect(arguments: list[str]) -> list[Path]:
    files: list[Path] = []
    for argument in arguments:
        path = Path(argument)
        if path.is_dir():
            files.extend(sorted(path.glob("*.md")))
        elif path.is_file():
            files.append(path)
        else:
            raise FileNotFoundError(argument)
    return files


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    try:
        files = collect(sys.argv[1:])
    except FileNotFoundError as missing:
        print(f"Nie ma takiego pliku ani katalogu: {missing}")
        return 2
    totals = {ERROR: 0, WARN: 0, INFO: 0}
    for path in files:
        for finding in lint(path):
            totals[finding.level] += 1
            location = f"{path}:{finding.line}" if finding.line else f"{path}"
            excerpt = f" – „{finding.excerpt}”" if finding.excerpt else ""
            print(f"{location}: {finding.level}: {finding.message}{excerpt}")
    print(f"\nPliki: {len(files)}; błędy: {totals[ERROR]}, uwagi: {totals[WARN]}, informacje: {totals[INFO]}")
    return 1 if totals[ERROR] else 0


if __name__ == "__main__":
    sys.exit(main())
