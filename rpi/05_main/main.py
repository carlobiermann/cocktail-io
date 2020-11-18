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

        Beschreibung = "Ich bin dein Barkeeper 4.0 \nAnhand der Stimmung und deinem Pegel weiss ich,\nwelchen Drink du jetzt brauchst."

        T = tk.Text(self)
        T.configure(font=('Arial',12), bg="#212121", borderwidth="0")
        T.configure(foreground="#ffffff")
        T.configure(wrap="word")
        T.insert("1.0", Beschreibung)
        T.place(relx=0.083, rely=0.329, relheight=0.34, relwidth=0.821)

        btn = tk.Button(self)
        btn.configure(text="Let's Go!", font=('Arial', 12), borderwidth="0")
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

        Beschreibung = "Zeig mir deine aktuelle Stimmung.\nDie Kamera befindet sich ueber dem Display."

        T = tk.Text(self)
        T.configure(font=('Arial',12), bg="#212121", borderwidth="0")
        T.configure(foreground="#ffffff")
        T.configure(wrap="word")
        T.insert("1.0", Beschreibung)
        T.place(relx=0.083, rely=0.329, relheight=0.34, relwidth=0.821)

        btn = tk.Button(self)
        btn.configure(text="Bereit!", font=('Arial', 12), borderwidth="0")
        btn.configure(bg="#212121", activebackground="#ff6666", foreground="#ffffff")
        btn.configure(command=lambda:master.switch_frame(PageTwo))
        btn.place(relx=0.331, rely=0.731, height=71, width=201)

class PageTwo(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)
        tk.Frame.configure(self, background="#212121")

        lbl1 = tk.Label(self)
        lbl1.configure(text="Es geht gleich los, schaue bitte in die Kamera", font=('Arial', 16, "bold"), bg="#212121")
        lbl1.configure(foreground="#ffffff")
        lbl1.place(relx=0.066, rely=0.172, height=83, width=519)

        lbl2 = tk.Label(self)
        lbl2.configure(activebackground="#f9f9f9")
        lbl2.configure(background="#8e8e8e")
        lbl2.configure(font=('Arial',40), borderwidth="0")
        lbl2.configure(text="3")
        
        #print(emotions.emotionDetection())


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
