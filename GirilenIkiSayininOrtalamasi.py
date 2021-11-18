class Program:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def OrtalamaHesapla(self):
        ortalama = (self.sayi1 + self.sayi2) / 2
        print(f"{self.sayi1} ve {self.sayi2} sayılarının ortalaması = {ortalama}")


while True:
    secim = input("1- Ortalama Hesapla\n2- Çıkış\n3- Seçiminiz: ")
    if secim == '2':
        break
    elif secim == '1':
        try:
            sayi1 = float(input("Sayı1: "))
            sayi2 = float(input("Sayı2: "))
            program = Program(sayi1, sayi2)
            program.OrtalamaHesapla()
        except Exception:
            print("Hatalı değer!")
    else:
        print("Hatalı seçim")
