#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from lexer.tokens import *
from errors.parser import Ly_SyntaxError
from numbers import parse_number
from strings import parse_string 
from sequences import parse_arr, parse_dict
from identifier import parse_identifier
from operators import parse_binary, parse_parenthesis, parse_unary
from const import UNOPS

def parse_primary(tokens):
    token = tokens.current()
    if isinstance(token, Ly_NumberToken):
        return parse_number(tokens)
    elif isinstance(token, Ly_StringToken):
        return parse_string(tokens)
    elif isinstance(token, Ly_IdentifierToken):
        return parse_identifier(tokens)
    elif token.value == "[":
        return parse_arr(tokens)
    elif token.value == "(":
        return parse_parenthesis(tokens)
    elif token.value == "{":
        return parse_dict(tokens)
    elif token.value == ";":
        tokens.next()
    elif isinstance(token, Ly_EOFToken):
        return
    else:
        Ly_SyntaxError(token.file, token.line, token.pos, token.string, "invalid syntax")
        return -1
    
def parse_expr(tokens):
    left = parse_primary(tokens)
    token = tokens.current()
    if token.value in ["++", "--"]:
        return parse_unary(tokens, left)
    elif token.value in const.OPERATORS:
        return parse_binary(tokens, left, 0)
    else:
        return left
