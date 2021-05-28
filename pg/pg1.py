from tkinter import *

root = Tk()
root.title("Test")
#root.configure(bg="#08296A")
def click():
    hey = 9*989
    label3 = Label(root, text=str(hey))
    #label3.grid(row=3,column=1)
    label3.pack()

#label1 = Label(root, text="Nice!")
#label2 = Label(root, text="Good!")
#button1 = Button(root, text="Test", padx=50, pady=10, command=click).grid(row=2,column=0)
button1 = Button(root, text="Test", command=click, fg="blue", bg="purple").pack()
input1 = Entry(root)
input1.place(width=50, height=50)
input1.pack()
#label1.grid(row=0,column=0)
#label2.grid(row=1,column=1)

root.mainloop()
