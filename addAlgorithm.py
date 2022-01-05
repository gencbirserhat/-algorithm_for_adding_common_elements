liste1 = []
liste2 = []
ortak_eleman = []
def girdi_al():
        liste1_eleman_sayisi = int(input("Kaç Elemanlı liste istiyorsunuz: "))
        for i in range(liste1_eleman_sayisi):
                eleman = int(input("Eleman Giriniz: "))
                liste1.append(eleman)
        liste2_eleman_sayisi = int(input("Kaç Elemanlı liste istiyorsunuz: "))
        for i in range(liste2_eleman_sayisi):
                eleman = int(input("Eleman Giriniz: "))
                liste2.append(eleman)
def ortaklari_bul():
        for i in liste1:
                for x in liste2:
                        if x == i:
                                ortak_eleman.append(x)
        print(sum(ortak_eleman))
        
girdi_al()
ortaklari_bul()
               