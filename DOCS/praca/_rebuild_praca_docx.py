# -*- coding: utf-8 -*-
"""Przebudowa PRACA INŻYNIERSKA.docx wg instrukcji promotora (formatowanie).
Treść: rozdział 3 (przegląd) + Literatura. Bez strony tytułowej WIMiIP.
3.6: wkład FARO — autonomia/SLAM jako rdzeń, Wi-Fi jako demonstracja.
"""
from __future__ import annotations

import shutil
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "PRACA INŻYNIERSKA.docx"
BACKUP = ROOT / "PRACA INŻYNIERSKA.backup-przed-formatowaniem.docx"

# Kolejność pierwszego cytowania w rozdziale 3
LIT = [
    "Lebreton, J. M., Murad, N., Lorion, R., 2016. Radio Frequency Mapping using an Autonomous Robot: Application to the 2.4 GHz Band. IOP Conference Series: Materials Science and Engineering 120, 012001. DOI: 10.1088/1757-899X/120/1/012001",
    "Wakim, R., Weitzen, J. A., 2017. An autonomous system for high-resolution mapping of indoor wireless coverage. 2017 IEEE 28th Annual International Symposium on Personal, Indoor, and Mobile Radio Communications (PIMRC), 1–5. DOI: 10.1109/PIMRC.2017.8292327",
    "Durrant-Whyte, H., Bailey, T., 2006. Simultaneous localization and mapping: part I. IEEE Robotics & Automation Magazine 13(2), 99–110. DOI: 10.1109/MRA.2006.1638022",
    "Grisetti, G., Stachniss, C., Burgard, W., 2007. Improved Techniques for Grid Mapping With Rao-Blackwellized Particle Filters. IEEE Transactions on Robotics 23(1), 34–46. DOI: 10.1109/TRO.2006.889486",
    "Hess, W., Kohler, D., Rapp, H., Andor, D., 2016. Real-time loop closure in 2D LIDAR SLAM. 2016 IEEE International Conference on Robotics and Automation (ICRA), 1271–1278. DOI: 10.1109/ICRA.2016.7487258",
    "Macenski, S., Jambrecic, I., 2021. SLAM Toolbox: SLAM for the dynamic world. Journal of Open Source Software 6(61), 2783. DOI: 10.21105/joss.02783",
    "RPLIDAR A1 Low Cost 360 Degree Laser Range Scanner – Introduction and Datasheet, Model A1M8, rev. 3.0, SLAMTEC; parametry: RPLIDAR-A1 Laser Range Scanner Parameters, SLAMTEC, https://www.slamtec.com/en/lidar/a1spec (dostęp 23.10.2026)",
    "Taheri, H., Qiao, B., Ghaeminezhad, N., 2015. Kinematic Model of a Four Mecanum Wheeled Mobile Robot. International Journal of Computer Applications 113(3), 6–9. DOI: 10.5120/19804-1586",
    "Kaemarungsi, K., Krishnamurthy, P., 2004. Properties of indoor received signal strength for WLAN location fingerprinting. First Annual International Conference on Mobile and Ubiquitous Systems: Networking and Services (MobiQuitous 2004), 14–23. DOI: 10.1109/MOBIQ.2004.1331706",
    "Hapsari, W. A., Umesh, A., Iwamura, M., Tomala, M., Gyula, B., Sebire, B., 2012. Minimization of drive tests solution in 3GPP. IEEE Communications Magazine 50(6), 28–36. DOI: 10.1109/MCOM.2012.6211483",
    "Shepard, D., 1968. A two-dimensional interpolation function for irregularly-spaced data. Proceedings of the 1968 23rd ACM National Conference, 517–524. DOI: 10.1145/800186.810616",
    "Cressie, N., 1990. The origins of kriging. Mathematical Geology 22(3), 239–252. DOI: 10.1007/BF00889887",
    "Ferris, B., Hähnel, D., Fox, D., 2006. Gaussian Processes for Signal Strength-Based Location Estimation. Proceedings of Robotics: Science and Systems II. DOI: 10.15607/RSS.2006.II.039",
    "Kim, K.-H., Min, A. W., Shin, K. G., 2010. Sybot: An Adaptive and Mobile Spectrum Survey System for WiFi Networks. Proceedings of the 16th Annual International Conference on Mobile Computing and Networking (MobiCom 2010), 293–304. DOI: 10.1145/1859995.1860029",
    "Zou, H., Chen, C., Li, M., Yang, J., Zhou, Y., Xie, L., Spanos, C. J., 2020. Adversarial Learning-Enabled Automatic WiFi Indoor Radio Map Construction and Adaptation With Mobile Robot. IEEE Internet of Things Journal 7(8), 6946–6954. DOI: 10.1109/JIOT.2020.2979413",
]


