# A program kezdő beállításai
korongok = []

def tabla_megjelenites():
    tabla = [["." for _ in range(8)] for _ in range(8)]
    for korong in korongok:
        sor = int(korong[0])
        oszlop = int(korong[2])
        tabla[sor - 1][oszlop - 1] = "O"
    for sor in tabla:
        sor_string = ""
        for mező in sor:
            sor_string += mező + " "
        print(sor_string)
    print()

while True:
    tabla = [["." for _ in range(8)] for _ in range(8)]
    for korong in korongok:
        sor, oszlop = map(int, korong.split("K"))
        tabla[sor - 1][oszlop - 1] = "O"
    for sor in tabla:
        print(" ".join(sor))
    print()

    print("Adja meg a korong pozícióját (sor oszlop), vagy nyomjon Enter-t a kilépéshez!")
    input_adat = input("Pozíció (pl. 3 5): ")

    if input_adat == "":
        break

    adatokat = input_adat.split()
    if len(adatokat) != 2:
        print("Két egész számot adjon meg, egyet a sorra és egyet az oszlopra!")
        continue

    sor, oszlop = adatokat

    if not (sor.isdigit() and oszlop.isdigit()):
        print("Csak számokat adjon meg!")
        continue

    sor = int(sor)
    oszlop = int(oszlop)

    if not (1 <= sor <= 8 and 1 <= oszlop <= 8):
        print("A sor és oszlop száma 1 és 8 között kell legyen!")
        continue

    pozicio = f"{sor}K{oszlop}"

    if pozicio in korongok:
        korongok.remove(pozicio)
        print(f"A {pozicio} helyről eltávolítottuk a korongot.")
    else:
        korongok.append(pozicio)
        print(f"Korong lerakva: {pozicio}")

print("Program vége. A végleges tábla:")
tabla_megjelenites()
