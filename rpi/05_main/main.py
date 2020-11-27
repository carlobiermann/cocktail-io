import sys
import emotions


try: 
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
     
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry("600x450+676+145")
        self.configure(background="#212121")
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(relx=0.0, rely=0.0, relheight=1,relwidth=1)

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)
        tk.Frame.configure(self, background="#212121")

        lbl = tk.Label(self)
        lbl.configure(text="Der Getrnk", font=('Arial', 32, "bold"), bg="#212121")
        lbl.configure(foreground="#ffffff")
        lbl.place(relx=0.066, rely=0.088, height=83, width=519)

        self.lbl1 = tk.Label(master)
        self.lbl1.configure(background="#212121")
        self.lbl1.configure(borderwidth="0")
        self.lbl1.configure(foreground="#ffffff")
        self.lbl1.place(relx=0.066, rely=0.344, height=43, width=519)

        self.lbl2 = tk.Label(master)
        self.lbl2.configure(background="#212121")
        self.lbl2.configure(borderwidth="0")
        self.lbl2.configure(foreground="#ffffff")
        self.lbl2.place(relx=0.066, rely=0.43, height=43, width=519)
        
        self.lbl3 = tk.Label(master)
        self.lbl3.configure(background="#212121")
        self.lbl3.configure(borderwidth="0")
        self.lbl3.configure(foreground="#ffffff")
        self.lbl3.place(relx=0.066, rely=0.516, height=43, width=519)

        zeile1 = "Ich bin dein Barkeeper 4.0"
        zeile2 = "Anhand deiner Stimmung und deinem Pegel"
        zeile3 = "weiss ich, welchen Drink du jetzt brauchst."

        self.lbl1.configure(text=zeile1, font=('Arial', 16, "bold"), bg="#212121")
        self.lbl2.configure(text=zeile2, font=('Arial', 16, "bold"), bg="#212121")
        self.lbl3.configure(text=zeile3, font=('Arial', 16, "bold"), bg="#212121")

        btn = tk.Button(self)
        btn.configure(text="Let's Go!", font=('Arial', 12, "bold"), borderwidth="0")
        btn.configure(bg="#212121", activebackground="#ff6666", foreground="#ffffff")
        btn.configure(command=lambda: master.switch_frame(PageOne))
        btn.place(relx=0.331, rely=0.731, height=71, width=201)

class PageOne(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)
        tk.Frame.configure(self, background="#212121")

        lbl = tk.Label(self)
        lbl.configure(text="Wie ist deine Laune?", font=('Arial', 32, "bold"), bg="#212121")
        lbl.configure(foreground="#ffffff")
        lbl.place(relx=0.066, rely=0.088, height=83, width=519)

        self.lbl1 = tk.Label(master)
        self.lbl1.configure(background="#212121")
        self.lbl1.configure(borderwidth="0")
        self.lbl1.configure(foreground="#ffffff")
        self.lbl1.place(relx=0.066, rely=0.344, height=43, width=519)

        self.lbl2 = tk.Label(master)
        self.lbl2.configure(background="#212121")
        self.lbl2.configure(borderwidth="0")
        self.lbl2.configure(foreground="#ffffff")
        self.lbl2.place(relx=0.066, rely=0.43, height=43, width=519)

        zeile1 = "Zeig mir deine aktuelle Stimmung."
        zeile2 = "Die Kamera befindet sich ueber dem Display."

        self.lbl1.configure(text=zeile1, font=('Arial', 16, "bold"), bg="#212121")
        self.lbl2.configure(text=zeile2, font=('Arial', 16, "bold"), bg="#212121")

        btn = tk.Button(self)
        btn.configure(text="Weiter", font=('Arial', 12, "bold"), borderwidth="0")
        btn.configure(bg="#212121", activebackground="#ff6666", foreground="#ffffff")
        btn.configure(command=lambda:master.switch_frame(PageTwo))
        btn.place(relx=0.331, rely=0.731, height=71, width=201)

