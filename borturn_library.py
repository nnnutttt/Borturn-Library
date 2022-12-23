from tkinter import *

booklist1 = [num for num in range(1,11)]
booklist2 = [num for num  in range(11,21)]
booklist3 = [num for num  in range(21,31)]

def namebook1():
    shownamebook1 = Tk()
    shownamebook1.title("Show All Book")
    shownamebook1.minsize(300,280)
    head = Label(shownamebook1,text = "Literature and Novel",font = "Arial 12 bold")
    head.grid(row=0,padx=10,pady=10,sticky=NW)
    book = Label(shownamebook1 ,text = " 1. Mademoiselle de Scuderi\n"
                 +" 2. Arsène Lupin versus Sherlock Holmes\n"
                 +" 3. The Storied Life of A. J. Fikry\n"
                 +" 4. A Study in Terror\n"
                 +" 5. Time We Walk Together\n"
                 +" 6. Pedro Paramo\n"
                 +" 7. The Glass Bead Game\n"
                 +" 8. Harry Potter\n"
                 +" 9. Animal Farm\n"
                 +"10. Burmese Days",font = "Arial 12")
    book.grid(row=1,column=0,columnspan=2,padx=30)
    btClosename = Button(shownamebook1,text="Back",width=10,command=shownamebook1.destroy)
    btClosename.grid(row=5,column=1,pady=10,sticky=SE,padx=10)

def namebook2():
    shownamebook2 = Tk()
    shownamebook2.title("Show All Book")
    shownamebook2.minsize(300,280)
    head = Label(shownamebook2,text = "Book for kids",font = "Arial 12 bold")
    head.grid(row=0,padx=10,pady=10,sticky=NW)
    book = Label(shownamebook2 ,text = "11. The Jungle Book\n"
                 +"12. Body Parts\n"
                 +"13. Peppa's First 100 Words\n"
                 +"14. Finishing the picture\n"
                 +"15. Grandma’s magic box\n"
                 +"16. Kind words are a Gift\n"
                 +"17. Joyful friends\n"
                 +"18. Disney Boys 365 Stories\n"
                 +"19. My Animal's ABC\n"
                 +"20. Buildablock",font = "Arial 12")
    book.grid(row=1,column=0,columnspan=2,padx=50)
    btClosename2 = Button(shownamebook2,text="Back",width=10,command=shownamebook2.destroy)
    btClosename2.grid(row=5,column=1,pady=10,sticky=SE,padx=10)

def namebook3():
    shownamebook3 = Tk()
    shownamebook3.title("Show All Book")
    shownamebook3.minsize(300,280)
    head = Label(shownamebook3,text = "Psychology",font = "Arial 12 bold")
    head.grid(row=0,padx=10,pady=10,sticky=NW)
    book = Label(shownamebook3 ,text = "21. Into The Magic Shop\n"
                 +"22. 12 Rules For Life\n"
                 +"23. Atomics Habits\n"
                 +"24. Thinking, Fast and Slow\n"
                 +"25. The Little Book of  Happiness\n"
                 +"26. Principles : Life & Work\n"
                 +"27. GRIT : The Power of Passion and Perseverance\n"
                 +"28. The Positive Shift\n"
                 +"29. A Life of Triumph\n"
                 +"30. Productivity",font = "Arial 12")
    book.grid(row=1,column=0,columnspan=2,padx=50)
    btClosename3 = Button(shownamebook3,text="Back",width=10,command=shownamebook3.destroy)
    btClosename3.grid(row=5,column=1,pady=10,sticky=SE,padx=10)

def showwin():
    showwin = Tk()
    showwin.title("Show All Book")
    showwin.minsize(200,200)
    head = Label(showwin ,text = "Choose Type Book",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=10,padx=100)
    btShow1 = Button(showwin,text="Literature and Novel",width=30,command=namebook1)
    btShow1.grid(row=2,columnspan=3,pady=5)
    btShow2 = Button(showwin,text="Book for kids",width=30,command=namebook2)
    btShow2.grid(row=3,columnspan=3,pady=5)
    btShow3 = Button(showwin,text="Psychology",width=30,command=namebook3)
    btShow3.grid(row=4,columnspan=3,pady=5)
    btCloseShow = Button(showwin,text="Back",width=10,command=showwin.destroy)
    btCloseShow.grid(row=5,column=2,pady=10,sticky=SE,padx=10)

