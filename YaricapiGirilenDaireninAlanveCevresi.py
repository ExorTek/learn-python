import math


class Program:
    def __init__(self, yaricap):
        self.yaricap = yaricap

    def AlanHesapla(self):
        alan = math.pi * (self.yaricap ** 2)
        print(f"Yarıçapı {self.yaricap} olan dairenin alanı = {alan}")

    def CevreHesapla(self):
        cevre = 2 * (math.pi * self.yaricap)
        print(f"Yarıçapı {self.yaricap} olan dairenin çevresi = {cevre}")

    def AlanveCevreHesapla(self):
        alan = math.pi * (self.yaricap ** 2)
        cevre = 2 * (math.pi * self.yaricap)
        print(f"Yarıçapı {self.yaricap} olan dairenin alanı = {alan}")
        print(f"Yarıçapı {self.yaricap} olan dairenin çevresi = {cevre}")


while True:
    secim = input("1- Alan Hesapla\n2- Çevre Hesapla\n3- Alan ve Çevre Hesapla\n4- Çıkış\nSeçiminiz: ")
    if secim == '4':
        break
    elif secim in ('1', '2', '3'):
        yaricap = float(input("Yarıçap: "))
        program = Program(yaricap)
        if secim == '1':
            program.AlanHesapla()
        elif secim == '2':
            program.CevreHesapla()
        else:
            program.AlanveCevreHesapla()
    else:
        print("Hatalı seçim!")
