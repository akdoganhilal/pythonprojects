from iö_Hilal_Akdoğan_lib import *
urunNesne = HilalAkdoganMarketOtomasyon()
import time

print("""************************
İŞLEM SEÇİNİZ
_____________________________
1. ÜRÜN EKLE
    a. Atıştırmalıklar
    b. Süt ve Süt Ürünleri
    c. Bakliyatlar
2. ÜRÜN GÜNCELLE
    a. Atıştırmalık Düzenle
    b. Süt Ürünü Düzenle
    c. Bakliyat Düzenle
3. TÜM ÜRÜNLERİ GÖSTER 
4. İSME GÖRE ÜRÜN GÖSTER
    a. Atıştırmalık Ara
    b. Süt Ürünü Ara
    c. Bakliyat Ara
5. ÜRÜN SİL
    a. Atıştırmalık Sil
    b. Süt Ürünü Sil
    c. Bakliyat Sil
_____________________________
Q. ÇIKIŞ
 ************************""")

while True:
    deger=input("İşlem Seçim: ")

    if (deger == "Q" or deger =="q"):
        print("---------------")
        print("Programdan Çıkılmıştır.")
        urunNesne.BaglantiyiKes()
        break

    elif (deger == "1"):
        deger2=input("--> Ürün Türü Seçimi: ")
        if (deger2 == "a" or deger2 =="A"):
            urunadi = input("Ürün Adı:")
            marka = input("Marka:")
            fiyat = float(input("Fiyat:"))
            skt = input("Son Kullanma Tarihi:")
            stok = input("Stok:")
            print("Ürün Ekleniyor...")
            time.sleep(1)
            urunNesnesi = Urun(urunadi, marka, fiyat, skt, stok)
            urunNesne.UrunEkle(urunNesnesi)
            print("Ürün Eklendi!")

        elif (deger2 == "b" or deger2 =="B"):
            urunadi = input("Ürün Adı:")
            marka = input("Marka:")
            fiyat = float(input("Fiyat:"))
            skt = input("Son Kullanma Tarihi:")
            stok = input("Stok:")
            print("Ürün Ekleniyor...")
            time.sleep(1)
            urunNesnesiS = Urun(urunadi, marka, fiyat, skt, stok)
            urunNesne.SUrunEkle(urunNesnesiS)
            print("Ürün Eklendi!")

        elif (deger2 == "c" or deger2 =="C"):
            urunadi = input("Ürün Adı:")
            marka = input("Marka:")
            fiyat = float(input("Fiyat:"))
            skt = input("Son Kullanma Tarihi:")
            stok = input("Stok:")
            print("Ürün Ekleniyor...")
            time.sleep(1)
            urunNesnesiB = Urun(urunadi, marka, fiyat, skt, stok)
            urunNesne.BUrunEkle(urunNesnesiB)
            print("Ürün Eklendi!")

        else:
            print("Geçersiz İşlem!")

    elif (deger == "2"):
        deger2 = input("--> Ürün Türü Seçimi: ")
        if (deger2 == "a" or deger2 == "A"):
            eskiurunadi = input("Güncellemek İstediğiniz Ürünün Adını Giriniz:")
            urunadi = input("Ürün Adı:")
            marka = input("Marka:")
            fiyat = float(input("Fiyat:"))
            skt = input("Son Kullanma Tarihi:")
            stok = input("Stok:")
            print("Ürün Güncelleniyor...")
            time.sleep(1)
            urunNesne.UrunGuncelle(urunadi, marka, fiyat, skt, stok, eskiurunadi)
            print("Ürün Güncellendi!")

        elif (deger2 == "b" or deger2 == "B"):
            eskiurunadi = input("Güncellemek İstediğiniz Ürünün Adını Giriniz:")
            urunadi = input("Ürün Adı:")
            marka = input("Marka:")
            fiyat = float(input("Fiyat:"))
            skt = input("Son Kullanma Tarihi:")
            stok = input("Stok:")
            print("Ürün Güncelleniyor...")
            time.sleep(1)
            urunNesne.SUrunGuncelle(urunadi, marka, fiyat, skt, stok, eskiurunadi)
            print("Ürün Güncellendi!")

        elif (deger2 == "c" or deger2 == "C"):
            eskiurunadi = input("Güncellemek İstediğiniz Ürünün Adını Giriniz:")
            urunadi = input("Ürün Adı:")
            marka = input("Marka:")
            fiyat = float(input("Fiyat:"))
            skt = input("Son Kullanma Tarihi:")
            stok = input("Stok:")
            print("Ürün Güncelleniyor...")
            time.sleep(1)
            urunNesne.BUrunGuncelle(urunadi, marka, fiyat, skt, stok, eskiurunadi)
            print("Ürün Güncellendi!")
        else:
            print("Geçersiz İşlem!")

    elif (deger == "3"):
        urunNesne.TumUrunlerA()
        print("-----------------")
        urunNesne.TumUrunlerS()
        print("-----------------")
        urunNesne.TumUrunlerB()

    elif (deger == "4"):
        deger2 = input("--> Ürün Türü Seçimi: ")
        urunadi = input("Ürün Adı Giriniz:")
        if (deger2 == "a" or deger2 == "A"):
            urunNesne.UrunAdinaGoreSorguA(urunadi)
        elif (deger2 == "b" or deger2 == "B"):
            urunNesne.UrunAdinaGoreSorguS(urunadi)
        elif (deger2 == "c" or deger2 == "C"):
            urunNesne.UrunAdinaGoreSorguB(urunadi)
        else:
            print("Markette Böyle Bir Ürün Bulunmamaktadır!")
    elif (deger == "5"):
        deger2 = input("--> Ürün Türü Seçimi: ")
        if (deger2 == "a" or deger2 == "A"):
            urunadi = input("Silmek İstediğiniz Ürünün Adını Giriniz:")
            urunNesne.UrunSilA(urunadi)
        elif (deger2 == "b" or deger2 == "B"):
            urunadi = input("Silmek İstediğiniz Ürünün Adını Giriniz:")
            urunNesne.UrunSilS(urunadi)
        elif (deger2 == "c" or deger2 == "C"):
            urunadi = input("Silmek İstediğiniz Ürünün Adını Giriniz:")
            urunNesne.UrunSilB(urunadi)

else:
    print("Geçersiz İşlem!")

