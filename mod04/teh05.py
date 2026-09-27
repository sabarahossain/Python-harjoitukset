
OIKEA_TUNNUS = "minä123"
OIKEA_SALASANA = "salainen456"

yritykset = 0

while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")
    
    # Tarkistetaan, ovatko molemmat oikein
    if tunnus == OIKEA_TUNNUS and salasana == OIKEA_SALASANA:
        print("Tervetuloa")
        break
    else:
        yritykset += 1
        print(f"Väärä tunnus tai salasana. Yrityskerrat: {yritykset}/5\n")
        
if yritykset == 5:
    print("Pääsy evätty")
