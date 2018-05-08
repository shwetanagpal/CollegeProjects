from tkinter import *
from tkinter import messagebox


def doNothing():
    print("I do nothing")


def login():
    username = usernameinput.get()
    # password = passinput.get()
    n = Label(root, text=username, font='20')
    # p = Label(root, text=password)
    messagebox.showinfo("Welcome", "Login Successful")
    frame.destroy()
    Label(root, text="Welcome!", font='20').pack()
    n.pack()
    createTable(username)


def createTable(username):
    f = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=900, height=900, bd= 0,  pady = 30, padx = 90)
    f.pack()
    height = 4
    width = 6
    # k = 0
    headings = {
        "0": "Sno.",
        "1": "Name",
        "2": "Sports Enrolled In",
        "3": "Age",
        "4": "Batch Time",
        "5": "Contact No"
    }
    for i in range(height):  # Rows
        for j in range(width):  # Columns
            bold = Label(f, text=headings[str(j)], padx=15, pady=15, font='Arial 13 bold')
            bold.grid(row=0, column=j)

    a = Entry(f)
    a.grid(row=1, column=0)
    b = Entry(f)
    b.grid(row=1, column=1)
    c = Entry(f)
    c.grid(row=1, column=2)
    d = Entry(f)
    d.grid(row=1, column=3)
    e = Entry(f)
    e.grid(row=1, column=4)
    g = Entry(f)
    g.grid(row=1, column=5)

    nameLabel = Label(f, text="Name")

    def save():

        sno = a.get()
        name = b.get()
        sportsEnrolledIn = c.get()
        age = d.get()
        batchTime = e.get()
        contactno = g.get()

        f.destroy()
        fr = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=900, height=900, bd=0, pady=30, padx=90)
        fr.pack()


        file = open(username+'.txt', 'a+')
        file.write("%s \t %s \t %s \t %s \t %s \t %s \n" % (sno, name, sportsEnrolledIn, age, batchTime, contactno))
        file.close()
        file = open(username+'.txt', 'r')
        data = file.readlines()
        for line in data:
            line.split('\t')
            for word in range(20):
                nos = Label(fr, text=data[word], font='Verdana')
                print("\t")
                nos.grid(row=word+1, column=1, sticky='W')
                print("\t")




# .write("%s \n %s \n %s \n" % (line1, line2, line3))
    btn = Button(f, text="Save", cursor="hand2", command=save)
    btn.grid(columnspan=6, sticky=E, padx=5, pady=5)


root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


# main layout

heading = Label(root, text="SPORTS ACADEMY MANAGEMENT SYSTEM", font='Verdana 30 bold')
heading.pack(padx=30, pady=30)
frame = Frame(root, highlightbackground="blue", highlightcolor="blue", highlightthickness=2, width=900, height=900, bd= 0,  pady = 30, padx = 90)
frame.pack(side=TOP)
l = Label(frame, text="Login!", font='Courier 21 bold')
usernamelabel = Label(frame, text="Username", font= "Courier 15")
passLabel = Label(frame, text="Password", font= "Courier 15")
usernameinput = Entry(frame)
passinput = Entry(frame)
submitbtn = Button(frame, text="Submit", cursor="hand2", font='Courier 10', command=login)
checkbox1 = Checkbutton(frame, text="Keep me logged in")
l.grid(columnspan=3, sticky=N)
usernamelabel.grid(row=2,column=1, sticky=E)
passLabel.grid(row=4,column=1, sticky=E)
usernameinput.grid(row=2,column=2)
passinput.grid(row=4,column=2)
checkbox1.grid(columnspan=3)
submitbtn.grid(row=6, column=2, sticky=E)

root.mainloop()

