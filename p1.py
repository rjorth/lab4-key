import sys
def read_file(string, filename):
    string = ""
    filename = ""
    open(filename, 'r')
    try:
        for line in filename:
            if string in line:
                print line
    except ValueError:
        print 'No match found!'

    pass
if __name__=="__main__":
    try:
        sys.argv == 2
    except ValueError:
        print 'Not enough arguments'

    read_file(string, filename)
