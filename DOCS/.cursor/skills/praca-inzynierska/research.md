# Research i przegląd literatury

## Zasada nadrzędna

Cytujesz tylko to, co otworzyłeś i sprawdziłeś. Metadane (autorzy, tytuł, rok, czasopismo lub konferencja, tom, strony, DOI) potwierdź na stronie wydawcy, przez rozwiązanie DOI (doi.org) albo w oficjalnych materiałach konferencji. Nie cytuj z pamięci modelu ani ze streszczeń generowanych przez inne narzędzia AI. Jeśli źródła nie da się sprawdzić, nadaj mu status `do weryfikacji` – wtedy nie trafia do tekstu.

## Proces

1. **Pytania.** Dla każdego podrozdziału zapisz 1–3 pytania, na które ma odpowiedzieć (punkt wyjścia niżej).
2. **Wyszukiwanie.** Google Scholar, Semantic Scholar, IEEE Xplore, ACM Digital Library, ScienceDirect, arXiv, materiały konferencji (np. roboticsproceedings.org) i Biblioteka Główna AGH – dostęp zdalny przez konto AGH; biblioteka udostępnia też narzędzia AI oparte na recenzowanych publikacjach. Szukaj po angielsku i po polsku.
3. **Selekcja.** W pierwszej kolejności prace recenzowane (czasopisma, konferencje IEEE, ACM, RSS), książki akademickie i normy. Parametry sprzętu bierz z kart katalogowych i dokumentacji producenta, opis oprogramowania – z oficjalnej dokumentacji albo publikacji autorów narzędzia. Klasyczne prace źródłowe (pierwszy opis metody) wolno cytować mimo wieku; przy szybko zmieniających się narzędziach sprawdzaj aktualność.
4. **Weryfikacja.** Otwórz stronę źródła, zapisz DOI albo adres URL i datę dostępu. Przeczytaj co najmniej abstrakt i fragment, na który się powołujesz.
5. **Notatka.** Dopisz pozycję do `praca/literatura/zrodla.md` (format niżej) z jednym lub dwoma zdaniami: co dokładnie źródło potwierdza i gdzie (rozdział, strona, tabela).
6. **Synteza.** Podrozdział przeglądu buduj z notatek według schematu: twierdzenie, cytowanie. Porównanie metod umieść w tabeli. Na końcu napisz, co z tego wynika dla FARO. Parafrazuj – nie tłumacz zdań źródła jedno po drugim.
7. **Kontrola.** `python3 .cursor/skills/praca-inzynierska/scripts/cytowania.py praca`

## Czego nie używać

- Wikipedii (zakaz wydziałowy). Można w niej znaleźć odnośniki do źródeł pierwotnych – cytuje się wtedy te źródła po ich sprawdzeniu.
- Blogów, poradników, Medium, filmów i stron z samymi rysunkami (np. podstrony „figure” w ResearchGate). Zamiast nich – publikacja pierwotna.
- Czasopism drapieżnych i prac bez recenzji, jeśli istnieje recenzowany odpowiednik.
- Treści niepublicznych, np. wewnętrznych materiałów Nokii.

## Prawa autorskie i dane

Nie przekazuj narzędziom AI pełnych tekstów płatnych artykułów. Korzystaj z wersji otwartych (arXiv, HAL, strony autorów, materiały konferencji) i z abstraktów. Płatny artykuł autor czyta sam i przekazuje agentowi własne notatki. Pliki PDF trzymaj poza repozytorium albo w katalogu `praca/literatura/pdf/` ignorowanym przez git.

## Format rejestru `praca/literatura/zrodla.md`

Każda pozycja to nagłówek `##` z kluczem i lista pól. Skrypt `cytowania.py` czyta pola `status` i `opis`.

```markdown
## ferris2006
- typ: konferencja
- status: zweryfikowane
- opis: Ferris, B., Hähnel, D., Fox, D., 2006. Gaussian Processes for Signal Strength-Based Location Estimation. Proceedings of Robotics: Science and Systems II. DOI: 10.15607/RSS.2006.II.039
- url: https://www.roboticsproceedings.org/rss02/p39.html
- dostęp: 19.10.2026
- potwierdza: proces gaussowski modeluje poziom sygnału Wi-Fi w przestrzeni; szum pomiaru i korelację przestrzenną wyznacza się z danych jako hiperparametry (abstrakt, wstęp)
```

- **Klucz:** nazwisko pierwszego autora i rok, małymi literami, bez polskich znaków (`taheri2015`); dla dokumentacji – producent i model (`slamtec_a1`).
- **Status:** `zweryfikowane` albo `do weryfikacji`.
- **Opis:** gotowy wpis do literatury w formacie z formatowanie.md.

