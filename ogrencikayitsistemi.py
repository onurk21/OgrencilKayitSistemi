ogrenciListesi = [] # Boş bir öğrenci listesi tanımlanıyor. Liste kullanıcıdan alınan veriye göre artacak.

def ogrenciEkle(): # Yeni bir öğrenci ekleme işlemini yapar.
    if len(ogrenciListesi) == 0:
        indeks = 1
    else:
        indeks = ogrenciListesi[-1]["numara"] + 1
    adSoyad = input("Eklemek istediğiniz öğrencinin adını ve soyadını giriniz: ")
    adSoyad = adSoyad.title()
    ogrenci = {"ad": adSoyad, "numara": indeks}
    ogrenciListesi.append(ogrenci)
    print(f"{adSoyad} isimli öğrenci listeye eklendi. Numarası: {indeks}")

def ogrenciSil(): # Var olan bir öğrenciyi listeden silme işlemini yapar.
    adSoyad = input("Silmek istediğiniz öğrencinin adı soyadı: ")
    for ogrenci in ogrenciListesi:
        if ogrenci["ad"] == adSoyad.title():
            ogrenciListesi.remove(ogrenci)
            print(f"{adSoyad} isimli öğrenci listeden silindi")
            return
    print(f"{adSoyad} isimli öğrenci listede bulunamadı")
# Öğrenci ekleme veya silme işlemi için kullanıcıya seçenekler sunulur ve kullanıcının seçimine göre işlem yapılır.
def topluOgrenciEkle():
    while True:
        ogrenciSayisi = input("Kaç öğrenci eklemek istiyorsunuz? (Çıkmak için 'q' tuşuna basın)")
        if ogrenciSayisi == 'q':
            break
        try:
            ogrenciSayisi = int(ogrenciSayisi)
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")
            continue
        for i in range(ogrenciSayisi):
            adSoyad = input(f"{i+1}. öğrencinin adını ve soyadını girin: ")
            adSoyad = adSoyad.title()
            indeks = len(ogrenciListesi) + 1
            ogrenci = {"ad": adSoyad, "numara": indeks}
            ogrenciListesi.append(ogrenci)
            print(f"{adSoyad} isimli öğrenci listeye eklendi. Numarası: {indeks}")


def topluOgrenciSil():
    while True:
        ogrenciSayisi = input("Kaç öğrenci silmek istiyorsunuz? (Çıkmak için 'q' tuşuna basın)")
        if ogrenciSayisi == 'q':
            break
        try:
            ogrenciSayisi = int(ogrenciSayisi)
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")
            continue
        for i in range(ogrenciSayisi):
            adSoyad = input(f"{i+1}. öğrencinin adını ve soyadını girin: ")
            adSoyad = adSoyad.title()
            for ogrenci in ogrenciListesi:
                if ogrenci["ad"] == adSoyad:
                    ogrenciListesi.remove(ogrenci)
                    print(f"{adSoyad} isimli öğrenci listeden silindi.")
                    break
            else:
                print(f"{adSoyad} isimli öğrenci listede bulunamadı.")



def cokluOgrenciEkleSilandtoplusilekle():
    while True:
        print("1 - Öğrenci ekle")
        print("2 - Öğrenci sil")
        print("3 - Toplu öğrenci ekle")
        print("4 - Toplu öğrenci sil")
        print("5 - Çıkış yap")
        secim = input("Seçiminiz: ")
        if secim == "1":
            ogrenciEkle()
        elif secim == "2":
            ogrenciSil()
        elif secim == "3":
            topluOgrenciEkle()
        elif secim == "4":
            topluOgrenciSil()

        elif secim == "5":
            break
        else:
            print("Geçersiz seçim.")
        
#Öğrencilerin listesi ekrana yazdırılır numarası ile birlikte. numarayı indeks olarak almakta varsayılan başlangıç indeksi 1 olarak alınmıştır.        
def listeYazdir():
    print("Öğrenci listesi:")
    for ogrenci in ogrenciListesi:
        print(f"{ogrenci['numara']}. {ogrenci['ad']}")

