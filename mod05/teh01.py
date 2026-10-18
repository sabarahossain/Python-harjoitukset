import random

# Kysytään käyttäjältä arpakuutioiden lukumäärä ja muutetaan se kokonaisluvuksi
arpakuutiot = int(input("Kuinka monta arpakuutiota heitetään? "))

# Alustetaan summamuuttuja nollaksi
summa = 0

# Heitetään arpakuutioita for-toistorakenteen avulla
for i in range(arpakuutiot):
    heitto = random.randint(1, 6)  # Arvotaan silmäluku väliltä 1-6
    summa += heitto               # Lisätään heiton tulos summaan

# Tulostetaan silmälukujen lopullinen summa
print(f"Silmälukujen summa on: {summa}")