class PageTwo(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)
        tk.Frame.configure(self, background="#212121")

        lbl1 = tk.Label(self)
        lbl1.configure(text="Druecke auf 'Bereit' und schaue nach dem Countdown in die Kamera", font=('Arial', 12, "bold"), bg="#212121")
        lbl1.configure(foreground="#ffffff")
        lbl1.place(relx=0.017, rely=0.172, height=83, width=579)

        self.lbl2 = tk.Label(master)
        self.lbl2.configure(activebackground="#f9f9f9")
        self.lbl2.configure(background="#212121")
        self.lbl2.configure(foreground="#ff6666")
        self.lbl2.configure(font=('Arial',60), borderwidth="0")
        self.lbl2.configure(text="3")
        self.lbl2.place(relx=0.198, rely=0.344, height=141, width=350)

        self.btn = tk.Button(master)
        self.btn.configure(text="Bereit!", font=('Arial', 12, "bold"), borderwidth="0")
        self.btn.configure(bg="#212121", activebackground="#ff6666", foreground="#ffffff")
        self.btn.configure(command=self.routineStart)
        self.btn.place(relx=0.331, rely=0.731, height=71, width=201)

        self.btn2 = tk.Button(master)
        self.btn2.configure(text="Weiter", font=('Arial', 12, "bold"), borderwidth="0")
        self.btn2.configure(bg="#216870", activebackground="#ff6666", foreground="#ffffff")
        self.btn2.configure(command=lambda:master.switch_frame(PageThree))
       
    def routineStart(self):
        stand = int(self.lbl2.cget('text'))
        if stand > 0:
            stand = stand - 1
            self.lbl2.configure(text=str(stand))
            self.lbl2.after(1000, self.routineStart)
        elif stand == 0:
            emotions.emotionDetection()
            self.btn.place_forget()
            self.btn2.place(relx=0.331, rely=0.731, height=71, width=201)
            self.lbl2.configure(text="Messung fertig", font=('Arial',24))

class PageThree(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)
        tk.Frame.configure(self, background="#212121")

        lbl = tk.Label(self)
        lbl.configure(text="Wie ist dein Pegel?", font=('Arial', 32, "bold"), bg="#212121")
        lbl.configure(foreground="#ffffff")
        lbl.place(relx=0.066, rely=0.088, height=83, width=519)

        self.lbl1 = tk.Label(master)
        self.lbl1.configure(background="#212121")
        self.lbl1.configure(borderwidth="0")
        self.lbl1.configure(foreground="#ffffff")
        self.lbl1.place(relx=0.066, rely=0.344, height=43, width=519)

        self.lbl2 = tk.Label(master)
        self.lbl2.configure(background="#212121")
        self.lbl2.configure(borderwidth="0")
        self.lbl2.configure(foreground="#ffffff")
        self.lbl2.place(relx=0.066, rely=0.43, height=43, width=519)

        zeile1 = "Finde heraus wie viel Alkohol du schon intus hast"
        zeile2 = "und puste in das Roehrchen neben der Kamera."

        self.lbl1.configure(text=zeile1, font=('Arial', 16, "bold"), bg="#212121")
        self.lbl2.configure(text=zeile2, font=('Arial', 16, "bold"), bg="#212121")

        btn = tk.Button(self)
        btn.configure(text="Weiter", font=('Arial', 12, "bold"), borderwidth="0")
        btn.configure(bg="#212121", activebackground="#ff6666", foreground="#ffffff")
        btn.configure(command=lambda:master.switch_frame(PageFour))
        btn.place(relx=0.331, rely=0.731, height=71, width=201)

class PageFour(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)
        tk.Frame.configure(self, background="#212121")

        lbl1 = tk.Label(self)
        lbl1.configure(text="Druecke auf 'Bereit' und puste nach dem Countdown in das Roehrchen.", font=('Arial', 12, "bold"), bg="#212121")
        lbl1.configure(foreground="#ffffff")
        lbl1.place(relx=0.017, rely=0.172, height=83, width=579)

        self.lbl2 = tk.Label(master)
        self.lbl2.configure(activebackground="#f9f9f9")
        self.lbl2.configure(background="#212121")
        self.lbl2.configure(foreground="#ff6666")
        self.lbl2.configure(font=('Arial',60), borderwidth="0")
        self.lbl2.configure(text="3")
        self.lbl2.place(relx=0.198, rely=0.344, height=141, width=350)

        self.btn = tk.Button(master)
        self.btn.configure(text="Bereit!", font=('Arial', 12, "bold"), borderwidth="0")
        self.btn.configure(bg="#212121", activebackground="#ff6666", foreground="#ffffff")
        self.btn.configure(command=self.routineStart)
        self.btn.place(relx=0.331, rely=0.731, height=71, width=201)

        self.btn2 = tk.Button(master)
        self.btn2.configure(text="Weiter", font=('Arial', 12, "bold"), borderwidth="0")
        self.btn2.configure(bg="#216870", activebackground="#ff6666", foreground="#ffffff")
        self.btn2.configure(command=lambda:master.switch_frame(PageFive))
       
    def routineStart(self):
        stand = int(self.lbl2.cget('text'))
        if stand > 0:
            stand = stand - 1
            self.lbl2.configure(text=str(stand))
            self.lbl2.after(1000, self.routineStart)
        elif stand == 0:
            # ARDUINO MEASUREMENT
            self.btn.place_forget()
            self.btn2.place(relx=0.331, rely=0.731, height=71, width=201)
            self.lbl2.configure(text="Messung fertig", font=('Arial',24))


