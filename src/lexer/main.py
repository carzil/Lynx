#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from tokenizer import Ly_Tokenize
from tokens import Ly_EOF


def get_tokens(string):
    tokenize = Ly_Tokenize(string)
    token = tokenize.get_tok()
    tokens = []
    while not token == Ly_EOF():
        tokens.append(token)
        token = tokenize.get_tok()
    return tokens    
    
