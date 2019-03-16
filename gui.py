from tkinter import *

#gui main window
root = Tk()

#create a text label
label1 = Label(root, text = "this is a label")
#place label the first place available
label1.pack()

#Do not close window until user presses the x button
root.mainloop()