# Kysytään käyttäjältä kuhan pituus senttimetreinä ja muutetaan se liukuluvuksi (float)
pituus = float(input("Anna kuhan pituus senttimetreinä: "))

# Asetetaan alimman sallitun pituuden raja
SALLITTU_PITUUS = 37

# Valintarakenne (if-else) pituuden tarkistamiseen
if pituus < SALLITTU_PITUUS:
    puuttuvat_sentit = SALLITTU_PITUUS - pituus
    print("Kuha on alamittainen.")
    # f-merkkijonolla saadaan muuttujan arvo helposti tulosteeseen
    print(f"Laske kuha takaisin järveen. Alimmasta sallitusta pyyntimitasta puuttuu {puuttuvat_sentit} cm.")
else:
    print("Kuha on täysimittainen, voit pitää sen!")
