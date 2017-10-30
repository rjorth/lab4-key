from Tkinter import *
root = Tk()


def convert_number(n):
    if n < 1: return "Number is out of range"
    if n == 1: return "I"
    if n == 4: return "IV"
    if n == 5: return "V"
    if n == 9:  return "IX"
    if n == 10: return "X"
    if n == 40: return "XL"
    if n == 50: return "L"
    if n == 90: return "XC"
    if n == 100: return "C"
    if n == 400: return "CD"
    if n == 500: return "D"
    if n == 900: return "CM"
    if n == 1000: return "M"
    if n == 1400: return "MCD"
    if n == 1500: return "MD"
    if n == 1900: return "MCM"
    if n > 9999: return "Number is out of range"

    for i in [1000, 100, 10, 1]:
        for j in [9 * i, 5 * i, 4 * i, i]:
            if n >= j:
                return convert_number(j) + convert_number(n - j)

t1=Label(root, text="Convert")
t1.grid(row=0, column=0)
e1 = Entry(root, bd = 10)
e1.grid(row=0, column=1)
converter_button = Button(root, text="Enter something", width=20, command=convert_number)
converter_button.grid(row=1, column=1)
root.mainloop()
