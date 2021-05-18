import model

def zdravnik_izpis_funkcij():
    return (
        "-za vpogled v svoje termine, vpiši 'termini'" +
        "-če želiš dodati prost termin, vpiši 'dodaj'" + 
        "-če želiš potrditi termin, vpiši 'potrdi' " +
        "-če želiš izbrisati termin, vpiši 'izbrisi'" +
        "-če želiš zaključiti, vpiši 'konec'"
    )

def pacient_izpis_funkcij():
    return (
        "-za vpogled v proste termine zdravnika, vpiši 'prosti -ime_zdravnika-'" +
        "-za vpogled v svoje naročene termine, vpiši 'naročeni'" +
        "-če se želiš naročiti, vpiši 'naroči'" + 
        "-če želiš potrditi termin, vpiši 'potrdi' " +
        "-če želiš izbrisati svoj naročeni termin, vpiši 'izbrisi'" +
        "-če želiš zaključiti, vpiši 'konec'"
    )

def vnos_datuma():
    return input("Vpiši datum termina: ")

def vnos_začetka():
    return input("Vpiši čas začetka termina: ")

def vnos_konca():
    return input("Vpiši čas konca termina: ")

def vnos_zdravnika():
    return input("Vpiši ime zdravnika: ")

def vnos_pacienta():
    return input("Vpiši ime pacienta: ")

def zdravnik_dodaj_termin(zdravnik):
    datum = vnos_datuma()
    zacetek = vnos_začetka()
    konec = vnos_konca()
    termin = model.nov_termin(datum, zacetek, konec, zdravnik, "še ni dodeljenega pacienta")
    return termin

def pozeni_urnik():
    urnik = model.nov_urnik()
    while True:
        print()