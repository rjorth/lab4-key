from Tkinter import *
root = Tk()

def check_value():
    if e1.get() == int(e1.get()):
        to_roman(e1.get())
    else:
        from_roman(e1.get())

roman_numeral_map = (('MCM', 1900),
                   ('MD', 1500),
                   ('MCD', 1400),
                   ('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))

def to_roman(n):
    result = ""
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    print result

roman_numeral_pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'

def from_roman(s):
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result

t1=Label(root, text="Convert")
t1.grid(row=0, column=0)
e1 = Entry(root, bd = 10)
e1.grid(row=0, column=1)
converter_button = Button(root, text="Enter something", width=20, command=check_value)
converter_button.grid(row=1, column=1)
root.mainloop()
