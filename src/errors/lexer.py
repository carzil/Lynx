#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import sys

class Ly_Error(object):
    def __init__(self, t_file, line):
        self.file = t_file
        self.line = line

    def error(self):
        pass

class Ly_InvalidNumberError(Ly_Error):
    def error(self, p_num, msg):
        print >> sys.stderr, "InvalidNumber error raised by lexer!"
        print >> sys.stderr, "File '" + self.file + "', line " + str(self.line)
        print >> sys.stderr, "Invalid number: '" + p_num  + "'! ", msg

class Ly_InvalidIdentifierError(Ly_Error):
    def error(self, p_id, msg):
        print >> sys.stderr, "InvalidIndentifier error raised by lexer!"
        print >> sys.stderr, "File '" + self.file + "', line " + str(self.line)
        print >> sys.stderr, "Invalid identifier: '" + p_id  + "'!", msg

class Ly_InvalidSpecCharError(Ly_Error):
    def error(self, p_char, msg):
        print >> sys.stderr, "InvalidString error raised by lexer!"
        print >> sys.stderr, "File '" + self.file + "', line " + str(self.line)
        print >> sys.stderr, "Invalid special character: '" + p_char  + "'!", msg

class Ly_InvalidStringError(Ly_Error):
    def error(self, p_string, msg):
        print >> sys.stderr, "InvalidString error raised by lexer!"
        print >> sys.stderr, "File '" + self.file + "', line " + str(self.line)
        print >> sys.stderr, "Invalid string: " + p_string  + "!", msg
