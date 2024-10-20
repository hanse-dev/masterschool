while True:
    print("\nEinfacher Taschenrechner")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")
    print("5. Potenz")
    print("6. Wurzel")
    print("7. Beenden")
    auswahl = input("Wählen Sie eine Operation (1-7): ")
    if auswahl in ('1', '2', '3', '4', '5', '6', '7'):
        if auswahl == '1':
            zahl1 = float(input("Geben Sie die erste Zahl ein: "))
            zahl2 = float(input("Geben Sie die zweite Zahl ein: "))
            ergebnis = zahl1 + zahl2
            print(f"Das Ergebnis von {zahl1} + {zahl2} ist: {ergebnis}")
        elif auswahl == '2':
            zahl1 = float(input("Geben Sie die erste Zahl ein: "))
            zahl2 = float(input("Geben Sie die zweite Zahl ein: "))
            ergebnis = zahl1 - zahl2
            print(f"Das Ergebnis von {zahl1} - {zahl2} ist: {ergebnis}")
        elif auswahl == '3':
            zahl1 = float(input("Geben Sie die erste Zahl ein: "))
            zahl2 = float(input("Geben Sie die zweite Zahl ein: "))
            ergebnis = zahl1 * zahl2
            print(f"Das Ergebnis von {zahl1} * {zahl2} ist: {ergebnis}")
        elif auswahl == '4':
            zahl1 = float(input("Geben Sie die erste Zahl ein: "))
            zahl2 = float(input("Geben Sie die zweite Zahl ein: "))
            if zahl2 != 0:
                ergebnis = zahl1 / zahl2
                print(f"Das Ergebnis von {zahl1} / {zahl2} ist: {ergebnis}")
            else:
                print("Fehler: Division durch Null ist nicht erlaubt!")
        elif auswahl == '5':
            zahl1 = float(input("Geben Sie die erste Zahl ein: "))
            zahl2 = float(input("Geben Sie die zweite Zahl ein: "))
            ergebnis = zahl1 ** zahl2
            print(f"Das Ergebnis von {zahl1} ^ {zahl2} ist: {ergebnis}")
        elif auswahl == '6':
            zahl1 = float(input("Geben Sie eine Zahl ein: "))
            if zahl1 >= 0:
                ergebnis = zahl1 ** 0.5
                print(f"Die Quadratwurzel von {zahl1} ist: {ergebnis}")
            else:
                print("Fehler: Kann keine Wurzel aus einer negativen Zahl ziehen!")
        elif auswahl == '7':
            print("Taschenrechner wird beendet. Auf Wiedersehen!")
            break
    else:
        print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und 7.")

    weitermachen = input("Möchten Sie eine weitere Berechnung durchführen? (ja/nein): ")
    if weitermachen.lower() != 'ja':
        print("Taschenrechner wird beendet. Auf Wiedersehen!")
        break
