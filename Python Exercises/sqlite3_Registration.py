import _sqlite3
import time as zaman

class ogrenci():

    def __init__(self):
        self.baglanti = _sqlite3.connect("universite.db")
        self.isaretci = self.baglanti.cursor()
        self.tablo_olustur()

    def tablo_olustur(self):
        self.isaretci.execute("create table if not exists universite(kisi TEXT, harfnotu TEXT, durum TEXT)")
        self.baglanti.commit()

    def tablo_veri_ekle(self,kisi,harfnotu,durum):
        self.isaretci.execute("insert into universite values(?,?,?)",(kisi,harfnotu,durum))
        self.baglanti.commit()

    def tablo_veri_cek(self):
        self.isaretci.execute("Select * from universite")
        veri = self.isaretci.fetchall()
        for i in veri:
            print(i)

    def tablo_veri_guncelle(self,eskiisim,yeniisim):
        self.isaretci.execute("update universite set kisi = ? where kisi = ?",(yeniisim,eskiisim))
        self.baglanti.commit()

    def tablo_veri_sil(self,isim):
        self.isaretci.execute("delete from universite where kisi = ?",(isim))
        self.baglanti.commit()

    def not_hesapla(self,vize,final):
        durum = vize*0.4 + final*0.6
        return durum

    def basari_durumu(self,durum):
        if durum > 90:
            return "AA"
        elif durum > 85:
             return "BA"
        elif durum > 80:
             return "BB"
        elif durum > 75:
             return "CB"
        elif durum > 70:
             return "CC"
        elif durum > 65:
             return "DC"
        elif durum >= 60:
             return "DD"
        else:
            return "FF"

ogrenci = ogrenci()
while True:
    secim = input("""
    ******* ...... Universitesine Hosgeldiniz *******
    Veri eklemek icin e'ye
    Veri silmek icin s'ye
    Veri guncellemek icin g'ye 
    cikis icin q'ya basiniz.""")
    if secim == 'q':
        break
    elif secim == 'e':
        isim = input("Ogrencinin adini ve soyadini giriniz:")
        vize = float(input("Ogrencinin vize notunu giriniz:"))
        final = float(input("Ogrencinin final notunu giriniz:"))
        print("Hesaplanıyor",end="")
        for i in range(3):
            zaman.sleep(1)
            print(".",end="")
        print("Başarıyla veri tabanına eklendi")
        durum = ogrenci.not_hesapla(vize,final)
        harf_notu = ogrenci.basari_durumu(durum)
        if durum >= 60:
            ogrenci.tablo_veri_ekle(isim, harf_notu,"Basarili")
        else:
            ogrenci.tablo_veri_ekle(isim, harf_notu,"Basarisiz")
        print("\nGuncel Veri Tabani :")
        ogrenci.tablo_veri_cek()
    elif secim == 's':
        c = input("Silinecek kisinin adini giriniz:")
        ogrenci.tablo_veri_sil(c)
    elif secim == 'g':
        eskiisim = input("degistirilmesi istenen bilgiyi giriniz:")
        yeniisim = input("yeni bilgiyi giriniz:")
        ogrenci.tablo_veri_guncelle(eskiisim,yeniisim)
    else:
        print("Lutfen gecerli bir deger giriniz.")







