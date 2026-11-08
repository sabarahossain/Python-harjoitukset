# 5. Funktio, joka karsii parittomat luvut ja palauttaa uuden listan parillisista luvuista
def karsi_parittomat(lukulista):
    parilliset = []
    
    # Käydään lista läpi ja tarkistetaan jokainen luku
    for luku in lukulista:
        # Jos luku jaettuna kahdella jättää jakojäännökseksi 0, se on parillinen
        if luku % 2 == 0:
            parilliset.append(luku)
            
    return parilliset

# Pääohjelma testausta varten
def pääohjelma():
    # Luodaan alkuperäinen testilista, joka sisältää sekä parillisia että parittomia lukuja
    alkuperäinen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Kutsutaan funktiota ja tallennetaan saatu uusi lista muuttujaan
    karsittu_lista = karsi_parittomat(alkuperäinen_lista)
    
    # Tulostetaan molemmat listat tehtävänannon mukaisesti
    print(f"Alkuperäinen lista: {alkuperäinen_lista}")
    print(f"Karsittu lista (vain parilliset): {karsittu_lista}")

pääohjelma()
