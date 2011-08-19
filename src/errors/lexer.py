#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import sys

class Ly_Error(object):
    def __init__(self, t_file, line, pos, string):
        self.file = t_file
        self.line = line
        self.pos = pos
        self.string = string

    def error(self):
        pass

class Ly_InvalidNumberError(Ly_Error):
    def error(self, msg):
        print("SyntaxError:", msg, file=sys.stderr)
        print("   ", "In file '" + self.file + "', on line " + str(self.line) + ":", file=sys.stderr)
        print("       ", self.string, file=sys.stderr)
        print("       ", " " * (self.pos[0] - 1), "^", file=sys.stderr)

class Ly_InvalidIdentifierError(Ly_Error):
    def error(self, msg):
        print("SyntaxError:", msg, file=sys.stderr)
        print("   ", "In file '" + self.file + "', on line " + str(self.line) + ":", file=sys.stderr)
        print("       ", self.string, file=sys.stderr)
        print("       ", " " * (self.pos[0] - 1), "^", file=sys.stderr)
        
class Ly_InvalidSpecCharError(Ly_Error):
    def error(self, msg):
        print("SyntaxError:", msg, file=sys.stderr)
        print("   ", "In file '" + self.file + "', on line " + str(self.line) + ":", file=sys.stderr)
        print("       ", self.string, file=sys.stderr)
        print("       ", " " * (self.pos[0] - 1), "^", file=sys.stderr)

class Ly_InvalidStringError(Ly_Error):
    def error(self):
        print("SyntaxError: unexpected EOF!", file=sys.stderr)
        print("   ", "In file '" + self.file + "', on line " + str(self.line) + ":", file=sys.stderr)
        print("       ", self.string, file=sys.stderr)
        print("     ", " " * (self.pos[1] - 1), "^", file=sys.stderr)
