import counterFunc
from tkinter import *


class barkeeperGUI:
    def __init__(self, master):
        self.master = master
        master.title("Barkeeper 4.0")

        master.geometry('640x480')
        master.config(bg="orange")

        self.label = Label(master, text="Barkeeper 4.0", font=("Arial Bold", 50))
        self.label.pack()

        self.start_button = Button(master, text="Starten", command=self.routineStart)
        self.start_button.pack()

        self.close_button = Button(master, text="Beenden", command=master.quit)
        self.close_button.pack()

        self.T = Text(master,bg="orange", height=10, width=52, font=("Arial", 14))
        self.T.pack()

        Beschreibung = "Willkommen zum Barkeeper der Zukunft :)\n\nWeiterer Dummy-Text um Benutzer/in zu beschreiben was genau getan wird mit diesem Programm usw. Eigentlich fülle ich hier nur grad den Text aus, also kann man an dieser Stelle auch schon mal aufhören zu lesen.\n\nWer einen besseren Textvorschlag hätte kann den gerne an mich weiter reichen."
        self.T.insert(END, Beschreibung)

    def routineStart(self):
        self.T.pack_forget()
        self.start_button.pack_forget()
        counterFunc.counter()

root = Tk()
my_gui = barkeeperGUI(root)
root.mainloop()
