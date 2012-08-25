from tkinter import *
class T:
    def __init__(self):
        self.tk=Tk()
        self.tk.geometry('400x300+270+50')
    def start(self):
        self.tk.mainloop()
    def creatAll(self):
        self.lab=Label(self.tk,text='L╮(╯▽╰)╭')
        self.tex=Entry(self.tk,bg='white')
        self.but=Button(self.tk,text='( ⊙ o ⊙ )')
        self.che=Checkbutton(self.tk,text='check')
        self.tbox=Text(self.tk)
    def packAll(self):
        self.lab.pack()
        self.tex.pack()
        self.but.pack()
        self.che.pack()
    def placeAll(self):
        self.lab.place(x=90,y=0)
        self.tex.place(x=30,y=40)
        self.but.place(x=20,y=40)
        self.che.place(x=70,y=20)
    def gridAll(self):
        self.lab.grid(row=0,column=0)
        self.tex.grid(row=0,column=1)
        self.but.grid(row=1,column=0)
        self.che.grid(row=1,column=1)        
if __name__=='__main__':
    t=T()
    t.creatAll()
    #t.packAll()
    #t.placeAll()
    t.gridAll()
    t.start()
