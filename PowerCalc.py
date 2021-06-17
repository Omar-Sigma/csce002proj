import tkinter as tk0
import tkinter.ttk as ttk0
from ttkthemes import ThemedStyle #This is in order to implement a certain theme. The colors, however, are manually created.
from tkinter.constants import DISABLED #This is imported automatically, since we are using the "state=DISABLED" option in some buttons
from sympy import * #This is where the bulk of the scientific functions come from
import togglebuttons as pctg0 #This is a file that one of the team members created. This will be used as import since it's a big file and putting it directly here would be a lot of work.

import helpsectiontext as hstext #This file contains a lot of text, so we put it in a seperate variable instead.
from sympy.functions.combinatorial.numbers import nC, nP #Importing permutations and combinations functions

#=================================================
#=================================================
#=================================================

"""
This is the root widget initialization. We imported tkinter as tk0 instead of importing all from tkinter to avoid any potential conflicts.
"""

root_or_win = tk0.Tk()
root_or_win.title("PowerCalc V1.0.1")
s=ThemedStyle(root_or_win)
s.theme_use('breeze')
root_or_win.configure(bg="#24292C")
root_or_win.geometry("1280x720")
#Instead of directly using the original window as a root window, I create a frame inside it that we will use as the root instead, so that we can control it, add padding, and more without affacting the main window.
root_win=tk0.Frame(root_or_win, bg="#24292C")
root_win.grid(column=0, row=0, columnspan=10, rowspan=15, padx=4, pady=4, sticky="nesw")

#Creating frames for the help and exit sections
helpsection=tk0.Frame(root_or_win, bg="#24292C")
aboutsection=tk0.Frame(root_or_win, bg="#24292C")

#Icon
try:
    root_or_win.iconphoto(True, tk0.PhotoImage(file='pcalcico.png'))
except:
    pass

#=================================================
#=================================================
#=================================================

"""
This is where we configure some stuff.
for example. by giving a weight of number 1 to the mentioned columns, we can
make them dynamically resizeable as the user changes the size of the window.
Here we configure both the main window (root_or_win), and the frame in which we are going to put everything in (root_win)
"""

root_or_win.columnconfigure(0, weight=1)
root_or_win.columnconfigure(1, weight=1)
root_or_win.columnconfigure(2, weight=1)
root_or_win.columnconfigure(3, weight=1)
root_or_win.columnconfigure(4, weight=1)
root_or_win.columnconfigure(5, weight=1)
root_or_win.columnconfigure(6, weight=1)
root_or_win.columnconfigure(7, weight=1)
root_or_win.columnconfigure(8, weight=1)
root_or_win.columnconfigure(9, weight=1)
root_or_win.rowconfigure(0, weight=1)
root_or_win.rowconfigure(1, weight=1)
root_or_win.rowconfigure(2, weight=1)
root_or_win.rowconfigure(3, weight=1)
root_or_win.rowconfigure(4, weight=1)
root_or_win.rowconfigure(5, weight=1)
root_or_win.rowconfigure(6, weight=1)
root_or_win.rowconfigure(7, weight=1)
root_or_win.rowconfigure(8, weight=1)
root_or_win.rowconfigure(9, weight=1)
root_or_win.rowconfigure(10, weight=1)
root_or_win.rowconfigure(11, weight=1)
root_or_win.rowconfigure(12, weight=1)
root_or_win.rowconfigure(13, weight=1)
root_or_win.rowconfigure(14, weight=1)

#Our WIndow configuration
root_win.columnconfigure(0, weight=1)
root_win.columnconfigure(1, weight=1)
root_win.columnconfigure(2, weight=1)
root_win.columnconfigure(3, weight=1)
root_win.columnconfigure(4, weight=1)
root_win.columnconfigure(5, weight=1)
root_win.columnconfigure(6, weight=1)
root_win.columnconfigure(7, weight=1)
root_win.columnconfigure(8, weight=1)
root_win.columnconfigure(9, weight=1)
root_win.rowconfigure(0, weight=1)
root_win.rowconfigure(1, weight=1)
root_win.rowconfigure(2, weight=1)
root_win.rowconfigure(3, weight=1)
root_win.rowconfigure(4, weight=1)
root_win.rowconfigure(5, weight=1)
root_win.rowconfigure(6, weight=1)
root_win.rowconfigure(7, weight=1)
root_win.rowconfigure(8, weight=1)
root_win.rowconfigure(9, weight=1)
root_win.rowconfigure(10, weight=1)
root_win.rowconfigure(11, weight=1)
root_win.rowconfigure(12, weight=1)
root_win.rowconfigure(13, weight=1)
root_win.rowconfigure(14, weight=1)

