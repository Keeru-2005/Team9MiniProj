print('Welcome to Meme Quiz2023!')
print('Python Project')
from tkinter import *
import random
movie_q={1:'question1',2:'question2',3:'question3',4:'question4',5:'question5',6:'question6',7:'question7',8:'question8',9:'question9',10:'question10'}
movie_a={1:('crt ans','c1','c2','c3','c4'),2:('crt ans','c1','c2','c3','c4'),3:('crt ans','c1','c2','c3','c4'),4:('crt ans','c1','c2','c3','c4'),5:('crt ans','c1','c2','c3','c4'),6:('crt ans','c1','c2','c3','c4'),7:('crt ans','c1','c2','c3','c4'),8:('crt ans','c1','c2','c3','c4'),9:('crt ans','c1','c2','c3','c4'),10:('crt ans','c1','c2','c3','c4')}
root=Tk()
root.geometry('700x600')
n=1

def m():
    rootm=Toplevel()
    def qa(n):
        if n in movie_q:
            label=Label(rootm,text='Your question:')
            label.grid(row=4,column=4)
            labelQ=Label(rootm,text=movie_q[n])
            labelQ.grid(row=6,column=2)
            ch=IntVar()
            for i in range(1,5):
                chb=Radiobutton(rootm,variable=ch,value=i,text=movie_a[n][i])
                chb.grid(row=i+7,column=3)
            
            nextB=Button(rootm,text="Next",command=lambda:qa(n+1))
            nextB.grid(row=12,column=10)
        else:
            print('thanks')
    qa(n)
movie_b=Button(root,text='movie',command=m)
movie_b.grid(row=6,column=6)
mainloop()