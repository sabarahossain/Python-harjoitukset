# (alkuehto)
tuumat = float(input("Anna tuumamäärä (negatiivinen luku lopettaa): "))

# Toistaminen

while tuumat >= 0:
    # Lasketaan muunnos (1 tuuma = 2,54 cm)
    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {senttimetrit:.2f} senttimetriä.")
    
    # Kysytään uusi arvo seuraavaa kierrosta varten
    tuumat = float(input("\nAnna uusi tuumamäärä (negatiivinen luku lopettaa): "))

print("Ohjelma lopetettu.")
