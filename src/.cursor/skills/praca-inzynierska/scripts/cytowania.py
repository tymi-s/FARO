#!/usr/bin/env python3
"""Numeruje cytowania [@klucz] w rozdziałach pracy i sprawdza rejestr źródeł.

Użycie: python3 cytowania.py <katalog_pracy>
Oczekuje plików <katalog_pracy>/rozdzialy/*.md oraz <katalog_pracy>/literatura/zrodla.md.
Rozdziały czyta w kolejności nazw plików (00-wstep.md, 01-..., ...).
Kod wyjścia: 0 – bez błędów, 1 – są błędy, 2 – zła ścieżka lub brak plików.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

CITATION = re.compile(r"\[@([^\]]+)\]")
ENTRY_HEADER = re.compile(r"^##\s+([a-z0-9][a-z0-9_-]*)\s*$")
ENTRY_FIELD = re.compile(r"^-\s*([^:\s]+)\s*:\s*(.*)$")
VERIFIED = "zweryfikowane"
MIN_SOURCES = 10


@dataclass
class Source:
    key: str
    fields: dict[str, str] = field(default_factory=dict)


def text_lines(path: Path) -> list[tuple[int, str]]:
    """Zwraca linie spoza bloków kodu wraz z numerami."""
    result: list[tuple[int, str]] = []
    in_code = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            result.append((number, line))
    return result


def parse_registry(path: Path) -> tuple[dict[str, Source], list[str]]:
    sources: dict[str, Source] = {}
    duplicates: list[str] = []
    current: Source | None = None
    for _, line in text_lines(path):
        header = ENTRY_HEADER.match(line.strip())
        if header:
            key = header.group(1)
            if key in sources:
                duplicates.append(key)
            current = sources.setdefault(key, Source(key))
            continue
        if line.startswith("#"):
            current = None
            continue
        entry_field = ENTRY_FIELD.match(line.strip())
        if current is not None and entry_field:
            current.fields[entry_field.group(1).lower()] = entry_field.group(2).strip()
    return sources, duplicates


def citation_order(chapters: list[Path]) -> list[tuple[str, str]]:
    """Klucze w kolejności pierwszego cytowania, z miejscem wystąpienia."""
    order: list[tuple[str, str]] = []
    seen: set[str] = set()
    for chapter in chapters:
        for number, line in text_lines(chapter):
            for group in CITATION.findall(line):
                for raw in group.split(";"):
                    key = raw.strip().lstrip("@").strip()
                    if key and key not in seen:
                        seen.add(key)
                        order.append((key, f"{chapter.name}:{number}"))
    return order


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    root = Path(sys.argv[1])
    chapters = sorted((root / "rozdzialy").glob("*.md"))
    registry = root / "literatura" / "zrodla.md"
    if not chapters:
        print(f"Brak rozdziałów w {root / 'rozdzialy'}")
        return 2
    if not registry.exists():
        print(f"Brak rejestru źródeł: {registry}")
        return 2

    sources, duplicates = parse_registry(registry)
    order = citation_order(chapters)
    errors: list[str] = []
    warnings: list[str] = []

    print("LITERATURA (kolejność pierwszego cytowania)\n")
    for number, (key, where) in enumerate(order, start=1):
        source = sources.get(key)
        if source is None:
            errors.append(f"[{number}] {key} ({where}): brak wpisu w {registry.name}")
            print(f"[{number}] ??? {key}")
            continue
        status = source.fields.get("status", "").lower()
        description = source.fields.get("opis", "")
        if status != VERIFIED:
            errors.append(
                f"[{number}] {key} ({where}): status „{status or 'brak'}” – "
                f"w tekście wolno cytować tylko źródła „{VERIFIED}”"
            )
        if not description:
            errors.append(f"[{number}] {key}: brak pola „opis”")
        print(f"[{number}] {description or key}")

    print("\nKLUCZE → NUMERY\n")
    for number, (key, where) in enumerate(order, start=1):
        print(f"{key} → [{number}]  (pierwsze cytowanie: {where})")

    cited = {key for key, _ in order}
    for key in duplicates:
        warnings.append(f"{key}: klucz występuje w {registry.name} więcej niż raz")
    unused = sorted(set(sources) - cited)
    if unused:
        warnings.append("wpisy niecytowane (nie trafią do literatury): " + ", ".join(unused))
    if len(order) < MIN_SOURCES:
        warnings.append(f"cytowanych źródeł: {len(order)}; promotor wymaga co najmniej {MIN_SOURCES}")

    if errors:
        print("\nBŁĘDY")
        for message in errors:
            print(f"- {message}")
    if warnings:
        print("\nUWAGI")
        for message in warnings:
            print(f"- {message}")
    print(f"\nCytowane źródła: {len(order)}; błędy: {len(errors)}, uwagi: {len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
