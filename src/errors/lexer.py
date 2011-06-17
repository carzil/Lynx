#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
class Ly_Error(object):
    def __init__(self, file, line):
        self.file = file
        self.line = line

    def error(self):
        pass

class Ly_InvalidNumberError(Ly_Error):
    def error(self, p_num, msg):
        print "InvalidNumber error raised by lexer!"
        print "File '" + self.file + "', line " + self.line
        print "Invalid number: '" + p_num  + "'! ", msg

class Ly_InvalidIdentifierError(Ly_Error):
    def error(self, p_id, msg):
        print "InvalidIndentifier error raised by lexer!"
        print "File '" + self.file + "', line " + self.line
        print "Invalid identifier: '" + p_id  + "'! ", msg

class Ly_InvalidSpecCharError(Ly_Error):

    def error(self, p_char, msg):
        print "InvalidIndentifier error raised by lexer!"
        print "File '" + self.file + "', line " + self.line
        print "Invalid special character: '" + p_char  + "'! ", msg



    
