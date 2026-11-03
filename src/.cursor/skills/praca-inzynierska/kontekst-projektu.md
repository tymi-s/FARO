# Kontekst projektu FARO

Ten plik jest dla agenta jedynym źródłem faktów o projekcie. Gdy autor poda nową informację albo coś się zmieni, popraw plik i zmień datę. Rzeczy planowane opisuj jako planowane, nigdy jako wykonane.

Stan na: 2026-10-19

## Osoby i formalności

- **Autor:** Tymon Szyler, kierunek Inżynieria Obliczeniowa, Wydział Inżynierii Metali i Informatyki Przemysłowej (WIMiIP) AGH, studia I stopnia, IV rok.
- **Promotor (opiekun):** Piotr Kustra. W podziękowaniach pracy przykładowej występuje jako dr inż. Aktualny tytuł sprawdź przed wpisaniem na stronę tytułową.
- **Konsultant i proponowany recenzent:** Opaliński – prowadził na kierunku zajęcia z sieci komputerowych i administracji systemów. Promotor zamierza zaproponować go na recenzenta; dla kierunku Inżynieria Obliczeniowa decyzję podejmuje kierownik Katedry Informatyki Stosowanej i Modelowania. Imię i tytuł: [DO UZUPEŁNIENIA].
- **Forma:** według zasad dyplomowania WIMiIP (od stycznia 2026) studia I stopnia kończą się projektem dyplomowym. Promotor nazywa dokument „pracą dyplomową” – oba określenia dotyczą tego samego dokumentu.
- **Rejestracja:** autor wgrywa plik do APD (USOS), który przesyła go do Jednolitego Systemu Antyplagiatowego (JSA). Na studiach stacjonarnych projekt trzeba zarejestrować do końca lutego. Opiekun wpisuje recenzję najpóźniej 5 dni roboczych przed tym terminem, więc wersję końcową trzeba oddać wcześniej. Tytuł podaje się po polsku i po angielsku.
- **Strona tytułowa:** oficjalny wzór WIMiIP ze strony dla dyplomantów; nie tworzyć własnej.
- **Obrona:** prezentacja ok. 7 minut (maksymalnie 10), razem z dyskusją ok. 20 minut (wskazówki redakcyjne WIMiIP).

## Temat

- **Tytuł oficjalny:** [DO UZUPEŁNIENIA – dokładnie tak jak w APD, po polsku i po angielsku]
- **Tytuł roboczy:** Autonomiczny robot mobilny do mapowania pomieszczeń i pomiaru pokrycia sieci Wi-Fi
- **Idea:** robot FARO samodzielnie buduje lidarem mapę pomieszczenia (SLAM) i zna na niej swoje położenie. W wybranych punktach mierzy jakość połączenia Wi-Fi, a z tych pomiarów metodą interpolacji przestrzennej wyznacza mapę pokrycia sieci i nakłada ją na mapę pomieszczenia.
- **Uzasadnienie:** pokrycie Wi-Fi w budynkach sprawdza się zwykle ręcznie – osoba z laptopem lub telefonem obchodzi pomieszczenia i zapisuje wyniki wraz z położeniem. Robot ma wykonywać takie pomiary powtarzalnie i sam przypisywać im położenie.
- **Wnioski z konsultacji z Opalińskim (21.09.2026):** pomysł jest dobry, jeśli robot autonomicznie mapuje teren, zna swoje położenie i sam nakłada mapę pokrycia. Sam pomiar sieci był już przedmiotem innych prac (np. pomiar telefonem), dlatego o wartości pracy decyduje autonomia. Lidar będzie potrzebny. Uwaga Opalińskiego: pole magnetyczne enkoderów może zakłócać pomiary – [DO WYJAŚNIENIA: których pomiarów dotyczy uwaga].
- **Promotor (21.09.2026)** zaakceptował ten kierunek tematu („mamy rozwiązanie problemu tematyki”).
- **Rozszerzalność (argument autora):** platforma, która zna swoje położenie, pozwala mapować dowolną wielkość mierzoną czujnikiem, np. stężenie tlenku węgla. To materiał do kierunków dalszych prac, nie do zakresu.

## Rdzeń obliczeniowy – argument na obronę na Inżynierii Obliczeniowej

Robot jest platformą pomiarową. Wkład obliczeniowy pracy stanowią:

- SLAM 2D z lidarem: estymacja położenia i mapy (filtr cząsteczkowy albo optymalizacja grafu położeń, dopasowanie skanów),
- kinematyka platformy z kołami Mecanum (zadanie proste i odwrotne), odometria, ewentualnie fuzja z IMU,
- interpolacja przestrzenna pomiarów (IDW, kriging, proces gaussowski) z jawnym uwzględnieniem szumu RSSI,
- ocena jakości: błąd mapy względem wymiarów zmierzonych ręcznie, powtarzalność lokalizacji, walidacja krzyżowa interpolacji (np. RMSE).

