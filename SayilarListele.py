class Program:
    def __init__(self, baslangic, bitis):
        self.baslangic = baslangic
        self.bitis = bitis

    def CiftListele(self):
        for sayi in range(self.baslangic, self.bitis + 1):
            if sayi % 2 == 0:
                print(sayi)

    def CiftTersListele(self):
        for sayi in range(self.baslangic, self.bitis - 1, -1):
            if sayi % 2 == 0:
                print(sayi)

    def TekListele(self):
        for sayi in range(self.baslangic, self.bitis + 1):
            if sayi % 2 != 0:
                print(sayi)

    def TekTersListele(self):
        for sayi in range(self.baslangic, self.bitis - 1, -1):
            if sayi % 2 != 0:
                print(sayi)

    def SayilariListele(self):
        for sayi in range(self.baslangic, self.bitis + 1):
            print(sayi)

    def SayilariTersListele(self):
        for sayi in range(self.baslangic, self.bitis - 1, -1):
            print(sayi)


def YildizKoy():
    print("*" * 50)


while True:
    try:
        YildizKoy()
        secim = input("1- Tek Listele\n2- Çift Listele\n3- Sayıları Listele\n4- Çıkış\nSeçiminiz: ")
        if secim == '4':
            break
        elif secim in ('1', '2', '3'):
            baslangic = int(input("Başlangıç: "))
            bitis = int(input("Bitiş: "))
            program = Program(baslangic, bitis)
            if baslangic < bitis and secim == '1':
                program.TekListele()
            elif baslangic > bitis and secim == '1':
                program.TekTersListele()
            elif baslangic < bitis and secim == '2':
                program.CiftListele()
            elif baslangic > bitis and secim == '2':
                program.CiftTersListele()
            else:
                if secim == '3':
                    if baslangic < bitis:
                        program.SayilariListele()
                    elif baslangic > bitis:
                        program.SayilariTersListele()
                else:
                    print("Başlangıç ve Bitiş değerleri eşit!")
            YildizKoy()
        else:
            print("Hatalı seçim!")
            YildizKoy()
    except Exception:
        print("Hatalı değer")
        YildizKoy()
