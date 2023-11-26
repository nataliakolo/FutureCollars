import output
import sys

argumenty = sys.argv

sciezka_do_pliku = sys.argv[1]
zarzadca_inwentarza = output.ZarzadcaInwentarza(sciezka_do_pliku)
saldo = zarzadca_inwentarza.pobierz_saldo()
saldo += int(sys.argv[2])
zarzadca_inwentarza.aktualizuj_saldo(saldo)
zarzadca_inwentarza.dodaj_do_historii(sys.argv[3])
