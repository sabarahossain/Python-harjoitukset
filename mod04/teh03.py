
pienin = None
suurin = None

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    
    # Tarkistetaan, painoiko käyttäjä pelkkää Enteriä
    if syote == "":
        break  
    
    # Muunnetaan syöte liukuluvuksi (float)
    luku = float(syote)
    
    # Jos tämä on ensimmäinen luku, se on sekä pienin että suurin
    if pienin is None and suurin is None:
        pienin = luku
        suurin = luku
    else:
       
        if luku < pienin:
            pienin = luku
       
        if luku > suurin:
            suurin = luku


if pienin is not None and suurin is not None:
    print(f"Pienin luku oli: {pienin}")
    print(f"Suurin luku oli: {suurin}")
else:
    print("Et syöttänyt yhtään lukua.")