## Pytania do podrozdziałów (punkt wyjścia)

- **SLAM:** Jak sformułowany jest problem SLAM? Czym różnią się metody oparte na filtrach cząsteczkowych od metod optymalizacji grafu? Które implementacje 2D z lidarem stosuje się na sprzęcie klasy Raspberry Pi i jakie mają wymagania?
- **Mecanum:** Jak wyglądają równania kinematyki prostej i odwrotnej platformy z czterema kołami Mecanum? Jakie błędy odometrii powoduje poślizg rolek?
- **Wi-Fi:** Jak RSSI zmienia się w czasie i od czego zależy (orientacja odbiornika, obecność ludzi, propagacja wielodrogowa)? Jakie metryki poza RSSI opisują jakość połączenia? Jak mierzy się dziś pokrycie (pomiar ręczny, narzędzia do pomiarów terenowych, MDT w sieciach komórkowych)?
- **Interpolacja:** Czym różnią się IDW, kriging i proces gaussowski? Jak każda z metod traktuje szum pomiarowy? Jak ocenia się jakość odtworzonej mapy (walidacja krzyżowa, RMSE)?
- **Dotychczasowe rozwiązania:** Jakie roboty i systemy automatycznie mapowały pokrycie radiowe? Jak ustalały położenie pomiarów i jak budowały mapę? Czym FARO się od nich różni?

## Mapa literatury – pozycje zweryfikowane 19.10.2026

Metadane sprawdzono na stronach wydawców, w DOI i w materiałach konferencji. Przed cytowaniem sprawdź jeszcze, czy źródło rzeczywiście potwierdza konkretne zdanie.

| Klucz | Pozycja | Zastosowanie |
| --- | --- | --- |
| durrantwhyte2006 | Durrant-Whyte, H., Bailey, T., 2006. Simultaneous localization and mapping: part I. IEEE Robotics & Automation Magazine 13(2), 99–110. DOI: 10.1109/MRA.2006.1638022 | definicja problemu SLAM i podstawowe metody |
| grisetti2007 | Grisetti, G., Stachniss, C., Burgard, W., 2007. Improved Techniques for Grid Mapping With Rao-Blackwellized Particle Filters. IEEE Transactions on Robotics 23(1), 34–46. DOI: 10.1109/TRO.2006.889486 | SLAM z filtrem cząsteczkowym na mapie zajętości (GMapping) |
| hess2016 | Hess, W., Kohler, D., Rapp, H., Andor, D., 2016. Real-time loop closure in 2D LIDAR SLAM. 2016 IEEE International Conference on Robotics and Automation (ICRA), 1271–1278. DOI: 10.1109/ICRA.2016.7487258 | SLAM 2D z lidarem i domykaniem pętli (Cartographer) |
| macenski2021 | Macenski, S., Jambrecic, I., 2021. SLAM Toolbox: SLAM for the dynamic world. Journal of Open Source Software 6(61), 2783. DOI: 10.21105/joss.02783 | slam_toolbox (ROS 2) |
| taheri2015 | Taheri, H., Qiao, B., Ghaeminezhad, N., 2015. Kinematic Model of a Four Mecanum Wheeled Mobile Robot. International Journal of Computer Applications 113(3), 6–9. DOI: 10.5120/19804-1586 | kinematyka prosta i odwrotna platformy z kołami Mecanum |
| kaemarungsi2004 | Kaemarungsi, K., Krishnamurthy, P., 2004. Properties of indoor received signal strength for WLAN location fingerprinting. First Annual International Conference on Mobile and Ubiquitous Systems: Networking and Services (MobiQuitous 2004), 14–23. DOI: 10.1109/MOBIQ.2004.1331706 | zmienność i rozkład RSSI w pomieszczeniach |
| shepard1968 | Shepard, D., 1968. A two-dimensional interpolation function for irregularly-spaced data. Proceedings of the 1968 23rd ACM National Conference, 517–524. DOI: 10.1145/800186.810616 | metoda IDW |
| ferris2006 | Ferris, B., Hähnel, D., Fox, D., 2006. Gaussian Processes for Signal Strength-Based Location Estimation. Proceedings of Robotics: Science and Systems II. DOI: 10.15607/RSS.2006.II.039 | proces gaussowski dla poziomu sygnału Wi-Fi; szum jako hiperparametr |
| lebreton2016 | Lebreton, J. M., Murad, N., Lorion, R., 2016. Radio Frequency Mapping using an Autonomous Robot: Application to the 2.4 GHz Band. IOP Conference Series: Materials Science and Engineering 120, 012001. DOI: 10.1088/1757-899X/120/1/012001 | autonomiczny robot mapujący RSSI; ręczny pomiar jako stan obecny; model tłumienia (wersja otwarta w HAL) |
| wakim2017 | Wakim, R., Weitzen, J. A., 2017. An autonomous system for high-resolution mapping of indoor wireless coverage. 2017 IEEE 28th Annual International Symposium on Personal, Indoor, and Mobile Radio Communications (PIMRC). DOI: 10.1109/PIMRC.2017.8292327 | autonomiczny system mapowania pokrycia wewnątrz budynków |
| zou2020 | Zou, H., Chen, C., Li, M., Yang, J., Zhou, Y., Xie, L., Spanos, C. J., 2020. Adversarial Learning-Enabled Automatic WiFi Indoor Radio Map Construction and Adaptation With Mobile Robot. IEEE Internet of Things Journal 7(8), 6946–6954. DOI: 10.1109/JIOT.2020.2979413 | robot z lidarowym SLAM budujący mapę radiową; regresja procesem gaussowskim |
| kim2010 | Kim, K.-H., Min, A. W., Shin, K. G., 2010. Sybot: An Adaptive and Mobile Spectrum Survey System for WiFi Networks. Proceedings of the 16th Annual International Conference on Mobile Computing and Networking (MobiCom 2010), 293–304. DOI: 10.1145/1859995.1860029 | robot do pomiarów Wi-Fi; dobór gęstości i czasu pomiarów |
| hapsari2012 | Hapsari, W. A., Umesh, A., Iwamura, M., Tomala, M., Gyula, B., Sebire, B., 2012. Minimization of drive tests solution in 3GPP. IEEE Communications Magazine. DOI: 10.1109/MCOM.2012.6211483 – tom i strony do uzupełnienia | MDT, czyli automatyzacja pomiarów w sieciach komórkowych |
| slamtec_a1 | RPLIDAR A1 Low Cost 360 Degree Laser Range Scanner – Introduction and Datasheet, Model A1M8, rev. 3.0, SLAMTEC, https://bucket-download.slamtec.com/d1e428e7efbdcd65a8ea111061794fb8d4ccd3a0/LD108_SLAMTEC_rplidar_datasheet_A1M8_v3.0_en.pdf | parametry lidaru: zasięg 0,15–12 m, 360°, typowa częstotliwość skanowania 5,5 Hz |

