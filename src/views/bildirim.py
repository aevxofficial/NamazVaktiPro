import customtkinter as ctk
from customtkinter import CTkToplevel, CTkFrame
from src.views.widgets import Widgets
from src.core.config import namazVaktiProConfig, configDegistir
import random

class Bildirim(CTkToplevel,Widgets):

    def __init__(self, parent,kalanZaman=False):
        super().__init__(parent)
        
        self.kalanZaman = kalanZaman
        
        self.attributes("-fullscreen", True)
        self.attributes("-topmost", True)
        self.configure(fg_color="#29166B")

        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.grid_columnconfigure((0,1,2,3), weight=1)

        self.icerik()

    def icerik(self):
        
        self.baslikFrame = self.frameGFX("","transparent")
        self.baslikFrame.grid(row=0,column=0,columnspan=4,sticky="we")
        self.baslikFrame.grid_columnconfigure((0,1,2,3), weight=1)
        

        self.baslik = self.labelGFX(
            self.baslikFrame,
            "وَالْحَمْدُ لِلّٰهِ رَبِّ الْعَالَم۪ينَ",
            font=3
        )
        
        self.baslik.grid(row=0,column=0,columnspan=4,pady=10)
        
        hr = self.hr(self.baslikFrame)
        hr.grid(row=1,column=0,columnspan=4,sticky="we")
        
        self.taslak = self.frameGFX("","transparent")
        self.taslak.grid(row=1,column=0,columnspan=4,sticky="n")
        self.taslak.grid_columnconfigure((0,1,2,3), weight=1)
        
        if self.kalanZaman["vakitSaat"] == "vakit":
            self.labelGFX(
                self.taslak,
                self.kalanZaman['sonrakiVakitAdi'],
                "#90A70E",
                font=('Times New Roman', 50)
            ).grid(row=0,column=0,columnspan=4,pady=10)

            self.labelGFX(
                self.taslak,
                "Vakti Girdi",
                font=('Times New Roman', 50)
            ).grid(row=1,column=0,columnspan=4,pady=10)
        else:
            self.labelGFX(
                self.taslak,
                self.kalanZaman['vakit'],
                "#90A70E",
                font=('Times New Roman', 50)
            ).grid(row=0,column=0,columnspan=4,pady=10)

            self.labelGFX(
                self.taslak,
                "Vaktinin Bitmesine Kalan Süre",
                font=('Times New Roman', 50)
            ).grid(row=1,column=0,columnspan=4,pady=10)
            
            self.labelGFX(
                self.taslak,
                self.kalanZaman['vakitSaat'],
                "#90A70E",
                font=('Times New Roman', 50)
                ).grid(row=2,column=0,columnspan=4,pady=10)
        
        self.ekBilgi = self.frameGFX("","transparent")
        self.ekBilgi.grid(row=2,column=0,columnspan=4,sticky="we")
        self.ekBilgi.grid_columnconfigure((0,1,2,3), weight=1)
        
        self.labelGFX(
            self.ekBilgi,
            f"Saat: {self.kalanZaman['saat']}",
            font=('Times New Roman', 50)
        ).grid(row=0,column=0,columnspan=2,pady=10)
        
        self.labelGFX(
            self.ekBilgi,
            f"Sonraki Vakit: {self.kalanZaman['sonrakiVakit']}",
            font=('Times New Roman', 50)
        ).grid(row=0,column=2,columnspan=4,padx=10)
        
        self.namazDurum = self.frameGFX("","transparent")
        self.namazDurum.grid(row=3,column=0,columnspan=4,sticky="we")
        self.namazDurum.grid_columnconfigure((0,1,2,3,4), weight=1)
        
        self.buttonGFX(
            self.namazDurum,
            "Namazı Kıl / Kıldım",
            self.namazKil
        ).grid(row=0,column=2,sticky="w",ipadx=10,ipady=10)

        self.buttonGFX(
            self.namazDurum,
            "Namazı Ertele",
            self.namazErtele
        ).grid(row=0,column=2,sticky="e",ipadx=10,ipady=10)

    def bildirimDialog(self,tus=False):
        self.destroy()
        
        self.dialog = CTkToplevel(self.master)
        self.dialog.attributes("-topmost", True)
        self.dialog.configure(fg_color="#29166B")
        self.dialog.grid_rowconfigure((0,1), weight=1)
        self.dialog.grid_columnconfigure(0, weight=1)
        
        if tus:
            veri = random.choice(namazVaktiProConfig()["namazTrue"])
            configDegistir(bildirim=False)
        else:
            veri = random.choice(namazVaktiProConfig()["namazFalse"])
        
        ayetNo = veri["ayetNo"]
        ayet = veri["ayet"]

        self.labelGFX(
            self.dialog,
            f"{ayetNo}\n{ayet}",
            text_color="#FFFFFF",
            font=("Segoe UI", 20, "bold")
        ).grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        
        self.dialog.after(5000, self.dialog.destroy)

    def namazKil(self):
        self.bildirimDialog(True)

    def namazErtele(self):
        self.bildirimDialog(False)