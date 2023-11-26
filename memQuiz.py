print('Welcome to Meme Quiz2023!')
print('Python Project')
from tkinter import *
import random
from data import travel_q
from data import travel_a
root=Tk()
root.geometry('700x600')
n=1
score=0
index=1
def sel(chb,ans):
    global index,score
    if index in ans:
        if chb['text']==ans[index][0]:
            score+=10
    index+=1
    
def T():
    rootm=Toplevel()
    rootm.geometry('800x500')
    rootm.withdraw()
    rootm.deiconify()
    def qa(n):
        rootm.withdraw()
        rootm.deiconify()
        if n in travel_q:
            label=Label(rootm,text='Your question:',padx=100)
            label.grid(row=4,column=2)
            labelQ=Label(rootm,text=travel_q[n],width=100,wraplength=600)
            labelQ.grid(row=6,column=2,sticky='W')
            ch=IntVar()
            
            chb1=Radiobutton(rootm,variable=ch,value=1,text=travel_a[n][1],command=lambda: sel(chb1,travel_a),padx=105)
            chb1.grid(row=10,column=2)
            chb2=Radiobutton(rootm,variable=ch,value=2,text=travel_a[n][2],command=lambda: sel(chb2,travel_a),padx=105)
            chb2.grid(row=11,column=2)
            chb3=Radiobutton(rootm,variable=ch,value=3,text=travel_a[n][3],command=lambda: sel(chb3,travel_a),padx=105)
            chb3.grid(row=12,column=2)
            chb4=Radiobutton(rootm,variable=ch,value=4,text=travel_a[n][4],command=lambda: sel(chb4,travel_a),padx=105)
            chb4.grid(row=13,column=2)
            
            nextB=Button(rootm,text="Next",command=lambda:qa(n+1))
            nextB.grid(row=20,column=2)
        else:
            sclabel=Label(rootm,text="your score :"+str(score))
            sclabel.grid(row=23,column=2)
    qa(n)
travel_b=Button(root,text='Travel',command=T)
travel_b.grid(row=6,column=6)
mainloop()