# GUI Basics
# Example 1-27

from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):                 # inheret init
    def reply(self):
        showinfo(title='popup', message='Ouch!')

if __name__ == '__main__':
    CustomGui().pack()
    mainloop()