#Help configuration
helpsection.columnconfigure(0, weight=1)
helpsection.columnconfigure(1, weight=1)
helpsection.columnconfigure(2, weight=1)
helpsection.columnconfigure(3, weight=1)
helpsection.columnconfigure(4, weight=1)
helpsection.columnconfigure(5, weight=1)
helpsection.columnconfigure(6, weight=1)
helpsection.columnconfigure(7, weight=1)
helpsection.columnconfigure(8, weight=1)
helpsection.columnconfigure(9, weight=1)
helpsection.rowconfigure(0, weight=1)
helpsection.rowconfigure(1, weight=1)
helpsection.rowconfigure(2, weight=1)
helpsection.rowconfigure(3, weight=1)
helpsection.rowconfigure(4, weight=1)
helpsection.rowconfigure(5, weight=1)
helpsection.rowconfigure(6, weight=1)
helpsection.rowconfigure(7, weight=1)
helpsection.rowconfigure(8, weight=1)
helpsection.rowconfigure(9, weight=1)
helpsection.rowconfigure(10, weight=1)
helpsection.rowconfigure(11, weight=1)
helpsection.rowconfigure(12, weight=1)
helpsection.rowconfigure(13, weight=1)
helpsection.rowconfigure(14, weight=1)

#About configuration
aboutsection.columnconfigure(0, weight=1)
aboutsection.columnconfigure(1, weight=1)
aboutsection.columnconfigure(2, weight=1)
aboutsection.columnconfigure(3, weight=1)
aboutsection.columnconfigure(4, weight=1)
aboutsection.columnconfigure(5, weight=1)
aboutsection.columnconfigure(6, weight=1)
aboutsection.columnconfigure(7, weight=1)
aboutsection.columnconfigure(8, weight=1)
aboutsection.columnconfigure(9, weight=1)
aboutsection.rowconfigure(0, weight=1)
aboutsection.rowconfigure(1, weight=1)
aboutsection.rowconfigure(2, weight=1)
aboutsection.rowconfigure(3, weight=1)
aboutsection.rowconfigure(4, weight=1)
aboutsection.rowconfigure(5, weight=1)
aboutsection.rowconfigure(6, weight=1)
aboutsection.rowconfigure(7, weight=1)
aboutsection.rowconfigure(8, weight=1)
aboutsection.rowconfigure(9, weight=1)
aboutsection.rowconfigure(10, weight=1)
aboutsection.rowconfigure(11, weight=1)
aboutsection.rowconfigure(12, weight=1)
aboutsection.rowconfigure(13, weight=1)
aboutsection.rowconfigure(14, weight=1)
#=================================================
#=================================================
#=================================================

"""
This is where we define our functions. The ones that are related to our buttons, text inputs, and more. 
We defined them here since we have to define out functions first and THEN use them. This could be avoided using classes for the widget,
but since we are using a procedural approach, we can't do that as easily (if at all).
"""

"""
Another note: It's usually very dangerous to use "eval" on unsanitized user input. However, since this is not a web application or something that could do direct harm to someone, we will use it.
"""

#These are going to be some user-defined variables and the "previous answer" variable
aa=0
bb=0
cc=0
dd=0
ee=0
ff=0

ans=0

def clearnotes():
    """This function clears the notes field"""
    inputnotes.delete("1.0", "end-1c") #The "Text" widget takes different parameters than simple entry, that's why the arguments are diiferent.
def clearinput():
    """This function clears the input field"""
    inputmain.delete(0,tk0.END)

def addsymbol(symbol):
    """This function adds the symbol of the button"""
    current=inputmain.get()
    inputmain.delete(0,tk0.END)
    inputmain.insert(0,current+ str(symbol))    

