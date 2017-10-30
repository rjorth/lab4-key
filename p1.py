import sys
def main():
    string = sys.argv[0]
    filename = sys.argv[1]
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

    main()
