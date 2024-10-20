import random

def erweiterte_lagerverwaltung():
    produkte = [
        {"name": "Laptop", "kategorie": "Elektronik", "bestand": 50, "preis": 800, "lieferant": "TechCorp"},
        {"name": "Smartphone", "kategorie": "Elektronik", "bestand": 100, "preis": 500, "lieferant": "MobileTech"},
        {"name": "Tisch", "kategorie": "Möbel", "bestand": 30, "preis": 200, "lieferant": "FurniturePlus"},
        {"name": "Stuhl", "kategorie": "Möbel", "bestand": 80, "preis": 100, "lieferant": "FurniturePlus"},
        {"name": "Buch", "kategorie": "Medien", "bestand": 200, "preis": 20, "lieferant": "MediaWorld"},
        {"name": "DVD", "kategorie": "Medien", "bestand": 150, "preis": 15, "lieferant": "MediaWorld"}
    ]
    gesamtwert = 0
    for produkt in produkte:
        gesamtwert += produkt["bestand"] * produkt["preis"]
    print(f"Gesamtwert des Lagers: {gesamtwert} €")
    print("\nDurchschnittspreise pro Kategorie:")
    kategorien = set(p["kategorie"] for p in produkte)
    for kategorie in kategorien:
        summe = 0
        anzahl = 0
        for produkt in produkte:
            if produkt["kategorie"] == kategorie:
                summe += produkt["preis"]
                anzahl += 1
        durchschnitt = summe / anzahl
        print(f"{kategorie}: {durchschnitt:.2f} €")
    print("\nDurchschnittlicher Bestand pro Kategorie:")
    for kategorie in kategorien:
        summe = 0
        anzahl = 0
        for produkt in produkte:
            if produkt["kategorie"] == kategorie:
                summe += produkt["bestand"]
                anzahl += 1
        durchschnitt = summe / anzahl
        print(f"{kategorie}: {durchschnitt:.2f} Stück")
    hoechster_bestandswert = 0
    produkt_mit_hoechstem_bestandswert = None
    for produkt in produkte:
        bestandswert = produkt["bestand"] * produkt["preis"]
        if bestandswert > hoechster_bestandswert:
            hoechster_bestandswert = bestandswert
            produkt_mit_hoechstem_bestandswert = produkt["name"]
    print(f"\nProdukt mit dem höchsten Bestandswert: {produkt_mit_hoechstem_bestandswert} ({hoechster_bestandswert} €)")
    niedrigster_bestandswert = float('inf')
    produkt_mit_niedrigstem_bestandswert = None
    for produkt in produkte:
        bestandswert = produkt["bestand"] * produkt["preis"]
        if bestandswert < niedrigster_bestandswert:
            niedrigster_bestandswert = bestandswert
            produkt_mit_niedrigstem_bestandswert = produkt["name"]
    print(f"Produkt mit dem niedrigsten Bestandswert: {produkt_mit_niedrigstem_bestandswert} ({niedrigster_bestandswert} €)")
    print("\nSimulierte Verkäufe:")
    for _ in range(10):
        produkt = random.choice(produkte)
        verkaufsmenge = random.randint(1, 5)
        if verkaufsmenge <= produkt["bestand"]:
            produkt["bestand"] -= verkaufsmenge
            print(f"{verkaufsmenge}x {produkt['name']} verkauft")
        else:
            print(f"Nicht genügend {produkt['name']} auf Lager")
    print("\nAktualisierte Bestandsliste:")
    for produkt in produkte:
        print(f"{produkt['name']}: {produkt['bestand']} Stück")
    print("\nNachbestellungen:")
    for produkt in produkte:
        if produkt["bestand"] < 30:
            nachbestellmenge = 50 - produkt["bestand"]
            produkt["bestand"] += nachbestellmenge
            print(f"{nachbestellmenge}x {produkt['name']} von {produkt['lieferant']} nachbestellt")
    gesamtwert = 0
    for produkt in produkte:
        gesamtwert += produkt["bestand"] * produkt["preis"]
    print(f"\nAktualisierter Gesamtwert des Lagers: {gesamtwert} €")
    print("\nBestandswert pro Lieferant:")
    lieferanten = set(p["lieferant"] for p in produkte)
    for lieferant in lieferanten:
        lieferant_wert = 0
        for produkt in produkte:
            if produkt["lieferant"] == lieferant:
                lieferant_wert += produkt["bestand"] * produkt["preis"]
        print(f"{lieferant}: {lieferant_wert} €")
    print("\nProdukte mit kritischem Bestand (weniger als 10% des Durchschnittsbestands):")
    for kategorie in kategorien:
        summe_bestand = 0
        anzahl_produkte = 0
        for produkt in produkte:
            if produkt["kategorie"] == kategorie:
                summe_bestand += produkt["bestand"]
                anzahl_produkte += 1
        durchschnitt_bestand = summe_bestand / anzahl_produkte
        for produkt in produkte:
            if produkt["kategorie"] == kategorie and produkt["bestand"] < 0.1 * durchschnitt_bestand:
                print(f"{produkt['name']} (aktueller Bestand: {produkt['bestand']}, Durchschnitt Kategorie: {durchschnitt_bestand:.2f})")

erweiterte_lagerverwaltung()