def correctinput(user_input):
    """
    This input changes some parts of the user's input to make it possible for the interpreter to evaluate them correctly
    """
    user_input_mod=user_input.replace("^","**").replace("√","sqrt").replace("²", "**2") #This is line replaces some human friendly symbols with actual symbols used for computation

#We revert the hyperbolic functions back to a format the interpreter understands. We didn't do it directly to avoid problems with accidently replacing "sin" with something for example if degrees are turned on.
    if pctg0.is_deg_on == True: #These lines are for the degree functionality. Here, radians are converted to degrees by multiplying them by pi/180
        user_input_mod=user_input_mod.replace("sin(","sin((pi/180)*")   
        user_input_mod=user_input_mod.replace("cos(","cos((pi/180)*")   
        user_input_mod=user_input_mod.replace("tan(","tan((pi/180)*")   
        user_input_mod=user_input_mod.replace("sec(","sec((pi/180)*")   
        user_input_mod=user_input_mod.replace("csc(","csc((pi/180)*")   
        user_input_mod=user_input_mod.replace("cot(","cot((pi/180)*")   
        user_input_mod=user_input_mod.replace("asiin(","(180/pi)*asin(") #For the inverse ones, we want asin(1) to get us 90 instead of pi/2. so we will multiplt by 180/pi BEFORE the function instead. Also, we changed the asin, acos, etc to asiin, acios, etc to avoid problems when replacing atan with something, since the atan inside the "atan" will be replaced as well. 
        user_input_mod=user_input_mod.replace("acios(","(180/pi)*acos(") 
        user_input_mod=user_input_mod.replace("atian(","(180/pi)*atan(") 
        user_input_mod=user_input_mod.replace("asiec(","(180/pi)*asec(") 
        user_input_mod=user_input_mod.replace("acisc(","(180/pi)*acsc(") 
        user_input_mod=user_input_mod.replace("aciot(","(180/pi)*acot(") 
    else:
        pass
        user_input_mod=user_input_mod.replace("asiin(","asin(") #Same as above, but ommitng the degree conversion 
        user_input_mod=user_input_mod.replace("acios(","acos(") 
        user_input_mod=user_input_mod.replace("atian(","atan(") 
        user_input_mod=user_input_mod.replace("asiec(","asec(") 
        user_input_mod=user_input_mod.replace("acisc(","acsc(") 
        user_input_mod=user_input_mod.replace("aciot(","acot(") 

    if pctg0.is_bin_on == True: #These lines check if the togglebuttons are enabled, and if they are, they change the result into the respective number system. 
        user_input_mod = "bin("+user_input_mod+")"
    elif pctg0.is_hex_on == True:
        user_input_mod = "hex("+user_input_mod+")"
    elif pctg0.is_oct_on == True:
        user_input_mod = "oct("+user_input_mod+")"
    else:
        pass

    if user_input=="":
        user_input_mod="0"
    else:
        pass
    return(user_input_mod)

def evaluateinput():
    """This function evaluates input"""
    global ans                                   #This is done to make it possible for function to change the "ans" variable globally
    inputmainans.configure(state="normal")       #make the answer field read and write
    user_input_mod=correctinput(inputmain.get()) #User input is stored in this variable
    try:                                         #This is to print an "Error" string in case something happened
        ans=eval(user_input_mod)                 #To evaluate The Mathimatical operation
    except:
        ans="Error"
    #inputmain.delete(0,tk0.END)                 #To Delete The Mathimatical operation #This line could be turned on if we want to remove the previous operation made by the user
    inputmainans.delete(0, tk0.END)              #This is to delete the previous answer
    inputmainans.insert(0,ans)                   #To Insert The Answer 
    inputmainans.configure(state="readonly")     #Make the answer field readonly

