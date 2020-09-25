from tkinter import *
from tkinter import ttk

root = Tk()
root.title("College Portal")
root.geometry("550x350")

my_notebook = ttk.Notebook(root)
my_notebook.pack()

my_frame1 = Frame(my_notebook, width=600, height=600, bg='maroon', bd=8)
my_frame1.pack(fill="both", expand=1)
my_frame2 = Frame(my_notebook, width=600, height=600, bg='grey', bd=8)
my_frame2.pack(fill="both", expand=1)
my_frame3 = Frame(my_notebook, width=600, height=600, bg='light blue', bd=8)
my_frame3.pack(fill="both", expand=1)
my_frame4 = Frame(my_notebook, width=600, height=600, bg="light grey", bd=8)
my_frame4.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="STUDENT")
my_notebook.add(my_frame2, text="LECTURER")
my_notebook.add(my_frame3, text="DEGREE")
my_notebook.add(my_frame4, text="COURSE")

label1 = Label(my_frame1, text="Forenames", width=30,
               bg="white", bd=2, anchor=W)
label1.grid(row=1, column=0)
label2 = Label(my_frame1, text="Surname", width=30,
               bg="white", bd=2, anchor=W)
label2.grid(row=2, column=0)
label3 = Label(my_frame1, text="Email", width=30,
               bg="white", bd=2, anchor=W)
label3.grid(row=3, column=0)
label4 = Label(my_frame1, text="Date of birth",
               width=30, bg="white", bd=2, anchor=W)
label4.grid(row=4, column=0)
label5 = Label(my_frame1, text="Degree", width=30,
               bg="white", bd=2, anchor=W)
label5.grid(row=5, column=0)
label6 = Label(my_frame1, text="Firstname", width=30,
               bg="white", bd=2, anchor=W)
label6.grid(row=6, column=0)
label7 = Label(my_frame1, text="Fullname", width=30,
               bg="white", bd=2, anchor=W)
label7.grid(row=7, column=0)

button1 = Button(my_frame1, text="Search", bd=2, padx=30, pady=5)
button1.grid(row=9, column=1)
button2 = Button(my_frame1, text="Register", bd=2, padx=50, pady=5)
button2.grid(row=8, column=1)

box1 = Entry(my_frame1, width=50, bd=5, fg="blue", bg="white")
box1.grid(row=1, column=1)
box2 = Entry(my_frame1, width=50, bd=5, fg="blue", bg="white")
box2.grid(row=2, column=1)
box3 = Entry(my_frame1, width=50, bd=5, fg="blue", bg="white")
box3.grid(row=3, column=1)
box4 = Entry(my_frame1, width=50, bd=5, fg="blue", bg="white")
box4.grid(row=4, column=1)
box5 = Entry(my_frame1, width=50, bd=5, fg="blue", bg="white")
box5.grid(row=5, column=1)
box6 = Entry(my_frame1, width=50, bd=5, fg="blue", bg="white")
box6.grid(row=6, column=1)
box7 = Entry(my_frame1, width=50, bd=5, fg="blue", bg="white")
box7.grid(row=7, column=1)
"""  """
label1 = Label(my_frame2, text="Forenames",
               width=30, bg="white", bd=2, anchor=W)
label1.grid(row=1, column=0)
label2 = Label(my_frame2, text="Surname", width=30,
               bg="white", bd=2, anchor=W)
label2.grid(row=2, column=0)
label3 = Label(my_frame2, text="Email", width=30,
               bg="white", bd=2, anchor=W)
label3.grid(row=3, column=0)
label4 = Label(my_frame2, text="Date of birth",
               width=30, bg="white", bd=2, anchor=W)
label4.grid(row=4, column=0)
label5 = Label(my_frame2, text="Degrees", width=30,
               bg="white", bd=2, anchor=W)
label5.grid(row=5, column=0)
label6 = Label(my_frame2, text="Firstname",
               width=30, bg="white", bd=2, anchor=W)