class PageFive(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)
        tk.Frame.configure(self, background="#212121")

        lbl = tk.Label(self)
        lbl.configure(text="Ergebnis", font=('Arial', 32, "bold"), bg="#212121")
        lbl.configure(foreground="#ffffff")
        lbl.place(relx=0.066, rely=0.088, height=83, width=519)

        Stimmung = "heiter"
        StimmungText = "Deine Stimmung ist " + Stimmung + ".\n"
        
        Pegel = "Einer geht noch!"
        PegelText = "Dein Pegel sagt: '" + Pegel + "'\n"
        
        Beschreibung = StimmungText + PegelText + "Diese Drinks passen jetzt am besten zu dir.\nWaehle einen aus."

        T = tk.Text(self)
        T.configure(font=('Arial',12), bg="#212121", borderwidth="0")
        T.configure(foreground="#ffffff")
        T.configure(wrap="word")
        T.insert("1.0", Beschreibung)
        T.place(relx=0.182, rely=0.329, relheight=0.211, relwidth=0.64)

        auswahlA = "Auswahl A"
        auswahlB = "Auswahl B"
        auswahlC = "Auswahl C"

        self.btn1 = tk.Button(master)
        self.btn1.configure(text=auswahlA, font=('Arial', 12, "bold"), borderwidth="0")
        self.btn1.configure(bg="#212121", activebackground="#ff6666", foreground="#ffffff")
        self.btn1.configure(command=self.drinkA)
        self.btn1.place(relx=0.083, rely=0.645, height=71, width=141)
 
        self.btn2 = tk.Button(master)
        self.btn2.configure(text=auswahlB, font=('Arial', 12, "bold"), borderwidth="0")
        self.btn2.configure(bg="#212121", activebackground="#ff6666", foreground="#ffffff")
        self.btn2.configure(command=self.drinkB)
        self.btn2.place(relx=0.38, rely=0.645, height=71, width=141)

        self.btn3 = tk.Button(master)
        self.btn3.configure(text=auswahlC, font=('Arial', 12, "bold"), borderwidth="0")
        self.btn3.configure(bg="#212121", activebackground="#ff6666", foreground="#ffffff")
        self.btn3.configure(command=self.drinkC)
        self.btn3.place(relx=0.678, rely=0.645, height=71, width=141)
    
        self.btn4 = tk.Button(master)
        self.btn4.configure(text="Weiter", font=('Arial', 12, "bold"), borderwidth="0")
        self.btn4.configure(bg="#216870", activebackground="#ff6666", foreground="#ffffff")
        self.btn4.configure(command=lambda:master.switch_frame(PageSix))

    def drinkA(self):
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn3.place_forget()
        self.btn4.place(relx=0.38, rely=0.645, height=71, width=141)
        print("Drink A")
        #SEND TO ARDUINO 
    
    def drinkB(self): 
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn3.place_forget()
        self.btn4.place(relx=0.38, rely=0.645, height=71, width=141)
        print("Drink B")
        #SEND TO ARDUINO

    def drinkC(self):
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn3.place_forget()
        self.btn4.place(relx=0.38, rely=0.645, height=71, width=141)
        print("Drink C")
        #SEND TO ARDUINO

class PageSix(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)
        tk.Frame.configure(self, background="#212121")

        lbl1 = tk.Label(self)
        lbl1.configure(text="Dein Drink wird zubereitet", font=('Arial', 12, "bold"), bg="#212121")
        lbl1.configure(foreground="#ffffff")
        lbl1.place(relx=0.066, rely=0.237, height=43, width=519)

        lbl2 = tk.Label(self)
        lbl2.configure(text="Have Fun!", font=('Arial', 12, "bold"), bg="#212121")
        lbl2.configure(foreground="#ffffff")
        lbl2.place(relx=0.066, rely=0.366, height=43, width=519)

        self.btn = tk.Button(master)
        self.btn.configure(text="Danke", font=('Arial', 12, "bold"), borderwidth="0")
        self.btn.configure(bg="#212121", activebackground="#ff6666", foreground="#ffffff")
        self.btn.configure(command=lambda:master.switch_frame(StartPage))
        self.btn.place(relx=0.331, rely=0.731, height=71, width=201)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

