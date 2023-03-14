ogrenciListesi = [] # Boş bir öğrenci listesi tanımlanıyor. Liste kullanıcıdan alınan veriye göre artacak.

def ogrenciEkle(): # Yeni bir öğrenci ekleme işlemini gerçekleştirir.
    isimSoyisim = input("Öğrencinin adı soyadı: ")
    ogrenciListesi.append(isimSoyisim)
    print(f"{isimSoyisim} isimli öğrenci listeye eklendi.")

def ogrenciSil(): # Var olan bir öğrenciyi listeden silme işlemini gerçekleştirir.
    isimSoyisim = input("Silmek istediğiniz öğrencinin adı soyadı: ")
    if isimSoyisim in ogrenciListesi:
        ogrenciListesi.remove(isimSoyisim)
        print(f"{isimSoyisim} isimli öğrenci listeden silindi.")
    else:
        print(f"{isimSoyisim} isimli öğrenci listede bulunamadı.")

# Öğrenci ekleme işlemi için kullanıcıya seçenekler sunulur ve kullanıcının seçimine göre işlem yapılır.
def cokluOgrenciEkle():
    while True:
        print("1 - Öğrenci ekle")
        print("2 - Çıkış yap")
        secim = input("Seçiminiz: ")
        if secim == "1":
            adSoyad = input("Eklemek istediğiniz öğrencinin adı soyadı: ")
            ogrenciListesi.append(adSoyad)
            print(f"{adSoyad} isimli öğrenci listeye eklendi.")
        elif secim == "2":
            break
        else:
            print("Geçersiz seçim.")
            
# Öğrenci listesindeki tüm öğrencilerin adı soyadı ekrana yazdırılır.
def listeYazdir():
    print("Öğrenci listesi:")
    for ogrenci in ogrenciListesi:
        print(ogrenci)
        
# Kullanıcının girdiği isim soyisime sahip öğrencinin numarası ekrana yazdırılır.
def ogrenciNoBul():
    isimSoyisim = input("Öğrencinin adı soyadı: ")
    if isimSoyisim in ogrenciListesi:
        indeks = ogrenciListesi.index(isimSoyisim)
        print(f"{isimSoyisim} isimli öğrencinin numarası: {indeks+1}")
    else:
        print(f"{isimSoyisim} isimli öğrenci listede bulunamadı.")

# Öğrenci silme işlemi için kullanıcıya seçenekler sunulur ve kullanıcının seçimine göre işlem yapılır.        
def cokluOgrenciSil():
    while True:
        print("1 - Öğrenci sil")
        print("2 - Çıkış yap")
        secim = input("Seçiminiz: ")
        if secim == "1":
            adSoyad = input("Silmek istediğiniz öğrencinin adı soyadı: ")
            if adSoyad in ogrenciListesi:
                ogrenciListesi.remove(adSoyad)
                print(f"{adSoyad} isimli öğrenci listeden silindi.")
            else:
                print(f"{adSoyad} isimli öğrenci listede bulunamadı.")
        elif secim == "2":
            break
        else:
            print("Geçersiz seçim.")
#Öğrenci listesindeki öğrenci sayısını gösterir.
def ogrenciSayisi():
    print(f"Toplam {len(ogrenciListesi)} öğrenci bulunmaktadır.")
# Öğrenci adı soyadında aranan kelimeyi içeren öğrencileri bulur.
def ogrenciAra():
    arananKelime = input("Aramak istediğiniz kelimeyi girin: ")
    eslesenOgrenciler = [ogrenci for ogrenci in ogrenciListesi if arananKelime.lower() in ogrenci.lower()]
    if len(eslesenOgrenciler) == 0:
        print("Eşleşen öğrenci bulunamadı.")
    else:
        print(f"{len(eslesenOgrenciler)} eşleşme bulundu:")
        for ogrenci in eslesenOgrenciler:
            print(ogrenci)
#Liste halinde öğrenci sıralama işlemini gerçekleştirir.
def ogrenciSirala():
    for i, ogrenci in enumerate(ogrenciListesi):
        print(f"{i}: {ogrenci}")
#Kullanıcının girdiği veriye istinaden öğrenci adının güncellenmesini sağlanmaktadır.       
def ogrenciGuncelle():
    ogrenciAdi = input("Bilgilerini güncellemek istediğiniz öğrencinin adı soyadı: ")
    if ogrenciAdi not in ogrenciListesi:
        print(f"{ogrenciAdi} isimli öğrenci listede bulunamadı.")
        return
    yeniBilgi = input("Yeni ad veya numara: ")
    ogrenciIndex = ogrenciListesi.index(ogrenciAdi)
    ogrenciListesi[ogrenciIndex] = yeniBilgi
    print(f"{ogrenciAdi} isimli öğrencinin bilgileri güncellendi.")

while True:
    print("1 - Öğrenci ekle")
    print("2 - Öğrenci sil")
    print("3 - Çoklu öğrenci ekle")
    print("4 - Çoklu öğrenci sil")
    print("5 - Öğrenci sayısı")
    print("6 - Öğrenci ara")
    print("7 - Öğrenci listele")
    print("8 - Öğrenci numarası bul")
    print("9 - Öğrenci bilgileri güncelle")
    print("10 - Çıkış yap")
    secim = input("Seçiminiz: ")
    if secim == "1":
        ogrenciEkle()
    elif secim == "2":
        ogrenciSil()
    elif secim == "3":
        cokluOgrenciEkle()
    elif secim == "4":
        cokluOgrenciSil()
    elif secim == "5":
        ogrenciSayisi()
    elif secim == "6":
        ogrenciAra()
    elif secim == "7":
        listeYazdir()
    elif secim == "8":
        ogrenciNoBul()
    elif secim == "9":
        ogrenciGuncelle()
    elif secim == "10":
        break
    else:
        print("Geçersiz seçim.")
