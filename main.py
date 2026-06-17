import os
import sys

from src.app import App

# Bismillahirrahmanirrahim
# OOP,src layout customtkinter denemesi

def otomatk_baslat_ayarla():
    if os.name != "nt":return

    try:
        import winreg

        py = sys.executable
        pythonw = os.path.join(os.path.dirname(py), "pythonw.exe")
        start = pythonw if os.path.exists(pythonw) else py

        kod = f'"{start}" "{sys.executable}"'

        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE,
        ) as key:
            winreg.SetValueEx(key, "NamazVaktiPro", 0, winreg.REG_SZ, kod)
    except Exception:
        pass


if __name__ == "__main__":
    otomatk_baslat_ayarla()
    app = App()
    app.mainloop()
