import time as zaman
import random as rastgele

class Winamp():
    def __init__(self,sarkilar = []):
        self.sarkilar = sarkilar
        self.durum = True
        self.ses = 100
        self.calansarki = ""
    def sesarttir(self):
        if(self.ses >= 96):
            self.ses = 100
        else:
            print("Ses arttiriliyor.")
            zaman.sleep(2)
            self.ses += 5
            print("Ses arttirildi. Guncel Ses = {}".format(self.ses))
    def sesazalt(self):
        if(self.ses <= 4):
            self.ses = 0
        else:
            print("Ses azaltiliyor.")
            zaman.sleep(2)
            self.ses -= 5
            print("Ses azaltildi. Guncel Ses = {}".format(self.ses))
    def sarkiekle(self,sarki):
        self.sarkilar.append(sarki)
    def sarkilistesi(self):
        print(self.sarkilar)
    def sarkisec(self):
        sayac = 1
        for i in self.sarkilar:
            print("{}.{}".format(sayac,i))
            sayac += 1
        secim = int(input("Sarki Numarasini Giriniz:"))
        zaman.sleep(2)
        self.calansarki = self.sarkilar [secim-1]
        print("Calan Sarki = {}".format(self.calansarki))
    def rastgelesarki(self):
        rastgelesayi = rastgele.randint(0,len(self.sarkilar))
        self.calansarki = self.sarkilar[rastgelesayi]
    def kapa(self):
        self.durum = False
    def sarkisil(self):
        secim= int(input("Silmek istediginiz Sarki Numarasini Giriniz:"))
        self.sarkilar.pop(secim-1)
    def bilgilerigoster(self):
        print("""
                Sarki Listesi = {}
                Calan Sarki = {}
                Ses = {}
                Durum = {}
                
                1- Sarki Sec
                2- Ses Arttir
                3- Ses Azalt
                4- Rastgele Sarki Sec
                5- Sarki ekle 
                6- Sarki sil
                7- Kapat """.format(self.sarkilar,self.calansarki,self.ses,self.durum))




o1 = Winamp(sarkilar = ["Talking Heads - Psycho Killer"])

while o1.durum:
    o1.bilgilerigoster()
    secim= int(input("Seciminizi girebilirsiniz"))
    if(secim == 1):
        o1.sarkisec()
    elif(secim == 2):
        o1.sesarttir()
    elif (secim == 3):
        o1.sesazalt()
    elif (secim == 4):
        o1.rastgelesarki()
    elif (secim == 5):
        sarki = input("Sarki giriniz:")
        o1.sarkiekle(sarki)
    elif (secim == 6):
        o1.sarkisil()
    elif (secim == 7):
        o1.kapa()
    else:
        print("Tekrar deneyiniz...")


