def AlanHesapla():
    kisaKenar = int(input("Kısakenar: "))
    UzunKenar = int(input("Uzunkenar: "))
    alan = kisaKenar * UzunKenar
    print(f"Kısakenarı = {kisaKenar} Uzunkenarı = {UzunKenar} olan dikdörtgenin alanı = {alan}")


def CevreHesapla():
    kisaKenar = int(input("Kısakenar: "))
    UzunKenar = int(input("Uzunkenar: "))
    cevre = 2 * (kisaKenar + UzunKenar)
    print(f"Kısakenarı = {kisaKenar} Uzunkenarı = {UzunKenar} olan dikdörtgenin çevresi = {cevre}")


AlanHesapla()
CevreHesapla()
