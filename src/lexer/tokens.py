#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import errors.lexer
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
        self.c_error = errors.lexer.Ly_InvalidNumberError(t_file, line, pos, string)
        if not self._valid():
            exit(exit_code)

    def _valid(self):
        flag = True
        for i in range(len(self.value)):
            if self.value[i] == "." and flag:
                flag = False
            elif self.value[i] == "." and not flag:
                self.c_error.error("repeating of '.' isn't possible!")
                return False
            elif self.value[i].lower() == "l" and i != len(self.value) - 1:
                self.c_error.error("indicator of type long (l or L) must be in end of number")
        return True

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
        self.c_error = errors.lexer.Ly_InvalidIdentifierError(t_file, line, pos, string)
        if not self._valid():
            exit(exit_code)
 
    def _valid(self):
        if not (self.value[0].isalpha() or self.value[0] == "_"):
            self.c_error.error("first symbol of identifier must be a letter or '_'!")
            return False
        return True

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
        self.c_error = errors.lexer.Ly_InvalidSpecCharError(t_file, line, pos, string)
        if not self._valid():
            exit(exit_code)

    def _valid(self):
        if self.value in const.OPERATORS:
            return True
        elif self.value in ["{", "}", "(", ")", "[", "]"]:
            return True
        else:
            self.c_error.error("unknown character '" + self.value + "'!")
            return False

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
        self.c_error = errors.lexer.Ly_InvalidStringError(t_file, line, pos, string)
        if not self._valid():
            exit(exit_code)
        

    def _valid(self):
        if self.value[0] != self.value[-1]:
            self.c_error.error()
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
        self.pos = pos
        self.string = string
        self.value = None

    def __eq__(self, obj):
        return isinstance(obj, Ly_EOFToken)

    def __repr__(self):
        return "<Ly_EOFToken() in file '" + self.file  + "'>\n"
