import tkinter as tk0
import tkinter.ttk as ttk0
from ttkthemes import ThemedStyle
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
s=ThemedStyle(root)
s.theme_use('breeze')
root.configure(bg="black")
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
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.columnconfigure(6, weight=1)
root.columnconfigure(7, weight=1)
root.columnconfigure(8, weight=1)
root.columnconfigure(9, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

#================================================
#================================================
#================================================

"""
This is where we define our functions. The ones that are related to out buttons, text inputs, and more. Since we have to define out functions first and THEN use them. This could be avoid using classes,
but since we are using a procedural approach, we can't do that as easily (if at all).
"""

def click():
    hey = 9*989
    label3 = tk0.Label(root, text=str(hey))
    label3.pack()

def addsymbol(number):
    current=inputmain.get()
    inputmain.delete(0,tk0.END)
    inputmain.insert(0,current+ str(number))    

#================================================
#================================================
#================================================

"""
This is where we define out buttons. text inputs, and more.
Each widget variable name has a descriptive name. so button-sin is for the sin button.
"""

#=====Input fields and buttons

"""
Note that we are defining fields here as well which act as containers
"""

#-----Main field: where the user enters the operation and takes the previous result

framemain = tk0.Frame(root)

#Same as with root. But with this frame instead
framemain.columnconfigure(0, weight=1)
framemain.columnconfigure(1, weight=1)
framemain.columnconfigure(2, weight=1)
framemain.columnconfigure(3, weight=1)
framemain.rowconfigure(0, weight=1)
framemain.rowconfigure(1, weight=1)
framemain.rowconfigure(2, weight=1)
framemain.rowconfigure(3, weight=1)


buttonmain = tk0.Button(framemain, text="Ans:", state=DISABLED)
inputmainans = tk0.Entry(framemain)
inputmain = tk0.Entry(framemain)

#Here we place our frame on a certain grid position and put our elements inside. We will be doing this several times from now on.
framemain.grid(row=0 ,column=3, rowspan=4, columnspan=4, sticky="nesw")
buttonmain.grid(row=0, column=0, columnspan=1,sticky="nesw")
inputmainans.grid(row=0, column =1,columnspan=3,sticky="nesw")
inputmain.grid(row=1, column=0, rowspan=3, columnspan=4, sticky="nesw")

#-----Notes field
#One button clears the fields. And the other is there for notes (for the user)

framenotes = tk0.Frame(root)
buttonnotes = tk0.Button(framenotes, text="Clear notes!")
inputnotes = tk0.Entry(framenotes)

framenotes.columnconfigure(0, weight=1)
framenotes.columnconfigure(1, weight=1)
framenotes.columnconfigure(2, weight=1)
framenotes.rowconfigure(0, weight=1)
framenotes.rowconfigure(1, weight=1)
framenotes.rowconfigure(2, weight=1)
framenotes.rowconfigure(3, weight=1)

framenotes.grid(row=0, column=0, rowspan=4, columnspan=3, sticky="nesw")
buttonnotes.grid(row=0, column=0, columnspan=3, sticky="nesw")
inputnotes.grid(row=1, column=0, rowspan=3, columnspan=3, sticky="nesw")

#-----Variable assignmnet fields
#This is where we can assign certain values to variables and use them as desired

framevar = tk0.Frame(root)
buttonvar = tk0.Button(framevar, text="Ans:")
inputvar = tk0.Entry(framevar)

framevar.columnconfigure(0, weight=1)
framevar.columnconfigure(1, weight=1)
framevar.columnconfigure(2, weight=1)
framevar.rowconfigure(0, weight=1)
framevar.rowconfigure(1, weight=1)
framevar.rowconfigure(2, weight=1)
framevar.rowconfigure(3, weight=1)

framevar.grid(row=0 ,column=7, rowspan=4, columnspan=3, sticky="nesw")
buttonvar.grid(row=0, column=0, columnspan=3, sticky="nesw")
inputvar.grid(row=1, column=0, rowspan=3, columnspan=3, sticky="nesw")

#=====Calculator Buttons


#This frame is for the 10 numbers and basic operations in addition to places for decimals.
framecalcnumbers = tk0.Frame(root, bg="#24292C")

#Frame configuration
framecalcnumbers.columnconfigure(0, weight=1)
framecalcnumbers.columnconfigure(1, weight=1)
framecalcnumbers.columnconfigure(2, weight=1)
framecalcnumbers.columnconfigure(2, weight=1)
framecalcnumbers.rowconfigure(0, weight=1)
framecalcnumbers.rowconfigure(1, weight=1)
framecalcnumbers.rowconfigure(2, weight=1)
framecalcnumbers.rowconfigure(3, weight=1)
framecalcnumbers.rowconfigure(4, weight=1)

class framecalcbutton:
    def __init__(self, text0, command0):
        self.text0 = text0
        self.command0 = command0
        self.button=tk0.Button(framecalcnumbers, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 14 bold", text=text0, command=lambda: addsymbol(command0))


#The number buttons
#button1=tk0.Button(framecalcnumbers, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 14 bold", text="1", command=add1)
button1=framecalcbutton("1", "1").button
button2=framecalcbutton("2", "2").button
button3=framecalcbutton("3", "3").button
button4=framecalcbutton("4", "4").button
button5=framecalcbutton("5", "5").button
button6=framecalcbutton("6", "6").button
button7=framecalcbutton("7", "7").button
button8=framecalcbutton("8", "8").button
button9=framecalcbutton("9", "9").button
button0=framecalcbutton("0", "0").button
#button2=tk0.Button(framecalcnumbers, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 14 bold", text="2", command=add2)
#button3=tk0.Button(framecalcnumbers, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 14 bold", text="3", command=add3)
#button4=tk0.Button(framecalcnumbers, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 14 bold", text="4", command=add4)
#button5=tk0.Button(framecalcnumbers, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 14 bold", text="5", command=add5)
#button6=tk0.Button(framecalcnumbers, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 14 bold", text="6", command=add6)
#button7=tk0.Button(framecalcnumbers, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 14 bold", text="7", command=add7)
#button8=tk0.Button(framecalcnumbers, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 14 bold", text="8", command=add8)
#button9=tk0.Button(framecalcnumbers, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 14 bold", text="9", command=add9)
#button0=tk0.Button(framecalcnumbers, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 14 bold", text="0", command=add0)

#Operations buttons
buttonpls=tk0.Button(framecalcnumbers, text="+", command=lambda: addsymbol)
buttonmis=tk0.Button(framecalcnumbers, text="-", command=lambda: addsymbol)
buttonmul=tk0.Button(framecalcnumbers, text="*", command=lambda: addsymbol)
buttondiv=tk0.Button(framecalcnumbers, text="/", command=lambda: addsymbol)
buttoneq=tk0.Button(framecalcnumbers, text="=", command=lambda: addsymbol)
buttonpo=tk0.Button(framecalcnumbers, text=".", command=lambda: addsymbol)
buttondec=tk0.Button(framecalcnumbers, text="dec", command=lambda: addsymbol)
buttonclr=tk0.Button(framecalcnumbers, text="clr", command=lambda: addsymbol)
inputdec=tk0.Button(framecalcnumbers,)

#This is where we place them
framecalcnumbers.grid(row=4 ,column=0, rowspan=5, columnspan=3, sticky="nesw") #The frame

button9.grid(row=0, column=0, padx=2, pady=2,sticky="nesw")
button8.grid(row=0, column=1, padx=1, pady=1,sticky="nesw")
button7.grid(row=0, column=2, padx=1, pady=1,sticky="nesw")
button6.grid(row=1, column=0, padx=1, pady=1,sticky="nesw")
button5.grid(row=1, column=1, padx=1, pady=1,sticky="nesw")
button4.grid(row=1, column=2, padx=1, pady=1,sticky="nesw")
button3.grid(row=2, column=0, padx=1, pady=1,sticky="nesw")
button2.grid(row=2, column=1, padx=1, pady=1,sticky="nesw")
button1.grid(row=2, column=2, padx=1, pady=1,sticky="nesw")
button0.grid(row=3, column=1, padx=1, pady=1,sticky="nesw")

buttonpls.grid(row=0, column=3, sticky="nesw")
buttonmis.grid(row=1, column=3, sticky="nesw")
buttonmul.grid(row=2, column=3, sticky="nesw")
buttondiv.grid(row=3, column=3, sticky="nesw")
buttoneq.grid(row=4, column=3, sticky="nesw")
buttonpo.grid(row=3, column=0, sticky="nesw")
buttondec.grid(row=4, column=0, sticky="nesw")
buttonclr.grid(row=3, column=2, sticky="nesw")
inputdec.grid(row=4, column=1, columnspan=2, sticky="nesw")

if __name__=="__main__":
    root.mainloop()
