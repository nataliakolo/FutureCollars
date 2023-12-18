import output
import sys

class Manager:
    def __init__(self,argumenty):
        self.argumenty = argumenty
        self.zarzadca_inwentarza = output.ZarzadcaInwentarza(self.argumenty[2])
        self.actions = {}

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb

        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self)


manager = Manager(sys.argv)

@manager.assign("saldo")
def saldo(manager):
    saldo = manager.zarzadca_inwentarza.pobierz_saldo()
    saldo += int(manager.argumenty[3])
    manager.zarzadca_inwentarza.aktualizuj_saldo(saldo)
    manager.zarzadca_inwentarza.dodaj_do_historii(manager.argumenty[4])

@manager.assign("konto")
def konto(manager):
    saldo = manager.zarzadca_inwentarza.pobierz_saldo()
    komentarz = "aktualny stan konta to " + str(saldo)
    manager.zarzadca_inwentarza.dodaj_do_historii(komentarz)

@manager.assign("magazyn")
def magazyn(manager):
    nazwa = manager.zarzadca_inwentarza.pobierz_nazwe_produktu(int(sys.argv[3]))
    ilosc = manager.zarzadca_inwentarza.pobierz_ilosc_produktu(int(sys.argv[3]))
    komentarz = "na magazynie dla " + nazwa + " jest sztuk: " + str(ilosc)
    manager.zarzadca_inwentarza.dodaj_do_historii(komentarz)

@manager.assign("przeglad")
def przeglad(manager):
    print(manager.zarzadca_inwentarza.pobiezrz_historie(int(sys.argv[3]), int(sys.argv[4])))

@manager.assign("sprzedaz")
def sprzedaz(manager):
    ilosc = manager.zarzadca_inwentarza.pobierz_ilosc_produktu(int(sys.argv[3]))
    sprzedano = int(sys.argv[5])
    nowa_ilosc = ilosc - sprzedano
    nowe_saldo = manager.zarzadca_inwentarza.pobierz_saldo() + int(sys.argv[4]) * int(sys.argv[5])

    manager.zarzadca_inwentarza.aktualizuj_ilosc_produktu(int(sys.argv[3]), nowa_ilosc)
    manager.zarzadca_inwentarza.aktualizuj_saldo(nowe_saldo)

    nazwa = manager.zarzadca_inwentarza.pobierz_nazwe_produktu(int(sys.argv[3]))
    komentarz = "sprzedano " + sys.argv[4] + " " + nazwa + " za " + sys.argv[4] + " zł "
    manager.zarzadca_inwentarza.dodaj_do_historii(komentarz)

@manager.assign("zakup")
def zakup(manager):
    ilosc = manager.zarzadca_inwentarza.pobierz_ilosc_produktu(int(sys.argv[3]))
    zakupiono = int(sys.argv[5])
    nowa_ilosc = ilosc + zakupiono
    nowe_saldo = manager.zarzadca_inwentarza.pobierz_saldo() - int(sys.argv[4]) * int(sys.argv[5])

    manager.zarzadca_inwentarza.aktualizuj_ilosc_produktu(int(sys.argv[3]), nowa_ilosc)
    manager.zarzadca_inwentarza.aktualizuj_saldo(nowe_saldo)

    nazwa = manager.zarzadca_inwentarza.pobierz_nazwe_produktu(int(sys.argv[3]))
    komentarz = "zakupiono " + sys.argv[5] + " " + nazwa + " za " + sys.argv[4] + " zł "
    manager.zarzadca_inwentarza.dodaj_do_historii(komentarz)



manager.execute(manager.argumenty[1])



"saldo warehouse.json 2000 ""dodano 2000"