def decevaluateinput():
    """This function evaluates input"""
    global ans                                   #This is done to make it possible for function to change the "ans" variable globally
    inputmainans.configure(state="normal")       #make the answer field read and write
    user_input_mod=correctinput(inputmain.get()) #User input is stored in this variable
    try:                                         #This is to print an "Error" string in case something happened
        ans=N(eval(user_input_mod), inputdec.get())                  #To evaluate The Mathimatical operation
    except:
        ans="Error"
    #inputmain.delete(0,tk0.END)                 #To Delete The Mathimatical operation #This line could be turned on if we want to remove the previous operation made by the user
    inputmainans.delete(0, tk0.END)              #This is to delete the previous answer
    inputmainans.insert(0,ans)                   #To Insert The Answer 
    inputmainans.configure(state="readonly")     #Make the answer field readonly



def checkvar(varname, inputfieldid):
    """
    This function checks the variable's validty. So that the variable is assigned a value of 0 if it doesn't make sense.
    This function takes the variable we want to check as an argument and the inputfield associated with it.
    """
    try:
        varname=eval(inputfieldid.get())
    except:
        inputfieldid.delete(0,tk0.END)
        inputfieldid.insert(0, "0")
        varname=0
    return varname

def assignvars():
    """This function assigns the values entered by the user to the variables"""
    global aa, bb, cc, dd, ee, ff
    aa=checkvar(aa,inputvar1) #Here we check the validty of the user-input and assign the value to it
    bb=checkvar(bb,inputvar2)
    cc=checkvar(cc,inputvar3)
    dd=checkvar(dd,inputvar4)
    ee=checkvar(ee,inputvar5)
    ff=checkvar(ff,inputvar6)
    
def clearvars():
    """This function resets the variables' values and clears their input fields"""
    global aa, bb, cc, dd, ee, ff
    aa=0; bb=0; cc=0; dd=0; ee=0; ff=0;
    inputvar1.delete(0, tk0.END)
    inputvar2.delete(0, tk0.END)
    inputvar3.delete(0, tk0.END)
    inputvar4.delete(0, tk0.END)
    inputvar5.delete(0, tk0.END)
    inputvar6.delete(0, tk0.END)


#The next three functions are for navigation between different frames as if they are screens
def gotohelp():
    root_win.grid_forget()
    helpsection.grid(column=0, row=0, columnspan=10, rowspan=15, padx=4, pady=4, sticky="nesw")

def gotoabout():
    root_win.grid_forget()
    aboutsection.grid(column=0, row=0, columnspan=10, rowspan=15, padx=4, pady=4, sticky="nesw")

def gotomain():
    try:
        aboutsection.grid_forget()
    except:
        pass
    try:
        helpsection.grid_forget()
    except:
        pass
    root_win.grid(column=0, row=0, columnspan=10, rowspan=16, padx=4, pady=4, sticky="nesw")


#=================================================
#=================================================
#=================================================

"""
This is where we define our buttons. text inputs, and more.
Each widget variable name has a descriptive name. so button-sin is for the sin button.
"""

#=====Input fields and buttons

"""
Note that we are defining frames here as well which act as containers
"""

#-----Main field: where the user enters the operation and takes the previous result

framemain = tk0.Frame(root_win, bg="#24292C")

#Same as with root_win. But with this frame instead
framemain.columnconfigure(0, weight=1)
framemain.columnconfigure(1, weight=1)
framemain.columnconfigure(2, weight=1)
framemain.columnconfigure(3, weight=1)
framemain.rowconfigure(0, weight=1)
framemain.rowconfigure(1, weight=1)
framemain.rowconfigure(2, weight=1)
framemain.rowconfigure(3, weight=1)


buttonmain = tk0.Button(framemain, text="Ans:", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command=lambda: addsymbol("ans")) 

inputmainans = tk0.Entry(framemain, bg="#323938", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, readonlybackground="#323739") 

inputmain = tk0.Entry(framemain, bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, insertbackground="#2293D6", width=framemain.winfo_width()) 


#Here we place our frame on a certain grid position and put our elements inside. We will be doing this several times from now on.
framemain.grid(row=0 ,column=0, rowspan=7,      padx=2, pady=2,columnspan=4, sticky="nesw")

buttonmain.grid(row=0, column=0, columnspan=1,  padx=1, pady=1,sticky="nesw")
inputmainans.grid(row=0, column =1,columnspan=3,padx=1, pady=1,sticky="nesw")
inputmain.grid(row=1, column=0, rowspan=3,      padx=1, pady=1,columnspan=4, sticky="nesw")










