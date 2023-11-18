import sys

class wychowawca:
    def __init__(self, imie):
        self.imie = imie
        self.klasy = []

    def dodaj_klase(self,klasa):
        self.klasy.append(klasa)

class nauczyciel:
    def __init__(self, imie, przedmiot):
        self.imie = imie
        self.przedmiot = przedmiot
        self.klasy = []

    def dodaj_klase(self, klasa):
        self.klasy.append(klasa)

class uczen:
    def __init__(self, imie, klasa):
        self.imie = imie
        self.klasy = klasa




wszyscy_wychowawcy = []
wszyscy_nauczyciele = []
wszyscy_uczniowie = []

argumenty = sys.argv

f = open(sys.argv[1])
lines = f.read().splitlines()
f.close()

for index, wartosc in enumerate(lines):

    if wartosc == "wychowawca":
        nowy_wycho = wychowawca(lines[index+1])
        licznik = index + 2

        while lines[licznik].strip():
            nowy_wycho.dodaj_klase(lines[licznik])
            licznik+=1

        wszyscy_wychowawcy.append(nowy_wycho)

    if wartosc == "nauczyciel":
        nowy_nauczyciel = nauczyciel(lines[index+1], lines[index+2])
        licznik = index + 3

        while lines[licznik].strip():
            nowy_nauczyciel.dodaj_klase(lines[licznik])
            licznik += 1

        wszyscy_nauczyciele.append(nowy_nauczyciel)

    if wartosc == "uczen":
        nowy_uczen = uczen(lines[index+1], lines[index+2])

        wszyscy_uczniowie.append(nowy_uczen)



if sys.argv[2][0] == "1" or sys.argv[2][0] == "2" or sys.argv[2][0] == "3":
    for wych in wszyscy_wychowawcy:
        for klas in wych.klasy:
            if klas == sys.argv[2]:
                print(wych.imie)

    for uczen in wszyscy_uczniowie:
        if uczen.klasy == sys.argv[2]:
            print(uczen.imie)
else:
    for wych in wszyscy_wychowawcy:
        if sys.argv[2] == wych.imie:
            print("opcja wychowawca")
            for klas in wych.klasy:
                for uczen in wszyscy_uczniowie:
                    if klas == uczen.klasy:
                        print(uczen.imie)
            break

    for nau in wszyscy_nauczyciele:
        if sys.argv[2] == nau.imie:
            print("opcja nauczyciel")
            for klas in nau.klasy:
                for wych in wszyscy_wychowawcy:
                    if klas in wych.klasy:
                        print(wych.imie)
            break

    for uczn in wszyscy_uczniowie:
        if sys.argv[2] == uczn.imie:
            print("opcja uczen")

            for nau in wszyscy_nauczyciele:
                if uczn.klasy in nau.klasy:
                    print(nau.przedmiot)
                    print(nau.imie)
            break

print("koniec")