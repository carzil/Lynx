#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from tokenizer import Ly_Tokenize
from tokens import Ly_EOFToken


def get_tokens(string, t_file):
    tokenize = Ly_Tokenize(string, t_file)
    token = tokenize.get_tok()
    tokens = []
    while not token == Ly_EOFToken(t_file):
        tokens.append(token)
        token = tokenize.get_tok()
    return tokens
