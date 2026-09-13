vuosi = int(input("Anna vuosiluku: "))

# Karkausvuoden ehto loogisilla operaattoreilla:
# Vuosi on karkausvuosi, jos se on jaollinen 4:llä JA EI jaollinen 100:lla,
# TAI jos se on jaollinen 400:lla.
if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print(f"Vuosi {vuosi} on karkausvuosi.")
else:
    print(f"Vuosi {vuosi} ei ole karkausvuosi.")