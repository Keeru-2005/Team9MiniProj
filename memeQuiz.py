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
l=Label(text='WELCOME TO MEME QUIZ!!',font=("gabriola",40,'bold'),foreground="white",bg='purple')
ltest=Label(text="CHOOSE A CATEGORY",font=("gabriola",40,"bold"),foreground="light blue",bg="purple")
l.place(x=550,y=50)
ltest.place(x=600,y=200)
n=1     
score=0 
index=1
def crt_wrg_meme(rootm,filename):
    crtmeme=Image.open(filename)
    crtmeme=crtmeme.resize((400,400))
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
def openimg(rootm,f):
    img=Image.open(f)
    img=img.resize((450,450))
    photo=ImageTk.PhotoImage(img)
    photo_label=Label(rootm,image=photo)
    photo_label.image=photo
    photo_label.grid(row=3,column=2)
lst=[10,20,30,40,50,60,70,80,90,100]

def final_score_meme(rootm,score,final):
    for i in lst:
        if score==i:
            openimg(rootm,final[lst.index(i)])
            break
    


def T():
    rootm=Toplevel()
    rootm.state('zoomed')
    bgq=Image.open('./images/quiz_pic.png')
    bgq=bgq.resize((100,90))
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
            
            chb1=Radiobutton(rootm,variable=ch,value=1,text=travel_a[n][1],command=lambda: sel(chb1,travel_a,rootm,'./images/tcrt.png','./images/twrg.png'),padx=105,font=("Cascadia Code",15))
            chb1.grid(row=10,column=2)
            chb2=Radiobutton(rootm,variable=ch,value=2,text=travel_a[n][2],command=lambda: sel(chb2,travel_a,rootm,'./images/tcrt.png','./images/twrg.png'),padx=105,font=("Cascadia Code",15))
            chb2.grid(row=11,column=2)
            chb3=Radiobutton(rootm,variable=ch,value=3,text=travel_a[n][3],command=lambda: sel(chb3,travel_a,rootm,'./images/tcrt.png','./images/twrg.png'),padx=105,font=("Cascadia Code",15))
            chb3.grid(row=12,column=2)
            chb4=Radiobutton(rootm,variable=ch,value=4,text=travel_a[n][4],command=lambda: sel(chb4,travel_a,rootm,'./images/tcrt.png','./images/twrg.png'),padx=105,font=("Cascadia Code",15))
            chb4.grid(row=13,column=2)

        
            nextB=Button(rootm,text="NEXT",command=lambda:qa(n+1),font="Times 15 bold")
            nextB.grid(row=20,column=2)
        else:
            sclabel=Label(rootm,text=" YOUR SCORE : "+str(score)+'/100',font="Georgia 20 ",padx=550,pady= 20)
            sclabel.grid(row=23,column=2)
            final_score_meme(rootm,score,travel_f)
    qa(n)
def P():
    rootm=Toplevel()
    rootm.state('zoomed')
    bgq=Image.open('./images/quiz_pic.png')
    bgq=bgq.resize((100,90))
    bgq_root=ImageTk.PhotoImage(bgq)
    bgq_label=Label(rootm, image=bgq_root)
    bgq_label.place(x=0,y=0,relwidth=1,relheight=1)
    def qa(n):
        clear(rootm)
        if n in python_q:
            label=Label(rootm,text='Your question:',padx=600,font=("Rockwell",16))
            label.grid(row=4,column=2)
            labelQ=Label(rootm,text=python_q[n],font=("Pristina",25,'bold'))
            labelQ.grid(row=6,column=2)
            ch=IntVar()
            
            chb1=Radiobutton(rootm,variable=ch,value=1,text=python_a[n][1],command=lambda: sel(chb1,python_a,rootm,'./images/pcrt.png','./images/pwrg.png'),padx=105,font=("Cascadia Code",15))
            chb1.grid(row=10,column=2)
            chb2=Radiobutton(rootm,variable=ch,value=2,text=python_a[n][2],command=lambda: sel(chb2,python_a,rootm,'./images/pcrt.png','./images/pwrg.png'),padx=105,font=("Cascadia Code",15))
            chb2.grid(row=11,column=2)
            chb3=Radiobutton(rootm,variable=ch,value=3,text=python_a[n][3],command=lambda: sel(chb3,python_a,rootm,'./images/pcrt.png','./images/pwrg.png'),padx=105,font=("Cascadia Code",15))
            chb3.grid(row=12,column=2)
            chb4=Radiobutton(rootm,variable=ch,value=4,text=python_a[n][4],command=lambda: sel(chb4,python_a,rootm,'./images/pcrt.png','./images/pwrg.png'),padx=105,font=("Cascadia Code",15))
            chb4.grid(row=13,column=2)

        
            nextB=Button(rootm,text="NEXT",command=lambda:qa(n+1),font="Times 15 bold")
            nextB.grid(row=20,column=2)
        else:
            sclabel=Label(rootm,text=" YOUR SCORE : "+str(score)+'/100',font="Georgia 20 ",padx=550,pady= 20)
            sclabel.grid(row=23,column=2)
            final_score_meme(rootm,score,python_f)
    qa(n)
