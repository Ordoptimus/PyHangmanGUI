#PyHangmanGUI: A Hangman Game with TKinter GUI.
#By Ordoptimus.

from tkinter import *
from tkinter import messagebox
import pickle
import json
import ast

def click():
    key=qs.get()
    key=key.lower()
    blanks.delete(0.0,END)
    try:
        keystr=qdmainl[key]
        global keylen
        keylen=len(keystr)
        global keylst
        keylst=list(keystr)
        for i in range(0,keylen):
            ansblanks.extend('_')
        ansblanksstr='   '.join(ansblanks)
        keystr=ansblanksstr
    except:
        keystr="No such question!"
    blanks.insert(END,keystr)
    
def click1(event=None):
    letter=letterentry.get()
    letter=letter.lower()
    blanks.delete(0.0,END)
    letterentry.delete(0,END)
    if(len(letter)!=1):
        global letterstr
        letter=letterstr
        blanks.insert(END,letter)
        messagebox.showinfo("Warning!", "Enter a single letter. (-_-)")
    else:
        flag=0
        doneinpflag=0
        for j in range(0,len(doneinputs)):
            if(letter==doneinputs[j]):
               letter=letterstr
               blanks.insert(END,letter)
               messagebox.showinfo("Warning","You already tried that, goldfish! ;-)")
               flag=2
               doneinpflag=1
            else:
               j+=1
        if(doneinpflag!=1):
            doneinputs.extend(letter)
        for k in range(0,keylen):
            if(flag!=2):
                if(letter==keylst[k]):
                    ansblanks[k]=letter
                    flag=1
                    global revcounter
                    revcounter+=1
                    if(revcounter==keylen):
                        messagebox.showinfo("You Won!","RESET and type the next question or EXIT (ESC).")
                        global wonflag
                        wonflag=1
                else:
                    k+=1
        letterstr='  '.join(ansblanks)
        letter=letterstr
        if(flag==1):
            blanks.insert(END,letter)
        elif(flag!=2):
            global counter
            counter+=1
            if(counter<6 and wonflag==0):
                global imgarr
                pic.configure(image=imgarr[counter])
                blanks.insert(END,letter)
            elif(wonflag==1):
                messagebox.showinfo("YOU WON!","RESET and type the next question or EXIT (ESC).")
            else:
                messagebox.showinfo("YOU LOST.","Better luck next time! :-P")

def click2():
    blanks.delete(0.0,END)
    qs.delete(0,END)
    letterentry.delete(0,END)
    pic.configure(image=img1)
    global ansblanks, counter, revcounter,doneinputs,wonflag
    ansblanks,doneinputs=[],[]
    counter,revcounter,wonflag=0,0,0

def click3(event=None):
    root.destroy()
    exit()
                  
root=Tk()
root.title("PyHangmanGUI | By Ordoptimus")
root.configure(background="black")
fonts=("Helvetica","12")

img0=PhotoImage(file="wizard3.png")
img1=PhotoImage(file="HangmanWord.png")
img2=PhotoImage(file="HangmanWord6.png")
img3=PhotoImage(file="HangmanWord5.png")
img4=PhotoImage(file="HangmanWord4.png")
img5=PhotoImage(file="HangmanWord3.png")
img6=PhotoImage(file="HangmanWord2.png")
img7=PhotoImage(file="HangmanWord1.png")

w=img0.width()
h=img0.height()
cv=Canvas(width=w,height=h)
cv.create_image(0,0,image=img0,anchor="nw")
cv.grid(columnspan=20,rowspan=15)

root.bind("<Return>",click1)
root.bind("<Escape>",click3)

pic=Label(root,image=img1,bg="black",fg="white",anchor=NE)
pic.grid(row=2,column=5,pady=50)

qs=Entry(root,width=50,bg="grey",fg="black",cursor="pencil white",font=fonts)
qs.grid(row=3,column=5,pady=10,padx=10)
l1=Label(root,bg="black",fg="white",text="Type the question here ->",font=fonts)
l1.grid(row=3,column=1)
b=Button(root,text="Submit Question",width=20,bg="black",fg="orange",command=click)
b.grid(row=5,column=5)

blanks=Text(root,width=30,height=3,wrap=WORD,background="black",foreground="yellow",cursor="circle",font=fonts)
blanks.grid(row=6,column=5,padx=80,pady=20)

