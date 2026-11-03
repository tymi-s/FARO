# 3. Przegląd literatury i dotychczasowych rozwiązań

Robot FARO łączy trzy zagadnienia: samolokalizację i budowę mapy pomieszczenia, pomiar jakości sieci Wi-Fi oraz odtworzenie ciągłej mapy pokrycia z pomiarów wykonanych w pojedynczych punktach. Przegląd porządkuje metody z każdego z tych obszarów i podaje tylko te zależności, z których korzystają dalsze rozdziały. Osobny podrozdział zestawia roboty opisane w literaturze, które już automatycznie mapowały pokrycie radiowe — autonomiczny pomiar pokrycia nie jest zagadnieniem nowym [@lebreton2016; @wakim2017].

Układ rozdziału odpowiada kolejnym krokom działania robota: lokalizacja i mapa (podrozdział 3.1), ruch platformy i odometria (3.2), pomiar sieci (3.3) oraz interpolacja pomiarów do mapy pokrycia (3.4). Podrozdział 3.5 opisuje dotychczasowe roboty pomiarowe, a 3.6 zestawia rozwiązania i uzasadnia wybór metod przyjętych w pracy.

## 3.1. Lokalizacja i mapowanie robotów mobilnych

Jednoczesna lokalizacja i budowa mapy (ang. *simultaneous localization and mapping*, SLAM) polega na równoczesnym wyznaczaniu mapy otoczenia i położenia robota na tej mapie na podstawie odczytów czujników [@durrantwhyte2006]. Robot nie potrzebuje więc wcześniej przygotowanego planu pomieszczenia, co odpowiada zadaniu FARO, który mapuje nieznane z góry wnętrze. Metoda SLAM jest ustaloną częścią robotyki mobilnej [@durrantwhyte2006].

Metody SLAM dzielą się na dwie główne rodziny. Pierwsza opiera się na filtrze cząsteczkowym: w podejściu Rao-Blackwella każda cząsteczka niesie własną mapę i trajektorię robota, a liczbę cząsteczek ogranicza się przez rozkład propozycji uwzględniający ostatni odczyt skanera oraz selektywne ponowne próbkowanie [@grisetti2007]. Implementacją tej rodziny jest GMapping [@grisetti2007]. Druga rodzina sprowadza SLAM do optymalizacji grafu pozycji, w którym krawędzie odpowiadają dopasowaniu kolejnych skanów, a domknięcie pętli (ang. *loop closure*) koryguje narastający błąd po powrocie robota w odwiedzone miejsce. Cartographer wyznacza takie domknięcia w czasie rzeczywistym, dopasowując skany do podmap metodą podziału i ograniczeń (ang. *branch and bound*) przy rozdzielczości mapy 5 cm i ograniczonych zasobach obliczeniowych [@hess2016]. Pakiet slam_toolbox buduje i aktualizuje mapy dużych, zmieniających się przestrzeni i jest powszechnie używany do SLAM 2D w systemie ROS 2 [@macenski2021].

Otoczenie reprezentuje się najczęściej jako mapa zajętości (ang. *occupancy grid*), czyli siatka komórek z prawdopodobieństwem zajęcia przez przeszkodę [@grisetti2007]. Dane do niej dostarcza skaner laserowy. W pracy przyjęto lidar RPLIDAR A1M8, który skanuje otoczenie w zakresie 360° z zasięgiem 0,15–12 m, rozdzielczością kątową ≤1° i prędkością obrotową 5,5 Hz, a wyniki przesyła interfejsem UART 3,3 V [@slamtec_a1]. Parametry te wyznaczają gęstość i zasięg pojedynczego skanu wykorzystywanego przez algorytm SLAM.

Tabela 3.1 zestawia trzy implementacje SLAM 2D rozważane w pracy.

Tabela 3.1. Porównanie rozważanych implementacji SLAM 2D z lidarem

| Implementacja | Rodzina metody | Domykanie pętli | Źródło |
| --- | --- | --- | --- |
| GMapping | filtr cząsteczkowy Rao-Blackwella | niejawne, w filtrze | [@grisetti2007] |
| Cartographer | optymalizacja grafu, dopasowanie skanów | jawne, branch and bound | [@hess2016] |
| slam_toolbox | optymalizacja grafu, ROS 2 | jawne | [@macenski2021] |

Źródło: opracowanie własne na podstawie [@grisetti2007; @hess2016; @macenski2021]

Dla FARO istotne jest, że SLAM 2D z lidarem działa na skanie płaskim i nie wymaga kamery ani znaczników w otoczeniu. Wybór implementacji spośród zestawionych w tabeli 3.1 zależy od zasobów Raspberry Pi 3 i integracji z resztą oprogramowania, dlatego jest przedmiotem rozdziału 5.

## 3.2. Kinematyka i odometria platform z kołami Mecanum

