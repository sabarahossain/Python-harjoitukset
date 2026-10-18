# Luodaan tyhjä lista käyttäjän syöttämiä lukuja varten
luvut = []

while True:
    syote = input("Syötä luku (tyhjä lopettaa): ")
    
    # Jos syöte on tyhjä merkkijono, katkaistaan silmukka
    if syote == "":
        break
    
    # Muutetaan syöte numeroksi ja lisätään listaan
    # (Käytetään float-tyyppiä, jotta ohjelma hyväksyy myös desimaaliluvut)
    luku = float(syote)
    luvut.append(luku)

# Järjestetään lista suurimmasta pienimpään reverse=True -argumentilla
luvut.sort(reverse=True)

# Otetaan listalta viisi ensimmäistä alkiota (eli 5 suurinta)
viisi_suurinta = luvut[:5]

# Tulostetaan tulokset
print("\nViisi suurinta lukua suurimmasta alkaen:")
for luku in viisi_suurinta:
    # Jos luku on kokonaisluku (esim. 5.0), tulostetaan se ilman desimaalia
    if luku.is_integer():
        print(int(luku))
    else:
        print(luku)