import output
import sys

argumenty = sys.argv

sciezka_do_pliku = sys.argv[1]
zarzadca_inwentarza = output.ZarzadcaInwentarza(sciezka_do_pliku)
nazwa = zarzadca_inwentarza.pobierz_nazwe_produktu(int(sys.argv[2]))
ilosc  = zarzadca_inwentarza.pobierz_ilosc_produktu(int(sys.argv[2]))
komentarz = "na magazynie dla " + nazwa + " jest sztuk: " + str(ilosc)



zarzadca_inwentarza.dodaj_do_historii(komentarz)
