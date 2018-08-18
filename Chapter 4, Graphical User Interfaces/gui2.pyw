# Adding Buttons and Callbacks
# Example 7-10

import sys
from tkinter import *

widget = Button(None, text='Hello widget world', command=sys.exit)
widget.pack()
widget.mainloop()
