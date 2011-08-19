#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from lexer.tokenizer import Ly_Tokenize
from errors.system import Ly_IOError
import os

class Tokens(object):
    def __init__(self, filename=None):
        if os.path.exists(os.path.realpath(filename)):
            f = open(filename)
            self.toks = Ly_Tokenize(f)
        else:
            Ly_IOError("file " + os.path.realpath(filename) + " does not exists")
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