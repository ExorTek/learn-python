class Program:
    def __init__(self, vize, final):
        self.vize = vize
        self.final = final

    def OrtalamaHesapla(self):
        ortalama = (self.vize * 0.4) + (self.final * 0.6)
        print(f"Girilen {self.vize} ve {self.final} notlarının ortalaması = {ortalama}")


while True:
    try:
        secim = str(input("1- Ortalama Hesapla\n2- Çıkış\n3- Seçiminiz: "))
        if secim == '2':
            break
        elif secim == '1':
            while True:
                vize = float(input("Vize: "))
                final = float(input("Final: "))
                if (vize >= 0 and vize <= 100 and final >= 0 and final <= 100):
                    break
                else:
                    print("Sınav notları 0 ve 100 arasında olmalıdır!")
            program = Program(vize, final)
            program.OrtalamaHesapla()
        else:
            print("Hatalı seçim!")
    except Exception:
        print("Hatalı değer!")
