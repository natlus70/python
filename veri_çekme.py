# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
while True:
    url = imput("url giriniz")
    etiket_bir = input("etiketismini giriniz")
    etiket_2 = input("diğer etiket ismini giriniz")
    etiket_3 = input("sitede bulunan etiket adını giriniz")
    
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content,"html.parser")
    
    Ele_gelen_veri = soup.find_all(etiket_bir,{etiket_2:etiket_3})
    print(Ele_gelen_veri)
    print("-"*20