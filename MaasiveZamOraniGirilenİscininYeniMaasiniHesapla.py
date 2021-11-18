class Program:
    def __init__(self, eskiMaas, zamOran):
        self.eskiMaas = eskiMaas
        self.zamOran = zamOran

    def YuzdeliHesapla(self):
        yeniMaas = self.eskiMaas + (self.eskiMaas * self.zamOran)
        print(f"Eski maaşı {self.eskiMaas} zam oranı {self.zamOran} olan işçinin yeni maaşı = {yeniMaas}")

    def NormalHesapla(self):
        yeniMaas = self.eskiMaas + (self.eskiMaas * self.zamOran / 100)
        print(f"Eski maaşı {self.eskiMaas} zam oranı {self.zamOran} olan işçinin yeni maaşı = {yeniMaas}")


while True:
    try:
        secim = input("1- Zam yap\n2- Çıkış\nSeçiminiz: ")
        if secim == '2':
            break
        elif secim == '1':
            zamOranSecim = input("1- Yüzdelik giriş(0.4 gibi)\n2- Normal giriş(40 gibi)\nSeçiminiz: ")
            eskiMaas = float(input("Şuanki maaş: "))
            zamOran = float(input("Zamoran: "))
            if zamOranSecim == '2':
                program = Program(eskiMaas, zamOran)
                program.NormalHesapla()
            elif zamOranSecim == '1':
                program = Program(eskiMaas, zamOran)
                program.YuzdeliHesapla()
            else:
                print("Hatalı seçim")
    except Exception:
        print("Hatalı değer girişi")