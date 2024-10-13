karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
import random






while True:
    hesap =input("hangi dosya için sifre istersin?/n")
    if hesap == "çıkış":
        break
    sayi = int(input("kaç karakterli bir şifre istersin?/n"))
    sifre = ""
    for i in range(sayi):
        sifre += random.choice(karakterler)
    with open("sifreler.txt","a") as file:
        file.write(f"{hesap} : {sifre}/n")
        print(f"{hesap} : {sifre}")

print(sifre)