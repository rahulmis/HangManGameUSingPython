def hangman():
    global ss,ll,ss1,n,ffdata,temps,first
    first = inpp.get()
    input1.delete(0,END)
    if(n>0):
        if(first in ss):
            for i in range(ss1):
                if(ss[i] == first and ll[i] == '*'):
                    ll.pop(i)
                    ll.insert(i,ss[i])
                    xx = ''.join(ll)
                    ss = list(ss)
                    ss.pop(i)
                    ss.insert(i,"*")
                    wordlabel.configure(text=xx)
                    if(xx==temps):
                        ans.configure(text='Congratulations You won The game......')
                        res = messagebox.askyesno("Notification",'Congratulations You won The game......\n want to play again ?')
                        if(res==True):
                            chooseword()
                        else:
                            root.destroy()
                    else:
                        break
        else:
            n -= 1
            leftchances.configure(text='Left = {}'.format(n))
    if(n<=0):
        ans.configure(text='OOps You Loss The game......')
        res = messagebox.askyesno("Notification", 'OOps You Loss The game......\n want to play again ?')
        if (res == True):
            chooseword()
        else:
            root.destroy()


def jj(event):
    hangman()
from tkinter import *
from tkinter import messagebox
import random
worldlist = ['yellow','blue','green','red','cyan','pink','black']

root = Tk()
root.geometry('800x500+300+100')
root.configure(bg='cyan')
root.iconbitmap('pp2.ico')
root.title('Hangman Game')

#---------------------------------------------------------------------------  Labels
introlabel = Label(root,text='Welcome to Hangman Game',font=('arial',35,'bold'),bg='cyan')
introlabel.place(x=100,y=0)

wordlabel = Label(root,text='',font=('arial',55,'bold'),bg='cyan')
wordlabel.place(x=300,y=150)

leftchances = Label(root,text='',font=('arial',25,'bold'),bg='cyan')
leftchances.place(x=650,y=100)

ans = Label(root,text='',font=('arial',25,'bold'),bg='cyan')
ans.place(x=100,y=440)

#---------------------------------------------------------------------------- Entry Box

inpp = StringVar()
input1 = Entry(root,font=('arial',25,'bold'),relief=RIDGE,bd=5,bg='green',justify='center',fg='white',textvariable=inpp)
input1.focus_set()
input1.place(x=210,y=250)
#------------------------------------------------------------------------------------- Button
bt1 = Button(root,text='Submit',font=('arial',15,'bold'),width=15,bd=5,bg='red',activebackground='blue'
             ,activeforeground='white',command=hangman)
bt1.place(x=300,y=350)
root.bind("<Return>",jj)
#------------------------------------------------------- World Select Function
def chooseword():
    global ss,ll,ss1,n,ffdata,temps
    ss = random.choice(worldlist)
    ll = ["*" for i in ss]
    ss1 = len(ss)
    n = ss1
    temps = ss
    leftchances.configure(text='Left = {}'.format(n))
    ffdata = ''
    for i in ll:
        ffdata += i+' '
    wordlabel.configure(text=ffdata)
    ans.configure(text='')


chooseword()
root.mainloop()