# Kysytään käyttäjän tiedot (sukupuoli muutetaan automaattisesti pieniksi kirjaimiksi)
sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ").lower()
hemo = float(input("Anna hemoglobiiniarvo (g/l): "))

# Naisten arvojen tarkistus
if sukupuoli == "nainen":
    if hemo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemo > 175:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")

# Miesten arvojen tarkistus
elif sukupuoli == "mies":
    if hemo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemo > 195:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")

# Jos syöte ei ole kumpikaan tunnistetuista sukupuolista
else:
    print("Virheellinen sukupuoli. Syötä 'nainen' tai 'mies'.")
