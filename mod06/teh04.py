# 4. Funktio, joka saa parametrinaan listan kokonaislukuja ja palauttaa niiden summan
def laske_summa(lukulista):
    # Pythonin sisäänrakennettu sum()-funktio laskee listan alkioiden summan
    return sum(lukulista)

# Pääohjelma testausta varten
def pääohjelma():
    # Luodaan testilista, joka sisältää kokonaislukuja
    testilista = [5, 12, 8, 24, 3, 11]
    
    # Kutsutaan funktiota ja tallennetaan sen palauttama arvo muuttujaan
    kokonaissumma = laske_summa(testilista)
    
    # Tulostetaan alkuperäinen lista ja saatu summa
    print(f"Testilistan luvut: {testilista}")
    print(f"Lukujen summa on: {kokonaissumma}")


pääohjelma()
