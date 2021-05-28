from tkinter import *

class GUI_Start:

    def __init__(self, master):
        self.master = master
        self.master.geometry('300x300')
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.win_colour = '#D2B48C'
        self.frames = {}

        for window in ['win1', 'win2']:
            frame = Frame(self.master, bg=self.win_colour, bd=10, relief=GROOVE)
            frame.grid(row=0, column=0, sticky='news')
            setattr(self, window, frame)
            self.frames[window] = frame

        Page_1(self.frames)

    def Next_Page(self, frames, controller):
        controller(frames)


class Page_1(GUI_Start):

    def __init__(self, master):
        self.master = master
        self.master['win1'].tkraise()

        page1_label = Label(self.master['win1'], text='PAGE 1')
        page1_label.pack(fill=X)

        page1_button = Button(self.master['win1'], text='Visit Page 2...', command=lambda: self.Next_Page(self.master, Page_2))
        page1_button.pack(fill=X, side=BOTTOM)


class Page_2(GUI_Start):

    def __init__(self, master):
        self.master = master
        self.master['win2'].tkraise()

        page2_label = Label(self.master['win2'], text='PAGE 2')
        page2_label.pack(fill=X)

        page2_button = Button(self.master['win2'], text='Back to Page 1...', command=lambda: self.Next_Page(self.master, Page_1))
        page2_button.pack(fill=X, side=BOTTOM)


root = Tk()
gui = GUI_Start(root)
root.mainloop()