def A():
    rootm=Toplevel()
    rootm.state('zoomed')
    bgq=Image.open('./images/quiz_pic.png')
    bgq=bgq.resize((100,90))
    bgq_root=ImageTk.PhotoImage(bgq)
    bgq_label=Label(rootm, image=bgq_root)
    bgq_label.place(x=0,y=0,relwidth=1,relheight=1)
    def qa(n):
        clear(rootm)
        if n in animals_q:
            label=Label(rootm,text='Your question:',padx=600,font=("Rockwell",16))
            label.grid(row=4,column=2)
            labelQ=Label(rootm,text=animals_q[n],font=("Pristina",25,'bold'))
            labelQ.grid(row=6,column=2)
            ch=IntVar()
            
            chb1=Radiobutton(rootm,variable=ch,value=1,text=animals_a[n][1],command=lambda: sel(chb1,animals_a,rootm,'./images/acrt.png','./images/awrg.png'),padx=105,font=("Cascadia Code",15))
            chb1.grid(row=10,column=2)
            chb2=Radiobutton(rootm,variable=ch,value=2,text=animals_a[n][2],command=lambda: sel(chb2,animals_a,rootm,'./images/acrt.png','./images/awrg.png'),padx=105,font=("Cascadia Code",15))
            chb2.grid(row=11,column=2)
            chb3=Radiobutton(rootm,variable=ch,value=3,text=animals_a[n][3],command=lambda: sel(chb3,animals_a,rootm,'./images/acrt.png','./images/awrg.png'),padx=105,font=("Cascadia Code",15))
            chb3.grid(row=12,column=2)
            chb4=Radiobutton(rootm,variable=ch,value=4,text=animals_a[n][4],command=lambda: sel(chb4,animals_a,rootm,'./images/acrt.png','./images/awrg.png'),padx=105,font=("Cascadia Code",15))
            chb4.grid(row=13,column=2)

        
            nextB=Button(rootm,text="NEXT",command=lambda:qa(n+1),font="Times 15 bold")
            nextB.grid(row=20,column=2)
        else:
            sclabel=Label(rootm,text=" YOUR SCORE : "+str(score)+'/100',font="Georgia 20 ",padx=550,pady= 20)
            sclabel.grid(row=23,column=2)
            final_score_meme(rootm,score,animals_f)
    qa(n)

def B():
    rootm=Toplevel()
    rootm.state('zoomed')
    bgq=Image.open('./images/quiz_pic.png')
    bgq=bgq.resize((100,90))
    bgq_root=ImageTk.PhotoImage(bgq)
    bgq_label=Label(rootm, image=bgq_root)
    bgq_label.place(x=0,y=0,relwidth=1,relheight=1)
    def qa(n):
        clear(rootm)
        if n in books_q:
            label=Label(rootm,text='Your question:',padx=600,font=("Rockwell",16))
            label.grid(row=4,column=2)
            labelQ=Label(rootm,text=books_q[n],font=("Pristina",25,'bold'))
            labelQ.grid(row=6,column=2)
            ch=IntVar()
            
            chb1=Radiobutton(rootm,variable=ch,value=1,text=books_a[n][1],command=lambda: sel(chb1,books_a,rootm,'./images/bcrt.png','./images/bwrg.png'),padx=105,font=("Cascadia Code",15))
            chb1.grid(row=10,column=2)
            chb2=Radiobutton(rootm,variable=ch,value=2,text=books_a[n][2],command=lambda: sel(chb2,books_a,rootm,'./images/bcrt.png','./images/bwrg.png'),padx=105,font=("Cascadia Code",15))
            chb2.grid(row=11,column=2)
            chb3=Radiobutton(rootm,variable=ch,value=3,text=books_a[n][3],command=lambda: sel(chb3,books_a,rootm,'./images/bcrt.png','./images/bwrg.png'),padx=105,font=("Cascadia Code",15))
            chb3.grid(row=12,column=2)
            chb4=Radiobutton(rootm,variable=ch,value=4,text=books_a[n][4],command=lambda: sel(chb4,books_a,rootm,'./images/bcrt.png','./images/bwrg.png'),padx=105,font=("Cascadia Code",15))
            chb4.grid(row=13,column=2)

        
            nextB=Button(rootm,text="NEXT",command=lambda:qa(n+1),font="Times 15 bold")
            nextB.grid(row=20,column=2)
        else:
            sclabel=Label(rootm,text=" YOUR SCORE : "+str(score)+'/100',font="Georgia 20 ",padx=550,pady= 20)
            sclabel.grid(row=23,column=2)
            final_score_meme(rootm,score,books_f)
    qa(n)

