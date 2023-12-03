print('Welcome to Meme Quiz2023!')
print('Python Project')
from tkinter import *
import random
from data import *
from PIL import Image, ImageTk
root=Tk()
root.state('zoomed')
#root.configure(background= "#F0ECE5")


bg=Image.open('./images/bg5.png')
bg=bg.resize((1700,900))
bg_root=ImageTk.PhotoImage(bg)
rootlabel=Label(root, image=bg_root)
rootlabel.place(x=0,y=0,relwidth=1,relheight=1)
l=Label(text='WELCOME TO MEME QUIZZ!!',font=("Ravie",30,'bold'),foreground="white",bg='midnight blue').pack()
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
def sel(chb,ans,rootm,crt,wrg):
    global index,score
    if index in ans:
        if chb['text']==ans[index][0]:
            score+=10
            disableButtons('disabled',chb)
            crt_wrg_meme(rootm,crt)
        else:
            disableButtons('disabled',chb)
            crt_wrg_meme(rootm,wrg)
    index+=1
def disableButtons(state,chb):
    chb['state']=state
def clear(root):
    for child in root.winfo_children():
        child.destroy()
def T():
    rootm=Toplevel()
    rootm.state('zoomed')
    bgq=Image.open('./images/quiz_pic.png')
    bgq=bgq.resize((1700,900))
    bgq_root=ImageTk.PhotoImage(bgq)
    bgq_label=Label(rootm, image=bgq_root)
    bgq_label.place(x=0,y=0,relwidth=1,relheight=1)
    def qa(n):
        clear(rootm)
        if n in travel_q:
            label=Label(rootm,text='Your question:',padx=600,font=("Rockwell",16))
            label.grid(row=4,column=2)
            labelQ=Label(rootm,text=travel_q[n],font=("Pristina",25,'bold'))
            labelQ.grid(row=6,column=2)
            ch=IntVar()
            
            chb1=Radiobutton(rootm,variable=ch,value=1,text=travel_a[n][1],command=lambda: sel(chb1,travel_a,rootm,'./images/tcrt.png','./images/Screenshot (21).png'),padx=105,font=("Cascadia Code",15))
            chb1.grid(row=10,column=2)
            chb2=Radiobutton(rootm,variable=ch,value=2,text=travel_a[n][2],command=lambda: sel(chb2,travel_a,rootm,'./images/tcrt.png','./images/Screenshot (21).png'),padx=105,font=("Cascadia Code",15))
            chb2.grid(row=11,column=2)
            chb3=Radiobutton(rootm,variable=ch,value=3,text=travel_a[n][3],command=lambda: sel(chb3,travel_a,rootm,'./images/tcrt.png','./images/Screenshot (21).png'),padx=105,font=("Cascadia Code",15))
            chb3.grid(row=12,column=2)
            chb4=Radiobutton(rootm,variable=ch,value=4,text=travel_a[n][4],command=lambda: sel(chb4,travel_a,rootm,'./images/tcrt.png','./images/Screenshot (21).png'),padx=105,font=("Cascadia Code",15))
            chb4.grid(row=13,column=2)

        
            nextB=Button(rootm,text="NEXT",command=lambda:qa(n+1),font="Times 15 bold")
            nextB.grid(row=20,column=2)
        else:
            sclabel=Label(rootm,text=" YOUR SCORE : "+str(score),font="Georgia 20 ",padx=550,pady= 20)
            sclabel.grid(row=23,column=2)
    qa(n)

r1=PhotoImage(file='button_travel.png')
travel_b=Button(root,image=r1,border=0,bg='midnight blue',command=T)
travel_b.place(x=500,y=450,anchor='center')

r2=PhotoImage(file='button_books.png')
books_b1=Button(root,image=r2,border=0,bg='midnight blue')
books_b1.place(x=800,y=450,anchor='center')

r3=PhotoImage(file='button_sports.png')
sports_b=Button(root,image=r3,border=0,bg='midnight blue')
sports_b.place(x=1100,y=450,anchor='center')

r4=PhotoImage(file='button_python.png')
python_b=Button(root,image=r4,border=0,bg='midnight blue')
python_b.place(x=500,y=600,anchor='center')

r5=PhotoImage(file='button_movies.png')
movies_b=Button(root,image=r5,border=0,bg='midnight blue')
movies_b.place(x=800,y=600,anchor='center')

r6=PhotoImage(file='button_animals.png')
animals_b4=Button(root,image=r6,border=0,bg='midnight blue')
animals_b4.place(x=1100,y=600,anchor='center')






mainloop()