## Historia decyzji (żeby nie wracać do odrzuconych pomysłów)

- Na początku FARO miał być robotem kroczącym wzorowanym na TARS z filmu „Interstellar”. Uczenie chodu metodą uczenia ze wzmocnieniem odrzucono jako zbyt trudne w dostępnym czasie.
- Promotor zapytał, po co robot kroczący na płaskiej powierzchni, skoro pojazd zrobi to szybciej. Wybrano więc robota kołowego.
- Autor pracuje w Nokii przy testach sieci, ale świadomie nie korzysta ze sprzętu ani z niepublicznej wiedzy firmy. Wybrano Wi-Fi zamiast sieci komórkowej, bo karta Wi-Fi jest wbudowana w Raspberry Pi i nie ma problemów z patentami.
- Po konsultacji z Opalińskim temat poszerzono o SLAM z lidarem.

## Sprzęt (stan na 2026-10-19)

| Element | Model / opis | Stan |
| --- | --- | --- |
| Podwozie | aluminiowe podwozie 4WD z czterema kołami Mecanum (zestaw) | zmontowane |
| Silniki | 4 motoreduktory DC typu TT z zestawu | zamontowane; czy mają enkodery: [DO UZUPEŁNIENIA] |
| Sterowniki silników | 2 × L298N (po dwa kanały, osobny kanał dla każdego koła – wymagane przy kołach Mecanum) | przed podłączeniem |
| Komputer | Raspberry Pi 3 (wersja: [DO UZUPEŁNIENIA]); wbudowana karta Wi-Fi służy też jako czujnik | – |
| Lidar | SLAMTEC RPLIDAR A1M8 (naklejka: A1M8-R5) z adapterem USB–UART | dostępny |
| IMU | MPU-6050 (moduł GY-521), magistrala I2C | – |
| Kamera | moduł kamery Raspberry Pi (złącze CSI), z przodu, nieruchoma | planowana |
| Zasilanie | 2 ogniwa 18650 połączone szeregowo (2S, ok. 7,4 V); przetwornica obniżająca LM2596 5 V / 3 A dla Raspberry Pi i logiki L298N; złączki WAGO 221; wyłącznik | planowane |
| Obudowa | projekt w SolidWorks, druk 3D; pokrywa z otworem na lidar | w projektowaniu |

## Oprogramowanie (plany – nic nie jest jeszcze wybrane na stałe)

- Python ≥ 3.11; zależności repozytorium: numpy, pandas, pytest, ruff; menedżer pakietów uv.
- SLAM: [DO WYBORU]. Kandydaci do porównania w przeglądzie: slam_toolbox (ROS 2), Cartographer, GMapping, Hector SLAM, lekkie biblioteki w Pythonie.
- Pomiar Wi-Fi: RSSI z wbudowanej karty (narzędzie `iw`); w każdym punkcie seria próbek, z której zapisuje się średnią i odchylenie standardowe. Opcjonalnie opóźnienie i utrata pakietów (`ping`) oraz przepustowość (`iperf3`).
- Procedura: robot zatrzymuje się w punkcie, wykonuje serię pomiarów i zapisuje (x, y, metryki, czas).
- Interpolacja: porównanie IDW z krigingiem albo procesem gaussowskim. Szum RSSI uwzględniany jawnie (składnik szumu w procesie gaussowskim, efekt samorodka w krigingu).

## Do ustalenia z promotorem

| Sprawa | Fakty | Wartość domyślna do czasu ustalenia |
| --- | --- | --- |
| Objętość | zasady WIMiIP od 2026: 20–35 stron; praca przykładowa: 49 stron | 30–35 stron |
| Numeracja wstępu | wydział: numerować rozdziały od wstępu; praca przykładowa: wstęp bez numeru | bez numeru, jak w pracy przykładowej |
| Numeracja „Literatury” | wydział: bez numeru; praca przykładowa: z numerem | bez numeru |
| Separator dziesiętny | polska norma: przecinek; praca przykładowa: kropka | przecinek |
| Wzór strony tytułowej | wydział ma osobne wzory dla projektu i dla pracy dyplomowej | wzór projektu dyplomowego |
| Zakres użycia GenAI | wytyczne WIMiIP: zakres ustala promotor z dyplomantem | granice z SKILL.md |
| Rozdział „Konwencja edytorska” | wydział: opcjonalny, gdy praca zawiera kod, polecenia i wyjście konsoli | dodać, maksymalnie 1 strona |
