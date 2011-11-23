#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from const import TYPES, UNOPS
from lexer.tokens import Ly_EOFToken, Ly_IdentifierToken
from errors.parser import Ly_SyntaxError
from types import parse_type
import core
from ly_ast import Ly_AST_MultipleAssignNode, Ly_AST_AssignNode, Ly_AST_IdentifierNode
from ly_ast import Ly_AST_TypeNode, Ly_AST_CallNode, Ly_AST_IndexingNode, Ly_AST_SliceNode
from base import parse_if, parse_while, parse_for
from operators import parse_unary 
    
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

def parse_call(tokens, name):
    token = tokens.current()
    args = []
    while token.value != ")":
        token = tokens.next()
        if isinstance(token, Ly_EOFToken):
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
        if token.value == ")":
            tokens.next()
            break
        res = core.parse_expr(tokens)
        tokens.expect(",", ")", msg="missing comma in function call", next=False)
        token = tokens.current()
        if token.value == ",":
            args.append(res)
        elif token.value == ")":
            args.append(res)
            tokens.next()
            break
    res = Ly_AST_CallNode(Ly_AST_IdentifierNode(name), args)
    return __parse_next_indexing(tokens, res)

def __parse_next_indexing(tokens, obj):
    token = tokens.current()
    while token.value == "[":
        return parse_indexing(tokens, obj)
    return obj
        
def parse_indexing(tokens, obj):
    token = tokens.next()
    if token.value != ":":
        res = core.parse_expr(tokens)
        token = tokens.current()
        if token.value == ":":
            token = tokens.next()
            if token.value == "]":
                tokens.next()
                res = Ly_AST_SliceNode(obj, res, "")
                return __parse_next_indexing(tokens, res)
            else:
                res2 = core.parse_expr(tokens)
                if res != -1: 
                    token = tokens.current()
                    if token.value != "]":
                        if tokens.next() != "]":
                            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "invalid syntax")
                        else:
                            tokens.next()
                            res = Ly_AST_SliceNode(obj, res, res2)
                            return __parse_next_indexing(tokens, res)
                    else:
                        tokens.next()
                        res = Ly_AST_SliceNode(obj, res, res2)
                        return __parse_next_indexing(tokens, res)
        elif token.value == "]":
            tokens.next()
            res = Ly_AST_IndexingNode(obj, res)
            return __parse_next_indexing(tokens, res)
        else:
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "invalid syntax")
    
def parse_initialization(tokens, name):
    pass

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
    elif token.value == "(":
        return parse_call(tokens, value)
    elif token.value == "[":
        return parse_indexing(tokens, value)
    elif token.value in TYPES:
        return parse_initialization(tokens, tokens)
    else:
        return Ly_AST_IdentifierNode(value)
