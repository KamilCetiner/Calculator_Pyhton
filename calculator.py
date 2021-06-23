

import tkinter
import tkinter.font as tkFont



root = tkinter.Tk()
root.title('Calculator')
root.geometry("378x500")
result_font = tkFont.Font(size=20)




#Create functions

value = ''

def addieren(number):
    global value
    value += number
    label_result.config(text=value)
    


def clear():
    global value
    print(value)
    value=''
    label_result.config(text=value)

def calculate():
    global value
    result = ""
    if value != "":
        try:
            result = eval(value)
        except:
            result = "error"
            value = ""
    label_result.config(text=result)



#Create GUI
label_result =tkinter.Label(root, text='0', width=9, height=2, font=result_font)
label_result.grid(row=0, column=0, columnspan=4)

button_1 =tkinter.Button(root, text='1', width=12, height=5, command= lambda : addieren('1'))
button_1.grid(row=1, column=0)


button_2 = tkinter.Button(root, text='2', width=12, height=5, command= lambda : addieren('2'))
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root, text='3', width=12, height=5,command= lambda : addieren('3') )
button_3.grid(row=1, column=2)

button_divide = tkinter.Button(root, text='/', width=12, height=5, command= lambda : addieren('/'))
button_divide.grid(row=1, column=3)

button_4 = tkinter.Button(root, text='4', width=12, height=5, command= lambda : addieren('4') )
button_4.grid(row=2, column=0)

button_5= tkinter.Button(root, text='5', width=12, height=5, command= lambda : addieren('5'))
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(root, text='6', width=12, height=5, command= lambda : addieren('6'))
button_6.grid(row=2, column=2)

button_multipication= tkinter.Button(root, text='*', width=12, height=5,command= lambda : addieren('*'))
button_multipication.grid(row=2, column=3)

button_7= tkinter.Button(root, text='7', width=12, height=5,command= lambda : addieren('7'))
button_7.grid(row=3, column=0)

button_8 = tkinter.Button(root, text='8', width=12, height=5, command= lambda : addieren('8'))
button_8.grid(row=3, column=1)

button_9=tkinter.Button(root, text='9', width=12, height=5, command= lambda : addieren('9'))
button_9.grid(row=3, column=2)

button_subtraction = tkinter.Button(root, text='-', width=12, height=5, command= lambda : addieren('-'))
button_subtraction.grid(row=3, column=3)


button_clear= tkinter.Button(root, text='C', width=12, height=5, command= lambda : clear())
button_clear.grid(row=4, column=0)

button_0 = tkinter.Button(root, text='0', width=12, height=5, command= lambda : addieren('0'))
button_0.grid(row=4, column=1)

button_dot=tkinter.Button(root, text='.', width=12, height=5, command= lambda : addieren('.'))
button_dot.grid(row=4, column=2)

button_addieren = tkinter.Button(root, text='+', width=12, height=5, command= lambda : addieren('+'))
button_addieren.grid(row=4, column=3)

button_gleich = tkinter.Button(root, text='=', width=52, height=4 ,command= lambda : calculate())
button_gleich.grid(row=5, column=0, columnspan=4)


root.mainloop()




