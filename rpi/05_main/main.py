import sys
import emotions
import arduinoI2C


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
     
class barkeeperApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._Frame = None
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", self.endFullscreen)
    
        self.geometry("800x480")
        self.title("Barkeeper 4.0")
        self.configure(bg="#212121")
        self.switchFrame(pageOne)
   
    def endFullscreen(self, event=None):
        self.state = False
        self.attributes("-fullscreen", False)
        return "break"

    def switchFrame(self, frameClass):
        newFrame = frameClass(self)
        if self._Frame is not None:
            self._Frame.destroy()
        self._Frame = newFrame
        self._Frame.place(relx=0.0, rely=0.0, relheight=1,relwidth=1)

class pageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.configure(self, bg="#212121")
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)

        self.heading = tk.Label(master)
        self.heading.configure(text="Der Getränk", font=('Arial', 32, "bold"))
        self.heading.configure(bg="#212121", fg="#ffffff")
        self.heading.place(relx=0.066, rely=0.088, height=83, width=519)

        self.lbl1 = tk.Label(master)
        self.lbl1.configure(bg="#212121", fg="#ffffff")
        self.lbl1.place(relx=0.066, rely=0.344, height=43, width=519)

        self.lbl2 = tk.Label(master)
        self.lbl2.configure(bg="#212121", fg="#ffffff")
        self.lbl2.place(relx=0.066, rely=0.43, height=43, width=519)
        
        self.lbl3 = tk.Label(master)
        self.lbl3.configure(bg="#212121", fg="#ffffff")
        self.lbl3.place(relx=0.066, rely=0.516, height=43, width=519)

        row1 = "Ich bin dein Barkeeper 4.0"
        row2 = "Anhand deiner Stimmung und deinem Pegel"
        row3 = "weiß ich, welchen Drink du jetzt brauchst."

        self.lbl1.configure(text=row1, font=('Arial', 16, "bold"))
        self.lbl2.configure(text=row2, font=('Arial', 16, "bold"))
        self.lbl3.configure(text=row3, font=('Arial', 16, "bold"))

        self.btn = tk.Button(master)
        self.btn.configure(text="Let's Go!", font=('Arial', 12, "bold"))
        self.btn.configure(bg="#212121",activebackground="#ff6666")
        self.btn.configure(foreground="#ffffff")
        self.btn.configure(command=lambda: master.switchFrame(pageTwo))
        self.btn.place(relx=0.331, rely=0.731, height=71, width=201)

class pageTwo(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.configure(self, bg="#212121")
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)

        self.heading = tk.Label(master)
        self.heading.configure(text="Wie ist deine Laune?", font=('Arial', 32, "bold"))
        self.heading.configure(bg="#212121", fg="#ffffff")
        self.heading.place(relx=0.066, rely=0.088, height=83, width=519)

        self.lbl1 = tk.Label(master)
        self.lbl1.configure(bg="#212121", fg="#ffffff")
        self.lbl1.place(relx=0.066, rely=0.344, height=43, width=519)

        self.lbl2 = tk.Label(master)
        self.lbl2.configure(bg="#212121", fg="#ffffff")
        self.lbl2.place(relx=0.066, rely=0.43, height=43, width=519)

        row1 = "Zeig mir deine aktuelle Stimmung."
        row2 = "Die Kamera befindet sich über dem Display."

        self.lbl1.configure(text=row1, font=('Arial', 16, "bold"))
        self.lbl2.configure(text=row2, font=('Arial', 16, "bold"))

        self.btn = tk.Button(master)
        self.btn.configure(text="Weiter", font=('Arial', 12, "bold"))
        self.btn.configure(bg="#212121", activebackground="#ff6666", fg="#ffffff")
        self.btn.configure(command=lambda:master.switchFrame(pageThree))
        self.btn.place(relx=0.331, rely=0.731, height=71, width=201)

class pageThree(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.configure(self, bg="#212121")
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)

        self.heading = tk.Label(master)
        self.heading.configure(text="Drücke auf 'Bereit' und schaue nach dem Countdown in die Kamera")
        self.heading.configure(font=('Arial', 12, "bold"))
        self.heading.configure(bg="#212121", fg="#ffffff")
        self.heading.place(relx=0.017, rely=0.172, height=83, width=579)

        self.lbl = tk.Label(master)
        self.lbl.configure(text="3", font=('Arial',60))
        self.lbl.configure(bg="#212121", fg="#ff6666")
        self.lbl.place(relx=0.198, rely=0.344, height=141, width=350)

        # non visible counter to keep track of time while decr. counter inside routineStart()
        self.counter = tk.IntVar()
        self.counter.set(3)

        self.btn1 = tk.Button(master)
        self.btn1.configure(text="Bereit!", font=('Arial', 12, "bold"))
        self.btn1.configure(bg="#212121", activebackground="#ff6666", fg="#ffffff")
        self.btn1.configure(command=self.startRoutine)
        self.btn1.place(relx=0.331, rely=0.731, height=71, width=201)

        self.btn2 = tk.Button(master)
        self.btn2.configure(text="Weiter", font=('Arial', 12, "bold"))
        self.btn2.configure(bg="#216870", activebackground="#ff6666", fg="#ffffff")
        self.btn2.configure(command=lambda:master.switchFrame(pageFour))
      
    # starting the emotion detection after a countdown of 3 seconds
    def startRoutine(self):
        state = int(self.counter.get())
        if state > 1:
            state = state - 1
            self.lbl.configure(text=str(state))
            self.counter.set(state)
            self.lbl.after(1000, self.startRoutine)
        elif state == 1:
            state = state - 1
            self.lbl.configure(text="Messung läuft", font=('Arial',24))
            self.counter.set(state)
            self.lbl.after(100, self.startRoutine)
        else:
            emoData = emotions.emotionDetection()
            print(emoData)
            self.btn1.place_forget()
            self.btn2.place(relx=0.331, rely=0.731, height=71, width=201)
            self.lbl.configure(text="Messung fertig")

