
class Program:
    def __init__(self, sinav1, sinav2, sinav3):
        self.sinav1 = sinav1
        self.sinav2 = sinav2
        self.sinav3 = sinav3

    def OrtalamaHesapla(self):
        ortalama = round(((self.sinav1 + self.sinav2 + self.sinav3) / 3) ,1)
        if ortalama >= 50:
            gecmeDurumu = "Sınıfı geçti!"
        else:
            gecmeDurumu = "Sınıfta kaldı!"
        print \
            (f"Girilen sınavların ortalaması = {ortalama} Geçme durumu = {gecmeDurumu}")
while True:
    try:
        secim = input("1- Ortalama Hesapla\n2- Çıkış\nSeçiminiz: ")
        if secim == '2':
            break
        elif secim == '1':
            while True:
                sinav1 = float(input("Sınav1: "))
                sinav2 = float(input("Sınav2: "))
                sinav3 = float(input("Sınav3: "))
                if (sinav1 >= 0 and sinav1 <= 100 and sinav2 >= 0 and sinav2 <= 100 and sinav3 >= 0 and sinav3 <= 100):
                    break
                else:
                    print("Sınav notları 0 ve 100 arasında olmalıdır!")
            program = Program(sinav1 ,sinav2 ,sinav3)
            program.OrtalamaHesapla()

        else:
            print("Hatalı Seçim")
    except Exception:
        print("Hatalı değer!")