def set_run_font(run, size=12, bold=False, italic=False):
    run.font.name = "Times New Roman"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic


def configure_styles(doc: Document) -> None:
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    pf = normal.paragraph_format
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    pf.first_line_indent = Cm(1)
    pf.space_after = Pt(0)
    pf.space_before = Pt(0)

    for style_name, size, bold in (("Heading 1", 14, True), ("Heading 2", 12, True)):
        st = doc.styles[style_name]
        st.font.name = "Times New Roman"
        st.font.size = Pt(size)
        st.font.bold = bold
        st._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
        sp = st.paragraph_format
        sp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        sp.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
        sp.first_line_indent = Cm(0)
        sp.space_before = Pt(12 if style_name == "Heading 2" else 0)
        sp.space_after = Pt(6)


def add_body(doc, text: str, *, first_indent: bool = True) -> None:
    p = doc.add_paragraph(style="Normal")
    p.paragraph_format.first_line_indent = Cm(1 if first_indent else 0)
    run = p.add_run(text)
    set_run_font(run)


def add_h1(doc, text: str) -> None:
    p = doc.add_paragraph(text, style="Heading 1")
    for run in p.runs:
        set_run_font(run, size=14, bold=True)


def add_h2(doc, text: str) -> None:
    p = doc.add_paragraph(text, style="Heading 2")
    for run in p.runs:
        set_run_font(run, size=12, bold=True)


def add_caption(doc, text: str) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run(text)
    set_run_font(run, size=10)


def add_source(doc, text: str) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(text)
    set_run_font(run, size=10, italic=True)


def add_formula_block(doc, lines: list[str], number: str) -> None:
    for line in lines:
        p = doc.add_paragraph()
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
        p.paragraph_format.first_line_indent = Cm(0)
        run = p.add_run(line)
        set_run_font(run, italic=True)
    p = doc.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    p.paragraph_format.first_line_indent = Cm(0)
    run = p.add_run(f"({number})")
    set_run_font(run)


def add_table(doc, headers: list[str], rows: list[list[str]]) -> None:
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        run = cell.paragraphs[0].add_run(h)
        set_run_font(run, size=10, bold=True)
    for r_i, row in enumerate(rows):
        for c_i, val in enumerate(row):
            cell = table.rows[r_i + 1].cells[c_i]
            cell.text = ""
            run = cell.paragraphs[0].add_run(val)
            set_run_font(run, size=10)


def add_lit_item(doc, n: int, text: str) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Cm(0.75)
    p.paragraph_format.first_line_indent = Cm(-0.75)
    run = p.add_run(f"[{n}] {text}")
    set_run_font(run, size=10)


