"""
 Porównanie zarobków na różnych stanowiskach Data Science w różnych krajach (Flask/CLI).
Aplikacja używa bazy danych z tabeli:
https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023
Użytkownik wybiera kraj - USA, Kanada, Wielka Brytania, Australia, Niemcy.
Aplikacja zwraca:
- Średnie roczne zarobki na każdym z dostępnych stanowisk Data Science w wybranym kraju.
- 3 firmy, które płacą najwięcej w danym kraju.
- O ile procent powyżej średniej wynoszą zarobki w tych firmach w porównaniu do średnich zarobków na danym stanowisku w danym kraju.
- Rekomendacja jakie stanowisko Data Science w której firmie jest najbardziej opłacalne w danym kraju.
"""
from itertools import islice
import csv
import sys
import os


# przykładowe dane: wejsciowe ds_salaries.csv ds_salaries2.csv 10 5 test

class FileCsv:
    def __init__(self, name):
        if os.path.exists(name):
            with open(name, 'r') as csv_file:
                csv_data = csv.reader(csv_file)
                self.data = list(csv_data)
        else:
            print("Plik wejsciowy nie istnieje")

    def srednie_zarobki(self, kraj):
        licznik = 0
        total = 0
        waluta = ""
        for item in self.data:
            if item[9] == kraj:
                licznik+=1
                total+=int(item[6])
        if total == 0:
            return "Brak danych"
        else:
            return "Średnie zarobki dla "+ kraj + " to " + str(total/licznik) +" USD "

    def najwieksze_place(self, nazwa):
        dane = []
        for item in self.data:
            if item[9] == nazwa:
             dane.append(item)

        sorted_place = sorted(dane, key=lambda item: int(item[6]) , reverse = True)
        return sorted_place[0:3]

    def srednia(self, nazwa):
        my_dict = {}

        # Dynamically create the dictionary with names and integer values
        for item in self.data:
            if item[9] == nazwa:
                if item[3] in my_dict:
                    value = my_dict[item[3]]
                    my_dict[item[3]] = [value[0] + int(item[6]), value[1]+1]
                else:
                    my_dict[item[3]] = [int(item[6]), 1]

        for key in my_dict:
            value = my_dict[key]
            new_value = value[0] / value[1]
            my_dict[key] = new_value

        return my_dict

    def procent_powyzej(self, nazw):
        data = self.najwieksze_place(nazw)
        srednie = self.srednia(nazw)
        wyniki = []

        for item in data:
            danasrednia =  float(srednie[item[3]])
            wynik = (float(item[6]) / danasrednia) - 1
            wyniki.append(wynik * 100)

        return wyniki

    def rekomendacja(self, nazwa):
        se = []
        for item in self.data:
            if item[9] == nazwa and item[3] == "Data Scientist" and item[1] == "SE":
                se.append(item)
        se = sorted(se, key=lambda item: int(item[6]) , reverse = True)

        en = []
        for item in self.data:
            if item[9] == nazwa and item[3] == "Data Scientist" and item[1] == "EN":
                en.append(item)
        en = sorted(en, key=lambda item: int(item[6]) , reverse = True)

        mi = []
        for item in self.data:
            if item[9] == nazwa and item[3] == "Data Scientist" and item[1] == "MI":
                mi.append(item)
        mi = sorted(mi, key=lambda item: int(item[6]) , reverse = True)

        if len(se) == 0:
            se = ["brak danych"]
        if len(en) == 0:
            en = ["brak danych"]
        if len(mi) == 0:
            mi = ["brak danych"]

        return [se[0],en[0],mi[0]]

file = FileCsv("ds_salaries.csv")

print("wybierz jeden skrót kraju:  USA podaj US, Kanada podaj CA, Wielka Brytania podaj GB, Australia podaj AU, Niemcy podaj DE	")
kraj = input("Podaj numer kraju: ")

print("Podaj srednie zarobki dla danego Kraju. Wybierz odpowiedni skrót")


print(file.srednie_zarobki(kraj))

print("===================================================================")
print("===================================================================")

print("3 firmy, które płacą najwięcej w danym kraju")
for item in file.najwieksze_place(kraj):
    print("job_title: " + item[3] + " salary_in_usd: " + item[6] + " USD")

print("===================================================================")
print("===================================================================")

print("średbnie powyżej 3 firmy, które płacą najwięcej w danym kraju")
licznik = 1
sredniepowyzej = file.procent_powyzej(kraj)
for item in sredniepowyzej:
    print("dla firmy " + str(licznik) + " średnia powyżej wynosi: "+ str(item) + " %")
    licznik+=1

print("===================================================================")
print("===================================================================")

print("Rekomendacja jakie stanowisko Data Science w której firmie jest najbardziej opłacalne w danym kraju")
dane = file.rekomendacja(kraj)

print("W zależności o doświadczenia są to najlepsze oferty")
for item in dane:
    print(item)

print("koniec")