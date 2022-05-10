import sympy
from math import *
from tkinter import *


root = Tk()
root.title('Prime Factorization')

# Input title
myLabel = Label(root, text="Enter the number to foctor into prime numbers : ")
myLabel.grid(row=0, column=0)

myInputBox = Entry(root)
myInputBox.grid(row=1, column=1)


def del_():
    myInputBox.delete(0, END)


del_button = Button(root, text="DEL", command=del_)
del_button.grid(row=1, column=2)


def prime_factor():
    try:
        # int(input("Enter the number to factor into prime numbers : "))
        input_number = int(myInputBox.get())
        number = input_number
    except ValueError:
        return 0
    # print(number)
    if number > 999999999999:
        ErrorLabel = Label(
            root, text="Enter the number to foctor into prime numbers : ")  # Input Error
        ErrorLabel.configure(text='Error')
        ErrorLabel.grid(row=6, column=0)
        return 1
    output = {}
    i = 0

    while number % 2 == 0:
        i += 1
        number = number / 2
        output[2] = i
    # All the prime numbers less than the inputed number
    prime_numbers = list(sympy.primerange(3, sqrt(number)+1))
    # print(prime_numbers)

    n_iterations = 0
    for n in prime_numbers:
        n_iterations += 1
        i = 0
        while number % n == 0:
            i += 1
            number = number / n
            output[n] = i
            prime_numbers = list(sympy.primerange(3, sqrt(number)+1))
            # print(prime_numbers)
    if int(number) != 1:
        output[int(number)] = 1
    # print(n_iterations)
    # print(output)
    # myOutput = Label(root, text=output)
    # myOutput.pack()
    myOutputBox = Entry(root)
    myOutputBox.grid(row=4, column=1)
    myOutputBox.delete(0, END)
    myOutputBox.insert(0, output)
    # myOutputBox.grid_forget()


'''

    def check_divisibility(number,divisor):
        while number % divisor == 0:
            number = number / divisor
            output += str(divisor) +'x'        

    for n in prime_numbers:
        check_divisibility(input_number,n)

    output = output[:len(output)-1]

    print(output)

'''


eval_button = Button(root, text="Evaluate", command=prime_factor)
eval_button.grid(row=2, column=1)


root.mainloop()
