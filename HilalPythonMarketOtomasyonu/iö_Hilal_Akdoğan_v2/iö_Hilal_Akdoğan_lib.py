import sqlite3

class Urun():
    def __init__(self, urunadi, marka, fiyat, skt, stok):
        self.urunadi=urunadi
        self.marka=marka
        self.fiyat=fiyat
        self.skt=skt
        self.stok=stok

class HilalAkdoganMarketOtomasyon():
    def __init__(self):
        self.Baglan()
        self.Grs = True

    def Baglan(self):
        self.baglanti = sqlite3.connect("iö_Hilal_Akdoğan.db")
        self.cursor=self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS atistirmalik(UrunAdi TEXT,Marka TEXT,Fiyat REAL,SKT TEXT,Stok INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

        sorgu2 = "CREATE TABLE IF NOT EXISTS suturunu(UrunAdi TEXT,Marka TEXT,Fiyat REAL,SKT TEXT,Stok INT)"
        self.cursor.execute(sorgu2)
        self.baglanti.commit()

        sorgu2 = "CREATE TABLE IF NOT EXISTS bakliyat(UrunAdi TEXT,Marka TEXT,Fiyat REAL,SKT TEXT,Stok INT)"
        self.cursor.execute(sorgu2)
        self.baglanti.commit()

    def UrunEkle(self, urunNesnesi):
        self.cursor.execute("Insert Into atistirmalik Values (?,?,?,?,?)", (urunNesnesi.urunadi, urunNesnesi.marka, urunNesnesi.fiyat, urunNesnesi.skt, urunNesnesi.stok,))
        self.baglanti.commit()
    def SUrunEkle(self, urunNesnesiS):
         self.cursor.execute("Insert Into suturunu Values (?,?,?,?,?)", (urunNesnesiS.urunadi, urunNesnesiS.marka, urunNesnesiS.fiyat, urunNesnesiS.skt, urunNesnesiS.stok,))
         self.baglanti.commit()
    def BUrunEkle(self, urunNesnesiB):
         self.cursor.execute("Insert Into bakliyat Values (?,?,?,?,?)", (urunNesnesiB.urunadi, urunNesnesiB.marka, urunNesnesiB.fiyat, urunNesnesiB.skt, urunNesnesiB.stok,))
         self.baglanti.commit()

    def UrunGuncelle(self, urunadi, marka, fiyat, skt, stok, eskiurunadi):
        self.cursor.execute("Update atistirmalik Set UrunAdi = ?, Marka = ?, Fiyat = ?, SKT = ?, Stok = ? Where UrunAdi =?",(urunadi, marka, fiyat, skt, stok, eskiurunadi))
        self.baglanti.commit()
    def SUrunGuncelle(self, urunadi, marka, fiyat, skt, stok, eskiurunadi):
        self.cursor.execute("Update suturunu Set UrunAdi = ?, Marka = ?, Fiyat = ?, SKT = ?,Stok = ? Where UrunAdi =?",(urunadi, marka, fiyat, skt, stok, eskiurunadi))
        self.baglanti.commit()
    def BUrunGuncelle(self, urunadi, marka, fiyat, skt, stok, eskiurunadi):
        self.cursor.execute("Update bakliyat Set UrunAdi = ?, Marka = ?, Fiyat = ?, SKT = ?, Stok = ? Where UrunAdi =?",(urunadi, marka, fiyat, skt, stok, eskiurunadi))
        self.baglanti.commit()

    def TumUrunlerA(self):
        print("Markette Bulunan Ürünler Aşağıda Gösterilmektedir.\n-----------------")
        self.cursor.execute("Select * From atistirmalik")
        urunler = self.cursor.fetchall()
        print("Atıştırmalıklar")
        for i in urunler:
            print(i)
    def TumUrunlerS(self):
        self.cursor.execute("Select * From suturunu")
        urunler = self.cursor.fetchall()
        print("Süt ve Süt Ürünleri")
        for i in urunler:
            print(i)
    def TumUrunlerB(self):
        self.cursor.execute("Select * From bakliyat")
        urunler = self.cursor.fetchall()
        print("Bakliyatlar")
        for i in urunler:
            print(i)

    def UrunAdinaGoreSorguA(self, urunadi):
        self.cursor.execute("Select * From atistirmalik Where UrunAdi = ?", (urunadi,))
        UrunSonuc = self.cursor.fetchall()
        print("Arattığınız Ürün Aşağıda Gösterilmektedir.\n-----------------")
        for i in UrunSonuc:
            for j in i:
                print(j, end=" - ")
            print()
    def UrunAdinaGoreSorguS(self, urunadi):
        self.cursor.execute("Select * From suturunu Where UrunAdi = ?", (urunadi,))
        UrunSonuc = self.cursor.fetchall()
        for i in UrunSonuc:
            for j in i:
                print(j, end=" - ")
            print()
    def UrunAdinaGoreSorguB(self, urunadi):
        self.cursor.execute("Select * From bakliyat Where UrunAdi = ?", (urunadi,))
        UrunSonuc = self.cursor.fetchall()
        for i in UrunSonuc:
            for j in i:
                print(j, end=" - ")
            print()

    def UrunSilA(self, urunadi):
        urunsorgu="SELECT * FROM atistirmalik WHERE UrunAdi = ?"
        self.cursor.execute(urunsorgu, (urunadi,))
        silinecekurun = self.cursor.fetchall()
        if (len(silinecekurun)==0):
            print("Markette Böyle Bir Ürün Bulunmamaktadır!")
        else:
            print("Ürün Silindi!")
        sorgu = "DELETE FROM atistirmalik WHERE UrunAdi = ?"
        self.cursor.execute(sorgu, (urunadi,))
        self.baglanti.commit()
    def UrunSilS(self, urunadi):
        urunsorgu="SELECT * FROM suturunu WHERE UrunAdi = ?"
        self.cursor.execute(urunsorgu, (urunadi,))
        silinecekurun = self.cursor.fetchall()
        if (len(silinecekurun)==0):
            print("Markette Böyle Bir Ürün Bulunmamaktadır!")
        else:
            print("Ürün Silindi!")
        sorgu = "DELETE FROM suturunu WHERE UrunAdi = ?"
        self.cursor.execute(sorgu, (urunadi,))
        self.baglanti.commit()
    def UrunSilB(self, urunadi):
        urunsorgu="SELECT * FROM bakliyat WHERE UrunAdi = ?"
        self.cursor.execute(urunsorgu, (urunadi,))
        silinecekurun = self.cursor.fetchall()
        if (len(silinecekurun)==0):
            print("Markette Böyle Bir Ürün Bulunmamaktadır!")
        else:
            print("Ürün Silindi!")
        sorgu = "DELETE FROM bakliyat WHERE UrunAdi = ?"
        self.cursor.execute(sorgu, (urunadi,))
        self.baglanti.commit()

    def BaglantiyiKes(self):
        self.baglanti.close()
