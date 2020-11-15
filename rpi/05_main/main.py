#import tkinter as tk

import sys
import run_New

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
        self.geometry("600x450+660+210")
        self.configure(background="#481b5e")
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
        tk.Frame.configure(self, background="#481b5e")

        lbl = tk.Label(self)
        lbl.configure(text="Barkeeper 4.0", font=('Arial', 24, "bold"), bg="#481b5e")
        lbl.place(relx=0.066, rely=0.022, height=51, width=519)

        Beschreibung = "Beschreibungstext bla bla llorem Ipusm Lorem ipsum dolor sit amet, consectetur adipiscing elit,\n\n sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n\n Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

        T = tk.Text(self)
        T.configure(font=('Arial',12), bg="#d5abff", borderwidth="0")
        T.place(relx=0.017, rely=0.176, relheight=0.47, relwidth=0.954)
        T.insert('end', Beschreibung)

        btn = tk.Button(self)
        btn.configure(text="Let's Go!", font=('Arial', 12), borderwidth="0")
        btn.configure(bg="#d5abff", activebackground="#ff6666")
        btn.configure(command=lambda: master.switch_frame(PageOne))
        btn.place(relx=0.38, rely=0.769, height=51, width=141)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=1, relwidth=1)
        tk.Frame.configure(self, background="#481b5e")
        
        lbl = tk.Label(self)
        lbl.configure(text="Barkeeper 4.0", font=('Arial', 24, "bold"), bg="#481b5e")
        lbl.place(relx=0.066, rely=0.022, height=51, width=519)
        
        Beschreibung = "Zeig mir dein Gesicht\nund ich zeig dir deinen Drink ;)\n"
        
        T = tk.Text(self)
        T.configure(font=('Arial',12), bg="#d5abff", borderwidth="0")
        T.place(relx=0.017, rely=0.176, relheight=0.47, relwidth=0.954)
        T.insert('end', Beschreibung)

        btn = tk.Button(self)
        btn.configure(text="Bereit", font=('Arial', 12), borderwidth="0")
        btn.configure(bg="#d5abff", activebackground="#ff6666")
        btn.configure(command=self.routineStart)
        btn.place(relx=0.38, rely=0.769, height=51, width=141)    

    def routineStart(self):
        run_New.emotionDetection()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
