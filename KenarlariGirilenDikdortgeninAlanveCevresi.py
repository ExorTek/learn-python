class Program:
    def __init__(self, kisaKenar, uzunKenar):
        self.kisaKenar = kisaKenar
        self.uzunKenar = uzunKenar

    def AlanHesapla(self):
        alan = self.kisaKenar * self.uzunKenar
        print(f"Kısakenarı : {self.kisaKenar} Uzunkenarı : {self.uzunKenar} olan dikdörtgenin alanı = {alan}")

    def CevreHesapla(self):
        cevre = 2 * (self.kisaKenar + self.uzunKenar)
        print(f"Kısakenarı : {self.kisaKenar} Uzunkenarı : {self.uzunKenar} olan dikdörtgenin çevresi = {cevre}")

    def AlanveCevreHesapla(self):
        alan = self.kisaKenar * self.uzunKenar
        cevre = 2 * (self.kisaKenar + self.uzunKenar)
        print(f"Kısakenarı : {self.kisaKenar} Uzunkenarı : {self.uzunKenar} olan dikdörtgenin alanı = {alan}")
        print(f"Kısakenarı : {self.kisaKenar} Uzunkenarı : {self.uzunKenar} olan dikdörtgenin çevresi = {cevre}")


def YildizKoy():
    print("*" * 50)


while True:
    try:
        secim = input("1- Alan Hesapla\n2- Çevre Hesapla\n3- Alan ve Çevre Hesapla\n4- Çıkış\nSeçiminiz: ")
        if secim == '4':
            break
        elif secim in ('1', '2', '3'):
            YildizKoy()
            kisaKenar = float(input("Kısakenar: "))
            uzunKenar = float(input("Uzunkenar: "))
            program = Program(kisaKenar, uzunKenar)
            if secim == '1':
                program.AlanHesapla()
            elif secim == '2':
                program.CevreHesapla()
            else:
                program.AlanveCevreHesapla()
        else:
            YildizKoy()
            print("Hatalı seçim!")
    except Exception:
        print("Hatalı değer")
    finally:
        YildizKoy()
