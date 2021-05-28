import tkinter as tk0
import tkinter.ttk as ttk0
from ttkthemes import ThemedStyle
from tkinter.constants import DISABLED
from sympy import *

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
root.configure(bg="#24292C")
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
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)
root.rowconfigure(8, weight=1)
root.rowconfigure(9, weight=1)

#================================================
#================================================
#================================================

"""
This is where we define our functions. The ones that are related to out buttons, text inputs, and more. 
We defined them here since we have to define out functions first and THEN use them. This could be avoided using classes,
but since we are using a procedural approach, we can't do that as easily (if at all).
"""
def clearnotes():
    inputnotes.delete("1.0", "end-1c")

def clearinput():
    inputmain.delete(0,tk0.END)

def addsymbol(symbol):
    current=inputmain.get()
    inputmain.delete(0,tk0.END)
    inputmain.insert(0,current+ str(symbol))    

def evaluateinput():
    inputmainans.configure(state="normal") #make the answer field read and write
    ans=eval(inputmain.get()) # To evaluate The Mathimatical operation
    #inputmain.delete(0,tk0.END) # To Delete The Mathimatical operation #This line could be turned on if we want to remove the previous operation made by the user
    inputmainans.delete(0, tk0.END) #This is to delete the previous answer
    inputmainans.insert(0,ans) # To Insert The Answer 
    inputmainans.configure(state="readonly") #make the answer field readonly
#================================================
#================================================
#================================================

"""
This is where we define out buttons. text inputs, and more.
Each widget variable name has a descriptive name. so button-sin is for the sin button.
"""

#=====Input fields and buttons

"""
Note that we are defining frames here as well which act as containers
"""

#-----Main field: where the user enters the operation and takes the previous result

framemain = tk0.Frame(root, bg="#24292C")


#Same as with root. But with this frame instead
framemain.columnconfigure(0, weight=1)
framemain.columnconfigure(1, weight=1)
framemain.columnconfigure(2, weight=1)
framemain.columnconfigure(3, weight=1)
framemain.rowconfigure(0, weight=1)
framemain.rowconfigure(1, weight=1)
framemain.rowconfigure(2, weight=1)
framemain.rowconfigure(3, weight=1)


buttonmain = tk0.Button(framemain, text="Ans:", state=DISABLED, bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, disabledforeground="#2293D6") 

inputmainans = tk0.Entry(framemain, bg="#323739", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, readonlybackground="#323739") 

inputmain = tk0.Entry(framemain, bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, insertbackground="#2293D6", width=framemain.winfo_width()) 


#Here we place our frame on a certain grid position and put our elements inside. We will be doing this several times from now on.
framemain.grid(row=0 ,column=0, rowspan=4,      padx=2, pady=2,columnspan=4, sticky="nesw")

buttonmain.grid(row=0, column=0, columnspan=1,  padx=1, pady=1,sticky="nesw")
inputmainans.grid(row=0, column =1,columnspan=3,padx=1, pady=1,sticky="nesw")
inputmain.grid(row=1, column=0, rowspan=3,      padx=1, pady=1,columnspan=4, sticky="nesw")

#-----Notes field
#One button clears the fields. And the other is there for notes (for the user)

framenotes = tk0.Frame(root, bg="#24292C")
buttonnotes = tk0.Button(framenotes,bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, text="Clear notes!", command=clearnotes)
inputnotes = tk0.Text(framenotes,bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, insertbackground="#2293D6", width=framemain.winfo_width(), height=(framemain.winfo_height())*3/4)

framenotes.columnconfigure(0, weight=1)
framenotes.columnconfigure(1, weight=1)
framenotes.columnconfigure(2, weight=1)
framenotes.rowconfigure(0, weight=1)
framenotes.rowconfigure(1, weight=1)
framenotes.rowconfigure(2, weight=1)
framenotes.rowconfigure(3, weight=1)

framenotes.grid(row=0, column=4, rowspan=4,     columnspan=3,padx=2, pady=2, sticky="nesw")
buttonnotes.grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky="nesw")
inputnotes.grid(row=1, column=0, rowspan=3,     padx=1, pady=1, columnspan=3, sticky="nesw")

#-----Variable assignmnet fields
#This is where we can assign certain values to variables and use them as desired

