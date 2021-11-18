class Program:
    def __init__(self, sayi):
        self.sayi = sayi

    def KontrolEt(self):
        asalMi = True
        for i in range(2, self.sayi):
            if self.sayi % i == 0:
                asalMi = False
                break
        if asalMi == True:
            print(f"Girilen {self.sayi} sayısı asal")
        else:
            print(f"Girilen {self.sayi} sayısı asal değil")


def YildizKoy():
    print("*" * 50)


while True:
    try:
        secim = input("1- Asal mı değil mi kontrol et\n2- Çıkış\nSeçiminiz: ")
        if secim == '2':
            break
        elif secim == '1':
            YildizKoy()
            sayi = int(input("Öğrenmek istediğiniz sayı: "))
            program = Program(sayi)
            program.KontrolEt()
        else:
            print("Hatalı seçim!")
    except Exception:
        print("Hatalı değer")
    finally:
        YildizKoy()