#-----Notes field
#One button clears the fields. And the other is there for notes (for the user)

framenotes = tk0.Frame(root_win, bg="#24292C")
buttonnotes = tk0.Button(framenotes,bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, text="Clear notes!", command=clearnotes)
inputnotes = tk0.Text(framenotes,bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, insertbackground="#2293D6", width=framemain.winfo_width(), height=(framemain.winfo_height())*3/4)

framenotes.columnconfigure(0, weight=1)
framenotes.columnconfigure(1, weight=1)
framenotes.columnconfigure(2, weight=1)
framenotes.rowconfigure(0, weight=1)
framenotes.rowconfigure(1, weight=1)
framenotes.rowconfigure(2, weight=1)
framenotes.rowconfigure(3, weight=1)

framenotes.grid(row=0, column=4, rowspan=7,     columnspan=3,padx=2, pady=2, sticky="nesw")
buttonnotes.grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky="nesw")
inputnotes.grid(row=1, column=0, rowspan=3,     padx=1, pady=1, columnspan=3, sticky="nesw")










#-----Variable assignmnet fields
#This is where we can assign certain values to variables and use them as desired

framevar = tk0.Frame(root_win, bg="#24292C")

#Defining a class that acts as blueprint for our Entry and Buttons

buttonvarass = tk0.Button(framevar, text="Assign", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command=assignvars) #This is a button for assigning values to variables

class inputvarf:
    """Same as above"""
    def __init__(self):
        self.entry=tk0.Entry(framevar, bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, insertbackground="#2293D6", width=3)

class buttonvarf:
    """This is for our buttons"""
    def __init__(self, text0, command0):
        self.text0=text0
        self.button=tk0.Button(framevar, borderwidth=0, highlightthickness=0, bg="#343A3E", fg="#2293D6", font="Courier 12 bold", text=text0, command=lambda: eval(command0), width=1)

buttonvarclr = tk0.Button(framevar, text="Clear", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, width=2, command=clearvars)

inputvar1 = inputvarf().entry
inputvar2 = inputvarf().entry
inputvar3 = inputvarf().entry
inputvar4 = inputvarf().entry
inputvar5 = inputvarf().entry
inputvar6 = inputvarf().entry

buttonvar1 = buttonvarf("aa=", "addsymbol(\"aa\")").button
buttonvar2 = buttonvarf("bb=", "addsymbol(\"bb\")").button
buttonvar3 = buttonvarf("cc=", "addsymbol(\"cc\")").button
buttonvar4 = buttonvarf("dd=", "addsymbol(\"dd\")").button
buttonvar5 = buttonvarf("ee=", "addsymbol(\"ee\")").button
buttonvar6 = buttonvarf("ff=", "addsymbol(\"ff\")").button

framevar.columnconfigure(0, weight=1)
framevar.columnconfigure(1, weight=1)
framevar.columnconfigure(2, weight=1)
framevar.rowconfigure(0, weight=1)
framevar.rowconfigure(1, weight=1)
framevar.rowconfigure(2, weight=1)
framevar.rowconfigure(3, weight=1)
framevar.rowconfigure(4, weight=1)
framevar.rowconfigure(5, weight=1)
framevar.rowconfigure(6, weight=1)

framevar.grid(row=0 ,column=7, rowspan=7, columnspan=3,padx=2, pady=2, sticky="nesw")
buttonvarass.grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky="nesw")
buttonvarclr.grid(row=1, column=2, rowspan=6, columnspan=1, padx=1, pady=1, sticky="nesw")

inputvar1.grid(row=1, column=1, padx=1, pady=1,  sticky="nesw")
inputvar2.grid(row=2, column=1, padx=1, pady=1,  sticky="nesw")
inputvar3.grid(row=3, column=1, padx=1, pady=1,  sticky="nesw")
inputvar4.grid(row=4, column=1, padx=1, pady=1,  sticky="nesw")
inputvar5.grid(row=5, column=1, padx=1, pady=1,  sticky="nesw")
inputvar6.grid(row=6, column=1, padx=1, pady=1,  sticky="nesw")

