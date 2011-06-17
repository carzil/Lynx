#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import os
import sys
sys.path.insert(0, os.path.realpath(".."))
print sys.path
import errors.lexer

class Ly_NumberToken(object):
    def __init__(self, value, line, file, exit_code):
        self.value = value
        self.line = line
        self.file = file
        self.c_error = errors.lexer.Ly_InvalidNumberError(file, line)
        if not self._valid():
            exit(exit_code)

    def _valid(self):
        flag = True
        for i in self.value:
            if not i.isdigit():
                self.c_error.error(self.value, "Illegal character for number: '" + i  + "'")
                return False
            elif i == "." and flag:
                flag = False
            elif i == "." and not flag:
                self.c_error.error(self.value, "Repeating of '.' isn't possible!")
                return False
        return True

    def __eq__(self, obj):
        return isinstance(obj, Ly_NumberToken) and self.value == obj.value
    
    def __repr__(self):
        return "<Ly_NumberToken(" + str(self.value)  + ")\nFile '" + self.file  + "', line " + str(self.line)  +  ">\n"

class Ly_IdentifierToken(object):
    def __init__(self, id, line, file, exit_code):
        self.id = id
        self.line = line
        self.file = file
        self.c_error = errors.lexer.Ly_InvalidIdentifierError(file, line)
        if not self._valid():
            exit(exit_code)
 
    def _valid(self):
       if not self.id[0].isalpha():
           self.c_error.error(self.id, "First symbol of identificator must be a letter or '_'!")
           return False
       return True

    def __eq__(self, obj):
        return isinstance(obj, Ly_IdentifierToken) and self.id == obj.id

    def __repr__(self):
        return "<Ly_IdentifierToken('" + str(self.id)  + "')\nFile '" + self.file  + "', line " + str(self.line)  +  ">\n"

class Ly_SpecCharToken(object):
    def __init__(self, char, line, file, exit_code):
        self.char = char
        self.line = line
        self.file = file
        self.c_error = errors.lexer.Ly_InvalidSpecCharError(file, line)
        if not self._valid():
            exit(exit_code)

    def _valid(self):
        for i in self.char:
            if i in ["+", "-", "*", "/", "%", "^", "!", "|", "&", "=", ">", "<"]:
                return True
            elif i in [";", ",", ".", ":", "(", ")", "[", "]", "{", "}"]:
                return True
            elif i in ["++", "--", "->", "==", "<=", ">=", "!=", "+=", "-=", "/=",\
                       "*=", "|=", "&=", "||", "&&", "**", "//"]:
                return True
            else:
                self.c_error.error(self.char, "Unknow character!")
                return False

    def __eq__(self, obj):
        return isinstance(obj, Ly_SpecCharToken) and self.char == obj.char

    def __repr__(self):
        return "<Ly_SpecCharToken('" + str(self.char)  + "')\nFile '" + self.file  + "', line " + str(self.line)  +  ">\n"
     
class Ly_CommentToken(object):
    def __init__(self, comment, line, file):
        self.value = value
        self.line = line
        self.file = file

    def __eq__(self, obj):
        return isinstance(obj, Ly_CommentToken) and self.comment == obj.comment

    def __repr__(self):
        return "<Ly_CommentToken('" + str(self.comment)  + "')\nFile '" + self.file  + "', line " + str(self.line)  +  ">\n"

class Ly_StringToken(object):
    def __init__(self, string, line, file):
        self.string = string
        self.line = line
        self.file = file

    def __eq__(self, obj):
        return isinstance(obj, Ly_StringToken) and self.string == obj.string

    def __repr__(self):
        return "<Ly_StringToken(" + str(self.string)  + ")\nFile '" + self.file  + "', line " + str(self.line)  +  ">\n"

class Ly_EOFToken(object):
    def __init__(self, file):
        self.file = file

    def __eq__(self, obj):
        return isinstance(obj, Ly_EOFToken)

    def __repr__(self):
        return "<Ly_EOFToken() in file '" + self.file  + "'>\n"


