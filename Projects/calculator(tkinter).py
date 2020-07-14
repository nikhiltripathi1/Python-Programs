from tkinter import *
class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.n1=Entry()
        self.n1.grid(row=2,column=4)
        self.n2=Entry()
        self.n2.grid(row=3,column=4)
        self.put=Text(width=17,height=1)
        self.put.grid(row=10,column=4)
        self.but1=Button(text=' + ',command=self.reveala).grid(row=6,column=0,sticky=W)
        self.but2=Button(text=' - ',command=self.reveals).grid(row=6,column=1,sticky=W)
        self.but3=Button(text=' * ',command=self.revealm).grid(row=6,column=2,sticky=W)
        self.but4=Button(text=' / ',command=self.reveald).grid(row=6,column=3,sticky=W)
    def reveala(self):
        num1=self.n1.get()
        num2=self.n2.get()
        result=int(num1)+int(num2)
        self.put.delete(0.0,END)
        self.put.insert(0.0,result)
    def reveals(self):
        num1=self.n1.get()
        num2=self.n2.get()
        result=int(num1)-int(num2)
        self.put.delete(0.0,END)
        self.put.insert(0.0,result)    
    def revealm(self):
        num1=self.n1.get()
        num2=self.n2.get()
        result=int(num1)*int(num2)
        self.put.delete(0.0,END)
        self.put.insert(0.0,result)
    def reveald(self):
        num1=self.n1.get()
        num2=self.n2.get()
        result=int(num1)/int(num2)
        self.put.delete(0.0,END)
        self.put.insert(0.0,result)    
root=Tk()
root.title("Calculator")
root.geometry("500x500")
app=Application(root)