buttonvar1.grid(row=1, column=0, padx=1, pady=1, sticky="nesw")
buttonvar2.grid(row=2, column=0, padx=1, pady=1, sticky="nesw")
buttonvar3.grid(row=3, column=0, padx=1, pady=1, sticky="nesw")
buttonvar4.grid(row=4, column=0, padx=1, pady=1, sticky="nesw")
buttonvar5.grid(row=5, column=0, padx=1, pady=1, sticky="nesw")
buttonvar6.grid(row=6, column=0, padx=1, pady=1, sticky="nesw")










#=====Calculator Buttons
#This frame is for the 10 numbers, certain symbols, and basic operations in addition to places for decimals.
framecalcnumbers = tk0.Frame(root_win, bg="#24292C")

#And these twos frames are for functions (like sin, cos, etc)
framecalcfuncs1= tk0.Frame(root_win, bg="#24292C")
framecalcfuncs2= tk0.Frame(root_win, bg="#24292C")

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
buttonfac = framecalcbutton("!", "addsymbol(\"factorial(\")").button
buttondec = framecalcbutton("dec", "decevaluateinput()").button
buttonclr = framecalcbutton("clr", "clearinput()").button
inputdec  = tk0.Entry(framecalcnumbers, bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, width=button2.winfo_width(), insertbackground="#2293D6") 

#Trigonometric and hyperbolic functions
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

#Inverse trigonometric and hyperbolic functions 
button_asin  =framefuncbutton1("sin-1",  "addsymbol(\"asiin(\")").button
button_acos  =framefuncbutton1("cos-1",  "addsymbol(\"acios(\")").button
button_atan  =framefuncbutton1("tan-1",  "addsymbol(\"atian(\")").button
button_acsc  =framefuncbutton2("csc-1",  "addsymbol(\"acisc(\")").button
button_asec  =framefuncbutton2("sec-1",  "addsymbol(\"asiec(\")").button
button_acot  =framefuncbutton2("cot-1",  "addsymbol(\"aciot(\")").button
button_asinh =framefuncbutton1("sinh-1", "addsymbol(\"asinh(\")" ).button
button_acosh =framefuncbutton1("cosh-1", "addsymbol(\"acosh(\")" ).button
button_atanh =framefuncbutton1("tanh-1", "addsymbol(\"atanh(\")" ).button
button_acsch =framefuncbutton2("csch-1", "addsymbol(\"acsch(\")" ).button
button_asech =framefuncbutton2("sech-1", "addsymbol(\"asech(\")" ).button
button_acoth =framefuncbutton2("coth-1", "addsymbol(\"acoth(\")" ).button

#Other operations and functions
button_square   =framefuncbutton1("x²",  "addsymbol(\"²\")").button
button_sqroot   =framefuncbutton1("√▯",  "addsymbol(\"√(\")").button
button_natlog   =framefuncbutton1("ln",  "addsymbol(\"ln(\")").button
button_power    =framefuncbutton1("x^▯",  "addsymbol(\"^\")").button

button_root     =framefuncbutton1("▯√x",  "addsymbol(\"root(_number_,_nthroot_)\")").button
button_log      =framefuncbutton1("log▯(x)",  "addsymbol(\"log(_number_, _base_)\")").button

button_deg  =framefuncbutton2("Deg",  "pctg0.switch_deg(button_deg)").button
button_nPr  =framefuncbutton2("nPr",  "addsymbol(\"nP(_number1_,_number2_)\")").button
button_nCr  =framefuncbutton2("nCr",  "addsymbol(\"nC(_number1_,_number2_)\")").button
button_bin  =framefuncbutton2("bin",  "pctg0.switch_bin(button_bin, button_hex, button_oct)").button
button_hex  =framefuncbutton2("hex",  "pctg0.switch_hex(button_bin, button_hex, button_oct)").button
button_oct  =framefuncbutton2("oct",  "pctg0.switch_oct(button_bin, button_hex, button_oct)").button

