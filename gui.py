from tkinter import *

#gui main window
root = Tk()

Welcome_label = Label(root, text="Welcome! Let's pipinstall lul", fg="black")
Domain_label = Label(root, text="Domain", fg="black")
Domain_text = Entry(root)
Install_button = Button(root, text="Install!")

Welcome_label.grid(row=0, columnspan=2, sticky=N)
Domain_label.grid(row=1, sticky=W)
Domain_text.grid(row=1, column=1)
Install_button.grid(row=2, columnspan=2)

# #frame
# TopFrame = Frame(root)
# TopFrame.pack(fill=X)

# #Frame Label
# #create a text label
# label1 = Label(TopFrame, text = "Welcome to pipinstall! Yes, it's pipinstall without a space.", bg="black", fg="white")
# #place label the first place available
# label1.pack(fill=X)
# #button
# button1 = Button(TopFrame, text = "Install!", width = '4', height = '1', bg="gray", fg="black")
# button1.pack(side=RIGHT)

#Do not close window until user presses the x button
root.mainloop()