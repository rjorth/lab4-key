import sys
import os
def main():
    read_file = sys.argv[0]
    write_file = sys.argv[1]
    open(read_file, 'r')
    lines=0
    words=0
    characters=0
    for line in read_file:
        line = line.strip(os.linesep)
        words_list=line.split()
        lines=lines + 1
        words=words+len(words_list)
        characters=characters+len(line)
    f = open(write_file, 'w')
    print(f, 'lines')
    print(f, 'words')
    print(f, 'characters')
