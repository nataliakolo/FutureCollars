liczba_elementow = int(input("Podaj liczbe elementów do wysyłki "))
liczba_paczek = 0
waga_aktualnej_paczki = 0
liczba_wyslanych_kilogramow = 0
suma_pustych_kilogramow = 0
numer_paczki = 0
wartosc_pustych_max = -1


for element in range(1,liczba_elementow +1):
    #print(element)
    print("liczba_wyslanych_kilogramow to: " + str(liczba_wyslanych_kilogramow))
    waga_elementu = int(input("Podaj wagę elementu " + str(element) + " " ))
    if waga_elementu < 1 or waga_elementu > 10:
        print("nieprawidłowa waga")
        break

    liczba_wyslanych_kilogramow = liczba_wyslanych_kilogramow + waga_elementu


    if waga_aktualnej_paczki + waga_elementu <= 20:
        waga_aktualnej_paczki = waga_aktualnej_paczki + waga_elementu
        print("waga_aktualnej_paczki to: " + str(waga_aktualnej_paczki))
        print("liczba paczek to: " +str(liczba_paczek + 1))
        print("============================================================")
    else:
        reszta_z_paczki = 20 - waga_aktualnej_paczki
        suma_pustych_kilogramow = suma_pustych_kilogramow + reszta_z_paczki
        if reszta_z_paczki > wartosc_pustych_max:
            wartosc_pustych_max = reszta_z_paczki
            numer_paczki = liczba_paczek + 1

        liczba_paczek = liczba_paczek + 1
        waga_aktualnej_paczki = waga_elementu
        print("waga_aktualnej_paczki to: " + str(waga_aktualnej_paczki))
        print("liczba paczek to: " + str(liczba_paczek + 1))
        print("============================================================")

reszta_z_paczki = 20 - waga_aktualnej_paczki
suma_pustych_kilogramow = suma_pustych_kilogramow + reszta_z_paczki

if reszta_z_paczki > wartosc_pustych_max:
    wartosc_pustych_max = reszta_z_paczki
    numer_paczki = liczba_paczek + 1


print("Podsumowanie: ")
print("liczba paczek to: " +str(liczba_paczek + 1))
print("liczba_wyslanych_kilogramow to: " + str(liczba_wyslanych_kilogramow))
print("suma pustych kilogramów to: " + str(suma_pustych_kilogramow))
print("paczka z największą ilością pustych kilogramów to: " + str(numer_paczki) + " było w niej pustych kilogramów: " + str(wartosc_pustych_max))







