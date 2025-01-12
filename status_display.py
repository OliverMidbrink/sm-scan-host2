import tkinter as tk
import time

class StatusDisplay(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.frame = tk.Frame(self.master, height=400)
        self.frame.grid(row=0, column=0)
        self.label = tk.Label(self.frame, text = 'New Window', font=("ARIAL", 40, "bold"))
        self.label.grid(row=0, column=0, pady=(300, 0))

        self.frame.pack()
        
        self.last_text=""
        self.last_bg=""

    def show_status(self, bg, text, duration):
        if self.last_bg == bg and self.last_text == text:
            return
        self.last_bg = bg
        self.last_text = text
        self.frame['bg'] = bg
        self.parent['bg'] = bg
        self.label['bg'] = bg
        self.label['text'] = text
        self.update()
        time.sleep(duration)


        

