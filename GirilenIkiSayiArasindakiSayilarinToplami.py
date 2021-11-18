class Program:
    def __init__(self, baslangic, bitis):
        self.baslangic = baslangic
        self.bitis = bitis
        self.sayac = 0
        self.ortalama = 0

    def TekToplam(self):
        tekToplam = 0
        if self.baslangic < self.bitis:
            for sayi in range(self.baslangic, self.bitis + 1):
                if sayi % 2 != 0:
                    tekToplam += sayi
            print(f"{self.baslangic} ve {self.bitis} arasındaki tek sayıların toplamı = {tekToplam}")

        elif self.baslangic > self.bitis:
            for sayi in range(self.baslangic, self.bitis - 1, -1):
                if sayi % 2 != 0:
                    tekToplam += sayi
            print(f"{self.bitis} ve {self.baslangic} arasındaki tek sayıların toplamı = {tekToplam}")

        else:
            print("Başlangıç ve bitiş değerleri aynı!")

    def CiftToplam(self):
        ciftToplam = 0
        if self.baslangic < self.bitis:
            for sayi in range(self.baslangic, self.bitis + 1):
                if sayi % 2 == 0:
                    ciftToplam += sayi
            print(f"{self.baslangic} ve {self.bitis} arasındaki çift sayıların toplamı = {ciftToplam}")

        elif self.baslangic > self.bitis:
            for sayi in range(self.baslangic, self.bitis - 1, -1):
                if sayi % 2 != 0:
                    ciftToplam += sayi
            print(f"{self.bitis} ve {self.baslangic} arasındaki çift sayıların toplamı = {ciftToplam}")

        else:
            print("Başlangıç ve bitiş değerleri aynı!")

    def SayilarinToplami(self):
        toplam = 0
        if self.baslangic < self.bitis:
            for sayi in range(self.baslangic, self.bitis + 1):
                toplam += sayi
            print(f"{self.bitis} ve {self.baslangic} arasındaki sayıların toplamı = {toplam}")

        elif self.baslangic > self.bitis:
            for sayi in range(self.baslangic, self.bitis - 1, -1):
                toplam += sayi
            print(f"{self.bitis} ve {self.baslangic} arasındaki çift sayıların toplamı = {toplam}")

        else:
            print("Başlangıç ve bitiş değerleri aynı!")

    def TekSayilarinOrtalamasi(self):
        tekToplam = 0
        if self.baslangic < self.bitis:
            for sayi in range(self.baslangic, self.bitis + 1):
                if sayi % 2 != 0:
                    tekToplam += sayi
                    self.sayac += 1
                    self.ortalama = tekToplam / self.sayac
            print(f"{self.baslangic} ve {self.bitis} arasındaki tek sayıların ortalaması = {self.ortalama}")

        elif self.baslangic > self.bitis:
            for sayi in range(self.baslangic, self.bitis - 1, -1):
                if sayi % 2 != 0:
                    tekToplam += sayi
                    self.sayac += 1
                    self.ortalama = tekToplam / self.sayac
            print(f"{self.bitis} ve {self.baslangic} arasındaki tek sayıların ortalaması = {self.ortalama}")

        else:
            print("Başlangıç ve bitiş değerleri aynı!")

    def CiftSayilarinOrtalamasi(self):
        ciftToplam = 0
        if self.baslangic < self.bitis:
            for sayi in range(self.baslangic, self.bitis + 1):
                if sayi % 2 == 0:
                    ciftToplam += sayi
                    self.sayac += 1
                    self.ortalama = ciftToplam / self.sayac
            print(f"{self.baslangic} ve {self.bitis} arasındaki çift sayıların ortalaması = {self.ortalama}")

        elif self.baslangic > self.bitis:
            for sayi in range(self.baslangic, self.bitis - 1, -1):
                if sayi % 2 != 0:
                    ciftToplam += sayi
                    self.sayac += 1
                    self.ortalama = ciftToplam / self.sayac
            print(f"{self.bitis} ve {self.baslangic} arasındaki çift sayıların ortalaması = {self.ortalama}")

        else:
            print("Başlangıç ve bitiş değerleri aynı!")

    def ToplamSayilarinOrtalamasi(self):
        toplam = 0
        if self.baslangic < self.bitis:
            for sayi in range(self.baslangic, self.bitis + 1):
                toplam += sayi
                self.sayac += 1
                self.ortalama = toplam / self.sayac
            print(f"{self.bitis} ve {self.baslangic} arasındaki sayıların toplamı = {self.ortalama}")

        elif self.baslangic > self.bitis:
            for sayi in range(self.baslangic, self.bitis - 1, -1):
                toplam += sayi
                self.sayac += 1
                self.ortalama = toplam / self.sayac
            print(f"{self.bitis} ve {self.baslangic} arasındaki çift sayıların toplamı = {self.ortalama}")

        else:
            print("Başlangıç ve bitiş değerleri aynı!")


def YildizKoy():
    print("*" * 50)


while True:
    try:
        secim = input("1- Tek sayıların toplamı\n2- Çift sayıların toplamı\n3- Bütün sayıların toplamı\n4- Çift "
                      "sayıların ortalaması\n5- Tek sayıların ortalaması\n6- Bütün sayıların ortalaması\n7- Çıkış\nSeçiminiz: ")
        if secim == '7':
            break
        elif secim in ('1', '2', '3', '4', '5', '6'):
            YildizKoy()
            baslangic = int(input("Başlangıç: "))
            bitis = int(input("Bitiş: "))
            program = Program(baslangic, bitis)
            if secim == '1':
                program.TekToplam()
            elif secim == '2':
                program.CiftToplam()
            elif secim == '3':
                program.SayilarinToplami()
            elif secim == '4':
                program.CiftSayilarinOrtalamasi()
            elif secim == '5':
                program.TekSayilarinOrtalamasi()
            else:
                program.ToplamSayilarinOrtalamasi()
        else:
            print("Hatalı seçim!")
    except Exception:
        print("Hatalı değer!")
    finally:
        YildizKoy()
