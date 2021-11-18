import math

class HesapMakinesi:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def Toplama(self):
        result = self.sayi1 + self.sayi2
        print(f"{self.sayi1} ve {self.sayi2} sayılarının toplamı = {result}")

    def Cikarma(self):
        result = self.sayi1 - self.sayi2
        print(f"{self.sayi1} ve {self.sayi2} sayılarının farkı = {result}")

    def Carpma(self):
        result = self.sayi1 * self.sayi2
        print(f"{self.sayi1} ve {self.sayi2} sayılarının çarpımı = {result}")

    def Bolme(self):
        result = self.sayi1 / self.sayi2
        print(f"{self.sayi1} ve {self.sayi2} sayılarının bölümü = {result}")


class UsAlma(HesapMakinesi):
    def UsHesapla(self):
        result = sayi1 ** sayi2
        print(f"tabanı {sayi1} üs kuvveti {sayi2} olan sayı = {result}")

while True:
    secim = input(
        "1- Toplama\n2- Çıkarma\n3- Çarpma\n4- Bölme\n5- Üs alma\n6- Çıkış\nSeçiminiz: ")
    if secim == '6':
        break
    elif secim in ('1', '2', '3', '4','5'):
        sayi1 = int(input("Sayı1: "))
        sayi2 = int(input("Sayı2: "))
        hesapMakinesi = HesapMakinesi(sayi1, sayi2)
        usHesapla = UsAlma(sayi1, sayi2)
        if secim == '1':
            hesapMakinesi.Toplama()
        elif secim == '2':
            hesapMakinesi.Cikarma()
        elif secim == '3':
            hesapMakinesi.Carpma()
        elif secim == '4':
            hesapMakinesi.Bolme()
        else:
            usHesapla.UsHesapla()
    else:
        print("Hatalı seçim!")
