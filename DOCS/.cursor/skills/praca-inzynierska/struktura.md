# Struktura pracy

## Wymagany układ (zasady dyplomowania WIMiIP, od 2026)

1. **Część początkowa:** strona tytułowa (wzór wydziału) i automatyczny spis treści.
2. **Wstęp** (2–3 strony): uzasadnienie tematu, cel pracy, założenia techniczne i krótkie streszczenie. Wydział zaleca pisać go na końcu.
3. **Część analityczna:** wprowadzenie do tematu, analiza literatury, przegląd dotychczasowych rozwiązań i uzasadnienie wybranego sposobu rozwiązania. Z przeglądu literatury powinien wynikać cel pracy.
4. **Część syntetyczna:** przyjęte rozwiązania i uzasadnienie ich wyboru, czyli praca własna.
5. **Część weryfikacyjna:** warunki testów, metody badań, wyniki z analizą i wnioski.
6. **Zakończenie:** podsumowanie i kierunki dalszych prac.
7. **Wykorzystanie narzędzi GenAI** (wytyczne GenAI WIMiIP): obowiązkowy rozdział na końcu pracy, potrzebny także wtedy, gdy AI nie użyto.
8. **Bibliografia** oraz ewentualne załączniki (np. schematy, dłuższe kody, instrukcje).

Według zasad 2026 objętość ma wynosić 20–35 stron (do potwierdzenia – kontekst-projektu.md). Co najmniej połowa tekstu ma opisywać pracę wykonaną samodzielnie.

## Wzór: praca przykładowa u tego samego promotora

Praca Patrycji Szlachty dotyczy detekcji defektów na przewijanym materiale modelem YOLOv8 i prototypu linii inspekcyjnej z druku 3D. Ma 49 stron, ok. 10,6 tys. słów, 14 pozycji literatury i ok. 40 podpisów rysunków, tabel i fragmentów kodu.

| Rozdział w przykładzie | Część według wydziału | Zawartość |
| --- | --- | --- |
| Podziękowania | – | opcjonalne |
| Wstęp (bez numeru) | wstęp | kontekst przemysłowy, problem (ręczna kontrola jest zawodna), podejście (AI), konkretny przypadek firmy i założenie systemu |
| 1. Cel pracy | wstęp | akapit z celem głównym, akapit z celem dodatkowym (prototyp), akapit „zakres pracy” wyliczający etapy |
| 2. Przegląd literatury | analityczna | akapit wprowadzający z cytowaniem; podrozdziały o pojęciach podstawowych i o wybranej metodzie |
| 3–6. Dane, trening, implementacja, budowa prototypu | syntetyczna | w każdym rozdziale: co i po co, jak to zrobiono, krótkie fragmenty kodu z omówieniem, rysunki |
| 7. Analiza wyników treningu i skuteczności | weryfikacyjna | objaśnienie metryk, wyniki na wykresach i w tabelach, porównanie z wartościami rzeczywistymi, przyczyny ograniczeń |
| 8. Podsumowanie i wnioski | zakończenie | co zrobiono w kolejnych etapach, co wykazały testy, ograniczenia, ocena realizacji celów |
| 9. Wykorzystanie narzędzi GenAI | – | jeden akapit: do czego użyto AI (wyjaśnianie błędów kodu, rozszerzenie zbioru obrazów, redakcja językowa) |
| 10. Literatura | bibliografia | przypisy końcowe Worda |

**Warto przejąć:** wprowadzenie każdego rysunku i fragmentu kodu w tekście przed jego pojawieniem się; konkretne liczby z jednostkami i porównanie wyniku z wartością rzeczywistą; rzetelne omówienie ograniczeń razem z ich przyczynami; krótkie fragmenty kodu z objaśnieniem; termin angielski w nawiasie przy pierwszym użyciu.

**Nie powielać:** ogólnikowych otwarć („Współczesne przedsiębiorstwa poprzez dynamiczny rozwój…”), częstego „kluczowy” i „warto podkreślić”, wielokrotnego powtarzania tej samej oceny, podręcznikowych objaśnień pojęć powszechnie znanych. Tekstu pracy przykładowej nie kopiuj ani nie parafrazuj.

## Proponowany spis treści FARO (roboczy, do uzgodnienia z promotorem)

```
Wstęp
1. Cel i zakres pracy
2. Konwencja edytorska (opcjonalnie, maksymalnie 1 strona)
3. Przegląd literatury i dotychczasowych rozwiązań
   3.1. Lokalizacja i mapowanie robotów mobilnych (problem SLAM, mapa zajętości, metody 2D z lidarem)
   3.2. Kinematyka i odometria platform z kołami Mecanum
   3.3. Pomiar jakości sieci Wi-Fi (RSSI i jego zmienność, inne metryki, sposoby pomiaru pokrycia)
   3.4. Interpolacja przestrzenna pomiarów (IDW, kriging, proces gaussowski)
   3.5. Roboty do automatycznego pomiaru pokrycia sieci
   3.6. Porównanie rozwiązań i uzasadnienie wyboru
4. Projekt i budowa platformy mobilnej (mechanika, elektronika, zasilanie, schemat połączeń)
5. Oprogramowanie sterujące i system SLAM (sterowanie kołami Mecanum, odometria, lidar, mapowanie, nawigacja do punktów)
6. Pomiar jakości Wi-Fi i budowa mapy pokrycia (procedura pomiaru, format danych, interpolacja, nałożenie na mapę)
7. Badania i analiza wyników – pisze autor
8. Podsumowanie i wnioski – pisze autor
9. Wykorzystanie narzędzi GenAI
Literatura
Załączniki (opcjonalnie)
```

