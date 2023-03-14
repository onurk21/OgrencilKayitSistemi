ogrenciListesi = []# Boş bir öğrenci listesi tanımlanıyor. Liste kullanıcıdan alınan veriye göre artacak.
indeks = 1

def ogrenciEkle():# Yeni bir öğrenci ekleme işlemini yapar.
    global indeks
    isimSoyisim = input("Eklemek istediğiniz öğrencinin adını ve soyadını giriniz: ")
    isimSoyisim.title()
    ogrenci = {"ad": isimSoyisim, "indeks": indeks}
    ogrenciListesi.append(ogrenci)
    print(f"{isimSoyisim} isimli öğrenci listeye eklendi. Numarası: {indeks}")
    indeks += 1


def ogrenciSil(): # Var olan bir öğrenciyi listeden silme işlemini yaparrr.
    isimSoyisim = input("Silmek istediğiniz öğrencinin adı soyadı: ")
    if isimSoyisim in ogrenciListesi:
        ogrenciListesi.remove(isimSoyisim)
        print(f"{isimSoyisim} isimli öğrenci jisteden silindi")
    else:
        print(f"{isimSoyisim} isimli öğrenci listede bulunamadıı")

# Öğrenci ekleme işlemi için kullanıcıya seçenekler sunulur ve kullanıcının seçimine göre işlem yapılır.
def cokluOgrenciEkle():
    while True:
        print("1 - Öğrenci ekle")
        print("2 - Çıkış yap")
        secim = input("Seçiminiz: ")
        if secim == "1":
            adSoyad = input("Eklemek istediğini öğrencinin adı soyadı: ")
            ogrenciListesi.append(adSoyad)
            print(f"{adSoyad} isimli öğrenci listeye eklendi")
        elif secim == "2":
            break
        else:
            print("Geersiz seçim")
            
#Öğrencilerin listesi ekrana yazdırılır numarası ile birlikte. numarayı indeks olarak almakta varsayılan başlangıç indeksi 1 olarak alınmıştır.        
def listeYazdir():
    print("Öğrenci listesi:")
    for ogrenci in ogrenciListesi:
        print(f"{ogrenci['indeks']}. {ogrenci['ad']}")

# Kullanıcının girdiği isim soyisime sahip öğrencinin numarası ekrana yazdırılır.
def ogrenciNoBul():
    isimSoyisim = input("Aramak istediğiniz öğrencinin adı soyadı: ")
    if isimSoyisim in ogrenciListesi:
        indeks = ogrenciListesi.index(isimSoyisim)
        print(f"{isimSoyisim} isimli öğrencinin numarası: {indeks}")
    else:
        print(f"{isimSoyisim} isimli öğrenci listede bulunamadı.")

# Öğrenci silme işlemi için kullanıcıya seçenekler sunulur ve kullanıcının seçimine göre işlem yapar.        
def cokluOgrenciSil():
    while True:
        print("1 - Öğrenci sl")
        print("2 - Çıkış yap")
        secim = input("Seçiminiz: ")
        if secim == "1":
            adSoyad = input("Silmek istediğiniz öğrencinin adı soyadı: ")
            if adSoyad in ogrenciListesi:
                ogrenciListesi.remove(adSoyad)
                print(f"{adSoyad} isimli öğrenci listeden silindi.")
            else:
                print(f"{adSoyad} isimli örenci listede bulunamadı.")
        elif secim == "2":
            break
        else:
            print("Geçersiz seçim")
#Öğrenci listesindeki öğrenci sayısını gösterir.
def ogrenciSayisi():
    print(f"Toplam {len(ogrenciListesi)} öğrenci bulunmaktadır.")
# Öğrenci adı soyadında aranan kelimeyi içeren öğrencileri bulur.
def ogrenciAra():
    arananKelime = input("Aramak istediğiniz kelimeyi girin: ")
    eslesenOgrenciler = [ogrenci for ogrenci in ogrenciListesi if arananKelime.lower() in ogrenci.lower()]
    if len(eslesenOgrenciler) == 0:
        print("Eşleşen öğrenci bulunamadı")
    else:
        print(f"{len(eslesenOgrenciler)} eşleşme bulundu:")
        for ogrenci in eslesenOgrenciler:
            print(ogrenci)


#Kullanıcının girdiği veriye istinaden öğrenci adının güncellenmesini sağlanmaktadır. 
      
def ogrenciAdiGuncelle():
    eskiAdSoyad = input("Güncellemek istediniz öğrencinin adı soyadı: ")
    if eskiAdSoyad in ogrenciListesi:
        yeniAdSoyad = input("Yeni adı soyadı: ")
        ogrenciListesi[ogrenciListesi.index(eskiAdSoyad)] = yeniAdSoyad
        print(f"{eskiAdSoyad} adlı öğrencinin adı soyadı {yeniAdSoyad} olarak güncellendi")
    else:
        print(f"{eskiAdSoyad} adlı öğrenci listede bulunamadı")


def ogrenci_bul(indeks, ogrenciListesi):
    for ogrenci in ogrenciListesi:
        if ogrenci['indeks'] == indeks:
            return ogrenci
    return None
#Ögrenci isminden ögrencinin numarasını bulma indekse göre bulma işlemi yapar. İndeks varsayılan başlangıcı1 olarak alınmıştır.
def ogrenci_bul2():
    indeks = int(input("Öğrenci numarasını girin: "))
    ogrenci = ogrenci_bul(indeks, ogrenciListesi)
    if ogrenci:
        print("Öğrenci adı:", ogrenci['ad'])
    else:
        print(f"{indeks} numaralı öğrenci bulunamadı")


#Menüleme işlemi yapmaktadır.
while True:
    print("Bu menüden istediğiniz işleve ait numarayı secebilirsiniz. Yapmak istediğiniz işleme ait numarayı yazınızzz")
    print("1 - Öğrenci ekleme işlemi yap")
    print("2 - Öğrenci silme işlemi yap")
    print("3 - Çoklu öğrenci ekleme işlemi yap")
    print("4 - Çoklu öğrenci silme işlemi yap")
    print("5 - Öğrenci sayısı")
    print("6 - Öğrenci ara")
    print("7 - Öğrenci listele")
    print("8 - Öğrenci numarası bul")
    print("9 - Öğrenci bilgileri güncelle")
    print("10 - Öğrenci numarasından ögrenci adını ve soyadını bul")
    print("11 - Çıkış yap")
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
        ogrenciAdiGuncelle()
    elif secim == "10":
        ogrenci_bul2()
    
    elif secim == "11":
        break
    else:
        print("Geçersiz seçin")
