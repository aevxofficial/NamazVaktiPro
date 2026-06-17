import os
import sys
import winreg

if os.name == "nt":
    try:
        def calistir_arkaplan():
            py = sys.executable
            pythonw = os.path.join(os.path.dirname(py), "pythonw.exe")
            start = pythonw if os.path.exists(pythonw) else py
            script = os.path.abspath(__file__)
            kod = f'"{start}" "{script}"'

            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, "NamazVaktiPro", 0, winreg.REG_SZ, kod)

        calistir_arkaplan()
    except Exception:pass

from src.app import App

# Bismillahirrahmanirrahim
# OOP,src layout customtkinter denemesi

if __name__ == "__main__":
    app = App()
    app.mainloop()
