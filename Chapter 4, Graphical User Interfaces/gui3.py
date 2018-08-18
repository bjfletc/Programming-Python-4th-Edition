# Adding User-Defined Callback Handlers
# Example 7-12

import sys
from tkinter import *

def quit():
    print('Hello, I must be going...')
    sys.exit()

widget = Button(None, text='Press Me', command=quit)
widget.pack(side=LEFT)
widget.mainloop()
