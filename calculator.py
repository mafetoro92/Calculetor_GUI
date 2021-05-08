from tkinter import *

# root the our GUI
root = Tk()
root.title('Calculator.')
root.config(bg='gray')

# Frame our GUI
myFrame = Frame(root)
myFrame.pack()
myFrame.config(bg="pink")
myFrame.config(relief='sunken')
myFrame.config(bd=15)
myFrame.config(cursor='heart')

secreen_reset = False
operation = ""
result = 0

# setup screen
screen_number = StringVar()

screen = Entry(myFrame, textvariable=screen_number)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(background="black", fg="#03f943", justify="right")


# keystrokes

def pressed_numbers(num):
    global operation

    global secreen_reset

    if secreen_reset != False:

        screen_number.set(num)

        secreen_reset = False

    else:

        screen_number.set(screen_number.get() + num)


# sum funtion

def sum(num):
    global operation

    global result

    global secreen_reset

    result += int(num)  # resultado=resultado+int(num)

    operation = "suma"

    secreen_reset = True

    screen_number.set(result)


# subtraction funtion

num1 = 0

subtraction_counter = 0


def subtraction(num):
    global operation

    global result

    global num1

    global subtraction_counter

    global secreen_reset

    if subtraction_counter == 0:

        num1 = int(num)

        result = num1

    else:

        if subtraction_counter == 1:

            result = num1 - int(num)

        else:

            result = int(result) - int(num)

        screen_number.set(result)

        result = screen_number.get()

    subtraction_counter = subtraction_counter + 1

    operation = "subtraction"

    secreen_reset = True


# multiplication funtion
multi_counter = 0


def multiplication(num):
    global operation

    global result

    global num1

    global multi_counter

    global secreen_reset

    if multi_counter == 0:

        num1 = int(num)

        result = num1

    else:

        if multi_counter == 1:

            result = num1 * int(num)

        else:

            result = int(result) * int(num)

        screen_number.set(result)

        result = screen_number.get()

    multi_counter = multi_counter + 1

    operation = "multiplication"

    secreen_reset = True


# division funtion

divi_counter = 0


def divide(num):
    global operation

    global result

    global num1

    global divi_counter

    global secreen_reset

    if divi_counter == 0:

        num1 = float(num)

        result = num1

    else:

        if divi_counter == 1:

            result = num1 / float(num)

        else:

            result = float(result) / float(num)

        screen_number.set(result)

        result = screen_number.get()

    divi_counter = divi_counter + 1

    operation = "division"

    secreen_reset = True


# funtion result

def the_result():
    global result

    global operation

    global subtraction_counter

    global multi_counter

    global divi_counter

    if operation == "sum":

        screen_number.set(result + int(screen_number.get()))

        result = 0

    elif operation == "subtraction":

        screen_number.set(int(result) - int(screen_number.get()))

        result = 0

        subtraction_counter = 0

    elif operation == "multiplication":

        screen_number.set(int(result) * int(screen_number.get()))

        result = 0

        multi_counter = 0

    elif operation == "division":

        screen_number.set(int(result) / int(screen_number.get()))

        result = 0

        divi_counter = 0


# row 1

boton7 = Button(myFrame, text="7", width=3, command=lambda: pressed_numbers("7"))
boton7.grid(row=2, column=1)
boton8 = Button(myFrame, text="8", width=3, command=lambda: pressed_numbers("8"))
boton8.grid(row=2, column=2)
boton9 = Button(myFrame, text="9", width=3, command=lambda: pressed_numbers("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(myFrame, text="/", width=3, command=lambda: divide(screen_number.get()))
botonDiv.grid(row=2, column=4)

# row 2

boton4 = Button(myFrame, text="4", width=3, command=lambda: pressed_numbers("4"))
boton4.grid(row=3, column=1)
boton5 = Button(myFrame, text="5", width=3, command=lambda: pressed_numbers("5"))
boton5.grid(row=3, column=2)
boton6 = Button(myFrame, text="6", width=3, command=lambda: pressed_numbers("6"))
boton6.grid(row=3, column=3)
botonMult = Button(myFrame, text="x", width=3, command=lambda: multiplication(screen_number.get()))
botonMult.grid(row=3, column=4)

# row 3
boton1 = Button(myFrame, text="1", width=3, command=lambda: pressed_numbers("1"))
boton1.grid(row=4, column=1)
boton2 = Button(myFrame, text="2", width=3, command=lambda: pressed_numbers("2"))
boton2.grid(row=4, column=2)
boton3 = Button(myFrame, text="3", width=3, command=lambda: pressed_numbers("3"))
boton3.grid(row=4, column=3)
botonRest = Button(myFrame, text="-", width=3, command=lambda: subtraction(screen_number.get()))
botonRest.grid(row=4, column=4)

# row 4
boton0 = Button(myFrame, text="0", width=3, command=lambda: pressed_numbers("0"))
boton0.grid(row=5, column=1)
botonComa = Button(myFrame, text=",", width=3, command=lambda: pressed_numbers("."))
botonComa.grid(row=5, column=2)
botonIgual = Button(myFrame, text="=", width=3, command=lambda: the_result())
botonIgual.grid(row=5, column=3)
botonSum = Button(myFrame, text="+", width=3, command=lambda: sum(screen_number.get()))
botonSum.grid(row=5, column=4)

root.mainloop()
