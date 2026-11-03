# Formatowanie

Źródła zasad: instrukcja promotora („Praca dyplomowa – instrukcja”), wskazówki redakcyjne WIMiIP oraz formatowanie odczytane z pliku pracy przykładowej.

## Strona i tekst

| Element | Wartość |
| --- | --- |
| Papier, marginesy | A4, 2 cm (wydział; tak samo w pracy przykładowej) |
| Tekst podstawowy | Times New Roman 12 pt, interlinia 1,5, wyjustowany, wcięcie pierwszego wiersza 1 cm |
| Nagłówki | style Nagłówek 1/2/3 z numeracją wielopoziomową, najwyżej trzy poziomy; w pracy przykładowej Nagłówek 1 to TNR 14 pt pogrubiony, Nagłówek 2 to TNR 12 pt pogrubiony |
| Podpisy rysunków, tabel i kodu | TNR 10 pt, interlinia pojedyncza |
| Lista przypisów końcowych (literatura) | 10 pt, interlinia pojedyncza |
| Kod | czcionka o stałej szerokości (Consolas albo Courier New) 10 pt, w ramce, z kolorowaniem składni |

Krótkie akapity i wypunktowania można wyrównać do lewej, jeśli justowanie nadmiernie rozciągnęłoby odstępy między słowami.

## Rozdziały

- Każdy rozdział główny zaczyna się od nowej strony.
- Rozdział zawsze zaczyna się tekstem, a nie od razu tytułem podrozdziału.
- Rozdział ma co najmniej dwa podrozdziały albo nie ma ich wcale – nigdy jeden.
- Tytuły muszą być konkretne („Projekt i budowa platformy mobilnej”), nie ogólne („Część praktyczna”). Na końcu tytułu nie stawia się kropki.
- Bez numeru: spis treści, literatura, załączniki, wykazy. Numeracja wstępu – patrz „Do ustalenia z promotorem” w kontekst-projektu.md.
- Do rozdziału odwołuj się numerem: „W rozdziale 5.1 przedstawiono…”.

## Wypunktowania

- W całej pracy ten sam znak wypunktowania (punkt albo myślnik), bez ozdobnych symboli.
- Pozycja, która nie jest pełnym zdaniem, zaczyna się małą literą i kończy przecinkiem; ostatnia kończy się kropką.

Przykład:

- mapowanie pomieszczenia lidarem,
- pomiar poziomu sygnału w punktach pomiarowych,
- wyznaczenie mapy pokrycia.

## Wzory

- Numer ma postać „rozdział.kolejny numer” w nawiasie okrągłym, wyrównany do prawej: (3.1).
- Pod wzorem akapit zaczynający się od „gdzie:” z definicją każdego symbolu i jednostką w nawiasie kwadratowym, np. „gdzie: r – promień koła [m], ω – prędkość kątowa koła [rad/s]”.
- W tekście odwołuj się numerem w nawiasie: „ze wzoru (3.1)”. Oznaczenia muszą być spójne w całej pracy.

## Rysunki, tabele i fragmenty kodu

| Obiekt | Etykieta | Położenie podpisu | Przykład |
| --- | --- | --- | --- |
| rysunek, wykres, schemat | Rys. | pod obiektem, wyśrodkowany | Rys. 4.1. Schemat zasilania robota |
| tabela | Tabela (pełne słowo) | nad tabelą, do lewej | Tabela 3.1. Porównanie metod SLAM z lidarem 2D |
| kod | Fragment kodu | pod kodem | Fragment kodu 5.1. Wyznaczanie prędkości kół Mecanum |

- Format podpisu: etykieta, spacja, numer rozdziału, kropka, numer obiektu, kropka, spacja, opis bez kropki na końcu. Numeracja biegnie w obrębie rozdziału (zasada promotora), osobno dla rysunków, tabel i fragmentów kodu.
- Pod rysunkiem i pod tabelą podaj źródło: `Źródło: opracowanie własne`, `Źródło: [3]` albo `Źródło: opracowanie własne na podstawie [3]`. Przy zapożyczonym rysunku lub zapożyczonych danych cytowanie jest obowiązkowe; może też stać w podpisie („Rys. 3.1. Schemat … [3]”).
- Każdy obiekt przywołaj w tekście przed jego pojawieniem się, podając numer: „Na rysunku 4.1 przedstawiono…”, „(tab. 3.1)”.
- Zostaw jeden pusty wiersz po podpisie rysunku i fragmentu kodu oraz przed tabelą – albo użyj opcji akapitu „Razem z następnym”.
- Kod wstawiaj jako tekst, nie jako zrzut ekranu, z pokolorowaną składnią. Skopiowanie kodu z edytora (VS Code lub Cursor) do Worda zachowuje kolory. Pokazuj krótkie fragmenty – tylko to, co omawia tekst.

## Jednostki i liczby

- Wartość, spacja, jednostka: 0,15 m; 5,5 Hz; −62 dBm; 7,4 V; 25 °C. Wyjątek: stopień kątowy zapisuje się bez spacji (90°).
- Używaj jednostek SI w ich normowym zapisie. W objaśnieniach wzorów i nagłówkach tabel jednostka stoi w nawiasie kwadratowym.
- W całej pracy obowiązuje jeden separator dziesiętny (patrz „Do ustalenia z promotorem”).

## Cytowania i literatura

