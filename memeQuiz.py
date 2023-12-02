print('Welcome to Meme Quiz2023!')
print('Python Project')
from tkinter import *
import random
from data import *
from PIL import Image, ImageTk
root=Tk()
root.state('zoomed')
#root.configure(background= "#F0ECE5")

l=Label(text='Welcome to Meme Quizz!!',font=("Ravie",30,'bold'),foreground="#5B0888").pack(pady=20)
n=1
score=0
index=1
def crt_wrg_meme(rootm,filename):
    crtmeme=Image.open(filename)
    crtmeme=crtmeme.resize((150,150))
    p=ImageTk.PhotoImage(crtmeme)
    crtlabel=Label(rootm,image=p)
    crtlabel.image=p
    crtlabel.grid(row=25,column=2)
def sel(chb,ans,rootm):
    global index,score
    if index in ans:
        if chb['text']==ans[index][0]:
            score+=10
            disableButtons('disabled',chb)
            crt_wrg_meme(rootm,'./images/image_01.png')
        else:
            disableButtons('disabled',chb)
            crt_wrg_meme(rootm,'./images/image_02.png')
    index+=1
def disableButtons(state,chb):
    chb['state']=state
def clear(root):
    for child in root.winfo_children():
        child.destroy()
def T():
    rootm=Toplevel()
    rootm.state('zoomed')
    def qa(n):
        clear(rootm)
        if n in travel_q:
            label=Label(rootm,text='Your question:',padx=600,font=("Rockwell",16))
            label.grid(row=4,column=2)
            labelQ=Label(rootm,text=travel_q[n],font=("Pristina",25,'bold'))
            labelQ.grid(row=6,column=2)
            ch=IntVar()
            
            chb1=Radiobutton(rootm,variable=ch,value=1,text=travel_a[n][1],command=lambda: sel(chb1,travel_a,rootm),padx=105,font=("Cascadia Code",15))
            chb1.grid(row=10,column=2)
            chb2=Radiobutton(rootm,variable=ch,value=2,text=travel_a[n][2],command=lambda: sel(chb2,travel_a,rootm),padx=105,font=("Cascadia Code",15))
            chb2.grid(row=11,column=2)
            chb3=Radiobutton(rootm,variable=ch,value=3,text=travel_a[n][3],command=lambda: sel(chb3,travel_a,rootm),padx=105,font=("Cascadia Code",15))
            chb3.grid(row=12,column=2)
            chb4=Radiobutton(rootm,variable=ch,value=4,text=travel_a[n][4],command=lambda: sel(chb4,travel_a,rootm),padx=105,font=("Cascadia Code",15))
            chb4.grid(row=13,column=2)

        
            nextB=Button(rootm,text="NEXT",command=lambda:qa(n+1),font="Times 15 bold")
            nextB.grid(row=20,column=2)
        else:
            sclabel=Label(rootm,text=" YOUR SCORE : "+str(score),font="Georgia 20 ",padx=550,pady= 20)
            sclabel.grid(row=23,column=2)
    qa(n)


travel_b=Button(root,text='TRAVEL',command=T,font="TImes 15 bold",bg='#F21368',width=10,height=3)
travel_b.place(x=300,y=250,anchor='center')

travel_b1=Button(root,text='BOOKS',font="Times 15 bold",bg='#F21368',width=10,height=3)
travel_b1.place(x=650,y=250,anchor='center')

travel_b5=Button(root,text='SPORTS',font="Times 15 bold",bg='#F21368',width=10,height=3)
travel_b5.place(x=1000,y=250,anchor='center')

travel_b2=Button(root,text='PYTHON',font="Times 15 bold",bg='#F21368',width=10,height=3)
travel_b2.place(x=300,y=450,anchor='center')

travel_b3=Button(root,text='MOVIES',font="Times 15 bold",bg='#F21368',width=10,height=3)
travel_b3.place(x=650,y=450,anchor='center')

round=PhotoImage(file='button_animals.png')
travel_b4=Button(root,image=round,border=0)
travel_b4.place(x=1000,y=450,anchor='center')






mainloop()