class pageFour(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.configure(self, bg="#212121")
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)

        self.heading = tk.Label(master)
        self.heading.configure(text="Wie ist dein Pegel?")
        self.heading.configure(font=('Arial', 32, "bold"))
        self.heading.configure(bg="#212121", fg="#ffffff")
        self.heading.place(relx=0.066, rely=0.088, height=83, width=519)

        self.lbl1 = tk.Label(master)
        self.lbl1.configure(bg="#212121", fg="#ffffff")
        self.lbl1.place(relx=0.066, rely=0.344, height=43, width=519)

        self.lbl2 = tk.Label(master)
        self.lbl2.configure(bg="#212121", fg="#ffffff")
        self.lbl2.place(relx=0.066, rely=0.43, height=43, width=519)

        row1 = "Finde heraus wie viel Alkohol du schon intus hast"
        row2 = "und puste in das Röhrchen neben der Kamera."

        self.lbl1.configure(text=row1, font=('Arial', 16, "bold"))
        self.lbl2.configure(text=row2, font=('Arial', 16, "bold"))

        self.btn = tk.Button(master)
        self.btn.configure(text="Weiter", font=('Arial', 12, "bold"))
        self.btn.configure(bg="#212121", activebackground="#ff6666", fg="#ffffff")
        self.btn.configure(command=lambda:master.switchFrame(pageFive))
        self.btn.place(relx=0.331, rely=0.731, height=71, width=201)

class pageFive(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.configure(self, bg="#212121")
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)

        self.heading = tk.Label(master)
        self.heading.configure(text="Drücke auf 'Bereit' und puste nach dem Countdown in das Röhrchen.",)
        self.heading.configure(font=('Arial', 12, "bold"))
        self.heading.configure(bg="#212121", fg="#ffffff")
        self.heading.place(relx=0.017, rely=0.172, height=83, width=579)

        self.lbl = tk.Label(master)
        self.lbl.configure(text="3", font=('Arial',60))
        self.lbl.configure(bg="#212121", fg="#ff6666")
        self.lbl.place(relx=0.198, rely=0.344, height=141, width=350)

        self.btn1 = tk.Button(master)
        self.btn1.configure(text="Bereit!", font=('Arial', 12, "bold"))
        self.btn1.configure(bg="#212121", activebackground="#ff6666", fg="#ffffff")
        self.btn1.configure(command=self.startRoutine)
        self.btn1.place(relx=0.331, rely=0.731, height=71, width=201)

        # non visible counter to keep track of time while decr. counter inside routineStart()
        self.counter = tk.IntVar()
        self.counter.set(3)

        self.btn2 = tk.Button(master)
        self.btn2.configure(text="Weiter", font=('Arial', 12, "bold"))
        self.btn2.configure(bg="#216870", activebackground="#ff6666", fg="#ffffff")
        self.btn2.configure(command=lambda:master.switchFrame(pageSix))

    # starting the alcohol detection after a countdown of 3 seconds
    def startRoutine(self):
        state = int(self.counter.get())
        if state > 1:
            state = state - 1
            self.lbl.configure(text=str(state))
            self.counter.set(state)
            self.lbl.after(1000, self.startRoutine)
        elif state == 1:
            state = state - 1
            self.lbl.configure(text="Messung läuft", font=('Arial',24))
            self.counter.set(state)
            self.lbl.after(100, self.startRoutine)
        else:
            # arduino alcohol/sensor detection
            sensorData = arduinoI2C.readSensors() 
            print(sensorData)
            self.btn1.place_forget()
            self.btn2.place(relx=0.331, rely=0.731, height=71, width=201)
            self.lbl.configure(text="Messung fertig")
            # send all data to NN

