# Rejestr źródeł

Format wg research.md. Pole `status`: `zweryfikowane` albo `do weryfikacji`. Metadane potwierdzone 23.10.2026 przez Crossref (dane wydawcy), abstrakty przez Semantic Scholar i OpenAlex, parametry lidaru na oficjalnej stronie SLAMTEC.

## durrantwhyte2006
- typ: artykuł w czasopiśmie
- status: zweryfikowane
- opis: Durrant-Whyte, H., Bailey, T., 2006. Simultaneous localization and mapping: part I. IEEE Robotics & Automation Magazine 13(2), 99–110. DOI: 10.1109/MRA.2006.1638022
- url: https://doi.org/10.1109/MRA.2006.1638022
- dostęp: 23.10.2026
- potwierdza: definicja problemu SLAM (jednoczesne wyznaczanie mapy i położenia robota) oraz stwierdzenie, że ogólna metoda SLAM jest ustaloną częścią robotyki (abstrakt)

## grisetti2007
- typ: artykuł w czasopiśmie
- status: zweryfikowane
- opis: Grisetti, G., Stachniss, C., Burgard, W., 2007. Improved Techniques for Grid Mapping With Rao-Blackwellized Particle Filters. IEEE Transactions on Robotics 23(1), 34–46. DOI: 10.1109/TRO.2006.889486
- url: https://doi.org/10.1109/TRO.2006.889486
- dostęp: 23.10.2026
- potwierdza: SLAM filtrem cząsteczkowym Rao-Blackwella na mapie zajętości; każda cząsteczka niesie własną mapę; adaptacyjny rozkład propozycji z uwzględnieniem ostatniej obserwacji i selektywne ponowne próbkowanie redukują liczbę cząsteczek (abstrakt) — podstawa GMappingu

## hess2016
- typ: referat konferencyjny
- status: zweryfikowane
- opis: Hess, W., Kohler, D., Rapp, H., Andor, D., 2016. Real-time loop closure in 2D LIDAR SLAM. 2016 IEEE International Conference on Robotics and Automation (ICRA), 1271–1278. DOI: 10.1109/ICRA.2016.7487258
- url: https://doi.org/10.1109/ICRA.2016.7487258
- dostęp: 23.10.2026
- potwierdza: SLAM 2D z lidarem z domykaniem pętli w czasie rzeczywistym przy rozdzielczości 5 cm; dopasowanie skanów do podmap metodą podziału i ograniczeń (branch-and-bound); działanie przy ograniczonych zasobach obliczeniowych (abstrakt) — podstawa Cartographera

## macenski2021
- typ: artykuł w czasopiśmie
- status: zweryfikowane
- opis: Macenski, S., Jambrecic, I., 2021. SLAM Toolbox: SLAM for the dynamic world. Journal of Open Source Software 6(61), 2783. DOI: 10.21105/joss.02783
- url: https://doi.org/10.21105/joss.02783
- dostęp: 23.10.2026
- potwierdza: otwarty pakiet slam_toolbox do budowy i aktualizacji map dużych, zmieniających się przestrzeni dla robotów mobilnych (abstrakt, strona JOSS)

## taheri2015
- typ: artykuł w czasopiśmie
- status: zweryfikowane
- opis: Taheri, H., Qiao, B., Ghaeminezhad, N., 2015. Kinematic Model of a Four Mecanum Wheeled Mobile Robot. International Journal of Computer Applications 113(3), 6–9. DOI: 10.5120/19804-1586
- url: https://doi.org/10.5120/19804-1586
- dostęp: 23.10.2026
- potwierdza: wyprowadzenie kinematyki prostej i odwrotnej platformy z czterema kołami Mecanum; osiem ruchów bez zmiany orientacji; model odwrotny wiąże prędkości kół z prędkością platformy przy założeniu braku poślizgu rolek (abstrakt, rozdz. 2, eq. 14–16)

## kaemarungsi2004
- typ: referat konferencyjny
- status: zweryfikowane
- opis: Kaemarungsi, K., Krishnamurthy, P., 2004. Properties of indoor received signal strength for WLAN location fingerprinting. First Annual International Conference on Mobile and Ubiquitous Systems: Networking and Services (MobiQuitous 2004), 14–23. DOI: 10.1109/MOBIQ.2004.1331706
- url: https://doi.org/10.1109/MOBIQ.2004.1331706
- dostęp: 23.10.2026
- potwierdza: analiza właściwości RSSI z kart IEEE 802.11b w pomieszczeniach; porównanie dopasowania modelu Gaussa do danych zmierzonych (abstrakt)

## shepard1968
- typ: referat konferencyjny
- status: zweryfikowane
- opis: Shepard, D., 1968. A two-dimensional interpolation function for irregularly-spaced data. Proceedings of the 1968 23rd ACM National Conference, 517–524. DOI: 10.1145/800186.810616
- url: https://doi.org/10.1145/800186.810616
- dostęp: 23.10.2026
- potwierdza: metoda interpolacji danych nieregularnie rozmieszczonych do ciągłej powierzchni — źródłowy opis ważenia odwrotną odległością (IDW) (abstrakt)

## ferris2006
- typ: referat konferencyjny
- status: zweryfikowane
- opis: Ferris, B., Hähnel, D., Fox, D., 2006. Gaussian Processes for Signal Strength-Based Location Estimation. Proceedings of Robotics: Science and Systems II. DOI: 10.15607/RSS.2006.II.039
- url: https://www.roboticsproceedings.org/rss02/p39.html
- dostęp: 23.10.2026
- potwierdza: proces gaussowski jako model poziomu sygnału w przestrzeni; szum pomiaru i korelację przestrzenną wyznacza się z danych jako hiperparametry (abstrakt)

