from tkinter import *

def select(event):
    b=event.widget
    value=b['text']
    print(value)

    for i in range(15) :
       if value == correct_answer[i]:
          questionArea.delete(1.0,END)
          questionArea.insert(END,question[i+1])

          optionButton1.config(text=first_option[i+1])
          optionButton2.config(text=second_option[i+1])
          optionButton3.config(text=third_option[i+1])
          optionButton4.config(text=fourth_option[i+1])
          amountlabel.config(image=amountImages[i])

       if value not in correct_answer:
           def close():
               root1.destroy()
               root.destroy()

           def tryagain():
               questionArea.insert(END,question[0])

               optionButton1.config(text=first_option[0])
               optionButton2.config(text=second_option[0])
               optionButton3.config(text=third_option[0])
               optionButton4.config(text=fourth_option[0])
               amountlabel.config(image=amountImages[0])
               root1.destroy()

           root1=Toplevel()
           root1.config(bg='black')
           root1.geometry("570x570+150+100")
           root1.title('you won 0 wound')
           centerImage = PhotoImage(file='center.png')
           rootlabel = Label(root1, image=centerImage, bg='black', width=300, height=200)
           rootlabel.pack()

           loseLabel=Label(root1,text='YOU lose',font=('arial',40,'bold'),bg='black',fg='white')
           loseLabel.pack()

           tryagainbutton=Button(root1,text="TRY AGAIN", font=('arial',18,'bold'),bd=0,bg='black',fg='white',
                    activeforeground='white',activebackground='black',cursor='hand2',command=tryagain)
           tryagainbutton.pack()

           closebutton = Button(root1, text="CLOSE", font=('arial', 18, 'bold'), bd=0,bg='black',fg='white',
                                   activeforeground='white', activebackground='black', cursor='hand2',command=close)
           closebutton.pack()

           root1.mainloop()
           break

       if value == correct_answer[14]:
              def close():
                  root2.destroy()
                  root.destroy()

              root2 = Toplevel()
              root2.config(bg='black')
              root2.geometry("1000x500+150+200")
              root2.title('you are milliniore')
              centerImage = PhotoImage(file='center.png')
              rootlabel = Label(root2, image=centerImage, bg='black', width=300, height=200)
              rootlabel.pack()

              loseLabel = Label(root2, text='YOU ARE A MILLIONIER', font=('arial', 60, 'bold'), bg='black', fg='white')
              loseLabel.pack()
              closebutton = Button(root2, text="CLOSE", font=('arial', 18, 'bold'), bd=0,
                                   activeforeground='white', activebackground='black', cursor='hand2', command=close)
              closebutton.pack()

              root2.mainloop()
              break


question =['this is first','this nis second','this nis third','this is fourth','this is fifth','this is sixth',
           'this is seventh','this is 8','this is 9','this is 10',
           'this is 11','this is 12','this is 13','this is 14','this is 15',
           ]
first_option =["first1","first2","first3","first4","first5","first6","first7","first8","first9","first10","first11",
               "first12","first13","billioner","millioner"]

second_option =["second1","second2","second3","second4","second5","second6","second7","second8",
                "second9","second10","second11","second12","second13","second14","second15"]

third_option =["third1","third2","third3","third4","third5","third6","third7","third8",
               "third9","third10","third11","third12","third13","third14","third15"]
fourth_option =["foutrh1","foutrh2","foutrh3","foutrh4","foutrh5","foutrh6","foutrh7","foutrh8",
                "foutrh9","foutrh10","foutrh11","foutrh12","foutrh13","foutrh14","foutrh15",]
correct_answer=['first1','first2','first3','first4','first5',"first6","first7","first8","first9","first10","first11",
               "first12","first13","billioner","millioner"]
root=Tk()




root.geometry("1270x652+0+0")
root.title("kaun banega crorepati")
root.config(bg='black')

leftframe=Frame(root,bg='black',padx=90)
leftframe.grid(row=0 , column=0)

topframe=Frame(leftframe,bg='black',pady=12)
topframe.grid()

centerframe=Frame(leftframe,bg='black',pady=12)
centerframe.grid(row=1 , column=0)

bottomframe=Frame(leftframe)
bottomframe.grid(row=2,column=0)

rightframe=Frame(root,pady=80,padx=70,bg='black')
rightframe.grid(row=0,column=1)

