from sympy import *
from tkinter import *

#window
root=Tk()
root.configure(bg="#24292C")
#weight
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
root.rowconfigure(10, weight=1)
root.rowconfigure(11, weight=1)
root.rowconfigure(12, weight=1)
root.rowconfigure(13, weight=1)
root.rowconfigure(14, weight=1)
root.rowconfigure(15, weight=1)
#tracking button state
    
global is_deg_on
is_deg_on=False
global is_bin_on
is_bin_on=False
global is_hex_on
is_hex_on=False
global is_oct_on
is_oct_on=False
global is_dec_on
is_dec_on=False


#entry
e=Entry(root,width='205',font='none 8 bold',borderwidth='10',bg='red')
e.grid(row=0,column=0,columnspan='10', sticky="nesw")

#FUNCTIONS
def button_clear():
    e.delete(0,END)
def button_delete():
    
    e.delete(0)
    
    
    
    
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,current+ str(number))    

def button_equal():
    
    ans=int(eval(e.get())) # To evaluate The Mathimatical operation
    e.delete(0,END) # To Delete The Mathimatical operation
    e.insert(0,(ans)) # To Insert The Answer

def close_switches(c):
    if c==1:
        
        global is_bin_on
        if is_bin_on == True:
            button_bin.config(text=off_bin)
            button_bin.config(fg='#2293D6' ,bg='#343A3E')
            is_bin_on=False


        global is_hex_on
        if is_hex_on == True:
            button_hex.config(text=off_hex)
            button_hex.config(fg='#2293D6' ,bg='#343A3E')
            is_on=False



        global is_oct_on
        if is_oct_on == True:
            button_oct.config(text=off_oct)
            button_oct.config(fg='#2293D6' ,bg='#343A3E')
            is_oct_on=False

        global is_dec_on
        if is_dec_on == True:
            button_dec.config(text=off_dec)
            button_dec.config(fg='#2293D6' ,bg='#343A3E')
            is_dec_on=False


    elif c==2:
        
        global is_deg_on
        if is_deg_on == True:
            button_deg.config(text=off_deg)
            button_deg.config(fg='#2293D6' ,bg='#343A3E')
            is_deg_on=False
        
        if is_hex_on == True:
            button_hex.config(text=off_hex)
            button_hex.config(fg='#2293D6' ,bg='#343A3E')
            is_on=False



        
        if is_oct_on == True:
            button_oct.config(text=off_oct)
            button_oct.config(fg='#2293D6' ,bg='#343A3E')
            is_oct_on=False

        
        if is_dec_on == True:
            button_dec.config(text=off_dec)
            button_dec.config(fg='#2293D6' ,bg='#343A3E')
            is_dec_on=False
        

    elif c==3:
        
        if is_deg_on == True:
            button_deg.config(text=off_deg)
            button_deg.config(fg='#2293D6' ,bg='#343A3E')
            is_deg_on=False

        
        if is_bin_on == True:
            button_bin.config(text=off_bin)
            button_bin.config(fg='#2293D6' ,bg='#343A3E')
            is_bin_on=False

        
        if is_oct_on == True:
            button_oct.config(text=off_oct)
            button_oct.config(fg='#2293D6' ,bg='#343A3E')
            is_oct_on=False

        
        if is_dec_on == True:
            button_dec.config(text=off_dec)
            button_dec.config(fg='#2293D6' ,bg='#343A3E')
            is_dec_on=False


    elif c==4:
        
        if is_deg_on == True:
            button_deg.config(text=off_deg)
            button_deg.config(fg='#2293D6' ,bg='#343A3E')
            is_deg_on=False

        
        if is_bin_on == True:
            button_bin.config(text=off_bin)
            button_bin.config(fg='#2293D6' ,bg='#343A3E')
            is_bin_on=False


        
        if is_hex_on == True:
            button_hex.config(text=off_hex)
            button_hex.config(fg='#2293D6' ,bg='#343A3E')
            is_on=False
       
        if is_dec_on == True:
            button_dec.config(text=off_dec)
            button_dec.config(fg='#2293D6' ,bg='#343A3E')
            is_dec_on=False



    elif c==5:
        
        if is_deg_on == True:
            button_deg.config(text=off_deg)
            button_deg.config(fg='#2293D6' ,bg='#343A3E')
            is_deg_on=False

        
        if is_bin_on == True:
            button_bin.config(text=off_bin)
            button_bin.config(fg='#2293D6' ,bg='#343A3E')
            is_bin_on=False


        if is_hex_on == True:
            button_hex.config(text=off_hex)
            button_hex.config(fg='#2293D6' ,bg='#343A3E')
            is_on=False



       
        if is_oct_on == True:
            button_oct.config(text=off_oct)
            button_oct.config(fg='#2293D6' ,bg='#343A3E')
            is_oct_on=False





