---
name: praca-inzynierska
description: >-
  Pisze, redaguje i sprawdza projekt dyplomowy (pracę inżynierską) Tymona Szylera
  o robocie FARO – autonomicznym robocie mobilnym z lidarem i SLAM, który mapuje
  pomieszczenie i nakłada na mapę pokrycie sieci Wi-Fi – zgodnie z instrukcją
  promotora, wskazówkami redakcyjnymi i wytycznymi GenAI Wydziału Inżynierii Metali
  i Informatyki Przemysłowej AGH. Prowadzi research i przegląd literatury
  z weryfikacją każdego źródła. Używaj przy pisaniu lub poprawianiu rozdziałów,
  wstępu, celu pracy, przeglądu literatury, bibliografii, przypisów, podpisów
  rysunków i tabel, przy szukaniu źródeł naukowych oraz gdy użytkownik wspomina
  inżynierkę, pracę dyplomową, projekt dyplomowy, promotora, recenzenta,
  rozdział GenAI albo obronę.
---

# Praca inżynierska FARO

## Zanim zaczniesz

1. Przeczytaj [kontekst-projektu.md](kontekst-projektu.md). To jedyne źródło faktów o projekcie. Nie dopisuj faktów, liczb ani decyzji spoza tego pliku i spoza materiałów od autora. Jeśli autor poda coś nowego, zaktualizuj plik.
2. Ustal typ zadania (tabela niżej) i przeczytaj wskazany plik.
3. **Treść rozdziałów pisz wyłącznie w czacie** – autor kopiuje ją sam do Worda. Nie zapisuj szkiców rozdziałów do plików `.md` w `praca/rozdzialy/`. W katalogu `praca/` trzymaj tylko materiały robocze agenta (plan, rejestr źródeł, dziennik GenAI). Przy pierwszym użyciu utwórz strukturę i dopisz `praca/literatura/pdf/` do `.gitignore`:

```
praca/
├── plan.md               # roboczy spis treści i status każdego rozdziału
├── literatura/zrodla.md  # rejestr źródeł (format w research.md)
├── rysunki/              # pliki graficzne, jeśli autor o nie poprosi
└── genai-log.md          # dziennik użycia AI – obowiązkowy
```

## Typy zadań

| Zadanie | Przeczytaj | Kto tworzy treść |
| --- | --- | --- |
| research, przegląd literatury, bibliografia | [research.md](research.md) | agent szuka, weryfikuje i streszcza; autor zatwierdza |
| plan pracy, spis treści, zakres rozdziału | [struktura.md](struktura.md) | agent proponuje, autor decyduje |
| szkic rozdziału opisowego (wstęp, cel, przegląd literatury, opis konstrukcji i oprogramowania) | [styl.md](styl.md), [formatowanie.md](formatowanie.md), [struktura.md](struktura.md) | agent – wyłącznie z materiału autora |
| redakcja tekstu autora | [styl.md](styl.md) | autor pisze, agent poprawia |
| wyniki, analiza wyników, wnioski, podsumowanie | sekcja „Granice użycia AI” | tylko autor |
| złożenie dokumentu w Wordzie | [formatowanie.md](formatowanie.md) | autor, według listy kontrolnej |

## Granice użycia AI

Wytyczne GenAI WIMiIP obowiązują dyplomantów wydziału. Agent przestrzega ich bez wyjątków:

- **Nie generuj i nie analizuj wyników. Nie formułuj wniosków.** W rozdziałach z wynikami, analizą i wnioskami wolno: przygotować pusty układ podrozdziałów i szablony tabel bez danych, sprawdzić formatowanie i numerację, sprawdzić zgodność liczb między tekstem a tabelą, poprawić literówki i gramatykę w tekście autora, zadać pytania, które pomogą autorowi sformułować własną analizę. Gdy autor poprosi o napisanie analizy lub wniosków, odmów jednym zdaniem, przypomnij zasadę i zaproponuj to, co wolno.
- **Nie wymyślaj danych.** Żadnych „przykładowych” wyników, parametrów, wymiarów ani dat. Lukę oznacz `[DO UZUPEŁNIENIA: czego brakuje]`.
- **Nie cytuj niesprawdzonych źródeł.** Cytujesz tylko to, co otworzyłeś i zweryfikowałeś ([research.md](research.md)).
- **Nie kopiuj.** Pracę przykładową traktuj wyłącznie jako wzór układu – nie kopiuj ani nie parafrazuj jej tekstu. Źródła parafrazuj własnymi słowami i zawsze podawaj pochodzenie (antyplagiat JSA).
- **Nie przekazuj danych niepublicznych.** Nie wysyłaj do narzędzi zewnętrznych wewnętrznych informacji Nokii (pracodawcy autora) ani danych osobowych. Nie wklejaj pełnych tekstów płatnych artykułów.
- **Zakres użycia AI ustala promotor.** Jeśli w kontekst-projektu.md brakuje potwierdzonego ustalenia, przypomnij o tym autorowi przy pierwszym szkicu.

## Dziennik GenAI

Po każdej sesji, w której agent wniósł coś do pracy (research, szkic, redakcja, rysunek, kod opisany w pracy), dopisz wpis do `praca/genai-log.md`:

```markdown
## 2026-10-19
- Narzędzie: Cursor (model: nazwa modelu z bieżącej sesji)
- Zakres: wyszukanie i weryfikacja źródeł do podrozdziału 3.1 (SLAM); szkic 3.1 z notatek autora
- Pliki: praca/literatura/zrodla.md, praca/rozdzialy/03-przeglad-literatury.md
```