def winstatus1():
    def statusbook1():
        num  = int(myinput.get())
        if num  in booklist1:
            display.set("Book is Free")
        elif num  not in booklist1:
            if 1 <= num  <= 10:
                display.set("Book is Not Free")
            elif 11 <= num <= 20 or 21 <= num <=30:
                display.set("Book isn't in this types")
            elif num <=0 or num  >=30:
                print("\nBook isn't in library\n")
                display.set("Book isn't in library")
    def clear():
         inp.delete(0,"end")

    checkstatus1 = Tk()

    display = StringVar()
    myinput = IntVar()

    checkstatus1.title("CheckStatus")
    checkstatus1.minsize(100,210)

    head = Label(checkstatus1,text = "Literature and Novel",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,padx=100,pady=20)
    head1 = Label(checkstatus1,text = "Enter Number Book\nThat You Want To Check"
                  ,font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)
    inp = Entry(checkstatus1,textvariable=myinput,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()

    lbl = Label(checkstatus1,textvariable=display,pady=8,text="Red Text in Arial",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)

    btOK= Button(checkstatus1,text="OK",width=10,command=statusbook1)
    btOK.grid(row=4,column=0)

    btCLEA = Button(checkstatus1,text = 'Clear',width = 10,command = clear)
    btCLEA.grid(row=4,column=1)

    bt = Button(checkstatus1,text="Back",command = checkstatus1.destroy,width=10)
    bt.grid(row=4,column=2)
    mainloop()

def winstatus2():
    def statusbook2():
        num = int(myinput.get())
        if num in booklist1:
            display.set("Book is Free")
        elif num not in booklist1:
            if 11 <= num <= 20:
                display.set("Book is Not Free")
            elif 1 <= num <= 10 or 21 <= num <=30:
                display.set("Book isn't in this types")
            elif num <=0 or num >=30:
                print("\nBook isn't in library\n")
                display.set("Book isn't in library")
    def clear():
        inp.delete(0,"end")
    checkstatus2 = Tk()
    display = StringVar()
    myinput = IntVar()

    checkstatus2.title("CheckStatus")
    checkstatus2.minsize(200,210)

    head = Label(checkstatus2,text = "Book for kids",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=20,padx=130)
    head1 = Label(checkstatus2,text = "Enter Number Book\nThat You Want To Check"
                  ,font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)
    inp = Entry(checkstatus2,textvariable=myinput,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()

    lbl = Label(checkstatus2,textvariable=display,pady=8,text="Red Text in Arial",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)
    
    btOK= Button(checkstatus2,text="OK",width=10,command=statusbook2)
    btOK.grid(row=4,column=0)

    btCLEA = Button(checkstatus2,text = 'Clear',width = 10,command = clear)
    btCLEA.grid(row=4,column=1)
   
    bt = Button(checkstatus2,text="Back",command = checkstatus2.destroy,width=10)
    bt.grid(row=4,column=2)
    mainloop()

def winstatus3():
    def statusbook3():
        num = int(myinput.get())
        if num in booklist1:
            display.set("Book is Free")
        elif num not in booklist1:
            if 21 <= num <= 30:
                display.set("Book is Not Free")
            elif 1 <= num <= 10 or 11 <= num <=20:
                display.set("Book isn't in this types")
            elif num <=0 or num >=30:
                print("\nBook isn't in library\n")
                display.set("Book isn't in library")
    def clear():
        inp.delete(0,"end")

    checkstatus3 = Tk()
    display = StringVar()
    myinput = IntVar()

    checkstatus3.title("CheckStatus")
    checkstatus3.minsize(200,210)

    head = Label(checkstatus3,text = "Psychology",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=20,padx=135)
    head1 = Label(checkstatus3,text = "Enter Number Book\nThat You Want To Check"
                  ,font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)
    inp = Entry(checkstatus3,textvariable=myinput,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()

    lbl = Label(checkstatus3,textvariable=display,pady=8,text="Red Text in Arial",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)
    
    btOK= Button(checkstatus3,text="OK",width=10,command=statusbook3)
    btOK.grid(row=4,column=0)

    btCLEA = Button(checkstatus3,text = 'Clear',width = 10,command = clear)
    btCLEA.grid(row=4,column=1)
   
    bt = Button(checkstatus3,text="Back",command = checkstatus3.destroy,width=10)
    bt.grid(row=4,column=2)
    mainloop()

def CheckStatus():
    checkstatus = Tk()
    checkstatus.title("CheckStatus")
    checkstatus.minsize(200,200)
    head = Label(checkstatus ,text = "CheckStarus\n"+"One book at a time",font = "Arial 14")
    head.grid(row=1,column=0,columnspan=3,padx=100,pady=10)
    btcheck1 = Button(checkstatus,text="Literature and Novel",width=30,command=winstatus1)
    btcheck1.grid(row=2,columnspan=3,pady=5)
    btcheck2  = Button(checkstatus,text="Book for kids",width=30,command=winstatus2)
    btcheck2.grid(row=3,columnspan=3,pady=5)
    btcheck3  = Button(checkstatus,text="Psychology",width=30,command=winstatus3)
    btcheck3.grid(row=4,columnspan=3,pady=5)
    btCloseCheck  = Button(checkstatus,text="Back",width=10,command=checkstatus.destroy)
    btCloseCheck .grid(row=5,column=2,pady=10,sticky=SE,padx=10)

def borrow1():
    def borrowbook1():
        num = int(myinput.get())
        if num in booklist1:
            booklist1.remove(num)
            display.set("Success!")
        elif num not in booklist1:
            if num <=0 or num >=31:
                print("\nBook isn't in library\n")
                display.set("Book isn't in library")
            elif 11 <= num <= 20 or 21 <= num <= 30:
                display.set("Book isn't in this types")
            elif 1 <= num <= 10:
                display.set("Book was borrowed")
        
    def clear():
        inp.delete(0,"end")

    borrow1 = Tk()
    display = StringVar()
    myinput = IntVar()

    borrow1.title("BorrowBook")
    borrow1.minsize(200,210)

    head = Label(borrow1,text = "Literature and Novel",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=20,padx=100)
    head1 = Label(borrow1,text = "Enter Number Book\nThat You Want To Borrow"
                  ,font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)
    inp = Entry(borrow1,textvariable=myinput,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()

    lbl = Label(borrow1,textvariable=display,pady=8,text="Red Text in Arial",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)
    
    btOK= Button(borrow1,text="OK",width=10,command=borrowbook1)
    btOK.grid(row=4,column=0)

    btCLEA = Button(borrow1,text = 'Clear',width = 10,command = clear)
    btCLEA.grid(row=4,column=1)
   
    bt = Button(borrow1,text="Back",command = borrow1.destroy,width=10)
    bt.grid(row=4,column=2)
    mainloop()

def borrow2():
    def borrowbook2():
        num = int(myinput.get())
        if num in booklist2:
            booklist2.remove(num)
            display.set("Success!")
        elif num not in booklist2:
            if num <=0 or num >=31:
                print("\nBook isn't in library\n")
                display.set("Book isn't in library")
            elif 1 <= num <= 10 or 21 <= num <= 30:
                display.set("Book isn't in this types")
            elif 11 <= num <= 20:
                display.set("Book was borrowed")
        
    def clear():
        inp.delete(0,"end")

    borrow2 = Tk()
    display = StringVar()
    myinput = IntVar()

    borrow2.title("BorrowBook")
    borrow2.minsize(200,210)

    head = Label(borrow2,text = "Book for kids",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=20,padx=130)
    head1 = Label(borrow2,text = "Enter Number Book\nThat You Want To Borrow"
                  ,font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)
    inp = Entry(borrow2,textvariable=myinput,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()

    lbl = Label(borrow2,textvariable=display,pady=8,text="Red Text in Arial",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)
    
    btOK= Button(borrow2,text="OK",width=10,command=borrowbook2)
    btOK.grid(row=4,column=0)

    btCLEA = Button(borrow2,text = 'Clear',width = 10,command = clear)
    btCLEA.grid(row=4,column=1)
   
    bt = Button(borrow2,text="Back",command = borrow2.destroy,width=10)
    bt.grid(row=4,column=2)
    mainloop()

def borrow3():
    def borrowbook3():
        num = int(myinput.get())
        if num in booklist3:
            booklist3.remove(num)
            display.set("Success!")
        elif num not in booklist3:
            if num <=0 or num >=31:
                print("\nBook isn't in library\n")
                display.set("Book isn't in library")
            elif 1 <= num <= 10 or 11 <= num <= 20:
                display.set("Book isn't in this types")
            elif 21 <= num <= 30:
                display.set("Book was borrowed")
        
    def clear():
        inp.delete(0,"end")

    borrow3 = Tk()
    display = StringVar()
    myinput = IntVar()

    borrow3.title("BorrowBook")
    borrow3.minsize(200,210)

    head = Label(borrow3,text = "Psychology",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=20,padx=135)
    head1 = Label(borrow3,text = "Enter Number Book\nThat You Want To Borrow"
                  ,font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)
    inp = Entry(borrow3,textvariable=myinput,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()

    lbl = Label(borrow3,textvariable=display,pady=8,text="Red Text in Arial",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)
    
    btOK= Button(borrow3,text="OK",width=10,command=borrowbook3)
    btOK.grid(row=4,column=0)

    btCLEA = Button(borrow3,text = 'Clear',width = 10,command = clear)
    btCLEA.grid(row=4,column=1)
   
    bt = Button(borrow3,text="Back",command = borrow3.destroy,width=10)
    bt.grid(row=4,column=2)
    mainloop()

def BorrowBook():
    borrowbook = Tk()
    borrowbook.title("BorrowBook")
    borrowbook.minsize(200,200)
    head = Label(borrowbook ,text = "Borrow A Book\n"+"One book at a time",font = "Arial 14")
    head.grid(row=1,column=0,columnspan=3,padx=100,pady=10)
    btborrow1 = Button(borrowbook,text="Literature and Novel",width=30,command=borrow1)
    btborrow1.grid(row=2,columnspan=3,pady=5)
    btborrow2  = Button(borrowbook,text="Book for kids",width=30,command=borrow2)
    btborrow2.grid(row=3,columnspan=3,pady=5)
    btborrow3  = Button(borrowbook,text="Psychology",width=30,command=borrow3)
    btborrow3.grid(row=4,columnspan=3,pady=5)
    btCloseBorrow  = Button(borrowbook,text="Back",width=10,command=borrowbook.destroy)
    btCloseBorrow .grid(row=5,column=2,pady=10,sticky=SE,padx=10)

def return1():
    def returnbook1():
        num = int(myinput.get())
        if num not in booklist1:
            if num <=0 or num >= 31:
                print("\nBook isn't in library\n")
                display.set("Book isn't in library")
            elif 1 <= num <= 10:
                booklist1.append(num)
                display.sett("\nSuccess!\n")
            elif 11 <= num <= 20 or 21 <= num <= 30:
                display.sett("\nBook isn't in this types\n")
        elif num in booklist1:
            if 1<= num <= 10:
                display.set("\nBook was not borrowed\n")
    def clear():
        inp.delete(0,"end")

    return1 = Tk()
    display = StringVar()
    myinput = IntVar()

    return1.title("ReturnBook")
    return1.minsize(200,210)

    head = Label(return1,text = "Literature and Novel",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=20,padx=100)
    head1 = Label(return1,text = "Enter Number Book\nThat You Want To Return"
                  ,font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)
    inp = Entry(return1,textvariable=myinput,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()

    lbl = Label(return1,textvariable=display,pady=8,text="Red Text in Arial",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)
    
    btOK= Button(return1,text="OK",width=10,command=returnbook1)
    btOK.grid(row=4,column=0)

    btCLEA = Button(return1,text = 'Clear',width = 10,command = clear)
    btCLEA.grid(row=4,column=1)
   
    bt = Button(return1,text="Back",command = return1.destroy,width=10)
    bt.grid(row=4,column=2)
    mainloop()

def return2():
    def returnbook2():
        num = int(myinput.get())
        if num not in booklist2:
            if num <=0 or num >= 31:
                print("\nBook isn't in library\n")
                display.set("Book isn't in library")
            elif 11 <= num <= 20:
                booklist2.append(num)
                display.sett("\nSuccess!\n")
            elif 1 <= num <= 10 or 21 <= num <= 30:
                display.sett("\nBook isn't in this types\n")
        elif num in booklist2:
            if 11 <= num <= 20:
                display.set("\nBook was not borrowed\n")
    def clear():
        inp.delete(0,"end")

    return2 = Tk()
    display = StringVar()
    myinput = IntVar()

    return2.title("ReturnBook")
    return2.minsize(200,210)

    head = Label(return2,text = "Book for kids",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=20,padx=130)
    head1 = Label(return2,text = "Enter Number Book\nThat You Want To Return"
                  ,font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)
    inp = Entry(return2,textvariable=myinput,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()

    lbl = Label(return2,textvariable=display,pady=8,text="Red Text in Arial",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)
    
    btOK= Button(return2,text="OK",width=10,command=returnbook2)
    btOK.grid(row=4,column=0)

    btCLEA = Button(return2,text = 'Clear',width = 10,command = clear)
    btCLEA.grid(row=4,column=1)
   
    bt = Button(return2,text="Back",command = return2.destroy,width=10)
    bt.grid(row=4,column=2)
    mainloop()

def return3():
    def returnbook3():
        num = int(myinput.get())
        if num not in booklist3:
            if num <=0 or num >= 31:
                print("\nBook isn't in library\n")
                display.set("Book isn't in library")
            elif 21 <= num <= 30:
                booklist3.append(num)
                display.sett("\nSuccess!\n")
            elif 1 <= num <= 10 or 21 <= num <= 30:
                display.sett("\nBook isn't in this types\n")
        elif num in booklist3:
            if 21 <= num <= 30:
                display.set("\nBook was not borrowed\n")
    def clear():
        inp.delete(0,"end")

    return3 = Tk()
    display = StringVar()
    myinput = IntVar()

    return3.title("ReturnBook")
    return3.minsize(200,210)

    head = Label(return3,text = "Psychology",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=20,padx=135)
    head1 = Label(return3,text = "Enter Number Book\nThat You Want To Return"
                  ,font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)
    inp = Entry(return3,textvariable=myinput,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()

    lbl = Label(return3,textvariable=display,pady=8,text="Red Text in Arial",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)
    
    btOK= Button(return3,text="OK",width=10,command=returnbook3)
    btOK.grid(row=4,column=0)

    btCLEA = Button(return3,text = 'Clear',width = 10,command = clear)
    btCLEA.grid(row=4,column=1)
   
    bt = Button(return3,text="Back",command = return3.destroy,width=10)
    bt.grid(row=4,column=2)
    mainloop()

def ReturnBook():
    returnbook = Tk()
    returnbook.title("ReturnBook")
    returnbook.minsize(200,200)
    head = Label(returnbook ,text = "Return A Book\n"+"One book at a time",font = "Arial 14")
    head.grid(row=1,column=0,columnspan=3,padx=100,pady=10)
    btreturn1 = Button(returnbook,text="Literature and Novel",width=30,command=return1)
    btreturn1.grid(row=2,columnspan=3,pady=5)
    btreturn2  = Button(returnbook,text="Book for kids",width=30,command=return2)
    btreturn2.grid(row=3,columnspan=3,pady=5)
    btreturn3  = Button(returnbook,text="Psychology",width=30,command=return3)
    btreturn3.grid(row=4,columnspan=3,pady=5)
    btCloseReturn  = Button(returnbook,text="Back",width=10,command=returnbook.destroy)
    btCloseReturn.grid(row=5,column=2,pady=10,sticky=SE,padx=10)

'''def pay():
    def pay1():
        baht = int(myinput.get())
        payfine = baht * 20
        return payfine
    def clear():
        inp.delete(0,"end")

    pay = Tk()
    display = StringVar()
    myinput = IntVar()

    pay.title("Pay A Fine")
    pay.minsize(200,210)

    head = Label(pay,text = "Pay A Fine",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=20,padx=135)
    head1 = Label(pay,text = "How Many Book\nHave You Borrowed"
                  ,font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)
    inp = Entry(pay,textvariable=myinput,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()

    lbl = Label(pay,textvariable=display,pady=8,text="Red Text in Arial",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)
    
    btOK= Button(pay,text="OK",width=10,command=pay1)
    btOK.grid(row=4,column=0)

    btCLEA = Button(pay,text = 'Clear',width = 10,command = clear)
    btCLEA.grid(row=4,column=1)
   
    bt = Button(pay,text="Back",command = pay.destroy,width=10)
    bt.grid(row=4,column=2)'''
   
def convert():
    def pay1():
        baht = int(myinput.get())
        payfine = baht * 20
        return payfine
    def clear():
        inp.delete(0,"end")

#mainprogram
mainwin = Tk()
mainwin.title("Borturn Library")
mainwin.minsize(500,400)

display = StringVar()
myinput = DoubleVar()

head = Label(mainwin ,text = "\nWelcome To Borturn library! ",font = "Century 16 bold")
head.grid(row=0,column=0,columnspan=3,padx=150)
head1 = Label(mainwin ,text = "If you borrowed books for more than 7 days"
              +"\n You must pay a fine of  20 baht per book\n",font = "Arial 12")
head1.grid(row=1,column=0,columnspan=3)

btShow = Button(mainwin,text="SHOW ALL BOOK",width=30,command=showwin)
btShow.grid(row=2,pady=7,columnspan=3)

btCheck = Button(mainwin,text="CHECK BOOK STATUS",width=30,command=CheckStatus)
btCheck.grid(row=3,pady=7,columnspan=3)

btBorrow = Button(mainwin,text="BORROW A BOOK",width=30,command=BorrowBook)
btBorrow.grid(row=4,pady=7,columnspan=3)

btReturn = Button(mainwin,text="RETURN A BOOK",width=30,command=ReturnBook)
btReturn.grid(row=5,pady=7,columnspan=3)

def payafine():
    payafine = Tk()
    payafine.title("Pay A Fine")
    payafine.minsize(200,210)
    head = Label(payafine,text = "Pay A Fine",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=20,padx=135)
    head1 = Label(payafine,text = "How Many Book\nHave You Borrowed"
                  ,font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)
    inp = Entry(payafine,textvariable=myinput,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()
    lbl = Label(payafine,textvariable=display,pady=8,text="Red Text in Arial",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)
    
    btOK= Button(payafine,text="OK",width=10,command=convert)
    btOK.grid(row=4,column=0)

    btCLEA = Button(payafine,text = 'Clear',width = 10,command = convert)
    btCLEA.grid(row=4,column=1)
   
    bt = Button(payafine,text="Back",command = payafine.destroy,width=10)
    bt.grid(row=4,column=2)
btPay= Button(mainwin,text="PAY A FINE",width=30,command=payafine)
btPay.grid(row=6,pady=7,columnspan=3)

btEnd= Button(mainwin,text="End Program",width=30,command=mainwin.destroy)
btEnd.grid(row=7,pady=7,columnspan=3)

mainloop()