'''
global is_deg_on
if is_deg_on == True:
    button_deg.config(text=off_deg)
    is_deg_on=False

global is_bin_on
if is_bin_on == True:
    button_bin.config(text=off_bin)
    is_bin_on=False


global is_hex_on
if is_hex_on == True:
    button_hex.config(text=off_hex)
    is_on=False



global is_oct_on
if is_oct_on == True:
    button_oct.config(text=off_oct)
    is_oct_on=False

global is_dec_on
if is_dec_on == True:
    button_dec.config(text=off_dec)
    is_dec_on=False
fg="#2293D6"
bg="#343A3E"
 '''       
    
def switch_deg():
    
    close_switches(1)
    global is_deg_on
    if is_deg_on == True:
        button_deg.config(text=off_deg)
        button_deg.config(fg='#2293D6' ,bg='#343A3E')
        is_deg_on=False
    else:
        button_deg.config(text=on_deg)
        button_deg.config(fg='#343A3E' ,bg='#2293D6')
        is_deg_on=True
def switch_bin():
    
    close_switches(2)
    global is_bin_on
    if is_bin_on == True:
        button_bin.config(text=off_bin)
        button_bin.config(fg='#2293D6' ,bg='#343A3E')
        is_bin_on=False
    else:
        button_bin.config(text=on_bin)
        button_bin.config(fg='#343A3E' ,bg='#2293D6')
        is_bin_on=True
def switch_hex():
    
    close_switches(3)
    global is_hex_on
    if is_hex_on == True:
        button_hex.config(text=off_hex)
        button_hex.config(fg='#2293D6' ,bg='#343A3E')
        is_hex_on=False
    else:
        button_hex.config(text=on_hex)
        button_hex.config(fg='#343A3E' ,bg='#2293D6')
        is_hex_on=True
def switch_oct():
    
    close_switches(4)
    global is_oct_on
    if is_oct_on == True:
        button_oct.config(text=off_oct)
        button_oct.config(fg='#2293D6' ,bg='#343A3E')
        is_oct_on=False
    else:
        button_oct.config(text=on_oct)
        button_oct.config(fg='#343A3E' ,bg='#2293D6')
        is_oct_on=True
def switch_dec():
    
    close_switches(5)
    global is_dec_on
    if is_dec_on == True:
        button_dec.config(text=off_dec)
        button_dec.config(fg='#2293D6' ,bg='#343A3E')
        is_dec_on=False
    else:
        button_dec.config(text=on_dec)
        button_dec.config(fg='#343A3E' ,bg='#2293D6')
        is_dec_on=True
        

    

#buttons

# def text
on_deg='deg on'
off_deg='deg off'
on_bin='bin on'
off_bin='bin off'
on_dec='dec on'
off_dec='dec off'
on_hex='hex on'
off_hex='hex off'
on_oct='oct on'
off_oct='oct off'



