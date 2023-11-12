import sys

saldo = 100000
historia = []

magazyn = [
    {
       "id": 0,
       "nazwa": "rower",
       "ilosc": 10,
       "cena_jednostkowa": 1000
    },
    {
        "id": 1,
        "nazwa": "hulajnoga",
        "ilosc": 8,
        "cena_jednostkowa": 500
    }
]

print(magazyn[0]['ilosc'])


argumenty = sys.argv
print(argumenty)

for index, wartosc in enumerate(argumenty):
    if wartosc == "saldo":
        saldo += int(sys.argv[index+1])
        historia.append(sys.argv[index+2])
    elif wartosc == "sprzedaz":
        if magazyn[int(sys.argv[index+1])]['ilosc'] >= int(sys.argv[index + 3]):
            saldo += int(sys.argv[index+2]) * int(sys.argv[index+3])
            magazyn[int(sys.argv[index + 1])]['ilosc'] -= int(sys.argv[index + 3])
            historia.append("sprzedalismy " + str(sys.argv[index+3]) + " " + magazyn[int(sys.argv[index+1])]['nazwa'] )
        else:
            break
    elif wartosc == "zakup":
        if saldo > (int(sys.argv[index+2]) * int(sys.argv[index+3])):
            saldo -= int(sys.argv[index+2]) * int(sys.argv[index+3])
            magazyn[int(sys.argv[index+1])]['ilosc'] += int(sys.argv[index+3])
            historia.append(
                "kupilismy " + str(sys.argv[index + 3]) + " " + magazyn[int(sys.argv[index + 1])]['nazwa'])
        else:
            break
    elif wartosc == "konto":
        print("aktualny stan konta to " + str(saldo) )
    elif wartosc == "magazyn":
        print("stan na magazynie dla " + magazyn[int(sys.argv[index + 1])]['nazwa'] + " to: " + str(magazyn[int(sys.argv[index+1])]['ilosc']) + " sztuk")
    elif wartosc == "przeglad":
        if  int(sys.argv[index + 2]) <= len(historia):
            print(historia[int(sys.argv[index + 1]): int(sys.argv[index + 2])])



'''
Przykładowe dane wejsciowe: 
saldo -1000 "kupilam cos za 1000 zl" konto sprzedaz 1 500 2 zakup 0 1000 2 konto magazyn 1 magazyn 0 przeglad 1 3
'''