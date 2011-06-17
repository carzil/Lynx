#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from tokenizer import Ly_Tokenize
from tokens import Ly_EOFToken


def get_tokens(string, file):
    tokenize = Ly_Tokenize(string, file)
    token = tokenize.get_tok()
    tokens = []
    while not token == Ly_EOFToken(file):
        tokens.append(token)
        token = tokenize.get_tok()
    return tokens
