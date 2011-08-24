#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from sys import stderr

def Ly_SyntaxError(t_file, line, pos, string):
        print("SyntaxError:", "invalid syntax", file=stderr)
        print("   ", "In file '" + t_file + "', on line " + str(line) + ":", file=stderr)
        print("       ", string, file=stderr)
        if pos[0] != 0:
            print("       ", " " * (pos[0] - 1), "^", file=stderr)
        else:
            print("       ", "^", file=stderr)
