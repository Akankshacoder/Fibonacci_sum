from tkinter import*
import random as r1
root= Tk()
root.title("Fibonacci")
root.geometry("400x400")

e1=Entry(root)
e1.place(relx=0.5, rely=0.4, anchor=CENTER)

def fib():
    inp=int(e1.get())
    fn=0
    sn=1
    count=0
    trd=0
    final=0
    while (count<= inp):
        l1['text']+= str(trd)+" "
        l2["text"]= "Fibonacci Sum: "+str(final)
        count= count+1
        fn = sn
        sn = trd
        trd = fn+sn
        final= final+trd

l1 = Label(root, text="Fibonacci Series: ")
l1.place(relx=0.5, rely=0.6, anchor=CENTER)
l2 = Label(root)
l2.place(relx=0.5, rely=0.7, anchor=CENTER)

b1= Button(root,text="Show Fibonacci series", command= fib)
b1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()