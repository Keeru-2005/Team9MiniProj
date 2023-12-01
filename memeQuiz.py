print('Welcome to Meme Quiz2023!')
print('Python Project')
from tkinter import *
import random
from data import *
from PIL import Image, ImageTk
root=Tk()
root.state('zoomed')
root.configure(background= "#F49393")
n=1
score=0
index=1
def sel(chb,ans,rootm):
    global index,score
    if index in ans:
        if chb['text']==ans[index][0]:
            score+=10
            crtmeme=Image.open('./images/image_01.png')
            crtmeme=crtmeme.resize((150,150))
            p=ImageTk.PhotoImage(crtmeme)
            crtlabel=Label(rootm,image=p,text='Correct answer')
            crtlabel.image=p
            crtlabel.grid(row=25,column=2)
    index+=1
    
def T():
    rootm=Toplevel()
    rootm.state('zoomed')
    def qa(n):
        if n in travel_q:
            label=Label(rootm,text='Your question:',padx=100)
            label.grid(row=4,column=2)
            labelQ=Label(rootm,text=travel_q[n],width=200,wraplength=600)
            labelQ.grid(row=6,column=2)
            ch=IntVar()
            
            chb1=Radiobutton(rootm,variable=ch,value=1,text=travel_a[n][1],command=lambda: sel(chb1,travel_a,rootm),padx=105)
            chb1.grid(row=10,column=2)
            chb2=Radiobutton(rootm,variable=ch,value=2,text=travel_a[n][2],command=lambda: sel(chb2,travel_a,rootm),padx=105)
            chb2.grid(row=11,column=2)
            chb3=Radiobutton(rootm,variable=ch,value=3,text=travel_a[n][3],command=lambda: sel(chb3,travel_a,rootm),padx=105)
            chb3.grid(row=12,column=2)
            chb4=Radiobutton(rootm,variable=ch,value=4,text=travel_a[n][4],command=lambda: sel(chb4,travel_a,rootm),padx=105)
            chb4.grid(row=13,column=2)
            
            nextB=Button(rootm,text="Next",command=lambda:qa(n+1))
            nextB.grid(row=20,column=2)
        else:
            sclabel=Label(rootm,text="your score :"+str(score))
            sclabel.grid(row=23,column=2)
    qa(n)
travel_b=Button(root,text='TRAVEL',command=T,font="Times 15 bold",bg='#F21368',width=10,height=3)
#travel_b=("Bell Gothic Std Black",20,"bold")
#travel_b.configure(font=travel_b)
travel_b.place(x=300,y=250,anchor='center')

travel_b1=Button(root,text='BOOKS',font="Times 15 bold",bg='#F21368',width=10,height=3)
travel_b1.place(x=650,y=250,anchor='center')

travel_b5=Button(root,text='SPORTS',font="Times 15 bold",bg='#F21368',width=10,height=3)
travel_b5.place(x=1000,y=250,anchor='center')

travel_b2=Button(root,text='PYTHON',font="Times 15 bold",bg='#F21368',width=10,height=3)
travel_b2.place(x=300,y=450,anchor='center')

travel_b3=Button(root,text='MOVIES',font="Times 15 bold",bg='#F21368',width=10,height=3)
travel_b3.place(x=650,y=450,anchor='center')

travel_b4=Button(root,text='ANIMALS',font="Times 15 bold",bg='#F21368',width=10,height=3)
travel_b4.place(x=1000,y=450,anchor='center')






mainloop()
