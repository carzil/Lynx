#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from ast import Ly_AST_StringNode

def parse_string(tokens):
    value = tokens.current().value
    tokens.next()
    return Ly_AST_StringNode(value)