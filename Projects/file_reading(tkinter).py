from tkinter import *
from random import choice
class application(Frame):
    def __init__(self,master):
        super(application,self).__init__(master)
        self.grid()
        self.widgets()
    def widgets(self):
        self.txt=Text(width=15,height=1,wrap=WORD)
        self.but=Button(self,text='next',command=self.move)
        self.txt.grid(row=5,column=0)
        self.but.grid(row=1,column=0)
    def move(self):
        f=open("movie.txt","r")
        content=f.read()
        new=content.split('  ')
        movie=choice(new)
        self.txt.delete(0.0,END)
        self.txt.insert(0.0,movie)
root=Tk()
root.title('movie')
root.geometry('200x200')                 
app=application(root)
