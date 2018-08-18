# Binding Events
# Example 7-16

import sys
from tkinter import *

def hello(event):
    print('Press twice to exit')

def quit(event):
    print('Hello, I must be going...')
    sys.exit()

widget = Button(None, text='Hello event world! Example 7-16')
widget.pack()

widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)

widget.mainloop()
