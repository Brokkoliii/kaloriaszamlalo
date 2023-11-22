# Élelmiszer Kalória Kalkulátor

## Hallgató neve
* Juhász Marcell

## Projekt Leírás

Ez a projekt egy egyszerű Élelmiszer Kalória Kalkulátort implementál, amelynek felülete Tkinter segítségével van létrehozva. A program lehetővé teszi az ételnevek és kalóriatartalmak rögzítését, az összes kalória kiszámítását, az étel törlését a listából, valamint az adatok mentését és betöltését az aznapi dátummal ellátott txt fájlból.

## Felhasznált Modulok és Függvények

### Tkinter Modul
- `Tk`: A főablak létrehozásához.
- `Label`: Címkék megjelenítéséhez.
- `Entry`: Szövegbeviteli mezők készítéséhez.
- `Button`: Gombok készítéséhez.

### Datetime Modul
- `datetime`: Az aktuális dátum és idő lekérdezéséhez.

### OS Modul
- `path`: Fájlkezelési műveletek végrehajtásához.

### `Etel` Osztály
- `__init__(self, nev, kaloria)`: Étel nevének és kalóriatartalmának inicializálása.

### Fő Funkciók
- `osszkaloria_szamolasa(etelek)`: Ételobjektumok listájának összkalóriájának kiszámítása.
- `etel_hozzaadasa()`: Új étel hozzáadása a listához és a felület frissítése.
- `kijelolt_etel_torlese()`: Kijelölt étel törlése a listából és a felület frissítése.
- `frissites_megjelenites()`: A felület frissítése az aktuális ételadatok alapján.

### Mentés és Betöltés
- `mentes()`: Ételadatok mentése txt fájlba az aznapi dátummal ellátott névvel.
- `betoltes()`: Ételadatok betöltése txt fájlból az aznapi dátummal ellátott névvel.
