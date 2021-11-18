class Program:
    def __init__(self, baslangic, bitis, sayi1, sayi2):
        self.baslangic = baslangic
        self.bitis = bitis
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def Hesapla(self):
        YildizKoy()
        if self.baslangic < self.bitis:
            for sayi in range(self.baslangic, self.bitis + 1):
                if sayi % self.sayi1 == 0 and sayi % self.sayi2 == 0:
                    print(f"{self.sayi1} ve {self.sayi2} sayılarına bölünen sayılar = {sayi}")

        elif self.baslangic > self.bitis:
            for sayi in range(self.baslangic, self.bitis - 1, -1):
                if sayi % self.sayi1 == 0 and sayi % self.sayi2 == 0:
                    print(f"{self.sayi1} ve {self.sayi2} sayılarına bölünen sayılar = {sayi}")

        else:
            print("Başlangıç ve bitiş değerleri eşit!")
        YildizKoy()


def YildizKoy():
    print("*" * 50)


while True:
    try:
        secim = input("1- Bölünenleri Hesapla\n2- Çıkış\nSeçiminiz: ")
        if secim == '2':
            break
        elif secim == '1':
            baslangic = int(input("Başlangıç: "))
            bitis = int(input("Bitiş: "))
            sayi1 = int(input("Sayı1: "))
            sayi2 = int(input("Sayı2: "))
            program = Program(baslangic, bitis, sayi1, sayi2)
            program.Hesapla()
        else:
            print("Hatalı seçim!")
    except Exception:
        print("Hatalı değer!")
