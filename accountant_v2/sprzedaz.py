import output
import sys

argumenty = sys.argv

sciezka_do_pliku = sys.argv[1]
zarzadca_inwentarza = output.ZarzadcaInwentarza(sciezka_do_pliku)

ilosc = zarzadca_inwentarza.pobierz_ilosc_produktu(int(sys.argv[2]))
sprzedano = int(sys.argv[4])
nowa_ilosc = ilosc - sprzedano
nowe_saldo = zarzadca_inwentarza.pobierz_saldo() + int(sys.argv[3]) * int(sys.argv[4])

zarzadca_inwentarza.aktualizuj_ilosc_produktu(int(sys.argv[2]), nowa_ilosc)
zarzadca_inwentarza.aktualizuj_saldo(nowe_saldo)

nazwa = zarzadca_inwentarza.pobierz_nazwe_produktu(int(sys.argv[2]))
komentarz = "sprzedano " + sys.argv[4] +" " + nazwa + " za " + sys.argv[3] + " zł "
zarzadca_inwentarza.dodaj_do_historii(komentarz)

