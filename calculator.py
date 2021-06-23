import tkinter



root = tkinter.Tk()
root.title('Calculator')



#Create functions

def add():
    pass



#Create GUI
label_result =tkinter.Label(root, text='42')
label_result.grid(row=0, column=0, columnspan=4)

button_1 =tkinter.Button(root, text='1', command= add())
button_1.grid(row=1, column=0)


button_2 = tkinter.Button(root, text='2', command=())
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root, text='3', command=add() )
button_3.grid(row=1, column=2)

button_divide = tkinter.Button(root, text='/', command=add())
button_divide.grid(row=1, column=3)



root.mainloop()
