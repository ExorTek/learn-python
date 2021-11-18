class Toplama():
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def Topla(self):
        result = self.sayi1 + self.sayi2
        print(f"Girilen {self.sayi1} ve {self.sayi2} sayılarının toplamı = {result}")

while True:
    secim = input("1- Topla\n2- Çıkış\n3- Seçiminiz: ")
    if secim == '2':
        break
    elif secim == '1':
        try:
            sayi1 = float(input("Sayı1: "))
            sayi2 = float(input("Sayı2: "))
            toplama = Toplama(sayi1, sayi2)
            toplama.Topla()
        except Exception:
            print("Hatalı değer!")
    else:
        print("Hatalı seçim")
