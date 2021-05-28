import tkinter as tk0
from tkinter.constants import DISABLED

#================================================
#================================================
#================================================

"""
This is the root widget initialization. We imported tkinter as tk0 instead of importing all from tkinter to avoid any potential conflicts.
"""

root = tk0.Tk()
root.title("Test")
rooth=root.winfo_height()
rootw=root.winfo_width()
#root.configure(bg="#08296A")

#================================================
#================================================
#================================================

"""
This is where we configure some stuff.
for example. by giving a weight of number 1 to the mentioned columns, we can
make them dynamically resizeable as the user changes the size of the window.
"""

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
#root.columnconfigure(4, weight=1)
#root.columnconfigure(5, weight=1)
#root.columnconfigure(6, weight=1)
#root.columnconfigure(7, weight=1)
#root.columnconfigure(8, weight=1)
#root.columnconfigure(9, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
#oot.rowconfigure(2, weight=1)
#root.rowconfigure(3, weight=1)
#
##================================================
##================================================
##================================================
#
#"""
#This is where we define our functions. The ones that are related to out buttons, text inputs, and more. Since we have to define out functions first and THEN use them. This could be avoid using classes,
#but since we are using a procedural approach, we can't do that as easily (if at all).
#"""
#
#def click():
#    hey = 9*989
#    label3 = tk0.Label(root, text=str(hey))
#    label3.pack()
#
##================================================
##================================================
##================================================
#
#"""
#This is where we define out buttons. text inputs, and more.
#Each widget variable name has a descriptive name. so button-sin is for the sin button.
#"""
#
##=====Input fields and buttons
#
#"""
#Note that we are defining fields here as well which act as containers
#"""
#
##-----Main field: where the user enters the operation and take the previous result
#
#buttonmain = tk0.Button(root, text="Ans:", state=DISABLED)
#inputmainans = tk0.Entry(root)
#inputmain = tk0.Text(root)
#
##Here we place our frame on a certain grid position and put our elements inside. We will be doing this several times from now on.
#buttonmain.grid(row=0, column=3, columnspan=1,sticky="news")
#inputmainans.grid(row=0, column=4,columnspan=3,sticky="news")
#inputmain.grid(row=1, column=3, rowspan=3, columnspan=4, sticky="news")
#
##-----Notes field
##One button clears the fields. And the other is there for notes (for the user)
#
#buttonnotes = tk0.Button(root, text="Clear notes!")
#inputnotes = tk0.Text(root)
#buttonnotes.grid(row=0, column=0, columnspan=3, sticky="news")
#inputnotes.grid(row=1, column=0, rowspan=3, columnspan=3, sticky="news")
#
##-----Variable assignmnet fields
#
#buttonvar = tk0.Button(root, text="Ans:")
#inputvar = tk0.Text(root)
#
##Here we place our frame on a certain grid position and put our elements inside. We will be doing this several times from now on.
#buttonvar.grid(row=0, column=7, columnspan=3,sticky="news")
#inputvar.grid(row=1, column=7, rowspan=3, columnspan=3, sticky="news")
#
def click():
    pass

frame=tk0.Frame(root)
frame.rowconfigure(0, weight=1) 
frame.rowconfigure(1, weight=1) 
frame.columnconfigure(0, weight=1) 
frame.columnconfigure(1, weight=1) 
frame.grid(row=0, column=2, rowspan=2, columnspan=2, sticky="nesw")

button1 = tk0.Button(root, text="Test", command=click).grid(row=0,column=0, sticky="nesw")
button2 = tk0.Button(root, text="Test", command=click).grid(row=0,column=1, sticky="nesw")
button3 = tk0.Button(frame, text="Test", command=click).grid(row=0,column=0, sticky="nesw")
button4 = tk0.Button(frame, text="Test", command=click).grid(row=0,column=1, sticky="nesw")
button5 = tk0.Button(root, text="Test", command=click).grid(row=1,column=0, sticky="nesw", columnspan=2)
label6 = tk0.Text(frame).grid(row=1,column=0, sticky="nesw", columnspan=2)
#
#================================================
#================================================
#================================================

if __name__=="__main__":
    root.mainloop()
