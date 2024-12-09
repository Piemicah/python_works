import tkinter as tk
import tkinter.messagebox as msg

class MyGui:

    def __init__(self):
        self.win = tk.Tk()
        self.button = tk.Button(self.win,
                                text = 'Click on me',
                                command = self.perform
                                ).pack()
        self.win.mainloop()
        
    def perform(self):
        msg.showinfo('Info', 'This is Piemicah')


w = MyGui()