def M():
    rootm=Toplevel()
    rootm.state('zoomed')
    bgq=Image.open('./images/quiz_pic.png')
    bgq=bgq.resize((100,90))
    bgq_root=ImageTk.PhotoImage(bgq)
    bgq_label=Label(rootm, image=bgq_root)
    bgq_label.place(x=0,y=0,relwidth=1,relheight=1)
    def qa(n):
        clear(rootm)
        if n in movie_q:
            label=Label(rootm,text='Your question:',padx=600,font=("Rockwell",16))
            label.grid(row=4,column=2)
            labelQ=Label(rootm,text=movie_q[n],font=("Pristina",25,'bold'))
            labelQ.grid(row=6,column=2)
            ch=IntVar()
            
            chb1=Radiobutton(rootm,variable=ch,value=1,text=movie_a[n][1],command=lambda: sel(chb1,movie_a,rootm,'./images/mcrt.png','./images/mwrg.png'),padx=105,font=("Cascadia Code",15))
            chb1.grid(row=10,column=2)
            chb2=Radiobutton(rootm,variable=ch,value=2,text=movie_a[n][2],command=lambda: sel(chb2,movie_a,rootm,'./images/mcrt.png','./images/mwrg.png'),padx=105,font=("Cascadia Code",15))
            chb2.grid(row=11,column=2)
            chb3=Radiobutton(rootm,variable=ch,value=3,text=movie_a[n][3],command=lambda: sel(chb3,movie_a,rootm,'./images/mcrt.png','./images/mwrg.png'),padx=105,font=("Cascadia Code",15))
            chb3.grid(row=12,column=2)
            chb4=Radiobutton(rootm,variable=ch,value=4,text=movie_a[n][4],command=lambda: sel(chb4,movie_a,rootm,'./images/mcrt.png','./images/mwrg.png'),padx=105,font=("Cascadia Code",15))
            chb4.grid(row=13,column=2)

        
            nextB=Button(rootm,text="NEXT",command=lambda:qa(n+1),font="Times 15 bold")
            nextB.grid(row=20,column=2)
        else:
            sclabel=Label(rootm,text=" YOUR SCORE : "+str(score)+'/100',font="Georgia 20 ",padx=550,pady= 20)
            sclabel.grid(row=23,column=2)
            final_score_meme(rootm,score,movie_f)
    qa(n)
def S():
    rootm=Toplevel()
    rootm.state('zoomed')
    bgq=Image.open('./images/quiz_pic.png')
    bgq=bgq.resize((100,90))
    bgq_root=ImageTk.PhotoImage(bgq)
    bgq_label=Label(rootm, image=bgq_root)
    bgq_label.place(x=0,y=0,relwidth=1,relheight=1)
    def qa(n):
        clear(rootm)
        if n in sports_q:
            label=Label(rootm,text='Your question:',padx=600,font=("Rockwell",16))
            label.grid(row=4,column=2)
            labelQ=Label(rootm,text=sports_q[n],font=("Pristina",25,'bold'))
            labelQ.grid(row=6,column=2)
            ch=IntVar()
            
            chb1=Radiobutton(rootm,variable=ch,value=1,text=sports_a[n][1],command=lambda: sel(chb1,sports_a,rootm,'./images/scrt.png','./images/swrg.png'),padx=105,font=("Cascadia Code",15))
            chb1.grid(row=10,column=2)
            chb2=Radiobutton(rootm,variable=ch,value=2,text=sports_a[n][2],command=lambda: sel(chb2,sports_a,rootm,'./images/scrt.png','./images/swrg.png'),padx=105,font=("Cascadia Code",15))
            chb2.grid(row=11,column=2)
            chb3=Radiobutton(rootm,variable=ch,value=3,text=sports_a[n][3],command=lambda: sel(chb3,sports_a,rootm,'./images/scrt.png','./images/swrg.png'),padx=105,font=("Cascadia Code",15))
            chb3.grid(row=12,column=2)
            chb4=Radiobutton(rootm,variable=ch,value=4,text=sports_a[n][4],command=lambda: sel(chb4,sports_a,rootm,'./images/scrt.png','./images/swrg.png'),padx=105,font=("Cascadia Code",15))
            chb4.grid(row=13,column=2)

        
            nextB=Button(rootm,text="NEXT",command=lambda:qa(n+1),font="Times 15 bold")
            nextB.grid(row=20,column=2)
        else:
            sclabel=Label(rootm,text=" YOUR SCORE : "+str(score)+"/100",font="Georgia 20 ",padx=550,pady= 20)
            sclabel.grid(row=23,column=2)
            final_score_meme(rootm,score,sports_f)
    qa(n)

