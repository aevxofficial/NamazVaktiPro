from curl_cffi import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from threading import Thread
import time,os
from src.core.config import namazVaktiProConfig

class NamazVaktiAPI:
    def __init__(self):
        self.vakitler = {}

    sehirUrl = "https://namazvakitleri.diyanet.gov.tr/tr-TR/home/GetRegList?ChangeType=country&CountryId=2&Culture=tr-TR"
    ilceUrl = "https://namazvakitleri.diyanet.gov.tr/tr-TR/home/GetRegList?ChangeType=state&CountryId=2&Culture=tr-TR&StateId="
    baseUrl = "https://namazvakitleri.diyanet.gov.tr"
    
    def mevcutVakit(self):
        if not self.vakitler:
            return "Şehir Ayarlanmadı"
        
        su_an = datetime.now().strftime("%H:%M:%S")

        sonraki_imsak = self.bsDiyanet.find("td",attrs={"itemprop":"description"}).text
        
        def strp(vakit):
            if len(vakit.split(":")) == 2: vakit += ":00"

            return datetime.strptime(vakit, "%H:%M:%S")
        
        if self.vakitler["İmsak"] <= su_an <= self.vakitler["Sabah"]:
            return {
                "vakit":"İmsak",
                "kalanSure":str(strp(self.vakitler["Sabah"]) - strp(su_an))
            }

        elif self.vakitler["Sabah"] <= su_an <= self.vakitler["Öğle"]:
            return {
                "vakit":"Sabah",
                "kalanSure":str(strp(self.vakitler["Öğle"]) - strp(su_an))
            }

        elif self.vakitler["Öğle"] <= su_an <= self.vakitler["İkindi"]:
            return {
                "vakit":"Öğle",
                "kalanSure":str(strp(self.vakitler["İkindi"]) - strp(su_an))
            }

        elif self.vakitler["İkindi"] <= su_an <= self.vakitler["Akşam"]:            
            return {
                "vakit":"İkindi",
                "kalanSure":str(strp(self.vakitler["Akşam"]) - strp(su_an))
            }

        elif self.vakitler["Akşam"] <= su_an <= self.vakitler["Yatsı"]:
            return {
                "vakit":"Akşam",
                "kalanSure":str(strp(self.vakitler["Yatsı"]) - strp(su_an))
            }

        else:
            return {
                "vakit":"Yatsı",
                "kalanSure":str(strp(sonraki_imsak) - strp(su_an))
            }
    
    def asenkronKalanSure(self,callback):
        def guncelle():
            while True:
                callback(self.mevcutVakit()["kalanSure"])
                time.sleep(1)
        
        Thread(target=guncelle, daemon=True).start()

    
    def getirSehir(self):
        self.sehirList = []
        r = requests.get(self.sehirUrl).json()["StateList"]

        for i in r:
            self.sehirList.append({
                "ad": i["SehirAdi"].lower(),
                "id": i["SehirID"]
            })
            
        return self.sehirList
    
    def getirIlce(self, sehir):
        sehir = sehir.lower()
        
        sehirGetir = self.getirSehir()
        
        for i in sehirGetir:
            if i["ad"] == sehir:
                self.sehirNo = i["id"]
                break
        
        self.ilceList = []

        r = requests.get(self.ilceUrl + str(self.sehirNo)).json()["StateRegionList"]
        
        for i in r:
            self.ilceList.append({
                "ad": i["IlceAdi"].lower(),
                "url": i["IlceUrl"]
            })
            
        return self.ilceList
    
    def getirVakit(self):
        
        self.il = namazVaktiProConfig()["il"]
        self.ilce = namazVaktiProConfig()["ilce"]
        
        ilceGetir = self.getirIlce(self.il.lower())
        for i in ilceGetir:
            if i["ad"] == self.ilce.lower():
                self.ilceUrlAdi = i["url"]
                break
        
        r = requests.get(self.baseUrl + self.ilceUrlAdi).text
        
        self.bsDiyanet = BeautifulSoup(r, "html.parser")

        vakitler = self.bsDiyanet.find("div", {"class": "today-pray-times"})
        
        def vakitBul(vakitAdi):
            return vakitler.find("div", {"data-vakit-name": vakitAdi}).text.split("\n")[2]
        
        vakitJson = {
            "İmsak":vakitBul("imsak"),
            "Sabah":vakitBul("gunes"),
            "Öğle":vakitBul("ogle"),
            "İkindi":vakitBul("ikindi"),
            "Akşam":vakitBul("aksam"),
            "Yatsı":vakitBul("yatsi")
        }
        
        self.vakitler = vakitJson

        return vakitJson