Platforma FARO jeździ na czterech kołach Mecanum (ang. *Mecanum wheels*), których obwód tworzą swobodne rolki ustawione pod kątem 45°. Taki układ pozwala przesuwać się do przodu, w bok i obracać w miejscu bez skręcania kół, co daje osiem kierunków ruchu bez zmiany orientacji platformy [@taheri2015]. Zależność prędkości kątowych kół od zadanej prędkości platformy opisuje odwrotny model kinematyczny (3.1) [@taheri2015]:

$$
\begin{bmatrix} \omega_1 \\ \omega_2 \\ \omega_3 \\ \omega_4 \end{bmatrix}
= \frac{1}{r}
\begin{bmatrix}
1 & -1 & -(l_x+l_y) \\
1 & 1 & (l_x+l_y) \\
1 & 1 & -(l_x+l_y) \\
1 & -1 & (l_x+l_y)
\end{bmatrix}
\begin{bmatrix} v_x \\ v_y \\ \omega_z \end{bmatrix}
$$ (3.1)

gdzie: ω₁…ω₄ – prędkości kątowe czterech kół [rad/s], v_x, v_y – prędkości liniowe platformy wzdłuż i w poprzek kierunku jazdy [m/s], ω_z – prędkość kątowa platformy [rad/s], r – promień koła [m], l_x, l_y – połowa rozstawu osi i połowa rozstawu kół [m]. Znaki w macierzy zależą od przyjętej numeracji kół i orientacji rolek; pełne wyprowadzenie podano w [@taheri2015].

Model (3.1) zakłada brak poślizgu rolek o podłoże [@taheri2015]. W rzeczywistości rolki się ślizgają, a odometria (wyznaczanie położenia przez całkowanie przemieszczeń kół) kumuluje wtedy błąd rosnący z przebytą drogą. Z tego powodu położenie robota wyznacza SLAM, a odometria służy jako wejście predykcyjne algorytmu [@durrantwhyte2006]. Model (3.1) jest podstawą sterowania napędem opisanego w rozdziale 5.

## 3.3. Pomiar jakości sieci Wi-Fi

Jakość połączenia radiowego opisuje najczęściej wskaźnik poziomu odbieranego sygnału (ang. *received signal strength indicator*, RSSI), podawany w dBm [@kaemarungsi2004]. RSSI mierzony w jednym miejscu nie jest stały, a jego rozkład w pomieszczeniu bywa przybliżany modelem Gaussa [@kaemarungsi2004]. Pojedynczy odczyt nie wystarcza zatem do opisu punktu; w każdym punkcie pomiarowym pobiera się serię próbek i zapisuje ich średnią oraz odchylenie standardowe. Poza RSSI jakość połączenia opisują też przepustowość, opóźnienie i utrata pakietów.

Pokrycie sieci sprawdza się dziś głównie ręcznie: osoba z odbiornikiem obchodzi pomieszczenia i zapisuje poziom sygnału wraz z położeniem [@lebreton2016; @wakim2017]. Proces jest czasochłonny, a jego rozdzielczość i dokładność zależą od operatora [@wakim2017]. W sieciach komórkowych pomiary zautomatyzowano w ramach minimalizacji testów jezdnych (ang. *minimization of drive tests*, MDT), w której dane zbierają same terminale abonenckie zamiast operatora z miernikiem [@hapsari2012].

Dla FARO wynika z tego procedura pomiaru: robot zatrzymuje się w punkcie, pobiera serię próbek RSSI i zapisuje położenie odczytane z mapy SLAM wraz ze statystykami sygnału. Procedurę i format danych opisuje rozdział 6.

## 3.4. Interpolacja przestrzenna pomiarów

Pomiar daje wartości sygnału tylko w skończonej liczbie punktów, a mapa pokrycia wymaga wartości w całym pomieszczeniu, dlatego stosuje się interpolację przestrzenną. Najprostszą metodą jest ważenie odwrotną odległością (ang. *inverse distance weighting*, IDW), w którym wartość w punkcie szukanym jest średnią ważoną pomiarów, a wagi maleją z odległością, co opisuje wzór (3.2) [@shepard1968]:

$$ \hat{z}(x_0) = \frac{\sum_{i=1}^{n} w_i\, z_i}{\sum_{i=1}^{n} w_i}, \qquad w_i = \frac{1}{d(x_0, x_i)^p} $$ (3.2)

gdzie: ẑ(x₀) – wartość interpolowana w punkcie x₀, z_i – wartość zmierzona w punkcie x_i, d(x₀, x_i) – odległość między punktami [m], p – wykładnik wagi, n – liczba punktów pomiarowych. Jako interpolator dokładny IDW odtwarza w punktach pomiarowych wartości zmierzone i nie rozdziela sygnału od szumu pomiaru [@shepard1968].