#new buttons
button_deg=Button(root,text='deg off',bd='0',font='none 18 bold',pady='30',padx='51',bg="#343A3E",fg="#2293D6",command=switch_deg)
button_bin=Button(root,text='bin off',bd='0',font='none 18 bold',pady='30',padx='57',bg="#343A3E",fg="#2293D6",command=switch_bin)
button_hex=Button(root,text='hex off',bd='0',font='none 18 bold',pady='30',padx='63',bg="#343A3E",fg="#2293D6",command=switch_hex)
button_oct=Button(root,text='oct off',bd='0',font='none 18 bold',pady='30',padx='64',bg="#343A3E",fg="#2293D6",command=switch_oct)
button_dec=Button(root,text='dec off',bd='0',font='none 18 bold',pady='30',padx='36',bg="#343A3E",fg="#2293D6",command=switch_dec)

# def new buttons
button_deg.grid(row='2',column='3', sticky="nesw")
button_bin.grid(row='2',column='4', sticky="nesw")
button_oct.grid(row='4',column='4', sticky="nesw")
button_hex.grid(row='4',column='3', sticky="nesw")
button_dec.grid(row='4',column='5', sticky="nesw")
#dont scroll more it is all up bro
#
##
###
####











        
buttonequal=Button(root,text=' =',borderwidth='7',font='none 18 bold',pady='30',padx='60',bg='black',fg='red',command=button_equal)
buttonclear=Button(root,text='clear',borderwidth='7',font='none 18 bold',pady='30',padx='45',bg='black',fg='red',command= button_clear)


# un finished buttons
button_sin=Button(root,text=' sin',borderwidth='12',font='none 18 bold',pady='30',padx='45',bg='black',fg='red',command= lambda: button_click('sin('))
button_cos=Button(root,text=' cos',borderwidth='12',font='none 18 bold',pady='30',padx='45',bg='black',fg='red',command= lambda: button_click('cos('))              
button_tan=Button(root,text=' tan',borderwidth='12',font='none 18 bold',pady='30',padx='45',bg='black',fg='red',command= lambda: button_click('tan('))
button_csc=Button(root,text=' csc',borderwidth='12',font='none 18 bold',pady='30',padx='42',bg='black',fg='red',command= lambda: button_click('csc('))
button_sec=Button(root,text=' sec',borderwidth='12',font='none 18 bold',pady='30',padx='45',bg='black',fg='red',command= lambda: button_click('sec('))
button_cot=Button(root,text=' cot',borderwidth='12',font='none 18 bold',pady='30',padx='47',bg='black',fg='red',command= lambda: button_click('cot('))
button_sinh=Button(root,text=' sinh',borderwidth='12',font='none 18 bold',pady='30',padx='39',bg='black',fg='red',command= lambda: button_click('sinh('))
button_cosh=Button(root,text=' cosh',borderwidth='12',font='none 18 bold',pady='30',padx='39',bg='black',fg='red',command= lambda: button_click('cosh('))
button_tanh=Button(root,text=' tanh',borderwidth='12',font='none 18 bold',pady='30',padx='40',bg='black',fg='red',command= lambda: button_click('tanh('))
button_csch=Button(root,text=' csch',borderwidth='12',font='none 18 bold',pady='30',padx='37',bg='black',fg='red',command= lambda:button_click('csch('))
button_sech=Button(root,text=' sech',borderwidth='12',font='none 18 bold',pady='30',padx='39',bg='black',fg='red',command= lambda: button_click('sech('))
button_coth=Button(root,text=' coth',borderwidth='12',font='none 18 bold',pady='30',padx='40',bg='black',fg='red',command= lambda: button_click('coth('))


