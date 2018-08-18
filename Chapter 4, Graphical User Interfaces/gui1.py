# "Hello World" in Four Lines or Less
# Example 7-1

from tkinter import Label                       # get a widget object

widget = Label(None, text='Hello GUI World!')   # make one
widget.pack()                                   # arrange it
widget.mainloop()                               # start event loop