framevar = tk0.Frame(root, bg="#24292C")
buttonvar = tk0.Button(framevar, text="Ans:", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0)
inputvar = tk0.Entry(framevar)

framevar.columnconfigure(0, weight=1)
framevar.columnconfigure(1, weight=1)
framevar.columnconfigure(2, weight=1)
framevar.rowconfigure(0, weight=1)
framevar.rowconfigure(1, weight=1)
framevar.rowconfigure(2, weight=1)
framevar.rowconfigure(3, weight=1)

framevar.grid(row=0 ,column=7, rowspan=4, columnspan=3,padx=2, pady=2, sticky="nesw")
buttonvar.grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky="nesw")
inputvar.grid(row=1, column=0, rowspan=3,     padx=1, pady=1, columnspan=3, sticky="nesw")

#=====Calculator Buttons
#This frame is for the 10 numbers, certain symbols, and basic operations in addition to places for decimals.
framecalcnumbers = tk0.Frame(root, bg="#24292C")

#And these twos frames are for functions (like sin, cos, etc)
framecalcfuncs1= tk0.Frame(root, bg="#24292C")
framecalcfuncs2= tk0.Frame(root, bg="#24292C")

#Frames configuration
framecalcnumbers.columnconfigure(0, weight=1)
framecalcnumbers.columnconfigure(1, weight=1)
framecalcnumbers.columnconfigure(2, weight=1)
framecalcnumbers.columnconfigure(3, weight=1)
framecalcnumbers.rowconfigure(0, weight=1)
framecalcnumbers.rowconfigure(1, weight=1)
framecalcnumbers.rowconfigure(2, weight=1)
framecalcnumbers.rowconfigure(3, weight=1)
framecalcnumbers.rowconfigure(4, weight=1)
framecalcnumbers.rowconfigure(5, weight=1)

framecalcfuncs1.columnconfigure(0, weight=1)
framecalcfuncs1.columnconfigure(1, weight=1)
framecalcfuncs1.columnconfigure(2, weight=1)
framecalcfuncs1.rowconfigure(0, weight=1)
framecalcfuncs1.rowconfigure(1, weight=1)
framecalcfuncs1.rowconfigure(2, weight=1)
framecalcfuncs1.rowconfigure(3, weight=1)
framecalcfuncs1.rowconfigure(4, weight=1)
framecalcfuncs1.rowconfigure(5, weight=1)

framecalcfuncs2.columnconfigure(0, weight=1)
framecalcfuncs2.columnconfigure(1, weight=1)
framecalcfuncs2.columnconfigure(2, weight=1)
framecalcfuncs2.rowconfigure(0, weight=1)
framecalcfuncs2.rowconfigure(1, weight=1)
framecalcfuncs2.rowconfigure(2, weight=1)
framecalcfuncs2.rowconfigure(3, weight=1)
framecalcfuncs2.rowconfigure(4, weight=1)
framecalcfuncs2.rowconfigure(5, weight=1)

