from customtkinter import CTk as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton

class Widgets:
    def frameGFX(self,bg="#2A2442",fg="#140644"):

        return CTkFrame(
            self,
            fg_color=fg,
            border_width=1,
            border_color=bg,
            corner_radius=15
        )
    
    def labelGFX(self,frame,text,text_color="white",font=1):
        if font == 1:
            font = ("Segoe UI", 15, "bold")
        elif font == 2:
            font = ("Consolas", 15, "bold")
        elif font == 3:
            font = ("Arial", 30)
            
        if text_color == 1:
            text_color = "#1C1C5E"
        elif text_color == 2:
            text_color = "#00f0ff"
            
        
        return CTkLabel(
            frame,
            text=text,
            text_color=text_color,
            fg_color="transparent",
            anchor="center",
            font=font
        )
    
    def buttonGFX(self,frame=None,text="",command=None):
        if frame == None:frame = self
        
        return CTkButton(
            frame,
            text=text,
            fg_color="#3000F1",
            corner_radius=15,
            font=('Bahnschrift SemiBold Condensed', 25),
            command=command
        )
    
    def hr(self,master=None):
        if master == None:master = self

        return CTkFrame(master, height=2, fg_color="white")