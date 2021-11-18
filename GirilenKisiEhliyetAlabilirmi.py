import datetime


class Program:
    def __init__(self, ad, dogumYili, yas):
        self.ad = ad
        self.dogumYili = dogumYili
        self.yas = yas

    def KontrolEt(self):
        if self.yas >= 18:
            print(f"Merhaba {self.ad} yaşınız : {self.yas} ehliyet alabilirsiniz")
        elif self.yas < 18:
            print(f"Merhaba {self.ad} yaşınız : {self.yas} üzgünüz ehliyet için yaşınız yetersiz")


while True:
    try:
        secim = input("1- Ehliyet alabilmesini kontrol et\n2- Çıkış\nSeçiminiz: ")
        if secim == '2':
            break
        elif secim == '1':
            while True:
                secim2 = input("1- Hesapla\n2- Bir üst menü\nSeçiminiz: ")
                if secim2 == '2':
                    break
                elif secim == '1':
                    ad = str(input("Adınız: "))
                    dogumYili = int(input("Doğum yılınız: "))
                    simdi = datetime.datetime.now()
                    enFazlaYas = 100
                    yas = int(simdi.year - dogumYili)
                    if (yas < enFazlaYas and dogumYili < int(simdi.year)):
                        break
                    elif (yas > enFazlaYas and dogumYili < int(simdi.year)):
                        print("Yaş en fazla 100 olabilir!")
                    else:
                        print("Hatalı doğum yılı!")
            program = Program(ad, dogumYili, yas)
            program.KontrolEt()
        else:
            print("Hatalı seçim")
    except Exception:
        print("Hatalı Değer!")
