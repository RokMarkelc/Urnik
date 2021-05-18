TERMIN_ZASEDEN = "ZASEDENO"
TERMIN_PROST = "PROSTO"
TERMIN_POTRJEN = "POTRJEN"
TERMIN_OBISKAN = "OBISKAN"
TERMIN_ZAMUJEN = "NI OBISKAN"

from datetime import datetime
import json

class Termin:
    def __init__(self, datum, cas, zdravnik, pacient, stanje):
        self.datum = datum
        self.cas = cas
        self.zdravnik = zdravnik
        self.pacient = pacient
        self.stanje = stanje

#
#def popravi_datum(datum):
#    sez = datum.split('.')
#    while len(sez[0]) < 2:
#        sez[0] = '0' + sez[0]
#    while len(sez[1]) < 2:
#        sez[1] = '0' + sez[1]
#    while len(sez[1]) < 4:
#        sez[1] = ' ' + sez[1]
#    return ''.join(sez)

def nov_termin(datum_str, zacetek, konec, zdravnik, pacient):
    cas = (zacetek, konec)
    datum_obj = datetime.strptime(datum_str, '%d.%m.Y%')
    return Termin(datum_obj, cas, zdravnik, pacient, TERMIN_PROST)

class Urnik:
    def __init__(self):
        self.termini = {}

    def prost_ID_igre(self, pacient):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def dodaj_termin(self):
        termin = nov_termin
