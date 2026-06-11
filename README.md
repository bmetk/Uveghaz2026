Statikus IP-címek (dlink-E2CC - a projekt saját routere):
- Raspberry Pi 4: 192.168.10.193
- Raspberry Pi 3: 192.168.10.177

Beindítás:
- Kapcsold be a két Pi-t!
- Futtasd az asztalon található "Greenhouse Monitoring" nevezetű fájlt!
- Ha megnyílt a két böngészős oldal (vezérlés és monitorozás), akkor az Alt gombot lenyomva kattints rá a másik tab-ra a böngészőben, így osztott képrenyőben megjelenik a két felület.
- Az egeret vidd közére és húzd a képernyőelosztást balra, amíg a vezérlési felület kitölti a képernyőt!
- Tedd F11-el teljes képrenyőre!

Funkciók:
- A vezérlési felületen a bal felső sarokban lévő menüben tudsz váltani az automatizációs és a manuális vezérlési felületek között.
- Manuális vezérlés:
  -   A manuális vezérlési felületen a "Day Simulation" blokkban tudod elindítani/megállítani a napszimulációt.
  -   A szimuláció folyamatosan megy, amíg meg nem állítod.
  -   A szimuláció sebességét folyamatosan lehet állítani, akár futás közben is.
  -   A "reset" gombbal minden beavatkozót alaphelyzetbe tudsz állítani.
  -   A többi blokkban manuálisan tudo vezérelni az egyes beavatkozókat. Ilyenkor kapcsold ki a napszimulációt és az automatizációt is.
  - Automatizáció:
  -   Az automatizációs felületen be/ki tudod kapcsolni ezt a funkciót.
  -   Ha a mezőket nem írod át akkor a bennük látható alapértékek szerint szabályozza magát a makett.
  -   A Daylight Start és Daylight End mezők segítségével azt tudod megadni, hogy meddig tart a nappali időszak.
  -   Este hűvösebbre engedi a hőmérsékletet az automatizáció és nem kapcsolja be a fényeket.
  -   Napi egyszer locsol, ha a beállítot érték alatt van a talajnedvesség.
  -   Óránként 10 percen át keringeti a levegőt.