def build() -> None:
    if OUT.exists():
        shutil.copy2(OUT, BACKUP)

    doc = Document()
    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(2)
        section.bottom_margin = Cm(2)
        section.left_margin = Cm(2)
        section.right_margin = Cm(2)

    configure_styles(doc)

    add_body(
        doc,
        "Dokument roboczy projektu dyplomowego. Poniżej zamieszczono rozdział 3 "
        "(przegląd literatury i dotychczasowych rozwiązań) oraz listę literatury. "
        "Stronę tytułową należy wstawić z oficjalnego wzoru WIMiIP. Cytowania zapisano "
        "jako numery w nawiasach kwadratowych w kolejności pierwszego przywołania; "
        "w Wordzie należy je zamienić na przypisy końcowe (Odwołania → Wstaw przypis "
        "końcowy) i ująć znak przypisu w nawiasy kwadratowe. Wzory (3.1) i (3.2) są "
        "zapisane tekstowo — w wersji końcowej należy je przepisać w edytorze równań.",
        first_indent=False,
    )

    add_h1(doc, "3. Przegląd literatury i dotychczasowych rozwiązań")

    add_body(
        doc,
        "Pomiary parametrów w budynkach, na przykład pokrycia sieci "
        "bezprzewodowej, wykonuje się zwykle ręcznie. Operator obchodzi "
        "pomieszczenia i zapisuje wynik razem z położeniem [1, 2]. "
        "Automatyzacja tego obchodu polega na tym, że układ mobilny powtarza "
        "pomiar i sam przypisuje mu współrzędne na mapie. Ten sam zapis "
        "położenia nie jest ograniczony do sieci Wi-Fi. Na mapę można nałożyć "
        "odczyt innego czujnika, na przykład czujnika dymu. Jeden przejazd "
        "zastępuje wtedy ręczny obchód i daje zapis, który da się powtórzyć "
        "po zmianie czujnika.",
    )
    add_body(
        doc,
        "Mapę nieznanego pomieszczenia i położenie na niej wyznacza jednoczesna "
        "lokalizacja i budowa mapy (ang. simultaneous localization and mapping, "
        "SLAM). Układ buduje geometrię otoczenia z odczytów czujników "
        "i jednocześnie ustala własne położenie, bez wcześniej przygotowanego "
        "planu pomieszczenia [3]. Rozdział omawia tę metodę (podrozdział 3.1), "
        "kinematykę platformy kołowej (3.2), pomiar jakości sieci Wi-Fi (3.3), "
        "interpolację pomiarów punktowych (3.4) oraz roboty, które już "
        "automatycznie mierzyły pokrycie radiowe (3.5).",
    )

    # --- 3.1 (wersja dopracowana) ---
    add_h2(doc, "3.1. Lokalizacja i mapowanie robotów mobilnych")
    add_body(
        doc,
        "W pomieszczeniach metodę SLAM realizuje się najczęściej w dwóch "
        "wymiarach, na podstawie skanu w jednej płaszczyźnie. Metody SLAM "
        "dzielą się na dwie główne rodziny. Pierwsza opiera się na "
        "filtrze cząsteczkowym. W podejściu Rao-Blackwella każda cząsteczka niesie "
        "własną mapę i trajektorię robota. Liczbę cząsteczek ogranicza się przez "
        "rozkład propozycji uwzględniający ostatni odczyt skanera oraz przez "
        "selektywne ponowne próbkowanie [4]. Implementacją tej rodziny jest "
        "GMapping [4]. Druga rodzina sprowadza SLAM do optymalizacji grafu pozycji. "
        "Krawędzie grafu odpowiadają dopasowaniu kolejnych skanów. Domknięcie pętli "
        "(ang. loop closure) koryguje narastający błąd po powrocie robota "
        "w odwiedzone miejsce. Cartographer wyznacza takie domknięcia w czasie "
        "rzeczywistym. Algorytm dopasowuje skany do podmap metodą podziału "
        "i ograniczeń (ang. branch and bound) przy rozdzielczości mapy 5 cm "
        "i ograniczonych zasobach obliczeniowych [5]. Pakiet slam_toolbox buduje "
        "i aktualizuje mapy dużych, zmieniających się przestrzeni i jest stosowany "
        "do SLAM 2D w systemie ROS 2 [6].",
    )
    add_body(
        doc,
        "Otoczenie reprezentuje się najczęściej jako mapa zajętości (ang. occupancy "
        "grid), czyli siatka komórek z prawdopodobieństwem zajęcia przez przeszkodę "
        "[4]. Dane do mapy dostarcza skaner laserowy. W pracy przyjęto lidar "
        "RPLIDAR A1M8. Urządzenie skanuje otoczenie w zakresie 360° z zasięgiem "
        "0,15–12 m, rozdzielczością kątową ≤1° i prędkością obrotową 5,5 Hz. "
        "Wyniki przesyła interfejsem UART 3,3 V [7]. Parametry te wyznaczają "
        "gęstość i zasięg pojedynczego skanu wykorzystywanego przez algorytm SLAM.",
    )
    add_body(doc, "Tabela 3.1 zestawia trzy implementacje SLAM 2D rozważane w pracy.")
    add_caption(doc, "Tabela 3.1. Porównanie rozważanych implementacji SLAM 2D z lidarem")
    add_table(
        doc,
        ["Implementacja", "Rodzina metody", "Domykanie pętli", "Źródło"],
        [
            ["GMapping", "filtr cząsteczkowy Rao-Blackwella", "niejawne, w filtrze", "[4]"],
            ["Cartographer", "optymalizacja grafu, dopasowanie skanów", "jawne, branch and bound", "[5]"],
            ["slam_toolbox", "optymalizacja grafu, ROS 2", "jawne", "[6]"],
        ],
    )
    add_source(doc, "Źródło: opracowanie własne na podstawie [4, 5, 6]")
    add_body(
        doc,
        "Dla FARO istotne jest, że SLAM 2D z lidarem działa na skanie płaskim "
        "i nie wymaga kamery ani znaczników w otoczeniu. Wybór implementacji "
        "spośród zestawionych w tabeli 3.1 zależy od zasobów Raspberry Pi 3 "
        "i integracji z resztą oprogramowania. Zagadnienie to należy do rozdziału 5.",
    )

    # --- 3.2 ---
    add_h2(doc, "3.2. Kinematyka i odometria platform z kołami Mecanum")
    add_body(
        doc,
        "Platforma FARO jeździ na czterech kołach Mecanum (ang. Mecanum wheels), "
        "których obwód tworzą swobodne rolki ustawione pod kątem 45°. Taki układ "
        "pozwala przesuwać się do przodu, w bok i obracać w miejscu bez skręcania "
        "kół, co daje osiem kierunków ruchu bez zmiany orientacji platformy [8]. "
        "Zależność prędkości kątowych kół od zadanej prędkości platformy opisuje "
        "odwrotny model kinematyczny (3.1) [8]:",
    )
    add_formula_block(
        doc,
        [
            "[ω₁ ω₂ ω₃ ω₄]ᵀ = (1/r) · M · [vₓ vᵧ ω_z]ᵀ,",
            "wiersze macierzy M: [1, −1, −(lₓ+lᵧ)], [1, 1, (lₓ+lᵧ)],",
            "[1, 1, −(lₓ+lᵧ)], [1, −1, (lₓ+lᵧ)].",
        ],
        "3.1",
    )
    add_body(
        doc,
        "gdzie: ω₁…ω₄ – prędkości kątowe czterech kół [rad/s], vₓ, vᵧ – prędkości "
        "liniowe platformy wzdłuż i w poprzek kierunku jazdy [m/s], ω_z – prędkość "
        "kątowa platformy [rad/s], r – promień koła [m], lₓ, lᵧ – połowa rozstawu "
        "osi i połowa rozstawu kół [m]. Znaki w macierzy zależą od przyjętej "
        "numeracji kół i orientacji rolek; pełne wyprowadzenie podano w [8].",
        first_indent=False,
    )
    add_body(
        doc,
        "Model (3.1) zakłada brak poślizgu rolek o podłoże [8]. W rzeczywistości "
        "rolki się ślizgają, a odometria (wyznaczanie położenia przez całkowanie "
        "przemieszczeń kół) kumuluje wtedy błąd rosnący z przebytą drogą. Z tego "
        "powodu położenie robota wyznacza SLAM, a odometria służy jako wejście "
        "predykcyjne algorytmu [3]. Model (3.1) jest podstawą sterowania napędem "
        "opisanego w rozdziale 5.",
    )

    # --- 3.3 ---
    add_h2(doc, "3.3. Pomiar jakości sieci Wi-Fi")
    add_body(
        doc,
        "Jakość połączenia radiowego opisuje najczęściej wskaźnik poziomu "
        "odbieranego sygnału (ang. received signal strength indicator, RSSI), "
        "podawany w dBm [9]. RSSI mierzony w jednym miejscu nie jest stały, "
        "a jego rozkład w pomieszczeniu bywa przybliżany modelem Gaussa [9]. "
        "Pojedynczy odczyt nie wystarcza zatem do opisu punktu; w każdym punkcie "
        "pomiarowym pobiera się serię próbek i zapisuje ich średnią oraz "
        "odchylenie standardowe. Poza RSSI jakość połączenia opisują też "
        "przepustowość, opóźnienie i utrata pakietów.",
    )
    add_body(
        doc,
        "Pokrycie sieci sprawdza się dziś głównie ręcznie: osoba z odbiornikiem "
        "obchodzi pomieszczenia i zapisuje poziom sygnału wraz z położeniem "
        "[1, 2]. Proces jest czasochłonny, a jego rozdzielczość i dokładność "
        "zależą od operatora [2]. W sieciach komórkowych pomiary "
        "zautomatyzowano w ramach minimalizacji testów jezdnych (ang. "
        "minimization of drive tests, MDT), w której dane zbierają same "
        "terminale abonenckie zamiast operatora z miernikiem [10].",
    )
    add_body(
        doc,
        "Dla FARO wynika z tego procedura pomiaru: robot zatrzymuje się "
        "w punkcie, pobiera serię próbek RSSI i zapisuje położenie odczytane "
        "z mapy SLAM wraz ze statystykami sygnału. Procedurę i format danych "
        "opisuje rozdział 6.",
    )

    # --- 3.4 ---
    add_h2(doc, "3.4. Interpolacja przestrzenna pomiarów")
    add_body(
        doc,
        "Pomiar daje wartości sygnału tylko w skończonej liczbie punktów, "
        "a mapa pokrycia wymaga wartości w całym pomieszczeniu, dlatego "
        "stosuje się interpolację przestrzenną. Najprostszą metodą jest "
        "ważenie odwrotną odległością (ang. inverse distance weighting, IDW), "
        "w którym wartość w punkcie szukanym jest średnią ważoną pomiarów, "
        "a wagi maleją z odległością, co opisuje wzór (3.2) [11]:",
    )
    add_formula_block(
        doc,
        ["ẑ(x₀) = Σ wᵢ zᵢ / Σ wᵢ ,   wᵢ = 1 / d(x₀, xᵢ)^p"],
        "3.2",
    )
    add_body(
        doc,
        "gdzie: ẑ(x₀) – wartość interpolowana w punkcie x₀, zᵢ – wartość "
        "zmierzona w punkcie xᵢ, d(x₀, xᵢ) – odległość między punktami [m], "
        "p – wykładnik wagi. Jako interpolator dokładny IDW odtwarza "
        "w punktach pomiarowych wartości zmierzone i nie rozdziela sygnału "
        "od szumu pomiaru [11].",
        first_indent=False,
    )
    add_body(
        doc,
        "Kriging i proces gaussowski uwzględniają korelację przestrzenną "
        "danych. Kriging, metoda wywodząca się z geostatystyki, wyznacza "
        "wartość jako optymalną liniową kombinację pomiarów na podstawie "
        "przestrzennej struktury korelacji oszacowanej z danych [12]. Proces "
        "gaussowski (ang. Gaussian process, GP) opisuje sygnał jako realizację "
        "procesu losowego i pozwala wyznaczyć szum pomiaru oraz korelację "
        "przestrzenną z danych jako hiperparametry modelu [13]. Model GP "
        "zastosowano do szacowania poziomu sygnału Wi-Fi w [13].",
    )
    add_body(
        doc,
        "W odróżnieniu od IDW proces gaussowski jawnie ujmuje szum pomiaru "
        "jako osobny składnik modelu [13]; kriging ujmuje ten sam efekt przez "
        "tak zwany samorodek (ang. nugget). Jakość odtworzonej mapy ocenia się "
        "walidacją krzyżową, porównując wartości przewidziane z pomiarami "
        "w punktach pominiętych przy interpolacji, na przykład przez pierwiastek "
        "błędu średniokwadratowego (RMSE). W pracy porównano IDW z metodą "
        "uwzględniającą korelację przestrzenną, traktując szum RSSI jawnie; "
        "metodę interpolacji i jej ocenę przedstawia rozdział 6.",
    )

    # --- 3.5 ---
    add_h2(doc, "3.5. Roboty do automatycznego pomiaru pokrycia sieci")
    add_body(
        doc,
        "Autonomiczny pomiar pokrycia radiowego opisano w literaturze w kilku "
        "wariantach, zestawionych w tabeli 3.2. Lebreton i współautorzy "
        "zbudowali robota, który zbiera poziom sygnału w paśmie 2,4 GHz "
        "i dopasowuje pomiary do modelu tłumienia, tworząc mapę pola RF; "
        "jako stan wyjściowy wskazują pomiar ręczny [1]. Wakim i Weitzen "
        "opisali robota, który sam eksploruje obszar, wyznacza położenie "
        "względem mapy budynku i nakłada na nią metryki warstwy fizycznej, "
        "takie jak SNR, RSRP i CQI [2]. System Sybot mierzy parametry sieci "
        "Wi-Fi, ujmuje zmiany przestrzenno-czasowe sygnału i sam dobiera "
        "czas pomiaru oraz rozdzielczość przestrzenną w danym miejscu [14]. "
        "Zou i współautorzy połączyli budowę mapy przestrzeni i mapy radiowej "
        "Wi-Fi na jednym robocie mobilnym, stosując regresję procesem "
        "gaussowskim i wskazując koszt ręcznej budowy gęstej mapy radiowej "
        "jako główną barierę [15].",
    )
    add_caption(doc, "Tabela 3.2. Roboty do automatycznego pomiaru pokrycia radiowego")
    add_table(
        doc,
        ["Praca", "Źródło położenia", "Mierzona wielkość", "Odtworzenie mapy"],
        [
            ["[1]", "robot autonomiczny", "RSSI (2,4 GHz)", "model tłumienia"],
            ["[2]", "położenie względem mapy budynku", "SNR, RSRP, CQI", "nałożenie na mapę"],
            ["[14]", "robot mobilny (Sybot)", "RSSI Wi-Fi", "mapa parametrów, dobór gęstości"],
            ["[15]", "mapa przestrzeni z robota", "RSSI Wi-Fi", "regresja procesem gaussowskim"],
        ],
    )
    add_source(doc, "Źródło: opracowanie własne na podstawie [1, 2, 14, 15]")
    add_body(
        doc,
        "Wspólną cechą tych rozwiązań jest powiązanie każdego pomiaru "
        "z położeniem i odtworzenie ciągłej mapy z pomiarów punktowych. "
        "Różnią się one źródłem położenia oraz metodą odtworzenia mapy.",
    )

    # Literatura — bez 3.6. U Patrycji Szlachty przegląd kończy się opisem metody;
    # uzasadnienie wyboru należy do rozdziału „Cel i zakres”, nie do przeglądu.
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    add_h1(doc, "Literatura")
    add_body(
        doc,
        "Poniższa lista odpowiada kolejności pierwszego cytowania w rozdziale 3. "
        "W wersji oddawanej do APD pozycje należy przenieść do przypisów końcowych "
        "Worda zgodnie z instrukcją promotora.",
        first_indent=False,
    )
    for i, item in enumerate(LIT, start=1):
        add_lit_item(doc, i, item)

    try:
        doc.save(OUT)
        saved = OUT
    except PermissionError:
        saved = ROOT / "PRACA INŻYNIERSKA-poprawiona.docx"
        doc.save(saved)
        print("Plik oryginalny jest otwarty w Wordzie. Zapisano kopię:", saved)
    else:
        print("Zapisano:", saved)
    print("Backup:", BACKUP)
    print("Rozmiar:", saved.stat().st_size, "B")


if __name__ == "__main__":
    build()
