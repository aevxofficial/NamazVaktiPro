from datetime import date, datetime
from threading import Thread
from time import sleep

class Zaman:
    def tarih(self):
        return date.today()

    def saat(self,st=True):
        tm = datetime.now().second
    
        while True:
            if datetime.now().second != tm:
                if st:
                    return datetime.now().strftime("%H:%M:%S")
                else:
                    return datetime.now().strftime("%H:%M")
            sleep(0.01)


    def asenkronSaat(self, callback):
        def guncelle():
            while True:
                callback(self.saat())
        
        Thread(target=guncelle, daemon=True).start()
