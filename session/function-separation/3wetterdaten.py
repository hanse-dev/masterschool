import random

def analysiere_wetterdaten():
    temperaturen = [random.randint(-10, 35) for _ in range(30)]
    niederschlaege = [random.randint(0, 50) for _ in range(30)]
    summe_temp = 0
    for temp in temperaturen:
        summe_temp += temp
    durchschnitt_temp = summe_temp / len(temperaturen)
    print(f"Durchschnittstemperatur: {durchschnitt_temp:.1f}°C")
    hoechsttemp = temperaturen[0]
    for temp in temperaturen:
        if temp > hoechsttemp:
            hoechsttemp = temp
    print(f"Höchsttemperatur: {hoechsttemp}°C")
    niedrigsttemp = temperaturen[0]
    for temp in temperaturen:
        if temp < niedrigsttemp:
            niedrigsttemp = temp
    print(f"Niedrigste Temperatur: {niedrigsttemp}°C")
    summe_niederschlag = 0
    for niederschlag in niederschlaege:
        summe_niederschlag += niederschlag
    durchschnitt_niederschlag = summe_niederschlag / len(niederschlaege)
    print(f"Durchschnittlicher Niederschlag: {durchschnitt_niederschlag:.1f}mm")
    hoechster_niederschlag = niederschlaege[0]
    for niederschlag in niederschlaege:
        if niederschlag > hoechster_niederschlag:
            hoechster_niederschlag = niederschlag
    print(f"Höchster Niederschlag: {hoechster_niederschlag}mm")
    tage_mit_niederschlag = 0
    for niederschlag in niederschlaege:
        if niederschlag > 0:
            tage_mit_niederschlag += 1
    print(f"Tage mit Niederschlag: {tage_mit_niederschlag}")
    bericht = "Wetterbericht:\n"
    bericht += f"Durchschnittstemperatur: {durchschnitt_temp:.1f}°C\n"
    bericht += f"Temperaturbereich: {niedrigsttemp}°C bis {hoechsttemp}°C\n"
    bericht += f"Durchschnittlicher Niederschlag: {durchschnitt_niederschlag:.1f}mm\n"
    bericht += f"Höchster Niederschlag: {hoechster_niederschlag}mm\n"
    bericht += f"Tage mit Niederschlag: {tage_mit_niederschlag} von {len(niederschlaege)}"
    return bericht

wetterbericht = analysiere_wetterdaten()
print("\nZusammenfassung:")
print(wetterbericht)
