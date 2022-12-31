from tkinter import *

"""LABEL"""

# ST - Style

class frame:
    def __init__(self, style:dict, root:Tk, row:int, column:int):
        self.s = {"bg": style["bg"],
                  "bd": style["bd"],
                  "relief": style["relief"],
                  "padx": style["padx"],
                  "pady": style["pady"],
                  "ipadx": style["ipadx"],
                  "ipady": style["ipady"],
                  "sticky": style["sticky"]
                 }
        
        self.root = root
        self.row = row
        self.column = column
        pass

    def display(self):
        frame = Frame(self.root, 
                      bg=self.s["bg"],
                      bd=self.s["bd"], 
                      relief=self.s["relief"])
        frame.grid(row=self.row, column=self.column, padx=self.s["padx"], pady=self.s["pady"], sticky=self.s["sticky"], 
        ipadx=self.s["ipadx"], ipady=self.s["ipady"])

        return frame

class label:
    def __init__(self, style:dict, root:Tk, text:str, row:int, column:int):
        self.s = {"font": style["font"],
                  "justify": style["justify"],
                  "fg": style["fg"],
                  "bg": style["bg"],
                  "bd": style["bd"],
                  "relief": style["relief"],
                  "padx": style["padx"],
                  "pady": style["pady"],
                  "ipadx": style["ipadx"],
                  "ipady": style["ipady"],
                  "sticky": style["sticky"]
                 }
        
        self.root = root
        self.text = text
        self.row = row
        self.column = column
        pass

    def display(self):
        label = Label(self.root,
                     text=self.text,
                     font=self.s["font"],
                     justify=self.s["justify"],
                     fg=self.s["fg"],
                     bg=self.s["bg"],
                     bd=self.s["bd"], 
                     relief=self.s["relief"])
        label.grid(row=self.row, column=self.column, padx=self.s["padx"], pady=self.s["pady"], sticky=self.s["sticky"], 
        ipadx=self.s["ipadx"], ipady=self.s["ipady"])

        return label

class text:
    def __init__(self, style:dict, root:Tk, row:int, column:int):
        self.s = {"font": style["font"],
                  "fg": style["fg"],
                  "bg": style["bg"],
                  "bd": style["bd"],
                  "relief": style["relief"],
                  "padx": style["padx"],
                  "pady": style["pady"],
                  "ipadx": style["ipadx"],
                  "ipady": style["ipady"],
                  "sticky": style["sticky"],
                  "ht": style["ht"]
                 }
        self.root = root
        self.row = row
        self.column = column
        
        pass

    def display(self):
        text = Text(self.root,
                    font=self.s["font"],
                    fg=self.s["fg"],
                    bg=self.s["bg"],
                    bd=self.s["bd"], 
                    relief=self.s["relief"], 
                    highlightthickness=self.s["ht"])
        text.grid(row=self.row, column=self.column, padx=self.s["padx"], pady=self.s["pady"], sticky=self.s["sticky"], 
        ipadx=self.s["ipadx"], ipady=self.s["ipady"])

        return text

class button:
    def __init__(self, style:dict, root:Tk, text:str, row:int, column:int):
        self.s = {"font": style["font"],
                  "justify": style["justify"],
                  "fg": style["fg"],
                  "bg": style["bg"],
                  "bd": style["bd"],
                  "relief": style["relief"],
                  "padx": style["padx"],
                  "pady": style["pady"],
                  "ipadx": style["ipadx"],
                  "ipady": style["ipady"],
                  "sticky": style["sticky"],
                  "af": style["af"],
                  "ab": style["ab"],
                  "ht": style["ht"],
                  "cursor": style["cursor"]}
        self.root = root
        self.text = text
        self.row = row
        self.column = column

        pass

    def display(self):
        button = Button(self.root,
                        text=self.text,
                        font=self.s["font"],
                        justify=self.s["justify"],
                        fg=self.s["fg"],
                        bg=self.s["bg"],
                        bd=self.s["bd"], 
                        relief=self.s["relief"],
                        activeforeground=self.s["af"],
                        activebackground=self.s["ab"],
                        highlightthickness=self.s["ht"],
                        cursor=self.s["cursor"])
        button.grid(row=self.row, column=self.column, padx=self.s["padx"], pady=self.s["pady"], sticky=self.s["sticky"], 
        ipadx=self.s["ipadx"], ipady=self.s["ipady"])

        return button

class listbox:
    def __init__(self, style:dict, root:Tk, row:int, column:int):
        self.s = {"font": style["font"],
                  "justify": style["justify"],
                  "fg": style["fg"],
                  "bg": style["bg"],
                  "bd": style["bd"],
                  "relief": style["relief"],
                  "padx": style["padx"],
                  "pady": style["pady"],
                  "ipadx": style["ipadx"],
                  "ipady": style["ipady"],
                  "sticky": style["sticky"],
                  "sf": style["sf"],
                  "sb": style["sb"],
                  "ht": style["ht"],
                  "cursor": style["cursor"]}
        self.root = root
        self.text = text
        self.row = row
        self.column = column

        pass

    def display(self):
        listbox = Listbox(self.root,
                          font=self.s["font"],
                          justify=self.s["justify"],
                          fg=self.s["fg"],
                          bg=self.s["bg"],
                          bd=self.s["bd"], 
                          relief=self.s["relief"],
                          selectforeground=self.s["sf"],
                          selectbackground=self.s["sb"],
                          highlightthickness=self.s["ht"],
                          cursor=self.s["cursor"], )
        listbox.grid(row=self.row, column=self.column, padx=self.s["padx"], pady=self.s["pady"], sticky=self.s["sticky"], 
        ipadx=self.s["ipadx"], ipady=self.s["ipady"])

        return listbox


def rgb_to_hex(r:int, g:int, b:int):
    hexa = ""

    # To red color
    if r > 0 and r < 16:
        hexa = f"#0{hex(r)[2]}"
    else:
        if r > 256:
            hexa = "#ff"
        elif r > 0:
            hexa = f"#{hex(r)[2:4]}"
        else:
            hexa = "#00"

    # To green color
    if g > 0 and g < 16:
        hexa += f"0{hex(g)[2]}"
    else:
        if g > 256:
            hexa += "ff"
        elif g > 0:
            hexa += f"{hex(g)[2:4]}"
        else:
            hexa += "00"


    # To blue color
    if b > 0 and b < 16:
        hexa += f"0{hex(b)[2]}"
    else:
        if b > 256:
            hexa += "ff"
        elif b > 0:
            hexa += f"{hex(b)[2:4]}"
        else:
            hexa += "00"

    return hexa