#Here, we defined some classes to create buttons with certain colors and properties instead of having to always define them inline
class framecalcbutton:
    """
    This class makes buttons with certain color and style in general. But we can issue different commands and names to any object we define using this class.
    """
    def __init__(self, text0, command0):
        self.text0 = text0
        self.button=tk0.Button(framecalcnumbers, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 12 bold", text=text0, command=lambda: eval(command0))

class framefuncbutton1:
    """Same as above"""
    def __init__(self, text0, command0):
        self.text0 = text0
        self.button=tk0.Button(framecalcfuncs1, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 12 bold", text=text0, command=lambda: eval(command0))

class framefuncbutton2:
    """Same as above"""
    def __init__(self, text0, command0):
        self.text0 = text0
        self.button=tk0.Button(framecalcfuncs2, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 12 bold", text=text0, command=lambda: eval(command0))

#The number buttons
button1=framecalcbutton("1", "addsymbol(\"1\")").button
button2=framecalcbutton("2", "addsymbol(\"2\")").button
button3=framecalcbutton("3", "addsymbol(\"3\")").button
button4=framecalcbutton("4", "addsymbol(\"4\")").button
button5=framecalcbutton("5", "addsymbol(\"5\")").button
button6=framecalcbutton("6", "addsymbol(\"6\")").button
button7=framecalcbutton("7", "addsymbol(\"7\")").button
button8=framecalcbutton("8", "addsymbol(\"8\")").button
button9=framecalcbutton("9", "addsymbol(\"9\")").button
button0=framecalcbutton("0", "addsymbol(\"0\")").button

#Some buttons for some symbols
buttoneu=framecalcbutton("e", "addsymbol(\"E\")").button
buttonpi=framecalcbutton("π", "addsymbol(\"pi\")").button
buttonop=framecalcbutton("(", "addsymbol(\"(\")").button
buttoncs=framecalcbutton(")", "addsymbol(\")\")").button

#Operations buttons
buttonpls = framecalcbutton("+", "addsymbol(\"+\")").button
buttonmis = framecalcbutton("-", "addsymbol(\"-\")").button
buttonmul = framecalcbutton("*", "addsymbol(\"*\")").button
buttondiv = framecalcbutton("/", "addsymbol(\"/\")").button
buttoneq  = framecalcbutton("=", "evaluateinput()").button
buttonpo  = framecalcbutton(".", "addsymbol(\".\")").button
buttondec = framecalcbutton("dec", "evaluateinput()").button
buttonclr = framecalcbutton("clr", "clearinput()").button
inputdec  = tk0.Entry(framecalcnumbers, bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0) 

#Functios buttons
button_sin   =framefuncbutton1("sin",  "addsymbol(\"sin(\")").button
button_cos   =framefuncbutton1("cos",  "addsymbol(\"cos(\")").button
button_tan   =framefuncbutton1("tan",  "addsymbol(\"tan(\")").button
button_csc   =framefuncbutton2("csc",  "addsymbol(\"csc(\")").button
button_sec   =framefuncbutton2("sec",  "addsymbol(\"sec(\")").button
button_cot   =framefuncbutton2("cot",  "addsymbol(\"cot(\")").button
button_sinh  =framefuncbutton1("sinh", "addsymbol(\"sinh(\")").button
button_cosh  =framefuncbutton1("cosh", "addsymbol(\"cosh(\")").button
button_tanh  =framefuncbutton1("tanh", "addsymbol(\"tanh(\")").button
button_csch  =framefuncbutton2("csch", "addsymbol(\"csch(\")").button
button_sech  =framefuncbutton2("sech", "addsymbol(\"sech(\")").button
button_coth  =framefuncbutton2("coth", "addsymbol(\"coth(\")").button
button_asin  =framefuncbutton1("sin-1",  "addsymbol(\"asin(\")").button
button_acos  =framefuncbutton1("cos-1",  "addsymbol(\"acos(\")").button
button_atan  =framefuncbutton1("tan-1",  "addsymbol(\"atan(\")").button
button_acsc  =framefuncbutton2("csc-1",  "addsymbol(\"acsc(\")").button
button_asec  =framefuncbutton2("sec-1",  "addsymbol(\"asec(\")").button
button_acot  =framefuncbutton2("cot-1",  "addsymbol(\"acot(\")").button
button_asinh =framefuncbutton1("sinh-1", "addsymbol(\"asinh(\")" ).button
button_acosh =framefuncbutton1("cosh-1", "addsymbol(\"acosh(\")" ).button
button_atanh =framefuncbutton1("tanh-1", "addsymbol(\"atanh(\")" ).button
button_acsch =framefuncbutton2("csch-1", "addsymbol(\"acsch(\")" ).button
button_asech =framefuncbutton2("sech-1", "addsymbol(\"asech(\")" ).button
button_acoth =framefuncbutton2("coth-1", "addsymbol(\"acoth(\")" ).button


#This is where we place them
framecalcnumbers.grid(row=5 ,column=0, rowspan=5, columnspan=4,padx=2, pady=2, sticky="nesw") #The main buttons frame
#The other two frames
framecalcfuncs1.grid(row=4 ,column=4, rowspan=5, columnspan=3,padx=2, pady=2, sticky="nesw") #The main buttons frame
framecalcfuncs2.grid(row=4 ,column=7, rowspan=5, columnspan=3,padx=2, pady=2, sticky="nesw") #The main buttons frame

#The numbers buttons
button9.grid(row=0, column=0, padx=1, pady=1,sticky="nesw")
button8.grid(row=0, column=1, padx=1, pady=1,sticky="nesw")
button7.grid(row=0, column=2, padx=1, pady=1,sticky="nesw")
button6.grid(row=1, column=0, padx=1, pady=1,sticky="nesw")
button5.grid(row=1, column=1, padx=1, pady=1,sticky="nesw")
button4.grid(row=1, column=2, padx=1, pady=1,sticky="nesw")
button3.grid(row=2, column=0, padx=1, pady=1,sticky="nesw")
button2.grid(row=2, column=1, padx=1, pady=1,sticky="nesw")
button1.grid(row=2, column=2, padx=1, pady=1,sticky="nesw")
button0.grid(row=3, column=1, padx=1, pady=1,sticky="nesw")

#Symbols buttons
buttoneu.grid(row=5, column=0, padx=1, pady=1,sticky="nesw")
buttonpi.grid(row=5, column=1, padx=1, pady=1,sticky="nesw")
buttonop.grid(row=5, column=2, padx=1, pady=1,sticky="nesw")
buttoncs.grid(row=5, column=3, padx=1, pady=1,sticky="nesw")


#Placing operators
buttonpls.grid(row=0, column=3,padx=1, pady=1, sticky="nesw")
buttonmis.grid(row=1, column=3,padx=1, pady=1, sticky="nesw")
buttonmul.grid(row=2, column=3,padx=1, pady=1, sticky="nesw")
buttondiv.grid(row=3, column=3,padx=1, pady=1, sticky="nesw")
buttoneq.grid(row=4, column=3, padx=1, pady=1, sticky="nesw")
buttonpo.grid(row=3, column=0, padx=1, pady=1, sticky="nesw")
buttondec.grid(row=4, column=0,padx=1, pady=1, sticky="nesw")
buttonclr.grid(row=3, column=2,padx=1, pady=1, sticky="nesw")
inputdec.grid(row=4, column=1, padx=1, pady=1, columnspan=2, sticky="nesw")

#Placing functions
button_sin.grid(row=0, column=0, padx=1, pady=1, sticky="nesw")  
button_cos.grid(row=0, column=1, padx=1, pady=1, sticky="nesw")  
button_tan.grid(row=0, column=2, padx=1, pady=1, sticky="nesw")  
button_csc.grid(row=0, column=0, padx=1, pady=1, sticky="nesw")  
button_sec.grid(row=0, column=1, padx=1, pady=1, sticky="nesw")  
button_cot.grid(row=0, column=2, padx=1, pady=1, sticky="nesw")  
button_sinh .grid(row=1, column=0, padx=1, pady=1, sticky="nesw")  
button_cosh .grid(row=1, column=1, padx=1, pady=1, sticky="nesw")  
button_tanh .grid(row=1, column=2, padx=1, pady=1, sticky="nesw")  
button_csch .grid(row=1, column=0, padx=1, pady=1, sticky="nesw")  
button_sech .grid(row=1, column=1, padx=1, pady=1, sticky="nesw")  
button_coth .grid(row=1, column=2, padx=1, pady=1, sticky="nesw")  
button_asin .grid(row=2, column=0, padx=1, pady=1, sticky="nesw")  
button_acos .grid(row=2, column=1, padx=1, pady=1, sticky="nesw")  
button_atan .grid(row=2, column=2, padx=1, pady=1, sticky="nesw")  
button_acsc .grid(row=2, column=0, padx=1, pady=1, sticky="nesw")  
button_asec .grid(row=2, column=1, padx=1, pady=1, sticky="nesw")  
button_acot .grid(row=2, column=2, padx=1, pady=1, sticky="nesw")  
button_asinh.grid(row=3, column=0, padx=1, pady=1, sticky="nesw")  
button_acosh.grid(row=3, column=1, padx=1, pady=1, sticky="nesw")  
button_atanh.grid(row=3, column=2, padx=1, pady=1, sticky="nesw")  
button_acsch.grid(row=3, column=0, padx=1, pady=1, sticky="nesw")  
button_asech.grid(row=3, column=1, padx=1, pady=1, sticky="nesw")  
button_acoth.grid(row=3, column=2, padx=1, pady=1, sticky="nesw")  

if __name__=="__main__":
    root.mainloop()
