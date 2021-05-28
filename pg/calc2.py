from sympy import *
from tkinter import *

#window
root=Tk()


#entry
e=Entry(root,width='197',font='none 8 bold',borderwidth='6',bg='orange')
e.grid(row=0,column=0,columnspan='10')

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

#buttons
buttonequal=Button(root,text=' =',borderwidth='7',font='none 18 bold',pady='30',padx='60',bg='black',fg='orange',command=button_equal)
buttonclear=Button(root,text='clear',borderwidth='7',font='none 18 bold',pady='30',padx='45',bg='black',fg='orange',command= button_clear)


# un finished buttons
button_sin=Button(root,text=' sin',borderwidth='7',font='none 18 bold',pady='30',padx='45',bg='black',fg='orange',command= lambda: button_click('sin('))
button_cos=Button(root,text=' cos',borderwidth='7',font='none 18 bold',pady='30',padx='45',bg='black',fg='orange',command= lambda: button_click('cos('))              
button_tan=Button(root,text=' tan',borderwidth='7',font='none 18 bold',pady='30',padx='45',bg='black',fg='orange',command= lambda: button_click('tan('))
button_csc=Button(root,text=' csc',borderwidth='7',font='none 18 bold',pady='30',padx='42',bg='black',fg='orange',command= lambda: button_click('csc('))
button_sec=Button(root,text=' sec',borderwidth='7',font='none 18 bold',pady='30',padx='45',bg='black',fg='orange',command= lambda: button_click('sec('))
button_cot=Button(root,text=' cot',borderwidth='7',font='none 18 bold',pady='30',padx='47',bg='black',fg='orange',command= lambda: button_click('cot('))
button_sinh=Button(root,text=' sinh',borderwidth='7',font='none 18 bold',pady='30',padx='39',bg='black',fg='orange',command= lambda: button_click('sinh('))
button_cosh=Button(root,text=' cosh',borderwidth='7',font='none 18 bold',pady='30',padx='39',bg='black',fg='orange',command= lambda: button_click('cosh('))
button_tanh=Button(root,text=' tanh',borderwidth='7',font='none 18 bold',pady='30',padx='40',bg='black',fg='orange',command= lambda: button_click('tanh('))
button_csch=Button(root,text=' csch',borderwidth='7',font='none 18 bold',pady='30',padx='37',bg='black',fg='orange',command= lambda:button_click('csch('))
button_sech=Button(root,text=' sech',borderwidth='7',font='none 18 bold',pady='30',padx='39',bg='black',fg='orange',command= lambda: button_click('sech('))
button_coth=Button(root,text=' coth',borderwidth='7',font='none 18 bold',pady='30',padx='40',bg='black',fg='orange',command= lambda: button_click('coth('))


buttonadd=Button(root,text=' +',borderwidth='7',font='none 18 bold',pady='30',padx='60',bg='black',fg='orange',command= lambda: button_click('+'))
buttonsub=Button(root,text=' -',borderwidth='7',font='none 18 bold',pady='30',padx='63',bg='black',fg='orange',command= lambda: button_click('-'))
buttonmult=Button(root,text=' *',borderwidth='7',font='none 18 bold',pady='30',padx='62',bg='black',fg='orange',command= lambda: button_click('*'))
buttondiv=Button(root,text=' /',borderwidth='7',font='none 18 bold',pady='30',padx='64',bg='black',fg='orange',command= lambda: button_click('/'))
buttonlb=Button(root,text=' (',borderwidth='7',font='none 18 bold',pady='30',padx='60',bg='black',fg='orange',command= lambda: button_click('('))
buttonrb=Button(root,text=' )',borderwidth='7',font='none 18 bold',pady='30',padx='60',bg='black',fg='orange',command= lambda: button_click(')'))
buttonpower=Button(root,text='**',borderwidth='7',font='none 18 bold',pady='30',padx='58',bg='black',fg='orange',command= lambda: button_click('**'))
buttonsqrt=Button(root,text='√',borderwidth='7',font='none 18 bold',pady='30',padx='61',bg='black',fg='orange',command= lambda:button_click('sqrt('))

buttons_log=Button(root,text='log',borderwidth='7',font='none 18 bold',pady='30',padx='51',bg='black',fg='orange',command= lambda:button_click('log('))
button_ln=Button(root,text='ln',borderwidth='7',font='none 18 bold',pady='30',padx='57',bg='black',fg='orange',command= lambda:button_click('ln('))
button_com=Button(root,text=',',borderwidth='7',font='none 18 bold',pady='30',padx='63',bg='black',fg='orange',command= lambda:button_click(','))
button_dot=Button(root,text='.',borderwidth='7',font='none 18 bold',pady='30',padx='64',bg='black',fg='orange',command= lambda:button_click('.'))
button_delete=Button(root,text='delete',borderwidth='7',font='none 18 bold',pady='30',padx='36',bg='black',fg='orange',command= button_delete)



#defining buttons
buttonequal.grid(row='1',column='6')
buttonclear.grid(row='1',column='5')
button_delete.grid(row='4',column='5')

button_sin.grid(row='1',column='0')
button_cos.grid(row='1',column='1')
button_tan.grid(row='1',column='2')
button_csc.grid(row='2',column='0')
button_sec.grid(row='2',column='1')
button_cot.grid(row='2',column='2')
button_sinh.grid(row='3',column='0')
button_cosh.grid(row='3',column='1')
button_tanh.grid(row='3',column='2')
button_csch.grid(row='4',column='0')
button_sech.grid(row='4',column='1')
button_coth.grid(row='4',column='2')

buttonadd.grid(row='2',column='5')
buttonsub.grid(row='2',column='6')                  
buttonmult.grid(row='3',column='5')
buttondiv.grid(row='3',column='6')


buttonlb.grid(row='1',column='3')
buttonrb.grid(row='1',column='4')
buttonpower.grid(row='3',column='4')
buttonsqrt.grid(row='3',column='3')
buttons_log.grid(row='2',column='3')
button_ln.grid(row='2',column='4')
button_dot.grid(row='4',column='4')
button_com.grid(row='4',column='3')
