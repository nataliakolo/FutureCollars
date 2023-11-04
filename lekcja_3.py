import datetime

print("Witamy w programie kartka urodzinowa")
imie_solenizanta = input("Podaj imię solenizanta ")
rok_urodzenia = int(input("Podaj jego rok urodzenia "))
zyczenia = input("Napisz życzenia ")
imie_uzytkowanika = input("Podaj swoje imię ")
wiek_solenizanta = datetime.date.today().year - rok_urodzenia
print("wiek solenizanta to " + str(wiek_solenizanta)+"\n")

kartka_urodzinowa = (imie_solenizanta + ", wszystkiego najlepszego z okazji " + str(wiek_solenizanta) + " urodzin!\n" +
                     zyczenia + "\n" + imie_uzytkowanika)
print(kartka_urodzinowa)


