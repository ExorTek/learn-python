class Program:
    def __init__(self, sayi):
        self.sayi = sayi

    def KontrolEt(self):
        if self.sayi > 0:
            print(f"Girilen {self.sayi} sayısı pozitif")
        elif self.sayi < 0:
            print(f"Girilen {self.sayi} sayısı negatif")
        else:
            print(f"Girilen {self.sayi} sayısı 0 a eşit!")


while True:
    try:
        secim = input("1- Pozitif mi negatif mi bul\n2- Çıkış\nSeçiminiz: ")
        if secim == '2':
            break
        elif secim == '1':
            sayi = int(input("Sayı: "))
            program = Program(sayi)
            program.KontrolEt()
        else:
            print("Hatalı seçim")
    except Exception:
        print("Hatalı değer")