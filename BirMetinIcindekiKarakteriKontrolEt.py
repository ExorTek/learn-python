def KontrolEt():
    metin = input("Metin: ").lower()
    arananHarf = input("Aranan harf: ").lower()
    for harf in metin:
        if harf == arananHarf:
            print("Harf mevcut!")
            break
        else:
            print("Harf mevcut değil!")


while True:
    secim = input("1- Kontrol et\n2- Çıkış\nSeçiminiz: ")
    if secim == '2':
        break
    elif secim == '1':
        KontrolEt()