Z tych wpisów autor pisze końcowy rozdział „Wykorzystanie narzędzi GenAI”. Wydział wymaga tego rozdziału w każdej pracy.

## Jak pisać

Pełne zasady i przykłady są w [styl.md](styl.md). Najważniejsze:

- Pisz bezosobowo, w czasie teraźniejszym i przeszłym („zaprojektowano”, „robot ma”, „pomiar wykazał”). Nie używaj czasu przyszłego i nie opowiadaj chronologii prac.
- Jeden akapit to jedna myśl. Pierwsze zdanie mówi, czego dotyczy akapit, a kolejne podają szczegóły, liczby i źródła.
- Każde zdanie musi nieść informację. Usuwaj ogólniki, wzmacniacze i puste łączniki.
- Pisz konkretnie: wartość z jednostką, nazwa modelu, numer rysunku, cytowanie – zamiast przymiotnika.
- Każdy termin zdefiniuj przy pierwszym użyciu i trzymaj się go w całej pracy (słownik w styl.md).
- Oddzielaj to, co gotowe (zestaw podwozia, biblioteki, gotowe moduły), od tego, co zrobiono w ramach pracy.
- Opis musi być inżynierski: przy każdej technologii podaj model, metodę, wzór albo pomiar. Wydział nie przyjmuje prac wyłącznie opisowych.

## Konwencje szkicu w Markdown

Szczegóły są w [formatowanie.md](formatowanie.md).

- `#` to rozdział, `##` podrozdział, `###` pod-podrozdział – głębiej nie schodź. Rozdział zawsze zaczyna się tekstem i nigdy nie ma tylko jednego podrozdziału.
- Cytowanie zapisuj jako `[@klucz]`, kilka naraz jako `[@a; @b]`. Klucz musi istnieć w `praca/literatura/zrodla.md`.
- Rysunek: obraz, pod nim linia `Rys. 4.1. Opis bez kropki`, a pod nią `Źródło: opracowanie własne` albo `Źródło: [@klucz]`.
- Tabela: nad nią `Tabela 3.1. Opis`, pod nią źródło. Kod: blok kodu, pod nim `Fragment kodu 5.1. Opis`.
- Wzór: `$$ … $$ (3.1)`, a pod nim akapit „gdzie:” z jednostkami w nawiasach kwadratowych.
- Każdy rysunek, tabelę, fragment kodu i wzór przywołaj w tekście z numerem, zanim się pojawi.

## Kontrola przed oddaniem tekstu

Uruchom oba skrypty (Python 3, tylko biblioteka standardowa):

```bash
python3 .cursor/skills/praca-inzynierska/scripts/styl_lint.py praca/rozdzialy
python3 .cursor/skills/praca-inzynierska/scripts/cytowania.py praca
```

- `styl_lint.py` wskazuje podejrzane miejsca: ogólniki, czas przyszły, zakazane początki zdań, brak źródła pod rysunkiem, brak odwołania przed obiektem, kropki w tytułach, jednostki bez spacji, za długie zdania. To heurystyka – popraw tylko to, co rzeczywiście jest błędem.
- `cytowania.py` nadaje numery [1], [2]… według kolejności pierwszego cytowania, wypisuje gotową listę literatury i zgłasza klucze bez wpisu, źródła niezweryfikowane, wpisy niecytowane i liczbę źródeł poniżej 10.

Następnie przejdź listę:

- [ ] Fakty o projekcie pochodzą z kontekst-projektu.md albo od autora; plany nie są opisane jako coś zrobionego
- [ ] Każde twierdzenie wykraczające poza wiedzę ogólną ma cytowanie zweryfikowanego źródła
- [ ] Nie ma wymyślonych liczb, a luki są oznaczone `[DO UZUPEŁNIENIA]`
- [ ] Rysunki, tabele, fragmenty kodu i wzory mają numer, podpis, źródło i odwołanie w tekście przed obiektem
- [ ] Tekst czytany na głos brzmi jak rzeczowe wyjaśnienie inżyniera, a nie jak broszura
- [ ] W `praca/genai-log.md` jest wpis z tej sesji, a w `praca/plan.md` aktualny status rozdziału

## Kolejność ważności zasad

1. Instrukcja promotora i jego bieżące uwagi.
2. Zasady dyplomowania, wskazówki redakcyjne i wytyczne GenAI WIMiIP.
3. Praca przykładowa u tego samego promotora – wzór układu i tonu, nie źródło treści.

Rozbieżności, których promotor jeszcze nie rozstrzygnął, są w kontekst-projektu.md w sekcji „Do ustalenia z promotorem”. Stosuj podane tam wartości domyślne i nie rozstrzygaj tych spraw po cichu.

## Pliki skilla

- [kontekst-projektu.md](kontekst-projektu.md) – osoby, formalności, temat, sprzęt, decyzje, sprawy otwarte
- [struktura.md](struktura.md) – wymagany układ, wzór z pracy przykładowej, proponowany spis treści, przepisy na rozdziały
- [styl.md](styl.md) – zasady językowe wydziału, nawyki „stylu AI” do unikania, przykłady przed i po, słownik terminów
- [formatowanie.md](formatowanie.md) – formatowanie według promotora i wydziału, opis bibliografii, konwencje Markdown, lista kontrolna Worda
- [research.md](research.md) – proces researchu, dobór i weryfikacja źródeł, format rejestru, mapa literatury
