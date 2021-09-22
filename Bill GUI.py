from tkinter import *

window = Tk()
window.geometry("800x500")

window.title("Billing Software")

def calculate():
    masala_Dose=e1.get()
    open_Dosa = e2.get()
    set_Dosa = e3.get()
    benne_Dosa = e4.get()
    tea = e5.get()
    total = (int(masala_Dose)*60  + int(open_Dosa)*50 + int(set_Dosa)*40 + int(benne_Dosa)*45 + int(tea)*5)
    fbill = Label(window, text=total, font="times 18 bold")
    fbill.place(x=580, y=400)



label_title = Label(window,text="Chikku's 5* Hotel",font = "times 30 italic bold")
label_title.place(x=350,y=20,anchor="center")

# menu section---------

label1 = Label(window,text="MENU",font="times 28 bold")
label1.place(x=500,y=70)

label2 = Label(window,text="Masala Dosa              Rs 60",font="times 18 bold")
label2.place(x=450,y=120)

label3 = Label(window,text="Open Dosa                 Rs 50",font="times 18 bold")
label3.place(x=450,y=150)

label4 = Label(window,text="Set Dosa                     Rs 40",font="times 18 bold")
label4.place(x=450,y=180)

label5 = Label(window,text="Benne Dosa                Rs 45",font="times 18 bold")
label5.place(x=450,y=210)

label6 = Label(window,text="Tea                             Rs 5",font="times 18 bold")
label6.place(x=450,y=240)


# ----------  billing section------------------

label7 = Label(window,text="Select the items",font = "times 20 bold")
label7.place(x=100,y=70)

label8 = Label(window,text="Masala Dosa",font = "times 18")
label8.place(x=20,y=120)

e1 = Entry(window)
e1.place(x=20,y=150)

label9 = Label(window,text="Open Dosa",font = "times 18")
label9.place(x=250,y=120)

e2 = Entry(window)
e2.place(x=250,y=150)

label10 = Label(window,text="Set Dosa",font = "times 18")
label10.place(x=20,y=230)

e3 = Entry(window)
e3.place(x=20,y=260)

label11 = Label(window,text="Benne Dosa",font = "times 18")
label11.place(x=250,y=230)

e4 = Entry(window)
e4.place(x=250,y=260)

label12 = Label(window,text="Tea",font = "times 18")
label12.place(x=180,y=320)

e5 = Entry(window)
e5.place(x=150,y=350)


# ---------------------   Total   ------------------------


label13 = Label(window,text="Total: ",font = "times 18 bold")
label13.place(x=500,y=400)

b1 = Button(window,text='Bill',width=20,command=calculate, bg='blue', fg='white')
b1.place(x=130,y=420)

window.mainloop()