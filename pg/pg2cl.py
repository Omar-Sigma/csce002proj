import tkinter as tk0

class guicalc:
    def __init__(self,rootws):
        rootws.title("Test")
        rootws.columnconfigure(0, weight=1)
        rootws.columnconfigure(1, weight=1)
        rootws.columnconfigure(2, weight=1)
        rootws.columnconfigure(3, weight=1)
        rootws.rowconfigure(0, weight=1)
        rootws.rowconfigure(1, weight=1)

        #label1 = Label(rootws, text="Nice!")
        #label2 = Label(rootws, text="Good!")
        self.button1 = tk0.Button(rootws, text="Test", command=self.click).grid(row=0,column=0, sticky="nesw")
        self.button2 = tk0.Button(rootws, text="Test", command=self.click).grid(row=0,column=1, sticky="nesw")
        self.button3 = tk0.Button(rootws, text="Test", command=self.click).grid(row=0,column=2, sticky="nesw")
        self.button4 = tk0.Button(rootws, text="Test", command=self.click).grid(row=0,column=3, sticky="nesw")
        self.button5 = tk0.Button(rootws, text="Test", command=self.click).grid(row=1,column=0, sticky="nesw", columnspan=2)
        self.button6 = tk0.Button(rootws, text="Test", command=lambda: self.click(rootws)).grid(row=1,column=2, sticky="nesw", columnspan=2)

    def click(self, rootws):
        hey = 9*989
        self.label1= tk0.Label(rootws, text=str(hey))
        self.label1.grid(row=2,column=0,columnspan=4)
        #label3.grid(row=3,column=1)



    #label1.grid(row=0,column=0)
    #label2.grid(row=1,column=1)

root = tk0.Tk()
guis=guicalc(root)
#rooth=root.winfo_height()
#rootw=root.winfo_width()
if __name__ == "__main__":
    root.mainloop()
