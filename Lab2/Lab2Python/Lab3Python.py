import Lab3
import threading
import tkinter as tk
from tkinter.filedialog import askopenfilename

# Initialise l'application
def init_app():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

def main():
    init_app()

# Classe contenant l'application (tkinter)
class Application(tk.Frame):
    # Initialisation de la fenêtre
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.geometry("400x400")

    # Création de boutons
    def create_widgets(self):
        self.play = tk.Button(self)
        self.play["text"] = "Play/Pause"
        self.play["command"] = lambda: Lab3.sendInput("p")
        self.play.pack(side="top")

        self.rate = tk.Button(self)
        self.rate["text"] = "Change rate"
        self.rate["command"] = lambda: Lab3.sendInput("a")
        self.rate.pack(side="top")


        self.back = tk.Button(self)
        self.back["text"] = "Back"
        self.back["command"] = lambda: Lab3.sendInput("r")
        self.back.pack(side="top")

        self.selectFile = tk.Button(self)
        self.selectFile["text"] = "Select file"
        self.selectFile["command"] = self.select_file
        self.selectFile.pack(side="top")

        self.closePlayer = tk.Button(self)
        self.closePlayer["text"] = "Close video player"
        self.closePlayer["command"] = lambda: Lab3.sendInput("c")
        self.closePlayer.pack(side="top")

        self.quit = tk.Button(self, text="Quit", fg="red",
                              command=self.quit)
        self.quit.pack(side="bottom")

    # Fonction de sélection de fichier
    def select_file(self):
        filename = askopenfilename()
        Lab3.setFile(filename)

    # Fonction pour fermer l'application
    def quit(self):
        Lab3.sendInput("q")
        self.master.destroy()

if __name__ == "__main__":
    main()