from customtkinter import CTk
from pystray import Icon, Menu, MenuItem
from PIL import Image
import threading,sys,os

BASE_PATH = getattr(sys, '_MEIPASS', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ICON_PATH = os.path.join(BASE_PATH, 'src', 'assest', 'islam.ico')

from src.views.anasayfa import AnaSayfa
from src.views.ayarlar import Ayarlar
from src.api.namaz_api import NamazVaktiAPI
from src.utils.time_utils import Zaman


class App(CTk):
    def __init__(self):
        super().__init__()
        
        ww = self.winfo_screenwidth() // 5
        wh = self.winfo_screenheight() // 2
        
        self.iconbitmap(ICON_PATH)
        self.title("Namaz Vakti Pro - Aev")

        self.geometry(f"{ww}x{wh}")
        self.resizable(False, False)
        self.configure(fg_color="#1a0f3f")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.namaz = NamazVaktiAPI()
        self.zaman = Zaman()
        
        self.pencereAc()

        self.tray_icon = None
        self.protocol("WM_DELETE_WINDOW", self.gizle_tray)
        self.tray_olustur()
    
    def tray_olustur(self):
        try:
            icon = Image.open(ICON_PATH)
        except:
            icon = Image.new('RGB', (64, 64), color=(41, 22, 107))
        
        menu = Menu(
            MenuItem("Aç", self.pencereAc),
            MenuItem("Ayarlar", self.ayarlarAc),
            MenuItem("Kapat", self.pencereKapat)
        )
        
        self.tray_icon = Icon("Namaz Vakti Pro", icon, menu=menu)
        tray_thread = threading.Thread(target=self.tray_icon.run, daemon=True)
        tray_thread.start()
    
    def gizle_tray(self):
        self.withdraw()
    
    def pencereAc(self, icon=None, item=None):
        if hasattr(self, 'anasayfa'):
            self.anasayfa.grid(row=0, column=0, sticky="nsew")
        else:
            self.anasayfa = AnaSayfa(
                self,
                self.namaz,
                self.zaman
            )
            self.anasayfa.grid(row=0, column=0, sticky="nsew")
        
        self.deiconify()
        self.lift()
        self.focus()
    
    def ayarlarAc(self):
        self.ayarlar = Ayarlar(self)
        self.ayarlar.grid(row=0, column=0, sticky="nsew")
        
        self.deiconify()
        self.lift()
        self.focus()
    
    def pencereKapat(self):
        if self.tray_icon:
            self.tray_icon.stop()
        self.destroy()