class pageSix(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.configure(self, bg="#212121")
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)

        self.heading = tk.Label(master)
        self.heading.configure(text="Ergebnis", font=('Arial', 32, "bold"))
        self.heading.configure(bg="#212121", fg="#ffffff")
        self.heading.place(relx=0.017, rely=0.043, height=73, width=579)

        # wait for return from function that analyzes emotion/alcohol data 
        # and puts them into moods and levels of intoxication as strings

        # dummy input from said function
        Stimmung = "heiter"
        StimmungText = "Deine Stimmung ist " + Stimmung + "."
       
        # dummy input from said function
        Pegel = "Einer geht noch!"
        PegelText = "Dein Pegel sagt: '" + Pegel + "'"
        
        self.lbl1 = tk.Label(master)
        self.lbl1.configure(bg="#212121", fg="#ffffff")
        self.lbl1.place(relx=0.017, rely=0.237, height=33, width=579)

        self.lbl2 = tk.Label(master)
        self.lbl2.configure(bg="#212121", fg="#ffffff")
        self.lbl2.place(relx=0.017, rely=0.323, height=33, width=579)
        
        self.lbl3 = tk.Label(master)
        self.lbl3.configure(bg="#212121", fg="#ffffff")
        self.lbl3.place(relx=0.017, rely=0.409, height=33, width=579)

        self.lbl4 = tk.Label(master)
        self.lbl4.configure(bg="#212121", fg="#ffffff")
        self.lbl4.place(relx=0.017, rely=0.774, height=33, width=579)
        
        row1 = StimmungText
        row2 = PegelText
        row3 = "Diese Drinks passen jetzt am besten zu dir:"
        row4 = "Wähle einen aus."

        self.lbl1.configure(text=row1, font=('Arial', 16, "bold"))
        self.lbl2.configure(text=row2, font=('Arial', 16, "bold"))
        self.lbl3.configure(text=row3, font=('Arial', 16, "bold"))
        self.lbl4.configure(text=row4, font=('Arial', 16, "bold"))
       
        # dummy input from neurak network
        auswahlA = "Auswahl A"
        auswahlB = "Auswahl B"
        auswahlC = "Auswahl C"

        self.btn1 = tk.Button(master)
        self.btn1.configure(text=auswahlA, font=('Arial', 12, "bold"))
        self.btn1.configure(bg="#212121", activebackground="#ff6666", fg="#ffffff")
        self.btn1.configure(command=self.drinkA)
        self.btn1.place(relx=0.083, rely=0.559, height=71, width=141)
 
        self.btn2 = tk.Button(master)
        self.btn2.configure(text=auswahlB, font=('Arial', 12, "bold"))
        self.btn2.configure(bg="#212121", activebackground="#ff6666", fg="#ffffff")
        self.btn2.configure(command=self.drinkB)
        self.btn2.place(relx=0.38, rely=0.559, height=71, width=141)

        self.btn3 = tk.Button(master)
        self.btn3.configure(text=auswahlC, font=('Arial', 12, "bold"))
        self.btn3.configure(bg="#212121", activebackground="#ff6666", fg="#ffffff")
        self.btn3.configure(command=self.drinkC)
        self.btn3.place(relx=0.678, rely=0.559, height=71, width=141)
    
        self.btn4 = tk.Button(master)
        self.btn4.configure(text="Weiter", font=('Arial', 12, "bold"))
        self.btn4.configure(bg="#216870", activebackground="#ff6666", fg="#ffffff")
        self.btn4.configure(command=lambda:master.switchFrame(pageSeven))

    def drinkA(self):
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn3.place_forget()
        self.btn4.place(relx=0.38, rely=0.559, height=71, width=141)
        print("Drink A")
        #SEND TO ARDUINO 
        arduinoI2C.sendDrink(1)
    
    def drinkB(self): 
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn3.place_forget()
        self.btn4.place(relx=0.38, rely=0.559, height=71, width=141)
        print("Drink B")
        #SEND TO ARDUINO
        arduinoI2C.sendDrink(2)

    def drinkC(self):
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn3.place_forget()
        self.btn4.place(relx=0.38, rely=0.559, height=71, width=141)
        print("Drink C")
        #SEND TO ARDUINO
        arduinoI2C.sendDrink(3)

class pageSeven(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.configure(self, bg="#212121")
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)

        self.lbl1 = tk.Label(master)
        self.lbl1.configure(text="Dein Drink wird zubereitet", font=('Arial', 16, "bold"))
        self.lbl1.configure(bg="#212121", fg="#ffffff")
        self.lbl1.place(relx=0.066, rely=0.237, height=43, width=519)

        self.lbl2 = tk.Label(master)
        self.lbl2.configure(text="Have Fun!", font=('Arial', 16, "bold"))
        self.lbl2.configure(bg="#212121", fg="#ffffff")
        self.lbl2.place(relx=0.066, rely=0.366, height=43, width=519)

        self.btn = tk.Button(master)
        self.btn.configure(text="Danke", font=('Arial', 12, "bold"))
        self.btn.configure(bg="#212121", activebackground="#ff6666", fg="#ffffff")
        self.btn.configure(command=lambda:master.switchFrame(pageOne))
        self.btn.place(relx=0.331, rely=0.731, height=71, width=201)

if __name__ == "__main__":
    app = barkeeperApp()
    app.mainloop()

