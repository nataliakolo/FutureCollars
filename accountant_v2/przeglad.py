import output
import sys

argumenty = sys.argv

sciezka_do_pliku = sys.argv[1]
zarzadca_inwentarza = output.ZarzadcaInwentarza(sciezka_do_pliku)

print(zarzadca_inwentarza.pobiezrz_historie(int(sys.argv[2]),int(sys.argv[3])))

