import math

# 6. Funktio, joka laskee pizzan neliömetrihinnan
def laske_yksikköhinta(halkaisija_cm, hinta_euroa):
    # Muunnetaan halkaisija metreiksi ja lasketaan säde (r) metreinä
    säde_m = (halkaisija_cm / 100) / 2
    
    # Lasketaan pizzan (pii * r^2)
    pinta_ala_m2 = math.pi * (säde_m ** 2)
    
    # Lasketaan ja palautetaan hinta per neliömetri
    yksikköhinta = hinta_euroa / pinta_ala_m2
    return yksikköhinta

# Pääohjelma
def pääohjelma():
    print("--- Pizza 1 ---")
    halkaisija1 = float(input("Syötä 1. pizzan halkaisija (cm): "))
    hinta1 = float(input("Syötä 1. pizzan hinta (€): "))
    
    print("\n--- Pizza 2 ---")
    halkaisija2 = float(input("Syötä 2. pizzan halkaisija (cm): "))
    hinta2 = float(input("Syötä 2. pizzan hinta (€): "))
    
    # Lasketaan yksikköhinnat funktiota hyödyntäen
    yksikköhinta1 = laske_yksikköhinta(halkaisija1, hinta1)
    yksikköhinta2 = laske_yksikköhinta(halkaisija2, hinta2)
    
    # Tulostetaan laskelmat kahden desimaalin tarkkuudella (.2f)
    print(f"\n1. pizzan yksikköhinta on {yksikköhinta1:.2f} €/m²")
    print(f"2. pizzan yksikköhinta on {yksikköhinta2:.2f} €/m²")
    
    # Vertaillaan kummalla on alhaisempi yksikköhinta
    if yksikköhinta1 < yksikköhinta2:
        print("\nEnsimmäinen pizza antaa paremman vastineen rahalle!")
    elif yksikköhinta2 < yksikköhinta1:
        print("\nToinen pizza antaa paremman vastineen rahalle!")
    else:
        print("\nMolemmat pizzat ovat yhtä edullisia!")


pääohjelma()
