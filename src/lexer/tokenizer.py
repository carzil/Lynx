#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import lexer.tokens as tokens
    
class Ly_Tokenize(object):
    def __init__(self, fobj):
        self.line = 1
        self.file = fobj.name
        self.char = " "
        self.char_n = -1
        self.fobj = fobj
        self.lines = fobj.readlines()
        self.fobj.seek(0)
        
    def __del__(self):
        self.fobj.close()
        
    def get_char(self):
        self.char = self.fobj.read(1)
        self.char_n += 1
        if self.char == "":
            self.char = "-1"
             
    def get_id(self):
        t_id = self.char
        self.get_char()
        while self.char.isalnum() or self.char == "_":
            t_id += self.char
            self.get_char()
        return t_id

    def get_num(self):
        num = self.char
        self.get_char()
        while self.char.isdigit() or self.char == "." or self.char.lower() in ["l", "x", "b", "r", "a", "b", "c", "d", "e", "f"]:
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
                string += self.char
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
                self.char_n = -1
            self.get_char()
        
        if self.char.isalpha() or self.char == "_":
            cached = self.char_n
            return tokens.Ly_IdentifierToken(self.get_id(), self.line, self.file, (cached, self.char_n), self.lines[self.line - 1], 1)

        elif self.char.isdigit():
            cached = self.char_n
            return tokens.Ly_NumberToken(self.get_num(), self.line, self.file, (cached, self.char_n), self.lines[self.line - 1], 2)

        elif self.char == "#":
            cached = self.char_n
            return tokens.Ly_CommentToken(self.get_comment(), self.line, self.file, (cached, self.char_n), self.lines[self.line - 1])
       
        elif self.char == "'" or self.char == '"':
            cached = self.char_n
            return tokens.Ly_StringToken(self.get_string(), self.line, self.file, (cached, self.char_n), self.lines[self.line - 1], 1231233)

        elif self.char == "-1":
            if len(self.lines) > 1:
                return tokens.Ly_EOFToken(self.file, self.line, (self.char_n, self.char_n), self.lines[self.line - 2])
            elif len(self.lines) == 1:
                return tokens.Ly_EOFToken(self.file, self.line, (self.char_n, self.char_n), self.lines[0])
            else:
                return tokens.Ly_EOFToken(self.file, self.line, (self.char_n, self.char_n), "")
        
        elif self.char == "(" or self.char == ")" or self.char == "[" or self.char == "]" or self.char == "{" or self.char == "}":
            cached = self.char_n
            char = self.char
            self.get_char()
            return tokens.Ly_SpecCharToken(char, self.line, self.file, (cached, self.char_n), self.lines[self.line - 1], 4)
        
        else:
            cached = self.char_n
            return tokens.Ly_SpecCharToken(self.get_sc(), self.line, self.file, (cached, self.char_n), self.lines[self.line - 1], 4)