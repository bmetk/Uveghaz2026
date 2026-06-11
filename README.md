Statikus IP-címek (dlink-E2CC - a projekt saját routere):
- Raspberry Pi 4: 192.168.10.193
- Raspberry Pi 3: 192.168.10.177

Beindítás:
- Kapcsold be a két Pi-t!
- Futtasd az asztalon található "Greenhouse Monitoring" nevezetű fájlt!
- Ha megnyílt a két böngészős oldal (vezérlés és monitorozás), akkor az Alt gombot lenyomva kattints rá a másik tab-ra a böngészőben, így osztott képrenyőben megjelenik a két felület.
- Az egeret vidd közére és húzd a képernyőelosztást balra, amíg a vezérlési felület kitölti a képernyőt!
- Tedd F11-el teljes képrenyőre!

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