image50=PhotoImage(file='50-50.png')
lifeline50Button=Button(topframe,image=image50,bg='black',bd=0,width=180,height=80)
lifeline50Button.grid(row=0,column=0)

audiencepole=PhotoImage(file='audiencePole.png')
audiencepoleButton=Button(topframe,image=audiencepole,bg='black',bd=0,width=180,height=80)
audiencepoleButton.grid(row=0,column=1)

phonelifeline=PhotoImage(file='phoneAFriend.png')
phonelifelineButton=Button(topframe,image=phonelifeline,bg='black',bd=0,width=180,height=80)
phonelifelineButton.grid(row=0,column=2)

centerImage=PhotoImage(file='center.png')
logolabel=Label(centerframe,image=centerImage,bg='black',width=300,height=200)
logolabel.grid(row=0,column=0)

amountImage=PhotoImage(file='Picture0.png')
amountImage1=PhotoImage(file='Picture1.png')
amountImage2=PhotoImage(file='Picture2.png')
amountImage3=PhotoImage(file='Picture3.png')
amountImage4=PhotoImage(file='Picture4.png')
amountImage5=PhotoImage(file='Picture5.png')
amountImage6=PhotoImage(file='Picture6.png')
amountImage7=PhotoImage(file='Picture7.png')
amountImage8=PhotoImage(file='Picture8.png')
amountImage9=PhotoImage(file='Picture9.png')
amountImage10=PhotoImage(file='Picture10.png')
amountImage11=PhotoImage(file='Picture11.png')
amountImage12=PhotoImage(file='Picture12.png')
amountImage13=PhotoImage(file='Picture13.png')
amountImage14=PhotoImage(file='Picture14.png')
amountImage15=PhotoImage(file='Picture15.png')

amountImages= [amountImage1,amountImage2,amountImage3,amountImage4,amountImage5,amountImage6,amountImage7,amountImage8,
               amountImage9,amountImage10,amountImage11,amountImage12,amountImage13,amountImage14,amountImage15]

amountlabel=Label(rightframe,image=amountImage,bg='black')
amountlabel.grid(row=0,column=0)

layoutImage=PhotoImage(file='lay.png')
layoutlabel=Label(bottomframe,image=layoutImage,bg='black')
layoutlabel.grid(row=0,column=0)

questionArea=Text(bottomframe,font=('arial',18,'bold'),width=34,height=2,wrap='word',bg='black',fg='white',bd=0)
questionArea.place(x=70,y=10)

questionArea.insert(END,question[0])

labelA=Label(bottomframe,text='A:',bg='black',fg='white',font=('arial',18,'bold'))
labelA.place(x=60,y=110)

optionButton1=Button(bottomframe,text=first_option[0],bg='black',fg='white',font=('arial',18,'bold'),bd=0,
                    activeforeground='black',activebackground='white',cursor='hand2')
optionButton1.place(x=100,y=105)



labelB=Label(bottomframe,text='B:',bg='black',fg='white',font=('arial',18,'bold'))
labelB.place(x=330,y=110)

optionButton2=Button(bottomframe,text=second_option[0],bg='black',fg='white',font=('arial',18,'bold'),bd=0,
                    activeforeground='black',activebackground='white',cursor='hand2')
optionButton2.place(x=370,y=105)



labelC=Label(bottomframe,text='C:',bg='black',fg='white',font=('arial',18,'bold'))
labelC.place(x=60,y=185)

optionButton3=Button(bottomframe,text=third_option[0],bg='black',fg='white',font=('arial',18,'bold'),bd=0,
                    activeforeground='black',activebackground='white',cursor='hand2')
optionButton3.place(x=100,y=180)


labelD=Label(bottomframe,text='D:',bg='black',fg='white',font=('arial',18,'bold'))
labelD.place(x=330,y=185)

optionButton4=Button(bottomframe,text=fourth_option[0],bg='black',fg='white',font=('arial',18,'bold'),bd=0,
                    activeforeground='black',activebackground='white',cursor='hand2')
optionButton4.place(x=370,y=180)

optionButton1.bind('<Button-1>',select)
optionButton2.bind('<Button-1>',select)
optionButton3.bind('<Button-1>',select)
optionButton4.bind('<Button-1>',select)


root.mainloop()