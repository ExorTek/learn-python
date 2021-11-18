from random import randint

hak = 1
puan = 100
uretilenSayi = randint(1, 10)


def YildizKoy():
    print("*" * 50)


while hak < 6:
    try:
        YildizKoy()
        kalanHak = 5 - hak
        tahminEdilen = float(input("Tahmini sayınız: "))
        if tahminEdilen > uretilenSayi:
            print("Aranan sayı aşağıda")
            print(f"Kalan hakkınız = {kalanHak} puanınız = {puan - 20}")
        elif tahminEdilen < uretilenSayi:
            print("Aranan sayı yukarıda")
            print(f"Kalan hakkınız = {kalanHak} puanınız = {puan - 20}")
        elif tahminEdilen == uretilenSayi:
            print(f"{kalanHak} hak kala bildiniz puanınız = {puan}")
            break
        hak += 1
        puan -= 20
    except Exception:
        print("Hatalı değer girişi!")