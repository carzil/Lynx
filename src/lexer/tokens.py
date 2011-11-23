#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from errors.lexer import Ly_SyntaxError
import const

class Ly_Token(object):
    pass

class Ly_NumberToken(Ly_Token):
    def __init__(self, value, line, t_file, pos, string, exit_code):
        self.value = value
        self.line = line
        self.file = t_file
        self.pos = pos
        self.string = string
        if self._valid() == -1:
            exit(exit_code)

    def _valid(self):
        if self.value.count(".") > 2:
            Ly_SyntaxError(self.file, self.line, self.pos, self.string)
            return -1
        if self.value.lower().count("l") >= 1 and self.value[-1].lower() != "l":
            Ly_SyntaxError(self.file, self.line, self.pos, self.string)
            return -1
        if not self.value.isdigit():
            Ly_SyntaxError(self.file, self.line, self.pos, self.string)
            return -1
        

    def __eq__(self, obj):
        return isinstance(obj, Ly_NumberToken) and self.value == obj.value
    
    def __repr__(self):
        return "<Ly_NumberToken(" + str(self.value)  + ")\nStart: " + str(self.pos[0]) + "\nEnd: " + str(self.pos[1]) + "\nFile '" + self.file  + "', line " + str(self.line)  +  ">\n"

class Ly_IdentifierToken(Ly_Token):
    def __init__(self, value, line, t_file, pos, string, exit_code):
        self.value = value
        self.line = line
        self.file = t_file
        self.pos = pos
        self.string = string
        if self._valid() == -1:
            exit(exit_code)
 
    def _valid(self):
        if not (self.value[0].isalpha() or self.value[0] == "_"):
            Ly_SyntaxError(self.file, self.line, self.pos, self.string)
            return -1

    def __eq__(self, obj):
        return isinstance(obj, Ly_IdentifierToken) and self.value == obj.value

    def __repr__(self):
        return "<Ly_IdentifierToken('" + str(self.value)  + "')\nStart: " + str(self.pos[0]) + "\nEnd: " + str(self.pos[1]) + "\nFile '" + self.file  + "', line " + str(self.line)  +  ">\n"

class Ly_SpecCharToken(Ly_Token):
    def __init__(self, value, line, t_file, pos, string, exit_code):
        self.value = value
        self.line = line
        self.file = t_file
        self.pos = pos
        self.string = string
        if self._valid() == -1:
            exit(exit_code)

    def _valid(self):
        if self.value not in const.OPERATORS and self.value not in ["{", "}", "(", ")", "[", "]"]:
            Ly_SyntaxError(self.file, self.line, self.pos, self.string)

    def __eq__(self, obj):
        return isinstance(obj, Ly_SpecCharToken) and self.value == obj.value

    def __repr__(self):
        return "<Ly_SpecCharToken('" + str(self.value)  + "')\nStart: " + str(self.pos[0]) + "\nEnd: " + str(self.pos[1]) + "\nFile '" + self.file  + "', line " + str(self.line)  +  ">\n"
     
class Ly_CommentToken(Ly_Token):
    def __init__(self, value, line, t_file, pos, string):
        self.value = value
        self.line = line
        self.file = t_file
        self.pos = pos
        self.string = string

    def __eq__(self, obj):
        return isinstance(obj, Ly_CommentToken) and self.value == obj.value

    def __repr__(self):
        return "<Ly_CommentToken('" + str(self.value)  + "')\nStart: " + str(self.pos[0]) + "\nEnd: " + str(self.pos[1]) + "\nFile '" + self.file  + "', line " + str(self.line)  +  ">\n"

class Ly_StringToken(Ly_Token):
    def __init__(self, value, line, t_file, pos, string, exit_code):
        self.value = value
        self.line = line
        self.file = t_file
        self.pos = pos
        self.string = string
        if not self._valid():
            exit(exit_code)
        

    def _valid(self):
        if self.value[0] != self.value[-1]:
            Ly_SyntaxError(self.file, self.line, self.pos, self.string)
            return False
        return True

    def __eq__(self, obj):
        return isinstance(obj, Ly_StringToken) and self.value == obj.value

    def __repr__(self):
        return "<Ly_StringToken(" + str(self.value)  + ")\nStart: " + str(self.pos[0]) + "\nEnd: " + str(self.pos[1]) + "\nFile '" + self.file  + "', line " + str(self.line)  +  ">\n"

class Ly_EOFToken(Ly_Token):
    def __init__(self, t_file, line, pos, string):
        self.file = t_file
        self.line = line
        self.pos = (pos[0], pos[1] + 2)
        self.string = string
        self.value = None

    def __eq__(self, obj):
        return isinstance(obj, Ly_EOFToken)

    def __repr__(self):
        return "<Ly_EOFToken() in file '" + self.file  + "'>\n"