Kriging i proces gaussowski uwzględniają korelację przestrzenną danych. Kriging, metoda wywodząca się z geostatystyki, wyznacza wartość jako optymalną liniową kombinację pomiarów na podstawie przestrzennej struktury korelacji oszacowanej z danych [@cressie1990]. Proces gaussowski (ang. *Gaussian process*, GP) opisuje sygnał jako realizację procesu losowego i pozwala wyznaczyć szum pomiaru oraz korelację przestrzenną z danych jako hiperparametry modelu [@ferris2006]. Model GP zastosowano do szacowania poziomu sygnału Wi-Fi w [@ferris2006].

W odróżnieniu od IDW proces gaussowski jawnie ujmuje szum pomiaru jako osobny składnik modelu [@ferris2006]; kriging ujmuje ten sam efekt przez tak zwany samorodek (ang. *nugget*). Jakość odtworzonej mapy ocenia się walidacją krzyżową, porównując wartości przewidziane z pomiarami w punktach pominiętych przy interpolacji, na przykład przez pierwiastek błędu średniokwadratowego (RMSE). W pracy porównano IDW z metodą uwzględniającą korelację przestrzenną, traktując szum RSSI jawnie; metodę interpolacji i jej ocenę przedstawia rozdział 6.

## 3.5. Roboty do automatycznego pomiaru pokrycia sieci

Autonomiczny pomiar pokrycia radiowego opisano w literaturze w kilku wariantach, zestawionych w tabeli 3.2. Lebreton i współautorzy zbudowali robota, który zbiera poziom sygnału w paśmie 2,4 GHz i dopasowuje pomiary do modelu tłumienia, tworząc mapę pola RF; jako stan wyjściowy wskazują pomiar ręczny [@lebreton2016]. Wakim i Weitzen opisali robota, który sam eksploruje obszar, wyznacza położenie względem mapy budynku i nakłada na nią metryki warstwy fizycznej, takie jak SNR, RSRP i CQI [@wakim2017]. System Sybot mierzy parametry sieci Wi-Fi, ujmuje zmiany przestrzenno-czasowe sygnału i sam dobiera czas pomiaru oraz rozdzielczość przestrzenną w danym miejscu [@kim2010]. Zou i współautorzy połączyli budowę mapy przestrzeni i mapy radiowej Wi-Fi na jednym robocie mobilnym, stosując regresję procesem gaussowskim i wskazując koszt ręcznej budowy gęstej mapy radiowej jako główną barierę [@zou2020].

Tabela 3.2. Roboty do automatycznego pomiaru pokrycia radiowego

| Praca | Źródło położenia | Mierzona wielkość | Odtworzenie mapy |
| --- | --- | --- | --- |
| [@lebreton2016] | robot autonomiczny | RSSI (2,4 GHz) | model tłumienia |
| [@wakim2017] | położenie względem mapy budynku | SNR, RSRP, CQI | nałożenie na mapę |
| [@kim2010] | robot mobilny (Sybot) | RSSI Wi-Fi | mapa parametrów, dobór gęstości |
| [@zou2020] | mapa przestrzeni z robota | RSSI Wi-Fi | regresja procesem gaussowskim |

Źródło: opracowanie własne na podstawie [@lebreton2016; @wakim2017; @kim2010; @zou2020]

Wspólną cechą tych rozwiązań jest powiązanie każdego pomiaru z położeniem i odtworzenie ciągłej mapy z pomiarów punktowych. Różnią się one źródłem położenia oraz metodą odtworzenia mapy, co wskazuje, że o wartości takiego systemu decyduje dokładność lokalizacji i sposób interpolacji.

## 3.6. Porównanie rozwiązań i uzasadnienie wyboru

Z przeglądu wynikają decyzje techniczne przyjęte w pracy. Lokalizację i mapę zapewnia SLAM 2D z lidarem, zgodny z płaskim skanem RPLIDAR A1M8 i możliwy do uruchomienia przy ograniczonych zasobach obliczeniowych [@hess2016]; wybór implementacji spośród zestawionych w tabeli 3.1 jest przedmiotem rozdziału 5. Ruch platformy opisuje odwrotny model kinematyki kół Mecanum (3.1) [@taheri2015]. Pomiar Wi-Fi oparto na serii próbek RSSI w punkcie, gdyż pojedynczy odczyt obarczony jest zmiennością sygnału [@kaemarungsi2004]. Mapę pokrycia odtwarza interpolacja przestrzenna z jawnym uwzględnieniem szumu [@shepard1968; @ferris2006].

Dotychczasowe roboty zestawione w tabeli 3.2 pokazują, że automatyczny pomiar pokrycia radiowego nie jest nowy [@lebreton2016; @wakim2017; @kim2010; @zou2020]. Wkład pracy względem tych rozwiązań wymaga doprecyzowania zakresu z promotorem.

[DO UZUPEŁNIENIA: konkretne sformułowanie wkładu własnego FARO względem rozwiązań z tabeli 3.2 — po ustaleniu zakresu z promotorem; z tego sformułowania wynika cel pracy opisany w rozdziale 1]
