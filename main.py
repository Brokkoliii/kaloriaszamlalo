import tkinter as tk
from datetime import datetime
import os

# Az étel osztály, amely tárolja az étel nevét és kalóriatartalmát
class Etel:
    def __init__(self, nev, kaloria):
        self.nev = nev
        self.kaloria = kaloria

# Függvény a teljes kalória kiszámításához a megadott ételek listájából
def osszkaloria_szamolasa(etelek):
    ossz_kaloria = sum(etel.kaloria for etel in etelek)
    return ossz_kaloria

# Függvény az étel hozzáadásához a megadott név és kalória alapján
def etel_hozzaadasa():
    nev = bevitel_nev.get()
    kaloria = int(bevitel_kaloria.get())
    etel = Etel(nev, kaloria)
    etelek.append(etel)
    frissites_megjelenites()

# Függvény a kijelölt étel törléséhez a listából
def kijelolt_etel_torlese():
    kijelolt_indexek = lista_boksz.curselection()
    for index in kijelolt_indexek:
        etelek.pop(index)
    frissites_megjelenites()

# Függvény a GUI frissítéséhez az étel listája alapján
def frissites_megjelenites():
    lista_boksz.delete(0, tk.END)
    for etel in etelek:
        lista_boksz.insert(tk.END, f"{etel.nev}: {etel.kaloria} kalória")
    ossz_kaloria = osszkaloria_szamolasa(etelek)
    ossz_kaloria_cimke.config(text=f"Összes kalória: {ossz_kaloria}")

# Függvény az ételadatok mentéséhez txt fájlba az aznapi dátummal ellátott névvel
def mentes():
    # Aznapi dátum lekérése
    datum = datetime.now().strftime("%Y-%m-%d")
    fajlnev = f"mentes_{datum}.txt"

    with open(fajlnev, 'w') as f:
        for etel in etelek:
            f.write(f"{etel.nev},{etel.kaloria}\n")
    print(f"Az adatok mentése megtörtént: {fajlnev}")

# Függvény az ételadatok betöltéséhez txt fájlból az aznapi dátummal ellátott névvel
def betoltes():
    # Aznapi dátum lekérése
    datum = datetime.now().strftime("%Y-%m-%d")
    fajlnev = f"mentes_{datum}.txt"

    if os.path.exists(fajlnev):
        with open(fajlnev, 'r') as f:
            etelek.clear()
            for sor in f:
                nev, kaloria = sor.strip().split(',')
                etel = Etel(nev, int(kaloria))
                etelek.append(etel)
        frissites_megjelenites()
        print(f"Az adatok betöltése megtörtént: {fajlnev}")
    else:
        print(f"Nincs mentett adat a mai napra: {fajlnev}")

# Kezdeti étel lista
etelek = []

# Tkinter főablak létrehozása
foablak = tk.Tk()
foablak.title("Élelmiszer Kalória Kalkulátor")

# GUI elemek létrehozása és elrendezése
cimke_nev = tk.Label(foablak, text="Étel neve:")
cimke_nev.pack()

bevitel_nev = tk.Entry(foablak)
bevitel_nev.pack()

cimke_kaloria = tk.Label(foablak, text="Kalória mennyisége:")
cimke_kaloria.pack()

bevitel_kaloria = tk.Entry(foablak)
bevitel_kaloria.pack()

hozzaadas_gomb = tk.Button(foablak, text="Hozzáadás", command=etel_hozzaadasa)
hozzaadas_gomb.pack()

torles_gomb = tk.Button(foablak, text="Kijelölt étel törlése", command=kijelolt_etel_torlese)
torles_gomb.pack()

mentes_gomb = tk.Button(foablak, text="Mentés", command=mentes)
mentes_gomb.pack()

betoltes_gomb = tk.Button(foablak, text="Betöltés", command=betoltes)
betoltes_gomb.pack()

lista_boksz = tk.Listbox(foablak)
lista_boksz.pack()

ossz_kaloria_cimke = tk.Label(foablak, text="Összes kalória: 0")
ossz_kaloria_cimke.pack()

# Tkinter főciklus
foablak.mainloop()
