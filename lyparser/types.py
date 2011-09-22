#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from lylexer.tokens import Ly_IdentifierToken
from const import TYPES
from ast import Ly_AST_TypeNode
from lyerrors.parser import Ly_SyntaxError

def parse_type(tokens):
    type = ""
    token = tokens.current()
    
    while isinstance(token, Ly_IdentifierToken):
        type += token.value + " "
        token = tokens.next()
        
    if type[:-1] in TYPES:
        return Ly_AST_TypeNode(type[:-1])
    else:
        Ly_SyntaxError(token.file, token.line, token.pos, token.string,
                       "unexpected type '" + token.value + "'!")
        return -1