letterentry=Entry(root,width=50,bg="grey",fg="black",cursor="pencil white",font=fonts)
letterentry.grid(row=7,column=5,pady=5)
l2=Label(root,bg="black",fg="white",text="Type your letter answer here ->",font=fonts)
l2.grid(row=7,column=1,padx=50)
b1=Button(root,text="Submit Letter (or ENTER)",width=25,bg="black",fg="orange",command=click1)
b1.grid(row=9,column=5,pady=5)

b2=Button(root,text="RESET",width=20,bg="grey",command=click2)
b2.grid(row=10,column=5,pady=5)
b2=Button(root,text="EXIT (ESC)",width=20,bg="grey",command=click3)
b2.grid(row=11,column=5,pady=20)

#qdict={'immortal bird':'phoenix','disarming spell':'expelliarmus','awesome coder of hangman':"ar'yn",'wielder of the mantle':'aha maela'}
qdmain="{'The monster who killed/petrified people in the chamber of secrets':'Basilisk','The plant which Neville gave to Harry to survive underwater':'gillyweed','What is the name of the woman who owned the three broomsticks':'rosmerta','Which Weasley brother was bitten by Fenrir Greyback':'bill','What is the real name of lord Voldemort':'tom','What is the name of the dragon owned by Hagrid in the philosophers stone':'norbert','what is the name of the person who owns the philosophers stone':'nicholas flamel','Who was the half blood prince':'snape','Who betrayed James and Lily potter':'Peter Pettigrew','What curse was used  by Bellatrix lestrange on Nevilles parents':'cruciatus curse','Who was Harrys first girlfriend':'cho','The name of the goblin who showed Harry to his vault the first time he visited Gringotts':'griphook','Dumbledore duelled with this wizard in 1947':'grindelwald','Who was the editor of the daily prophet':'rita skeeter','Which is the most famous sport of wizarding world':'quidditch','Which ball is seeker supposed to catch':'snitch','Who was the founder of Order of Phoenix':'dumbledore','Who was the Hermiones cat':'crookshanks','Which spell is used for memory manipulation':'obliviate','Who was the famous Bulgarian seeker':'viktor krum','What was the surname of Rachels secretary whom she dated':'jones','What is the name of mother in how I met your mother':'tracy','What is the name of the actor who portrays Michael scott in the office':'steve','What is the name of Wills mother in stranger things':'joyce','What Is the surname of jake In Brooklyn nine nine':'peralta','What is the word that barney uses frequently in how I met your mother':'legendary','What is the name of the doppleganger of elena in the vampire diaries':'katherine','What is the name of bellas father in twilight':'charlie','What is the name of merediths mother in greys anatomy':'ellis','What is the name of hanna bakers mother in 13 reasons why':'olivia','What was the name of cheryls brother who was killed in riverdale':'jason','Who left ted at the altar':'stella','What was the name of the girl who shaved her head in friends':'bonnie','What is the name of Hoppers daughter who died':'sara','What is the name of merediths sister who died in a plane crash':'lexie','What is  leonards surname':'hofstader','The first web based email service':'hotmail','The ISRO navigation center was set up at':'bylalu','The process of killing diseases producing micro organism in food items by heat':'pasteurization','What is the name of the instrument that measures wind speed':'anemometer','A method of growing plants without soil':'hydroponics','The fear of being out of mobile phone contact is known as':'nomophobia','What astronomer suggested that the Sun was at the center of the solar system':'copernicus','Indias satellite launch pad is located at':'sriharikota','a person with very pale skin and eyes':'albino','In science, what is the name for the classification of plants and animals':'taxonomy','Process of cell division can take place by':'mitosis','Polymer used to manufacture electrical switches':'bakelite','Recyclable plastics':'thermoplastics','Which chemical is the reason behind the brown colour of human faces':'bilirubin','White poison':'sugar','Element excreted through human sweat':'sulphur','Metal causing itai itai disease':'cadmium','This has highly stable pH':'buffer','Study of electrical charges':'electrostatics','Who is known as human computer in India':'shakuntala devi'}"
qdict1=ast.literal_eval(qdmain)
#print(qdict1)
qdmainl=dict((k.lower(),v.lower()) for k,v in qdict1.items())
#print(qdmainl)

imgarr=[img1,img2,img3,img4,img5,img6,img7]
ansblanks,keylst,doneinputs=[],[],[]
letterstr='',''
keylen,counter,revcounter,wonflag=0,0,0,0

root.mainloop()