Orientacyjny podział dla ok. 35 stron (przegląd literatury do 5 stron – decyzja autora z 23.10.2026): wstęp 2, cel i zakres 1, konwencja edytorska 1, przegląd literatury 5 (3.1 SLAM 1,5; 3.2 Mecanum 0,5; 3.3 Wi-Fi 0,75; 3.4 interpolacja 1; 3.5 i 3.6 razem 1–1,25), platforma 5, oprogramowanie i SLAM 7, Wi-Fi i mapa pokrycia 5, badania 7, podsumowanie 1,5, GenAI 0,5. Rozdziały 4–7 (praca własna) muszą stanowić co najmniej połowę.

Nazwy plików: `praca/rozdzialy/00-wstep.md`, `01-cel-i-zakres.md`, `02-konwencja-edytorska.md`, `03-przeglad-literatury.md`, `04-platforma.md`, `05-oprogramowanie-slam.md`, `06-pomiar-wifi.md`, `07-badania.md`, `08-podsumowanie.md`, `09-genai.md`.

## Przepisy na rozdziały

### Wstęp – pisz na końcu

1. Konkretny problem: jak dziś sprawdza się pokrycie Wi-Fi i co w tym przeszkadza. Bez ogólników o „dzisiejszych czasach”.
2. Proponowane podejście: robot, SLAM, pomiar w punktach, interpolacja.
3. Cel w jednym zdaniu oraz założenia techniczne (platforma, czujniki, metody).
4. Krótkie streszczenie, czyli co zawierają kolejne rozdziały – bez wniosków.

Rysunek poglądowy całego systemu umieść w rozdziale 1, bo rysunek w nienumerowanym wstępie nie miałby numeru rozdziału.

### 1. Cel i zakres pracy

- Cel główny w jednym zdaniu.
- Cele szczegółowe jako równoważniki zdań w wypunktowaniu (mała litera, przecinek, kropka po ostatnim), a pod nimi akapit, który je rozwija.
- Zakres pracy: co wykonano samodzielnie, a z czego skorzystano gotowego (podwozie z zestawu, biblioteki SLAM, moduły elektroniczne).
- Założenia techniczne, np. jednopoziomowe pomieszczenia, pomiar na postoju, jedna sieć Wi-Fi – wpisuj tylko te, które autor potwierdził.

### 2. Konwencja edytorska (opcjonalnie)

Maksymalnie jedna strona. Jak w pracy odróżniono kod źródłowy, pliki konfiguracyjne, polecenia systemowe (z uprawnieniami administratora i bez) oraz wyjście konsoli – z jednym przykładem każdego rodzaju.

### 3. Przegląd literatury i dotychczasowych rozwiązań

- Każdy podrozdział odpowiada na pytania z research.md: opis metod z cytowaniami, ich ograniczenia i jedno lub dwa zdania o tym, co z tego wynika dla FARO.
- Podawaj tylko te wzory, z których korzystasz dalej (np. kinematyka Mecanum, wagi IDW, model procesu gaussowskiego).
- Podrozdział 3.6 zawiera tabelę porównawczą i uzasadnienie wyboru – z niego wynika cel pracy.
- Rzetelne pozycjonowanie: autonomiczne roboty do mapowania zasięgu radiowego były już opisywane (mapa literatury w research.md). Wkład FARO sformułuj konkretnie dopiero wtedy, gdy autor potwierdzi zakres.

### 4–6. Rozdziały syntetyczne

**Sprzęt (rozdział 4):** wymagania; dobór elementów z uzasadnieniem (tabela parametrów z cytowanych kart katalogowych); schemat połączeń i zasilania (rysunek własny); konstrukcja (CAD, druk 3D); bilans zasilania.

**Oprogramowanie (rozdziały 5–6)** według wskazówek redakcyjnych WIMiIP:

1. idea i przypadki użycia – po co, dla kogo, co ma robić,
2. zasada działania bez szczegółów technicznych (kolejność kroków, przepływ danych),
3. projekt: diagramy komponentów, sekwencji albo czynności (UML),
4. implementacja: najciekawsze fragmenty kodu z omówieniem,
5. uruchomienie, jeśli jest nietrywialne,
6. testy dowodzące, że system spełnia wymagania – to nie jest instrukcja obsługi.

Zawsze: co gotowe, a co własne; każda decyzja z uzasadnieniem; liczby z jednostkami.

### 7. Badania i analiza wyników – pisze autor

Agent może przygotować: układ podrozdziałów (warunki pomiarów, metody, wyniki, dyskusja), listę elementów, które powinny się znaleźć (opis pomieszczeń, liczba punktów, liczba próbek w punkcie, użyte metryki błędu), szablony tabel bez danych oraz kontrolę formatowania i zgodności liczb. Interpretację wyników i wnioski pisze wyłącznie autor.

### 8. Podsumowanie i wnioski – pisze autor

Według wytycznych: co zrobiono, wnioski ogólne, kierunki dalszych prac. Agent sprawdza tylko język oraz to, czy omówiono każdy cel z rozdziału 1.

### 9. Wykorzystanie narzędzi GenAI

Na podstawie `praca/genai-log.md`: nazwy narzędzi, do czego i w jakim zakresie ich użyto (research, redakcja, kod) oraz informacja, że nie używano ich do generowania i analizy wyników ani do formułowania wniosków. Agent może przygotować szkic z dziennika; ostateczną wersję zatwierdza autor.
