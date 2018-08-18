# Configuring Widget Options and Window Titles
# Example 7-8

from tkinter import *

root = Tk()     # root window

widget = Label(root)
widget.config(text='Hello GUI World. Example 7-8')
widget.pack(side=TOP, expand=YES, fill=BOTH)
root.title('gui1g.pyw')

root.mainloop()
