from PIL import Image, ImageTk
import tkinter
from tkinter import*

class Canvas:
    top = Tk()
    top.geometry("200x200")
    c = Canvas(top,bg = "pink",height = "200",width = 200)
    arc = c.create_arc((5,10,150,200),start = 0,extent = 150, fill= "white")
    c.pack()
    top.mainloop()
    

class UnoGame:
    colors = ["Red", "Green", "Blue", "Yellow", "noColor"]
    vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','Skip', 'Reverse', 'Draw2', 'Draw4', 'Wild']
    deck = []
    def __init__(self):
        self.img = Image.open("blue3.png")
        self.tatras = ImageTk.PhotoImage(self.img)
        canvas = Canvas(self, width=self.img.size[0]+20,
        height=self.img.size[1]+20)
        canvas.create_image(10, 10, anchor=NW, image=self.tatras)
        for i in range(0, 13):
            for x in range(0, 4):
                card = Card(vals[i], colors[x])
                deck.append(card)
        for i in range(14, 16):
            card = Card(vals[i], colors[4])
        

class Deck:
    def __init__(self, color, val):

        for i in fileList:
            card = Card()
class Card:
    def __init__(self, color, val):
        pass
        


# color val image

