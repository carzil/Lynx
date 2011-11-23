#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from lexer.tokenizer import Ly_Tokenize
from lexer.tokens import Ly_EOFToken
from errors.system import Ly_IOError
from errors.parser import Ly_SyntaxError
import os
import sys

def find_file(name):
    if os.path.exists(os.path.realpath(name)):
        return os.path.realpath(name)
    for i in sys.path:
        if os.path.isdir(i):
            s = i + os.sep + name
            if os.path.exists(s):
                return s
    return False

class Tokens(object):
    def __init__(self, filename):
        path = find_file(filename)
        if path:
            f = open(path, encoding="utf-8")
            self.toks = Ly_Tokenize(f)
        else:
            Ly_IOError("no such file '" + filename + "'")
            exit(1)
            
    def next(self):
        self.tok = self.toks.get_tok()
        return self.tok
    
    def current(self):
        try:
            return self.tok
        except:
            self.tok = self.toks.get_tok()
            return self.tok
        
    def expect(self, *what, EOF=False, next=True, msg="invalid syntax"):
        if next:
            token = self.next()
        else:
            token = self.current()
        if token.value not in what:
            if isinstance(what, Ly_EOFToken) and not EOF:
                Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
            elif isinstance(what, Ly_EOFToken) and EOF:
                return
            else:
                Ly_SyntaxError(token.file, token.line, token.pos, token.string, msg)
