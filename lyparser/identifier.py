#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from const import UNOPS
from lylexer.tokens import Ly_EOFToken, Ly_IdentifierToken
from lyerrors.parser import Ly_SyntaxError
from ast import Ly_AST_MultipleAssignNode, Ly_AST_AssignNode, Ly_AST_IdentifierNode
from base import parse_if, parse_while, parse_for
from operators import parse_unary
import core
 
    
def parse_assign(tokens, name):
    token = tokens.next()
    if isinstance(token, Ly_IdentifierToken):
        name2 = token.value
        token = tokens.next()
        if token.value == "=":
            return parse_multiple_assign(tokens, name, name2)
        else:
            res = Ly_AST_AssignNode(Ly_AST_IdentifierNode(name), Ly_AST_IdentifierNode(name2))
            tokens.expect(";", EOF=True, next=False)
            return res
    else:
        res = core.parse_expr(tokens)
        tokens.expect(";", EOF=True, next=False)
        return Ly_AST_AssignNode(Ly_AST_IdentifierNode(name), res)

def parse_multiple_assign(tokens, name, name2):
    names = [name, name2]
    token = tokens.current()
    value = None
    while token.value != ";":
        token = tokens.current()
        if token.value == ";":
            break
        token = tokens.next()
        if isinstance(token, Ly_IdentifierToken):
            names.append(Ly_AST_IdentifierNode(token.value))
            token = tokens.next()
            tokens.expect("=", ";", msg="missing equal in multiple assignment") 
        elif isinstance(token, Ly_EOFToken):
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
        else:
            value = core.parse_expr(tokens)
            token = tokens.current()
            tokens.expect("=", ";", msg="missing equal in multiple assignment", next=False)
    if not value:
        return Ly_AST_MultipleAssignNode(names[:-1], names[-1])
    return Ly_AST_MultipleAssignNode(names, value)
            
def parse_identifier(tokens):
    value = tokens.current().value
    if value == "if":
        return parse_if(tokens)
    elif value == "while":
        return parse_while(tokens)
    elif value == "for":
        return parse_for(tokens)
    token = tokens.next()
    if isinstance(token, Ly_EOFToken):
        Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
        return -1
    elif token.value in UNOPS:
        return parse_unary(tokens, value)
    elif token.value == "=":
        return parse_assign(tokens, value)
    else:
        return Ly_AST_IdentifierNode(value)