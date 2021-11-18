class Program:
    def __init__(self, sayi):
        self.sayi = sayi

    def TekmiCiftmi(self):
        if self.sayi % 2 == 0:
            print(f"Girilen {self.sayi} sayısı çift!")
        else:
            print(f"Girilen {self.sayi} sayısı tek!")


while True:
    try:
        secim = input("1- Tek mi çift mi bul\n2- Çıkış\nSeçiminiz: ")
        if secim == '2':
            break
        elif secim == '1':
            sayi = int(input("Sayı: "))
            program = Program(sayi)
            program.TekmiCiftmi()
        else:
            print("Hatalı seçim")
    except Exception:
        print("Hatalı değer")
