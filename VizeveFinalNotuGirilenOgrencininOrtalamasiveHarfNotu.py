class Program:
    def __init__(self, vize, final):
        self.vize = vize
        self.final = final

    def OrtalamaHesapla(self):
        ortalama = int((self.vize * 0.4) + (self.final * 0.6))
        if 100 >= ortalama >= 85:
            harfNotu = "AA"
        elif 85 >= ortalama >= 75:
            harfNotu = "BA"
        elif 75 >= ortalama >= 70:
            harfNotu = "BB"
        elif 70 >= ortalama >= 60:
            harfNotu = "CB"
        elif 60 >= ortalama >= 50:
            harfNotu = "CC"
        elif 50 >= ortalama >= 40:
            harfNotu = "DC"
        elif 40 >= ortalama >= 30:
            harfNotu = "DD"
        elif 30 >= ortalama >= 20:
            harfNotu = "FD"
        elif 20 >= ortalama >= 0:
            harfNotu = "FF"
        else:
            print("Hatalı ortalama")
        print(f"Girilen öğrencinin ortalaması = {ortalama} harfnotu = {harfNotu}")


while True:
    try:
        secim = input("1- Ortalama Hesapla\n2- Çıkış\nSeçiminiz: ")
        if secim == '2':
            break
        elif secim == '1':
            while True:
                vize = int(input("Vize: "))
                final = int(input("Final: "))
                if 0 <= vize <= 100 and 0 <= final <= 100:
                    break
                else:
                    print("Hatalı not girişi!")
            program = Program(vize, final)
            program.OrtalamaHesapla()
        else:
            print("Hatalı seçim!")
    except Exception:
        print("Hatalı değer!")
