#Kullanici Hesabi Acma

a = ["ad","soyad","cinsiyet","kullaniciadi","parola","mail","dogumtarihi"]
b = input("Lütfen İsminizi Giriniz:")
while True:
    c = input("Lütfen Cinsiyetinizi Giriniz(E/K):")
    if (c == "E"):
        print("Hoşgeldiniz",b,"Bey")
        break
    elif (c == "K"):
        print("Hoşgeldiniz",b,"Hanım")
        break
    else:
        print("Hata! Lütfen Tekrar Deneyiniz...")
d = input("Kayit olmak ister misiniz?\n(Eger kayit olmazsaniz sitemizin butun kaynaklarindan yararlanamazsiniz.)\nsitemiz aldigi kayitlari kimseyle paylasmamaktadir.(E/H):")        
if (d == "E"):
        while True:
            e = input("Adiniz:")
            f = input("Soyadiniz:")
            g = input("Kullaniciadiniz:")
            
            while True:
                h = input("Parolaniz:")
                j = input("Parolanizi tekrarlayin:")
                if (h == j):
                    break
                else:
                    print("Lutfen parolayi ve tekrarini ayni giriniz.")
            p = input("Sifrenizi unutmaniz durumunda karsılasacagınız ek soruyu seciniz\n(ilkokul ogrtmeninizin adi?:z)\n(en sevdiginiz renk?:x)\n(anne adinizin 3. harfi?:y)")
            if (p == "z"):
                    aa = input("ilkokul ogrtmeninizin adi?:")
            elif (p == "x"):
                    bb = input("en sevdiginiz renk?:")
            else:
                    cc = input("anne adinizin 3. harfi?:")
            k = input("Mail adresiniz:")
            l = input("Dogum tarihiniz:")
            a[0] = e
            a[1] = f
            a[2] = d
            a[3] = g
            a[4] = h
            a[5] = k
            a[6] = l
            print(a)
            i = input("bütün bilgileriniz doğru mu?(E/H):")
            if (i == "E"):
                    print("Sisteme Basariyla Kaydoldunuz...")
                    break
            elif (i == "H"):
                    while True:
                        m = input("Hangi bilginiz yanlis?ad icin(e),soyad icin(f),kullaniciadi icin(g),mail adresi icin(k),dogumtarihi icin(l) tusuna basın.")
                        if (m == "e"):
                            q = input("Yeni Adinizi Girin:")
                            q == a[0]
                        elif (m == "f"):
                            w = input("Yeni Soyadinizi Girin:")
                            w == a[1]
                        elif (m == "g"):
                            n = input("Yeni Kullaniciadinizi Girin:")
                            n == a[2]
                        elif (m == "k"):
                            r = input("Yeni Mail Adresiinizi Girin:")
                            r == a[3]
                        elif (m == "l"):
                            t = input("Yeni Dogum Tarihinizi Girin:")
                            t == a[4]
                        else:
                            print("Hata Lutfen Tekrar deneyiniz")
                        y = input("Degistirilecek baska bir bilginiz var mi?(E/H):")
                        if (y == "H"):
                            print("Butun bilgileriniz basariyla kaydedildi...")
                            break
                        else:
                            print("")
                    break            
                
            else:
                    print("Hata Lutfen Tekrar deneyiniz")
            print(a)
            print("Sisteme girmek icin lutfen kullanici adi ve parolayi giriniz")
            
        while True:
            u = input("Kullanici Adi:")
            o = input("Sifre:")
            if ((u == g) and (o == h)):
                    print("Sisteme giriliyor...")
                    print("Sisteme Hosgeldiniz")
                    break
            elif ((u != g) and (o == h)):
                    print("Yanlis Kullanici Adi\nLutfen tekrar deneyiniz")
            elif ((u == g) and (o != h)):
                    print("Yanlis Parola")
                    print("Sifreyi degistirmek ister misiniz?(E/H)")
                    cevap = input()
                    if (cevap == "E"): 
                        while True:
                            if (p == "z"):
                                dd = input("ilkokul ogrtmeninizin adi?:")
                                if (dd == aa):
                                    break
                                else:
                                    print()
                            elif (p == "x"):
                                ee = input("en sevdiginiz renk?:")
                                if (ee == bb):
                                    break
                                else: 
                                    print()
                            else:
                                ff = input("anne adinizin 3. harfi?:")
                                if (ff == cc):
                                    break
                                else:
                                    print()
                        while True:
                            yeniparola =  input("Yeni Sifrenizi Girin:")
                            yeniparola1 = input("Yeni Sifrenizi Tekrar Girin:")
                            if (yeniparola == yeniparola1):
                                    break
                            else:
                                    print("Lutfen parolayi ve tekrarini ayni giriniz.")
                        print("Lutfen Bekleyin")
                        h = yeniparola
                        print("Sifre Basariyla Kaydedildi")
                    elif (cevap == "H"):
                        print("Lutfen Tekrar Deneyin!")
                    else:
                        print("Hata! Tekrar Deneyin")
            elif ((u != g) and (o != h)):
                    print("Hatali Sifre-Kullanici Adi Kombinasyonu\nLutfen tekrar deneyiniz")
            else:
                    print("HATA Sistem yanlis calisiyor\nLutfen Sayfayi Yenileyin")
elif (d == "H"):
        print("Sisteme giriliyor...")
        print("Kisitli sisteme hosgeldiniz") 
else:  
        print("Hata! Lütfen Tekrar Deneyiniz...")          