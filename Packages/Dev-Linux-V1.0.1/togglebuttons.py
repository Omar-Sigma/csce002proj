#After Omar's Modifications to suit the other file
global is_deg_on
is_deg_on=False
global is_bin_on
is_bin_on=False
global is_hex_on
is_hex_on=False
global is_oct_on
is_oct_on=False

def close_switches(c, button_bin, button_hex, button_oct):
    global is_bin_on
    global is_hex_on
    global is_oct_on
    if c==2:
        
        if is_hex_on == True:
            button_hex.config(fg='#2293D6' ,bg='#343A3E')
            is_hex_on=False
            
        if is_oct_on == True:
            button_oct.config(fg='#2293D6' ,bg='#343A3E')
            is_oct_on=False
            
    elif c==3:
        if is_bin_on == True:
            button_bin.config(fg='#2293D6' ,bg='#343A3E')
            is_bin_on=False
            
        if is_oct_on == True:
            button_oct.config(fg='#2293D6' ,bg='#343A3E')
            is_oct_on=False
            
    elif c==4:
        if is_bin_on == True:
            button_bin.config(fg='#2293D6' ,bg='#343A3E')
            is_bin_on=False
            
        if is_hex_on == True:
            button_hex.config(fg='#2293D6' ,bg='#343A3E')
            is_hex_on=False
       
def switch_deg(button_deg):
    global is_deg_on
    if is_deg_on == False:
        button_deg.config(bg='#3daee9' ,fg='#FFFFFF')
        is_deg_on=True
        
    else:
        button_deg.config(bg='#343A3E' ,fg='#2293D6')
        is_deg_on=False

        
def switch_bin(button_bin, button_hex, button_oct):
    close_switches(2 , button_bin, button_hex, button_oct)
    global is_bin_on
    if is_bin_on == False:
        button_bin.config(bg='#3daee9' ,fg='#FFFFFF')
        is_bin_on=True
        
    else:
        button_bin.config(bg='#343A3E' ,fg='#2293D6')
        is_bin_on=False


def switch_hex(button_bin, button_hex, button_oct):
    close_switches(3 , button_bin, button_hex, button_oct)
    global is_hex_on
    if is_hex_on == False:
        button_hex.config(bg='#3daee9' ,fg='#FFFFFF')
        is_hex_on=True
        
    else:
        button_hex.config(bg='#343A3E' ,fg='#2293D6')
        is_hex_on=False


def switch_oct(button_bin, button_hex, button_oct):
    close_switches(4 , button_bin, button_hex, button_oct)
    global is_oct_on
    if is_oct_on == False:
        button_oct.config(bg='#3daee9' ,fg='#FFFFFF')
        is_oct_on=True
        
    else:
        button_oct.config(bg='#343A3E' ,fg='#2293D6')
        is_oct_on=False



