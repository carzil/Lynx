#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import ast as ast
from lyerrors.parser import Ly_SyntaxError
import types as types

def parse_num_type(value):
    try:
        if value[1] == "b":
            return ast.Ly_AST_TypeNode("bin")
        elif value[1] == "x":
            return ast.Ly_AST_TypeNode("hex")
        elif value[1] == "r":
            return ast.Ly_AST_TypeNode("complex")
        elif "." in value:
            return ast.Ly_AST_TypeNode("float")
    except:
        pass
    try:
        if int(value) > 2147483647 or int(value) < -2147483646 or "l" in value.lower():
            return ast.Ly_AST_TypeNode("long")
    except ValueError:
        return -1
    return ast.Ly_AST_TypeNode("int")
    
def parse_number(tokens):
    value = tokens.current().value
    token = tokens.next()
    if token.value != "->":
        res = parse_num_type(value)
        return ast.Ly_AST_NumberNode(value, res)
    token = tokens.next()
    res = types.parse_type(tokens)
    return ast.Ly_AST_NumberNode(value, res)