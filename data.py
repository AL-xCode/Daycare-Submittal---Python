import tkinter as tk

master = tk.Tk()
tk.Label(master, text="First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)
tk.Label(master, text="Date of Birth (00/00/0000)").grid(row=2)
tk.Label(master, text="Allergies").grid(row=3)
tk.Label(master, text="Date of Enrollment").grid(row=4)
tk.Label(master, text="Gender").grid(row=5)
tk.Label(master, text="Address").grid(row=6)
tk.Label(master, text="Guardian #1 Name").grid(row=7)
tk.Label(master, text="Guardian #2 Name").grid(row=8)
tk.Label(master, text="Emergency Contact Name").grid(row=9)
tk.Label(master, text="Emergency Contact Number").grid(row=10)
tk.Label(master, text="Person Pick up Name").grid(row=11)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)
e8 = tk.Entry(master)
e9 = tk.Entry(master)
e10 = tk.Entry(master)
e11 = tk.Entry(master)
e12 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)
e9.grid(row=8, column=1)
e10.grid(row=9, column=1)
e11.grid(row=10, column=1)
e12.grid(row=11, column=1)

def daycare_input():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get())

master = tk.Tk()
tk.Label(master,
         text="First Name").grid(row=0)
tk.Label(master,
         text="Last Name").grid(row=1)
tk.Label(master,
         text="Date of Birth (00/00/0000)").grid(row=2)
tk.Label(master,
         text="Allergies").grid(row=3)
tk.Label(master,
         text="Date of Enrollment").grid(row=4)
tk.Label(master,
         text="Gender").grid(row=5)
tk.Label(master,
         text="Address").grid(row=6)
tk.Label(master,
         text="Guardian #1 Name").grid(row=7)
tk.Label(master,
         text="Guardian #2 Name").grid(row=8)
tk.Label(master,
         text="Emergency Contact Name").grid(row=9)
tk.Label(master,
         text="Emergency Contact Number").grid(row=10)
tk.Label(master,
         text="Person Pick Up Name").grid(row=11)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)
e8 = tk.Entry(master)
e9 = tk.Entry(master)
e10 = tk.Entry(master)
e11 = tk.Entry(master)
e12 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)
e9.grid(row=8, column=1)
e10.grid(row=9, column=1)
e11.grid(row=10, column=1)
e12.grid(row=11, column=1)


button1 = tk.Button(master,
          text='Add Records',
          command=master.quit).grid(row=13,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
button2 = tk.Button(master,
          text='Display Records', command=daycare_input()).grid(row=13,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)


tk.mainloop()