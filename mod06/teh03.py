# 3. Funktio muuntaa Yhdysvaltain nestegallonat litroiksi
def gallonat_litroiksi(gallonat):
    # Yksi gallona on 3,785 litraa
    return gallonat * 3.785

def pääohjelma():
    while True:
        # Kysytään float
        gallonat = float(input("Syötä bensiinin määrä gallonoina (negatiivinen luku lopettaa): "))
        
        # Jos syöte on negatiivinen, katkaistaan silmukan suoritus
        if gallonat < 0:
            print("Ohjelma lopetetaan.")
            break
            
        # Tallennetaan tulos muuttujaan
        litrat = gallonat_litroiksi(gallonat)
        
        # Tulostetaan vastaava litramäärä kahden desimaalin tarkkuudella
        print(f"{gallonat} gallonaa on {litrat:.2f} litraa.\n")

# Suoritetaan pääohjelma
pääohjelma()
