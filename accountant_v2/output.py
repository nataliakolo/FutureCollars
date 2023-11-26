import json


class ZarzadcaInwentarza:
    def __init__(self, sciezka_pliku):
        self.sciezka_pliku = sciezka_pliku
        self.dane = self.zaladuj_dane()

    def zaladuj_dane(self):
        with open(self.sciezka_pliku, 'r') as plik:
            dane = json.load(plik)
            return dane

    def zapisz_dane(self):
        with open(self.sciezka_pliku, 'w') as plik:
            json.dump(self.dane, plik, indent=2)

    def pobierz_saldo(self):
        return self.dane.get('saldo', 0)

    def pobierz_inwentarz(self):
        return self.dane.get('magazyn', [])

    def pobierz_ilosc_produktu(self, id_produktu):
        inwentarz = self.pobierz_inwentarz()
        for produkt in inwentarz:
            if produkt.get('id') == id_produktu:
                return produkt['ilosc']
        return None

    def pobierz_cene_produktu(self, id_produktu):
        inwentarz = self.pobierz_inwentarz()
        for produkt in inwentarz:
            if produkt.get('id') == id_produktu:
                return produkt['cena_jednostkowa']
        return None

    def pobierz_nazwe_produktu(self, id_produktu):
        inwentarz = self.pobierz_inwentarz()
        for produkt in inwentarz:
            if produkt.get('id') == id_produktu:
                return produkt['nazwa']
        return None

    def aktualizuj_saldo(self, nowe_saldo):
        self.dane['saldo'] = nowe_saldo
        self.zapisz_dane()

    def aktualizuj_ilosc_produktu(self, id_produktu, nowa_ilosc):
        inwentarz = self.pobierz_inwentarz()
        for produkt in inwentarz:
            if produkt.get('id') == id_produktu:
                produkt['ilosc'] = nowa_ilosc
                self.zapisz_dane()
                return True
        return False

    def dodaj_do_historii(self, nowe_wydarzenie):
        self.dane['historia'].append(nowe_wydarzenie)
        self.zapisz_dane()

    def pobiezrz_historie(self, start, end):
        return self.dane['historia'][start:end]
