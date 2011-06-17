#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import tokens

class Ly_Tokenize(object):
    def __init__(self, string, t_file):
        self.line = 1
        self.file = t_file
        self.str = string
        self.pos = -1
        self.str_size = len(string) - 1
        self.char = " "

    def get_char(self):
        self.pos += 1
        if self.pos <= self.str_size:
            self.char = self.str[self.pos]
        else:
            self.char = "-1"
    
    def get_id(self):
        t_id = self.char
        self.get_char()
        while self.char.isalpha() or self.char == "_":
            t_id += self.char
            self.get_char()
        return t_id

    def get_num(self):
        num = self.char
        self.get_char()
        while self.char.isdigit() or self.char == ".":
            num += self.char
            self.get_char()
        return num
  
    def get_sc(self):
        sc = self.char
        self.get_char()
        while self.char in ["+", "-", "*", "/", "|", "&", "*", ">", "<", "="]:
            sc += self.char
            self.get_char()
        return sc
    
    def get_comment(self):
        comment = self.char
        self.get_char()
        while not self.char == "\n":
            comment += self.char
            self.get_char()
        return comment
 
    def get_string(self):
        string = self.char
        self.get_char()
        while not self.char == string[0]:
            if self.char == "-1":
                string += string[0]
                break
            string += self.char
            self.get_char()
        string += self.char
        self.get_char()
        return string

    def get_tok(self):
        while self.char.isspace():
            if self.char == "\n" or self.char == "\r":
                self.line += 1
            self.get_char()
        
        if self.char.isalpha():
            return tokens.Ly_IdentifierToken(self.get_id(), self.line, self.file, 1)

        elif self.char.isdigit():
            return tokens.Ly_NumberToken(int(self.get_num()), self.line, self.file, 2)

        elif self.char == "#":
            return tokens.Ly_CommentToken(self.get_comment(), self.line, self.file, 3)
       
        elif self.char == "'" or self.char == '"':
            return tokens.Ly_StringToken(self.get_string(), self.line, self.file)

        elif self.char == "-1":
            return tokens.Ly_EOFToken(self.file)
        
        else:
            return tokens.Ly_SpecCharToken(self.get_sc(), self.line, self.file, 5)
