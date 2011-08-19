#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import sys

def Ly_SyntaxError(t_file, line, pos, string, msg):
    print("SyntaxError:", msg, file=sys.stderr)
    print("   ", "In file '" + t_file + "', on line " + str(line) + ":", file=sys.stderr)
    print("       ", string, file=sys.stderr)
    print("       ", " " * (pos[0] - 1), "^", file=sys.stderr)
    
def Ly_DefError(t_file, line, pos, string, msg):
    print("DefinitionError:", msg, file=sys.stderr)
    print("   ", "In file '" + t_file + "', on line " + str(line) + ":", file=sys.stderr)
    print("       ", string, file=sys.stderr)
    print("       ", " " * (pos[0] - 1), "^", file=sys.stderr)

    

    