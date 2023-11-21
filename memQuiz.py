print('Welcome to Meme Quiz2023!')
print('Python Project')
from tkinter import *
import random
movie_q={1:'question1',2:'question2',3:'question3',4:'question4',5:'question5',6:'question6',7:'question7',8:'question8',9:'question9',10:'question10'}
movie_a={1:('crt ans','c1','c2','c3','c4'),2:('crt ans','c1','c2','c3','c4'),3:('crt ans','c1','c2','c3','c4'),4:('crt ans','c1','c2','c3','c4'),5:('crt ans','c1','c2','c3','c4'),6:('crt ans','c1','c2','c3','c4'),7:('crt ans','c1','c2','c3','c4'),8:('crt ans','c1','c2','c3','c4'),9:('crt ans','c1','c2','c3','c4'),10:('crt ans','c1','c2','c3','c4')}
root=Tk()
label=Label(root,text='Your question:')
label.pack()
qn=random.randint(1,10)
labelQ=Label(root,text=movie_q[qn])
labelQ.pack()
ch=IntVar()
for i in range(1,5):
    chb=Radiobutton(root,variable=ch,value=i,text=movie_a[qn][i])
    chb.pack()

mainloop()