#This is where we place them
framecalcnumbers.grid(row=7 ,column=0, rowspan=5, columnspan=4,padx=2, pady=2, sticky="nesw") #The main buttons frame
#The other two frames
framecalcfuncs1.grid(row=7 ,column=4, rowspan=5, columnspan=3,padx=2, pady=2, sticky="nesw") #The main buttons frame
framecalcfuncs2.grid(row=7 ,column=7, rowspan=5, columnspan=3,padx=2, pady=2, sticky="nesw") #The main buttons frame

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
buttonfac.grid(row=4, column=0,padx=1, pady=1, sticky="nesw")
buttondec.grid(row=4, column=1,padx=1, pady=1, sticky="nesw")
buttonclr.grid(row=3, column=2,padx=1, pady=1, sticky="nesw")
inputdec.grid(row=4, column=2, padx=1, pady=1, sticky="nesw")

#Placing buttons of class framecalcfuncs1 
button_sin.   grid(row=0, column=0, padx=1, pady=1, sticky="nesw")  
button_cos.   grid(row=0, column=1, padx=1, pady=1, sticky="nesw")  
button_tan.   grid(row=0, column=2, padx=1, pady=1, sticky="nesw")  
button_csc.   grid(row=0, column=0, padx=1, pady=1, sticky="nesw")  
button_sec.   grid(row=0, column=1, padx=1, pady=1, sticky="nesw")  
button_cot.   grid(row=0, column=2, padx=1, pady=1, sticky="nesw")  
button_sinh  .grid(row=1, column=0, padx=1, pady=1, sticky="nesw")  
button_cosh  .grid(row=1, column=1, padx=1, pady=1, sticky="nesw")  
button_tanh  .grid(row=1, column=2, padx=1, pady=1, sticky="nesw")  
button_csch  .grid(row=1, column=0, padx=1, pady=1, sticky="nesw")  
button_sech  .grid(row=1, column=1, padx=1, pady=1, sticky="nesw")  
button_coth  .grid(row=1, column=2, padx=1, pady=1, sticky="nesw")  

button_square.grid(row=4, column=0, padx=1, pady=1, sticky="nesw")    
button_sqroot.grid(row=4, column=1, padx=1, pady=1, sticky="nesw")    
button_natlog.grid(row=4, column=2, padx=1, pady=1, sticky="nesw")    
button_power .grid(row=5, column=0, padx=1, pady=1, sticky="nesw")    
button_root  .grid(row=5, column=1, padx=1, pady=1, sticky="nesw")    
button_log   .grid(row=5, column=2, padx=1, pady=1, sticky="nesw")    

#Placing buttons of class framecalcfuncs1 
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

button_deg  .grid(row=4, column=0, padx=1, pady=1, sticky="nesw")    
button_nPr  .grid(row=4, column=1, padx=1, pady=1, sticky="nesw")    
button_nCr  .grid(row=4, column=2, padx=1, pady=1, sticky="nesw")    
button_bin  .grid(row=5, column=0, padx=1, pady=1, sticky="nesw")    
button_hex  .grid(row=5, column=1, padx=1, pady=1, sticky="nesw")    
button_oct  .grid(row=5, column=2, padx=1, pady=1, sticky="nesw")    










#-----Exit frame
#Help, About, and Exit buttons and their frames
frameaccess=tk0.Frame(root_win ,bg="#24292C")
buttonhelp = tk0.Button(frameaccess, text="Help", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0  , command = gotohelp)
buttonabout = tk0.Button(frameaccess, text="About", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command = gotoabout)
buttonexit = tk0.Button(frameaccess, text="Exit", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command = root_or_win.destroy)
buttonmainh = tk0.Button(helpsection, text="Main", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command = gotomain)
buttonmaina = tk0.Button(aboutsection, text="Main", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command = gotomain)

#Help
labelh1SB= tk0.Scrollbar(helpsection, orient='vertical', troughcolor="#343A3E", bg="#464c4b", elementborderwidth=0, bd=0) #Scrollbar

