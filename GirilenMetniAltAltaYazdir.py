class Program:
    def __init__(self, metin):
        self.metin = metin

    def Listele(self):
        for harf in metin:
            print(harf)

def YildizKoy():
    print("*" * 50)
while True:
    try:
        YildizKoy()
        secim = input("1- Alt alta yazdır\n2- Çıkış\nSeçiminiz: ")
        if secim == '2':
            break
        elif secim == '1':
            metin = input("Metni giriniz: ")
            if len(metin) > 0:
                program = Program(metin)
                program.Listele()
            else:
                print("metin en az 1 karakter içermelidir!")
        else:
            print("Hatalı seçim!")
    except Exception:
        print("Hata oluştu")
    finally:
        YildizKoy()