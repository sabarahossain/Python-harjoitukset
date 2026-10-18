# Luodaan tyhjä lista kaupunkien nimiä varten
kaupungit = []

# Kysytään viiden kaupungin nimet for-toistorakenteen avulla
for i in range(5):
    kaupunki = input(f"Syötä {i+1}. kaupungin nimi: ")
    kaupungit.append(kaupunki)  # Tallennetaan nimi listaan

# Tulostetaan kaupungit allekkain käyttäen for/in -toistorakennetta
print("\nSyöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)