from Tkinter import *
root = Tk()
root.title('Roman Numerals')
root.geometry('400x300')


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

def to_roman(s):
    roman_string = ''
    n = int(eval(s))
    wrong_value = 'Number is out of range'
    if not 1 <= n <= 9999:
        return wrong_value
    for string, integer in roman_numeral_map:
        while n >= integer:
            roman_string += string
            n -= integer
    print (roman_string)


def from_roman(s):
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    print result

def check_value():
    s = e1.get()
    if isinstance(s, int):
        to_roman(s)
    else:
        from_roman(s)

convert_button = Button(root, text='Convert', command=check_value)
e1 = Entry(root)
e1.pack()
e1.delete(0, END)
e1.insert(0, 'Enter a Number')
convert_button.pack()
root.mainloop()