def S():
    rootm=Toplevel()
    rootm.state('zoomed')
    bgq=Image.open('./images/quiz_pic.png')
    bgq=bgq.resize((100,90))
    bgq_root=ImageTk.PhotoImage(bgq)
    bgq_label=Label(rootm, image=bgq_root)
    bgq_label.place(x=0,y=0,relwidth=1,relheight=1)
    def qa(n):
        clear(rootm)
        if n in sports_q:
            label=Label(rootm,text='Your question:',padx=600,font=("Rockwell",16))
            label.grid(row=4,column=2)
            labelQ=Label(rootm,text=sports_q[n],font=("Pristina",25,'bold'))
            labelQ.grid(row=6,column=2)
            ch=IntVar()
            
            chb1=Radiobutton(rootm,variable=ch,value=1,text=sports_a[n][1],command=lambda: sel(chb1,sports_a,rootm,'./images/scrt.png','./images/swrg.png'),padx=105,font=("Cascadia Code",15))
            chb1.grid(row=10,column=2)
            chb2=Radiobutton(rootm,variable=ch,value=2,text=sports_a[n][2],command=lambda: sel(chb2,sports_a,rootm,'./images/scrt.png','./images/swrg.png'),padx=105,font=("Cascadia Code",15))
            chb2.grid(row=11,column=2)
            chb3=Radiobutton(rootm,variable=ch,value=3,text=sports_a[n][3],command=lambda: sel(chb3,sports_a,rootm,'./images/scrt.png','./images/swrg.png'),padx=105,font=("Cascadia Code",15))
            chb3.grid(row=12,column=2)
            chb4=Radiobutton(rootm,variable=ch,value=4,text=sports_a[n][4],command=lambda: sel(chb4,sports_a,rootm,'./images/scrt.png','./images/swrg.png'),padx=105,font=("Cascadia Code",15))
            chb4.grid(row=13,column=2)

        
            nextB=Button(rootm,text="NEXT",command=lambda:qa(n+1),font="Times 15 bold")
            nextB.grid(row=20,column=2)
        else:
            sclabel=Label(rootm,text=" YOUR SCORE : "+str(score)+'/100',font="Georgia 20 ",padx=550,pady= 20)
            sclabel.grid(row=23,column=2)
            final_score_meme(rootm,score,sports_f)
    qa(n)




r1=PhotoImage(file='button_travel.png')
travel_b=Button(root,image=r1,border=0,bg='midnight blue',command=T)
travel_b.place(x=500,y=450,anchor='center')

r2=PhotoImage(file='button_books.png')
books_b1=Button(root,image=r2,border=0,bg='midnight blue',command=B)
books_b1.place(x=800,y=450,anchor='center')

r3=PhotoImage(file='button_sports.png')
sports_b=Button(root,image=r3,border=0,bg='midnight blue',command=S)
sports_b.place(x=1100,y=450,anchor='center')

r4=PhotoImage(file='button_python.png')
python_b=Button(root,image=r4,border=0,bg='midnight blue',command=P)
python_b.place(x=500,y=600,anchor='center')

r5=PhotoImage(file='button_movies.png')
movies_b=Button(root,image=r5,border=0,bg='midnight blue',command=M)
movies_b.place(x=800,y=600,anchor='center')

r6=PhotoImage(file='button_animals.png')
animals_b4=Button(root,image=r6,border=0,bg='midnight blue',command=A)
animals_b4.place(x=1100,y=600,anchor='center')
mainloop()
