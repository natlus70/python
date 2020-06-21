KDV1 = float(0.18)
KDV2 = float(0.08)
KDV3 = float(0.01)
kDvhesap = input("Kdv Oranı seçiniz: 1= %18 2= %8 3= %1 4= 0. şeklinde giriniz.")
tutar = float(input("Ürünün Fıyatını Giriniz..."))
birim = int(input("Ürünün Miktarını giriniz..."))

    

    
    
def kdvhesaplayıcı1(tutar):
    kdv = tutar*KDV1
    toplam = tutar+kdv
    çıkar = tutar-kdv
    ttoplamkdv = toplam*birim
    ccıkışkdv = çıkar*birim
    kdv1toplam = kdv*birim
    print("Kdv Dahil adet fiyatı = " + str(toplam)) 
    print("Adet Kdv tutarı= " + str(kdv))
    print("Adet Kdv Hariç= " +str(çıkar))
    print("Toplam Kdv Dahil= " +str(ttoplamkdv))  
    print("Toplam Kdv Hariç= "+ str(ccıkışkdv))
    print("Toplam Kdv= " + str(kdv1toplam))

def kdvhesaplayıcı2(tutar):
    kdv = tutar*KDV2
    toplam = tutar+kdv
    çıkar = tutar-kdv
    ttoplamkdv = toplam*birim
    ccıkışkdv = çıkar*birim
    kdv1toplam = kdv*birim
    print("Kdv Dahil adet fiyatı = " + str(toplam)) 
    print("Adet Kdv tutarı= " + str(kdv))
    print("Adet Kdv Hariç= " +str(çıkar))
    print("Toplam Kdv Dahil= " +str(ttoplamkdv))  
    print("Toplam Kdv Hariç= "+ str(ccıkışkdv))
    print("Toplam Kdv= " + str(kdv1toplam))    
     
def kdvhesaplayıcı3(tutar):
    kdv = tutar*KDV3
    toplam = tutar+kdv
    çıkar = tutar-kdv
    ttoplamkdv = toplam*birim
    ccıkışkdv = çıkar*birim
    kdv1toplam = kdv*birim
    print("Kdv Dahil adet fiyatı = " + str(toplam)) 
    print("Adet Kdv tutarı= " + str(kdv))
    print("Adet Kdv Hariç= " +str(çıkar))
    print("Toplam Kdv Dahil= " +str(ttoplamkdv))  
    print("Toplam Kdv Hariç= "+ str(ccıkışkdv))
    print("Toplam Kdv= " + str(kdv1toplam))    



def kdvhesaplayıcı4(tutar):
    kdv = tutar*KDV4
    toplam = tutar+kdv
    çıkar = tutar-kdv
    ttoplamkdv = toplam*birim
    ccıkışkdv = çıkar*birim
    kdv1toplam = kdv*birim
    print("Kdv Dahil adet fiyatı = " + str(toplam)) 
    print("Adet Kdv tutarı= " + str(kdv))
    print("Adet Kdv Hariç= " +str(çıkar))
    print("Toplam Kdv Dahil= " +str(ttoplamkdv))  
    print("Toplam Kdv Hariç= "+ str(ccıkışkdv))
    print("Toplam Kdv= " + str(kdv1toplam))
 
 


if kDvhesap == "1":
    print(kdvhesaplayıcı1(tutar))

elif kDvhesap== "2":
    print(kdvhesaplayıcı2(tutar))
elif kDvhesap == "3":
    print(kdvhesaplayıcı3(tutar))
elif kDvhesap=="4":
    KDV4 = float(input("istediğiniz oranı girin"))
    print(kdvhesaplayıcı4(tutar))
else:
   print("Lütfen Birini Seçiniz...") 
   


