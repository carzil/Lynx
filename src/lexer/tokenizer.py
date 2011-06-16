#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import tokens

class Ly_Tokenize(object):
    def __init__(self, string):
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
        id = self.char
        self.get_char()
        while self.char.isalpha() or self.char == "_":
            id += self.char
            self.get_char()
        return id

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
        while self.char in ["+", "-", "*", "/", "|", "&", "%", "!", "*", ";", ",", "."]:
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
            self.get_char()
        
        if self.char.isalpha():
            return tokens.Ly_Identifier(self.get_id())

        elif self.char.isdigit():
            return tokens.Ly_Number(int(self.get_num()))

        elif self.char == "#":
            return tokens.Ly_Comment(self.get_comment())
       
        elif self.char == "'" or self.char == '"':
            return tokens.Ly_String(self.get_string())

        elif self.char == "-1":
            return tokens.Ly_EOF()
        
        else:
            return tokens.Ly_SpecChar(self.get_sc())