- W tekście numer w nawiasie kwadratowym stoi przed kropką: „…położenie robota [4].”
- W Wordzie cytowanie to przypis końcowy (Odwołania → Wstaw przypis końcowy) z numeracją 1, 2, 3. Znak przypisu ujmij ręcznie w nawiasy kwadratowe – w tekście i na liście. Numery idą w kolejności pierwszego cytowania.
- Ponowne odwołanie do tej samej pozycji wstaw jako odsyłacz (Odwołania → Odsyłacz → typ „Przypis końcowy” → numer przypisu), a nie jako nowy przypis.
- Kilka źródeł naraz zapisuj jako [3, 5].
- Lista przypisów końcowych stoi na końcu dokumentu pod nagłówkiem „Literatura”.
- Promotor wymaga co najmniej 10 pozycji. Każda pozycja musi być przywołana w tekście. Wikipedia jest zakazana. Nie zostawiaj samego adresu URL: zawsze podaj tytuł, autora (jeśli jest) i datę dostępu; adres wpisz bez hiperłącza.
- Nie stosuj przypisów dolnych – skróty i pojęcia objaśniaj w tekście.

### Opis pozycji

Format wzorowany na przykładach promotora, z dodanym DOI, jeśli istnieje. W całej pracy jeden format dla każdego typu pozycji.

- **Książka:** `A. Nazwisko, B. Nazwisko, „Tytuł”, Wydawnictwo, Miasto Rok`
  - `A. Milenin, „Podstawy metody elementów skończonych”, Wydawnictwa AGH, Kraków 2010`
- **Artykuł w czasopiśmie:** `Nazwisko, A., Nazwisko, B., Rok. Tytuł. Czasopismo Tom(Numer), strony. DOI: …`
  - `Grisetti, G., Stachniss, C., Burgard, W., 2007. Improved Techniques for Grid Mapping With Rao-Blackwellized Particle Filters. IEEE Transactions on Robotics 23(1), 34–46. DOI: 10.1109/TRO.2006.889486`
- **Referat konferencyjny:** `Nazwisko, A., …, Rok. Tytuł. Nazwa konferencji, strony. DOI: …`
  - `Hess, W., Kohler, D., Rapp, H., Andor, D., 2016. Real-time loop closure in 2D LIDAR SLAM. 2016 IEEE International Conference on Robotics and Automation (ICRA), 1271–1278. DOI: 10.1109/ICRA.2016.7487258`
- **Dokumentacja, karta katalogowa, strona internetowa:** `Tytuł dokumentu, Autor lub organizacja, adres URL (dostęp dd.mm.rrrr)`
  - `RPLIDAR-A1 Laser Range Scanner Parameters, SLAMTEC, https://www.slamtec.com/en/lidar/a1spec (dostęp 19.10.2026)`

## Konwencje szkicu w Markdown

| W szkicu | W Wordzie |
| --- | --- |
| `# Tytuł`, `## …`, `### …` | Nagłówek 1, 2, 3 |
| `[@klucz]`, `[@a; @b]` | przypis końcowy [n]; przy ponownym cytowaniu odsyłacz; kilka źródeł: [3, 5] |
| obraz, linia `Rys. X.Y. Opis`, linia `Źródło: …` | rysunek, podpis (Wstaw podpis, etykieta „Rys.”), źródło |
| linia `Tabela X.Y. Opis`, tabela Markdown, linia `Źródło: …` | tabela z podpisem nad nią |
| blok kodu, linia `Fragment kodu X.Y. Opis` | kod w ramce, pokolorowany, z podpisem pod spodem |
| `$$ wzór $$ (X.Y)`, akapit „gdzie: …” | edytor równań, numer wyrównany do prawej |
| `[DO UZUPEŁNIENIA: …]`, `[DO WERYFIKACJI: …]`, `[RYS: opis potrzebnego rysunku]` | nie mogą zostać w wersji końcowej |

Rysunki zapisuj jako `praca/rysunki/rN-krotki-opis.png`, gdzie N to numer rozdziału.

## Złożenie dokumentu w Wordzie – lista kontrolna

Wklej tekst do dokumentu z ustawionymi stylami i przejdź listę:

- [ ] Strona tytułowa z oficjalnego wzoru WIMiIP
- [ ] Style: Normalny (TNR 12, interlinia 1,5, justowanie, wcięcie 1 cm), Nagłówek 1–3 z numeracją, styl podpisu (TNR 10, interlinia pojedyncza)
- [ ] Marginesy 2 cm, format A4
- [ ] Spis treści z Odwołania → Spis treści, zaktualizowany na końcu
- [ ] Każdy rozdział główny od nowej strony
- [ ] Cytowania jako przypisy końcowe (numeracja 1, 2, 3, nawiasy kwadratowe), powtórzenia jako odsyłacze, kolejność zgodna z wynikiem `cytowania.py`
- [ ] Podpisy przez Odwołania → Wstaw podpis; etykiety „Rys.”, „Tabela”, „Fragment kodu”; numeracja z numerem rozdziału i kropką jako separatorem
- [ ] Odwołania do rysunków i tabel w tekście, najlepiej jako odsyłacze Worda
- [ ] Wzory w edytorze równań, numer (X.Y) wyrównany do prawej
- [ ] Kod w ramce, czcionką o stałej szerokości, z kolorowaniem składni
- [ ] Bez dzielenia wyrazów, bez Entera w środku akapitu, bez spacji zamiast wcięć i wyrównania
- [ ] Tuż przed oddaniem: twarde spacje (Ctrl+Shift+Spacja) po jednoliterowych wyrazach na końcu wiersza (a, i, o, u, w, z)
- [ ] Kontrola wdów i sierot; podpisy z opcją „Razem z następnym”
- [ ] Usunięte komentarze; wszystkie śledzone zmiany zaakceptowane albo odrzucone
- [ ] Nie zostało żadne `[DO UZUPEŁNIENIA]`, `[DO WERYFIKACJI]` ani `[RYS: …]`
- [ ] Rozdział „Wykorzystanie narzędzi GenAI” na końcu pracy, przed literaturą