## lebreton2016
- typ: referat konferencyjny
- status: zweryfikowane
- opis: Lebreton, J. M., Murad, N., Lorion, R., 2016. Radio Frequency Mapping using an Autonomous Robot: Application to the 2.4 GHz Band. IOP Conference Series: Materials Science and Engineering 120, 012001. DOI: 10.1088/1757-899X/120/1/012001
- url: https://doi.org/10.1088/1757-899X/120/1/012001
- dostęp: 23.10.2026
- potwierdza: autonomiczny robot budujący mapę pola RF w paśmie 2,4 GHz; dopasowanie pomiarów do modelu tłumienia sygnału; pomiar ręczny jako stan obecny (abstrakt)

## wakim2017
- typ: referat konferencyjny
- status: zweryfikowane
- opis: Wakim, R., Weitzen, J. A., 2017. An autonomous system for high-resolution mapping of indoor wireless coverage. 2017 IEEE 28th Annual International Symposium on Personal, Indoor, and Mobile Radio Communications (PIMRC), 1–5. DOI: 10.1109/PIMRC.2017.8292327
- url: https://doi.org/10.1109/PIMRC.2017.8292327
- dostęp: 23.10.2026
- potwierdza: autonomiczny robot mapujący pokrycie wewnątrz budynków; pomiar ręczny wymaga chodzenia i ręcznego zapisu położenia; robot sam wyznacza położenie względem mapy budynku i nakłada metryki (SNR, RSRP, CQI) na tę mapę (abstrakt)

## zou2020
- typ: artykuł w czasopiśmie
- status: zweryfikowane
- opis: Zou, H., Chen, C., Li, M., Yang, J., Zhou, Y., Xie, L., Spanos, C. J., 2020. Adversarial Learning-Enabled Automatic WiFi Indoor Radio Map Construction and Adaptation With Mobile Robot. IEEE Internet of Things Journal 7(8), 6946–6954. DOI: 10.1109/JIOT.2020.2979413
- url: https://doi.org/10.1109/JIOT.2020.2979413
- dostęp: 23.10.2026
- potwierdza: mobilny robot budujący jednocześnie mapę przestrzeni i mapę radiową Wi-Fi; regresja procesem gaussowskim (GPR); koszt ręcznej budowy gęstej mapy radiowej jako główna bariera (abstrakt)

## kim2010
- typ: referat konferencyjny
- status: zweryfikowane
- opis: Kim, K.-H., Min, A. W., Shin, K. G., 2010. Sybot: An Adaptive and Mobile Spectrum Survey System for WiFi Networks. Proceedings of the 16th Annual International Conference on Mobile Computing and Networking (MobiCom 2010), 293–304. DOI: 10.1145/1859995.1860029
- url: https://doi.org/10.1145/1859995.1860029
- dostęp: 23.10.2026
- potwierdza: robot do pomiaru widma sieci Wi-Fi; ujmuje zmiany przestrzenno-czasowe RSS; sam dobiera czas pomiaru i rozdzielczość przestrzenną w danym miejscu (abstrakt)

## hapsari2012
- typ: artykuł w czasopiśmie
- status: zweryfikowane
- opis: Hapsari, W. A., Umesh, A., Iwamura, M., Tomala, M., Gyula, B., Sebire, B., 2012. Minimization of drive tests solution in 3GPP. IEEE Communications Magazine 50(6), 28–36. DOI: 10.1109/MCOM.2012.6211483
- url: https://doi.org/10.1109/MCOM.2012.6211483
- dostęp: 23.10.2026
- potwierdza: minimalizacja testów jezdnych (MDT) w 3GPP — automatyzacja zbierania pomiarów sieci komórkowej zamiast pomiaru ręcznego (tytuł, dane Crossref: tom 50, nr 6, s. 28–36)

## cressie1990
- typ: artykuł w czasopiśmie
- status: zweryfikowane
- opis: Cressie, N., 1990. The origins of kriging. Mathematical Geology 22(3), 239–252. DOI: 10.1007/BF00889887
- url: https://doi.org/10.1007/BF00889887
- dostęp: 23.10.2026
- potwierdza: kriging jako geostatystyczna metoda interpolacji przestrzennej; pochodzenie i formalizacja metody (tytuł, dane Crossref/OpenAlex)

## slamtec_a1
- typ: dokumentacja / karta katalogowa
- status: zweryfikowane
- opis: RPLIDAR A1 Low Cost 360 Degree Laser Range Scanner – Introduction and Datasheet, Model A1M8, rev. 3.0, SLAMTEC. Parametry potwierdzone na oficjalnej stronie: RPLIDAR-A1 Laser Range Scanner Parameters, SLAMTEC, https://www.slamtec.com/en/lidar/a1spec (dostęp 23.10.2026)
- url: https://www.slamtec.com/en/lidar/a1spec
- dostęp: 23.10.2026
- potwierdza: zasięg 0,15–12 m, zakres kątowy 360°, rozdzielczość kątowa ≤1°, prędkość obrotowa 5,5 Hz, wyjście UART 3,3 V, zasilanie 5 V (tabela parametrów na stronie SLAMTEC)
