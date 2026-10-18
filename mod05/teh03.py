# Kysytään käyttäjältä kokonaisluku
luku = int(input("Syötä kokonaisluku: "))

# Alkuluvut ovat suurempia kuin 1
if luku > 1:
    on_alkuluku = True
    
    # Kokeillaan jakaa luku kaikilla luvuilla väliltä 2 - (luku - 1)
    for i in range(2, luku):
        if luku % i == 0:
            # Jos jako menee tasan (jakojäännös % on 0), luku ei ole alkuluku
            on_alkuluku = False
            break  # Lopetetaan etsiminen heti, koska yksi jakaja riittää todisteeksi
            
    # Tulostetaan vastaus tuloksen mukaan
    if on_alkuluku:
        print(f"Luku {luku} on alkuluku.")
    else:
        print(f"Luku {luku} ei ole alkuluku.")
else:
    # Luvut, jotka ovat 1 tai pienempiä (kuten 0 tai negatiiviset), eivät ole alkulukuja
    print(f"Luku {luku} ei ole alkuluku.")