**Ważne dla określenia wkładu pracy:** autonomiczne roboty do mapowania zasięgu radiowego były już opisywane (lebreton2016, wakim2017, zou2020, kim2010). Przegląd musi to uczciwie pokazać, a wkład FARO trzeba sformułować konkretnie – dopiero po uzgodnieniu zakresu z autorem.

## Do weryfikacji – znane pozycje, jeszcze niesprawdzone

- Thrun, S., Burgard, W., Fox, D. – „Probabilistic Robotics”, MIT Press (2005)
- Rasmussen, C. E., Williams, C. K. I. – „Gaussian Processes for Machine Learning”, MIT Press (2006); wersja otwarta na stronie autorów
- Cressie, N. – „Statistics for Spatial Data”, Wiley (wydanie poprawione 1993) – kriging
- Bailey, T., Durrant-Whyte, H. – „Simultaneous localization and mapping (SLAM): part II”, IEEE Robotics & Automation Magazine (2006)
- Kohlbrecher, S. i in. – Hector SLAM, IEEE SSRR (2011)
- Bahl, P., Padmanabhan, V. N. – RADAR, IEEE INFOCOM (2000) – lokalizacja w Wi-Fi metodą odcisków sygnału
- Ilon, B. E. – patent na koło Mecanum (1975)
- standard IEEE 802.11, dokumentacja narzędzia `iw` (Linux), dokumentacja Raspberry Pi, karta katalogowa MPU-6050, nota katalogowa L298 (STMicroelectronics)

## Przykładowe zapytania

- `2D lidar SLAM comparison Raspberry Pi`, `occupancy grid mapping Rao-Blackwellized particle filter`, `pose graph optimization 2D SLAM`
- `mecanum wheel odometry error slip`, `mecanum forward inverse kinematics`
- `indoor RSSI temporal variation WLAN`, `Wi-Fi site survey methodology`
- `spatial interpolation radio map kriging Gaussian process comparison`, `radio environment map interpolation cross-validation RMSE`
- `autonomous robot Wi-Fi coverage mapping`, `robot radio map construction SLAM`
- po polsku: `mapa pokrycia sieci Wi-Fi pomiar`, `robot mobilny SLAM lidar`, `interpolacja przestrzenna kriging zastosowania`
