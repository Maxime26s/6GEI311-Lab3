import Lab3
import threading
import tkinter as tk
from tkinter.filedialog import askopenfilename

def init_app():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()



# Initialise les threads du clavier et de la vidéo
def main():
    path = ""
    #init_app()
    
    #path = ""

    #threadApp = threading.Thread(target=init_app)
    threadVideo = threading.Thread(target=Lab3.initPlayer, args=["..\\Example.avi" if len(path) == 0 else path])

    #threadApp.start()
    threadVideo.start()

    #threadApp.join()
    threadVideo.join()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

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

        self.quit = tk.Button(self, text="Quit", fg="red",
                              command=self.quit)
        self.quit.pack(side="bottom")

    def select_file(self):
        filename = askopenfilename()
        Lab3.setFile(filename)

    def quit(self):
        Lab3.sendInput("q")
        self.master.destroy()

if __name__ == "__main__":
    main()