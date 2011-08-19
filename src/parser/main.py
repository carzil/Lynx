#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from lexer.main import Tokens
from lexer.tokens import Ly_EOFToken
from core import parse_primary

def main(filename):
    tokens = Tokens(filename)
    programm = parse_primary(tokens)
    return programm