#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from lylexer.tokens import Ly_NumberToken, Ly_StringToken, Ly_IdentifierToken, Ly_EOFToken
from lyerrors.parser import Ly_SyntaxError 
from numbers import parse_number
from strings import parse_string
from sequences import parse_arr, parse_dict
from identifier import parse_identifier
from trailer import parse_trailer
from operators import parse_binary, parse_parenthesis
from const import OPERATORS

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
    
def parse_expr(tokens):
    return parse_trailer(tokens, parse_primary(tokens))

def parse_program(tokens):
    return parse_binary(tokens)