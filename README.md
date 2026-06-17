## Hálózati beállítások & Indítás

### 🌐 Statikus IP-címek
A projekt egy saját routerhez (**dlink-E2CC**) csatlakozik, amelyen az alábbi fix IP-címek vannak kiosztva:

* **Raspberry Pi 4:** `192.168.10.193`
* **Raspberry Pi 3:** `192.168.10.177`

### 🚀 Beindítási folyamat

A rendszer elindításához kövesd pontosan az alábbi lépéseket:

1. **Hardver indítása:** Kapcsold be mindkét Raspberry Pi-t.
2. **Szoftver futtatása:** Indítsd el az asztalon található `Greenhouse Monitoring` nevű fájlt.
3. **Képernyő felosztása:** 
    * Miután megnyílt a két böngészőlap (vezérlés és monitorozás), nyomd meg és tartsd lenyomva az `Alt` billentyűt.
    * Kattints a másik böngészőfülre (tab-ra) a két felület osztott képernyős megjelenítéséhez.
4. **Nézet igazítása:** Vidd az egeret a képernyő elválasztóvonalának közepére, majd húzd balra az elosztást addig, amíg a vezérlési felület teljesen ki nem tölti a kívánt részt.
5. **Teljes képernyő:** Nyomd meg az `F11` billentyűt a teljes képernyős mód (fullscreen) aktiválásához.

## Funkciók

A vezérlési felületen a bal felső sarokban lévő menüben tudsz váltani az automatizációs és a manuális vezérlési felületek között.

### 🎮 Manuális vezérlés
A manuális vezérlési felületen az egyes beavatkozókat teljesen önállóan irányíthatod. 
*⚠️ Fontos: Manuális vezérlés közben kapcsold ki a napszimulációt és az automatizációt is!*

* **Day Simulation (Napszimuláció) blokk**
    * **Indítás/Megállítás:** Itt tudod elindítani vagy leállítani a napszimulációt.
    * **Folyamatos futás:** A szimuláció megszakítás nélkül megy, amíg manuálisan meg nem állítod.
    * **Sebességállítás:** A szimuláció sebessége futás közben is bármikor, folyamatosan módosítható.
* **Alaphelyzet gomb**
    * A **Reset** gomb megnyomásával minden beavatkozót azonnal alaphelyzetbe tudsz állítani.
* **Egyéb blokkok**
    * A felület többi részén az egyes beavatkozók közvetlen, manuális vezérlésére van lehetőséged.

### 🤖 Automatizáció
Az automatizációs felületen a makett önálló szabályozását tudod kezelni és testreszabni.

* **Funkció kapcsoló:** Az automatizációs felületen tetszőlegesen be- és kikapcsolható a funkció.
* **Alapértékek:** Ha a mezőket nem írod át, a rendszer a bennük látható gyári alapértékek szerint szabályozza magát.
* **Időzítések és Szabályok:**
    * **Nappali időszak:** A *Daylight Start* és *Daylight End* mezők segítségével pontosan megadható a nappali időszak kezdete és vége.
    * **Éjszakai üzemmód:** Este az automatizáció hűvösebbre engedi a hőmérsékletet, és a fényeket sem kapcsolja be.
    * **Locsolás:** Napi egy alkalommal öntöz a rendszer, de csak akkor, ha a talajnedvesség a beállított érték alá süllyed.
    * **Légkeringetés:** A rendszer óránként 10 percen keresztül automatikusan keringeti a levegőt.

---

## 📊 Felületek elérése & Beállítások

### 📈 Grafana (Monitorozó felület)
A mérési adatok vizuális megjelenítésére a Grafana dashboard szolgál.

* **Elérhetőség:** `http://192.168.10.193:3000` (Raspberry Pi 4 IP-címe : 3000)
* **Hitelesítési adatok:**
  * **Felhasználónév:** `admin`
  * **Jelszó:** `admin`

**A dashboard megnyitásának lépései:**
1. Jelentkezz be a megadott adatokkal.
2. Kattints a bal felső sarokban található **Menü** (☰) ikonra.
3. Válaszd ki a **Dashboards** menüpontot.
4. Kattints a **Greenhouse Sensors** nevű dashboardra a monitorozó felület megjelenítéséhez.

---

### 🗄️ InfluxDB (Adatbázis felület)
A nyers adatok ellenőrzésére és egyedi lekérdezésekre az InfluxDB felülete használható.

* **Elérhetőség:** [http://192.168.10.193:8086](http://192.168.10.193:8086)
* **Hitelesítési adatok:**
  * **Felhasználónév:** `Uveghaz`
  * **Jelszó:** `UveghazProject`
* **⚠️ Adattárolási szabály:** Az adatbázis úgy van konfigurálva, hogy automatikusan csak az **elmúlt 7 nap** mérési adatait őrzi meg és tárolja.

**Adatok lekérdezése és grafikon rajzolása:**
1. Jelentkezz be, majd a bal oldali menüsávból válaszd ki a **Data Explorer** lehetőséget.
2. A szűrők között (Filter) válaszd ki a `greenhouse/measurements` opciót.
3. Az ezután megjelenő új szűrőpanelen válaszd ki a megtekinteni kívánt **üvegházi paramétereket** (pl. hőmérséklet, páratartalom).
4. Igény szerint állítsd be a jobb felső sarokban, hogy az **elmúlt mennyi idő** adatait szeretnéd látni.
5. Kattints a <kbd>Submit</kbd> gombra a grafikon kirajzolásához.