buttonadd=Button(root,text=' +',borderwidth='12',font='none 18 bold',pady='30',padx='60',bg='black',fg='red',command= lambda: button_click('+'))
buttonsub=Button(root,text=' -',borderwidth='12',font='none 18 bold',pady='30',padx='63',bg='black',fg='red',command= lambda: button_click('-'))
buttonmult=Button(root,text=' *',borderwidth='12',font='none 18 bold',pady='30',padx='62',bg='black',fg='red',command= lambda: button_click('*'))
buttondiv=Button(root,text=' /',borderwidth='12',font='none 18 bold',pady='30',padx='64',bg='black',fg='red',command= lambda: button_click('/'))
buttonlb=Button(root,text=' (',borderwidth='12',font='none 18 bold',pady='30',padx='60',bg='black',fg='red',command= lambda: button_click('('))
buttonrb=Button(root,text=' )',borderwidth='12',font='none 18 bold',pady='30',padx='60',bg='black',fg='red',command= lambda: button_click(')'))
buttonpower=Button(root,text='**',borderwidth='12',font='none 18 bold',pady='30',padx='58',bg='black',fg='red',command= lambda: button_click('**'))
buttonsqrt=Button(root,text='√',borderwidth='12',font='none 18 bold',pady='30',padx='61',bg='black',fg='red',command= lambda:button_click('sqrt('))

# def text
on_deg='deg on'
off_deg='deg off'
on_bin='bin on'
off_bin='bin off'
on_dec='dec on'
off_dec='dec off'
on_hex='hex on'
off_hex='hex off'
on_oct='oct on'
off_oct='oct off'



#new buttons
button_deg=Button(root,text='deg off',bd='0',font='none 18 bold',pady='30',padx='51',bg='black',fg='red',command=switch_deg)
button_bin=Button(root,text='bin off',bd='0',font='none 18 bold',pady='30',padx='57',bg='black',fg='red',command=switch_bin)
button_hex=Button(root,text='hex off',bd='0',font='none 18 bold',pady='30',padx='63',bg='black',fg='red',command=switch_hex)
button_oct=Button(root,text='oct off',bd='0',font='none 18 bold',pady='30',padx='64',bg='black',fg='red',command=switch_oct)
button_dec=Button(root,text='dec off',bd='0',font='none 18 bold',pady='30',padx='36',bg='black',fg='red',command=switch_dec)

# def new buttons
button_deg.grid(row='2',column='3', sticky="nesw")
button_bin.grid(row='2',column='4', sticky="nesw")
button_oct.grid(row='4',column='4', sticky="nesw")
button_hex.grid(row='4',column='3', sticky="nesw")
button_dec.grid(row='4',column='5', sticky="nesw")





#defining buttons
buttonequal.grid(row='1',column='6', sticky="nesw")
buttonclear.grid(row='1',column='5', sticky="nesw")

button_sin.grid(row='1',column='0', sticky="nesw")
button_cos.grid(row='1',column='1', sticky="nesw")
button_tan.grid(row='1',column='2', sticky="nesw")
button_csc.grid(row='2',column='0', sticky="nesw")
button_sec.grid(row='2',column='1', sticky="nesw")
button_cot.grid(row='2',column='2', sticky="nesw")
button_sinh.grid(row='3',column='0', sticky="nesw")
button_cosh.grid(row='3',column='1', sticky="nesw")
button_tanh.grid(row='3',column='2', sticky="nesw")
button_csch.grid(row='4',column='0', sticky="nesw")
button_sech.grid(row='4',column='1', sticky="nesw")
button_coth.grid(row='4',column='2', sticky="nesw")

buttonadd.grid(row='2',column='5', sticky="nesw")
buttonsub.grid(row='2',column='6', sticky="nesw")                  
buttonmult.grid(row='3',column='5', sticky="nesw")
buttondiv.grid(row='3',column='6', sticky="nesw")


buttonlb.grid(row='1',column='3', sticky="nesw")
buttonrb.grid(row='1',column='4', sticky="nesw")
buttonpower.grid(row='3',column='4', sticky="nesw")
buttonsqrt.grid(row='3',column='3', sticky="nesw")



if __name__ == "__main__": #Used because we won't be using the application directly. We will use it as an import instead.
    root.mainloop()