label6.grid(row=6, column=0)
label7 = Label(my_frame2, text="Fullname", width=30,
               bg="white", bd=2, anchor=W)
label7.grid(row=7, column=0)

button1 = Button(my_frame2, text="Search", bd=2, padx=40, pady=5)
button1.grid(row=11, column=1)
button2 = Button(my_frame2, text="Register", bd=2, padx=50, pady=5)
button2.grid(row=9, column=1)

box1 = Entry(my_frame2, width=50, bd=5, fg="blue", bg="white")
box1.grid(row=1, column=1)
box2 = Entry(my_frame2, width=50, bd=5, fg="blue", bg="white")
box2.grid(row=2, column=1)
box3 = Entry(my_frame2, width=50, bd=5, fg="blue", bg="white")
box3.grid(row=3, column=1)
box4 = Entry(my_frame2, width=50, bd=5, fg="blue", bg="white")
box4.grid(row=4, column=1)
box5 = Entry(my_frame2, width=50, bd=5, fg="blue", bg="white")
box5.grid(row=5, column=1)
box6 = Entry(my_frame2, width=50, bd=5, fg="blue", bg="white")
box6.grid(row=6, column=1)
box7 = Entry(my_frame2, width=50, bd=5, fg="blue", bg="white")
box7.grid(row=7, column=1)

label1 = Label(my_frame3, text="Degree name", width=30,
               bg="white", bd=2, anchor=W)
label1.grid(row=1, column=0)
label2 = Label(my_frame3, text="Duration in years", width=30,
               bg="white", bd=2, anchor=W)
label2.grid(row=2, column=0)
label3 = Label(my_frame3, text="Courses", width=30,
               bg="white", bd=2, anchor=W)
label3.grid(row=3, column=0)
label4 = Label(my_frame3, text="Lecturer",
               width=30, bg="white", bd=2, anchor=W)
label4.grid(row=4, column=0)

button1 = Button(my_frame3, text="Search", bd=2, padx=40, pady=5)
button1.grid(row=11, column=1)
button2 = Button(my_frame3, text="Enter", bd=2, padx=50, pady=5)
button2.grid(row=9, column=1)

box1 = Entry(my_frame3, width=50, bd=5, fg="blue", bg="white")
box1.grid(row=1, column=1)
box2 = Entry(my_frame3, width=50, bd=5, fg="blue", bg="white")
box2.grid(row=2, column=1)
box3 = Entry(my_frame3, width=50, bd=5, fg="blue", bg="white")
box3.grid(row=3, column=1)
box4 = Entry(my_frame3, width=50, bd=5, fg="blue", bg="white")
box4.grid(row=4, column=1)

label1 = Label(my_frame4, text="Course name", width=30,
               bg="white", bd=2, anchor=W)
label1.grid(row=1, column=0)
label2 = Label(my_frame4, text="Duration in months", width=30,
               bg="white", bd=2, anchor=W)
label2.grid(row=2, column=0)
label3 = Label(my_frame4, text="Courses", width=30,
               bg="white", bd=2, anchor=W)
label3.grid(row=3, column=0)
label4 = Label(my_frame4, text="Degree linked to course",
               width=30, bg="white", bd=2, anchor=W)
label4.grid(row=4, column=0)

button1 = Button(my_frame4, text="Search", bd=2, padx=40, pady=5)
button1.grid(row=11, column=1)
button2 = Button(my_frame4, text="Enter", bd=2, padx=50, pady=5)
button2.grid(row=9, column=1)

box1 = Entry(my_frame4, width=50, bd=5, fg="blue", bg="white")
box1.grid(row=1, column=1)
box2 = Entry(my_frame4, width=50, bd=5, fg="blue", bg="white")
box2.grid(row=2, column=1)
box3 = Entry(my_frame4, width=50, bd=5, fg="blue", bg="white")
box3.grid(row=3, column=1)
box4 = Entry(my_frame4, width=50, bd=5, fg="blue", bg="white")
box4.grid(row=4, column=1)

root.mainloop()