labelh1 = tk0.Text(helpsection, bg="#323938", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, yscrollcommand=labelh1SB.set) #The text widget with the scrollbaar
labelh1SB.config(command=labelh1.yview)
labelh1.tag_configure("center", justify='center') #In these four lines, we are adding a tag to the text widget to change it's appearence. This tag allows us to center text.
labelh1.insert("end-1c", hstext.text) #We are inserting out text into the box here
labelh1.tag_add("center", "1.0", "end")
labelh1.config(state=DISABLED)  #Here, we are making our textbox disabled. It should be readonly.

#About
textofabout1="""CSCE002 Project: Advanced GUI Scientific Calculator
===================================================
PowerCalc V1.0.1
================

This application is designed to be an advanced gui calculator that 
employs features of scientific calculators with even more perks.

License
=======
This calculator is liensed under the LGPL-2.1 License.

Developers
==========
1-Abdelrahman A. AbelkarimRagab
2-Omar M. A. Elsayed

For bugs
========
Let us know on github.

For more info, go to github. Click on the button to copy the link."""

textofabout2=tk0.StringVar(value="https://github.com/Omar-Sigma/csce002proj")

labela1 = tk0.Label(aboutsection, text=textofabout1 , bg="#323938", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0)

buttongithub = tk0.Button(aboutsection, text="Github: ", bg="#343A3E", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, command=lambda : root_or_win.clipboard_append("https://github.com/Omar-Sigma/Phys002-Projects")) #This command copies the link to the clipboard

labela2 = tk0.Entry(aboutsection, textvariable=textofabout2, bg="#323938", fg="#2293D6", font="Courier 12 bold", borderwidth=0, highlightthickness=0, insertbackground="#2293D6", width=30, state="readonly", readonlybackground="#323938") 





#Placing them
frameaccess.grid(row=12, column=0, padx=2, pady=2, columnspan=10, rowspan=3, sticky="nesw")

frameaccess.rowconfigure(0, weight=1)
frameaccess.rowconfigure(1, weight=1)
frameaccess.rowconfigure(2, weight=1)
frameaccess.columnconfigure(0, weight=1)
frameaccess.columnconfigure(1, weight=1)
frameaccess.columnconfigure(2, weight=1)
frameaccess.columnconfigure(3, weight=1)
frameaccess.columnconfigure(4, weight=1)
frameaccess.columnconfigure(5, weight=1)
frameaccess.columnconfigure(6, weight=1)
frameaccess.columnconfigure(7, weight=1)
frameaccess.columnconfigure(8, weight=1)
frameaccess.columnconfigure(9, weight=1)

buttonhelp .grid(row=0, column=0, padx=2, pady=2, columnspan=10, sticky="nesw")    
buttonabout.grid(row=1, column=0, padx=2, pady=2,columnspan=10, sticky="nesw")    
buttonexit .grid(row=2, column=0, padx=2, pady=2, columnspan=10, sticky="nesw")    





#Placing Help and About stuff
#Help
buttonmainh   .grid(row=14, column=0, padx=2, pady=2, columnspan=10, sticky="nesw")    
labelh1       .grid(row=0, column=0, rowspan=14, columnspan=9, sticky="nesw")    
labelh1SB     .grid(row=0, column=9, padx=2, pady=2, rowspan=14, sticky="nesw")    





#About
buttonmaina .grid(row=14, column=0, padx=2, pady=2, columnspan=10, sticky="nesw")    

labela1     .grid(row=0, column=0, padx=2, pady=2, rowspan=13, columnspan=10, sticky="nesw")    
buttongithub .grid(row=13, column=0, padx=2, pady=2, columnspan=2,sticky="nesw")    
labela2     .grid(row=13, column=2, padx=2, pady=2, columnspan=8,sticky="nesw")    

#=================================================
#=================================================
#=================================================

"""
This is where we finally start our application. So now, let's quickly explain what these lines mean.
the __name__ is a kind of variable that python assigns a value to depending on how the user uses this script.
so if the user uses it as a main script (a gui for example), the the value assigned is equal to "__main__". If not - such as when using the script as an import - another value is assigned.
This line helps us execute the main windows (the line inside the if block) if the user runs it as a gui/script, but not if it's imported from.
"""

#Starting the application
if __name__ == "__main__":
    root_or_win.mainloop()

if __name__!= "__main__": #This is to destroy the window if it is run as an import due to some reason
    root_or_win.destroy()