# Kullanıcının girdiği isim soyisime sahip öğrencinin numarası ekrana yazdırılır.
def ogrenciNoBul():
    isimSoyisim = input("Aramak istediğiniz öğrencinin adı soyadı: ")
    for ogrenci in ogrenciListesi:
        if ogrenci["ad"] == isimSoyisim.title():
            print(f"{isimSoyisim} isimli öğrencinin numarası: {ogrenci['numara']}")
            return
    print(f"{isimSoyisim} isimli öğrenci listede bulunamadı.")

#Öğrenci listesindeki öğrenci sayısını gösterir.
def ogrenciSayisi():
    print(f"Toplam {len(ogrenciListesi)} öğrenci bulunmaktadır.")
# Öğrenci adı soyadında aranan kelimeyi içeren öğrencileri bulur.
def ogrenciAra():
    arananKelime = input("Aramak istediğiniz kelimeyi girin: ")
    eslesenOgrenciler = [ogrenci for ogrenci in ogrenciListesi if arananKelime.lower() in ogrenci["ad"].lower()]
    if len(eslesenOgrenciler) == 0:
        print("Eşleşen öğrenci bulunamadı")
    else:
        print(f"{len(eslesenOgrenciler)} eşleşme bulundu:")
        for ogrenci in eslesenOgrenciler:
            print(ogrenci)

def ogrenci_bul(adSoyad, ogrenciListesi):
    for ogrenci in ogrenciListesi:
        if ogrenci["ad"] == adSoyad.title():
            return ogrenci
    return None

#Kullanıcının girdiği veriye istinaden öğrenci adının güncellenmesini sağlanmaktadır. 
def ogrenciAdiGuncelle():
    eskiAdSoyad = input("Güncellemek istediğiniz öğrencinin adı soyadı: ")
    ogrenci = ogrenci_bul(eskiAdSoyad, ogrenciListesi)
    if ogrenci:
        yeniAdSoyad = input("Yeni adı soyadı: ")
        ogrenci["ad"] = yeniAdSoyad.title()
        print(f"{eskiAdSoyad} adlı öğrencinin adı soyadı {yeniAdSoyad} olarak güncellendi")
    else:
        print(f"{eskiAdSoyad} adlı öğrenci listede bulunamadı")


def ogrenci_bull(numara, ogrenciListesi):
    for ogrenci in ogrenciListesi:
        if ogrenci['numara'] == numara:
            return ogrenci
    return None
#Ögrenci isminden ögrencinin numarasını bulma indekse göre bulma işlemi yapar. İndeks varsayılan başlangıcı1 olarak alınmıştır.
def ogrenci_bul2():
    indeks = int(input("Öğrenci numarasını girin: "))
    ogrenci = ogrenci_bull(indeks, ogrenciListesi)
    if ogrenci:
        print("Öğrenci adı:", ogrenci['ad'])
    else:
        print(f"{indeks} numaralı öğrenci bulunamadı")


#Menüleme işlemi yapmaktadır.
while True:
    print("Bu menüden istediğiniz işleve ait numarayı secebilirsiniz. Yapmak istediğiniz işleme ait numarayı yazınızzz")
    print("1 - Öğrenci ekleme işlemi yap")
    print("2 - Öğrenci silme işlemi yap")
    print("3 - Çoklu öğrenci ekleme veya silme işlemi yap")
    print("4 - Öğrenci sayısı")
    print("5 - Öğrenci ara")
    print("6 - Öğrenci listele")
    print("7 - Öğrenci numarası bul")
    print("8 - Öğrenci bilgileri güncelle")
    print("9 - Öğrenci numarasından ögrenci adını ve soyadını bul")
    print("10 - Çıkış yap")
    secim = input("Seçiminiz: ")
    if secim == "1":
        ogrenciEkle()
    elif secim == "2":
        ogrenciSil()
    elif secim == "3":
        cokluOgrenciEkleSilandtoplusilekle()
    elif secim == "4":
        ogrenciSayisi()
    elif secim == "5":
        ogrenciAra()
    elif secim == "6":
        listeYazdir()
    elif secim == "7":
        ogrenciNoBul()
    elif secim == "8":
        ogrenciAdiGuncelle()
    elif secim == "9":
        ogrenci_bul2()
    
    elif secim == "10":
        break
    else:
        print("Geçersiz seçin")
