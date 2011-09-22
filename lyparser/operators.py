#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from const import PRECEDENCE as PREC
from lylexer.tokens import Ly_SpecCharToken, Ly_IdentifierToken
from lyerrors.parser import Ly_SyntaxError
from ast import Ly_AST_LTNode, Ly_AST_LENode, Ly_AST_GTNode, Ly_AST_GENode, Ly_AST_NENode, Ly_AST_EQNode,\
                   Ly_AST_AddNode, Ly_AST_SubNode, Ly_AST_MulNode, Ly_AST_DivNode, Ly_AST_PowNode, Ly_AST_ModNode,\
                   Ly_AST_NegNode, Ly_AST_NotNode
import core
import const
                   
bop = {
       "+": Ly_AST_AddNode,
       "-": Ly_AST_SubNode,
       "*": Ly_AST_MulNode,
       "//": Ly_AST_DivNode,
       "%": Ly_AST_ModNode,
       "**": Ly_AST_PowNode,
       "<": Ly_AST_LTNode,
       "<=": Ly_AST_LENode,
       ">": Ly_AST_GTNode,
       ">=": Ly_AST_GENode,
       "!=": Ly_AST_NENode,
       "==": Ly_AST_EQNode,
       
       }
def parse_parenthesis(tokens):
    tokens.next()
    res = core.parse_expr(tokens)
    tokens.expect(")", next=False)
    tokens.next()
    return res 

def getPrecedence(tokens):
    tok = tokens.current()
    if isinstance(tok, Ly_SpecCharToken):
        return PREC.get(tok.value, -1)
    else:
        return -1
    
def parse_binary(tokens):
#    """
#    @bug: running of expression '3 * (3 + 1) * 3 + 1 * 4 - 40 > 0' return 37, instead of True
#    """
#    while True:
#        p = getPrecedence(tokens)
#        if p < prec:
#            return LHS
#        token = tokens.current()
#        op = bop.get(token.value, -1)
#        if op == -1:
#            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "invalid operator")
#        tokens.next()
#        RHS = core.parse_expr(tokens)
#        np = getPrecedence(tokens)
#        if p < np:
#            RHS = parse_binary(tokens, RHS, prec + 1)
#        LHS = op(LHS, RHS)
    return parse_cmp(tokens)
        
def parse_cmp(tokens):
    obj = parse_factor(tokens)
    token = tokens.current()
    while token.value in ["<", ">", "==", "<=", ">=", "!="]:
        v = token.value
        token = tokens.next()
        obj = bop.get(v)(obj, parse_factor(tokens))
        token = tokens.current()
    return obj

def parse_factor(tokens):
    obj = parse_term(tokens)
    token = tokens.current()
    while token.value in ["+", "-"]:
        v = token.value
        token = tokens.next()
        obj = bop.get(v)(obj, parse_term(tokens))
        token = tokens.current()
    return obj

def parse_term(tokens):
    obj = parse_unary(tokens)
    token = tokens.current()
    while token.value in ["*", "/", "**"]:
        v = token.value
        token = tokens.next()
        obj = bop.get(v)(obj, parse_unary(tokens))
        token = tokens.current()
    return obj

def parse_unary(tokens):
    token = tokens.current()
    if token.value == "-":
        tokens.next()
        return Ly_AST_NegNode(parse_unary())
    elif token.value == "!":
        tokens.next()
        return Ly_AST_NotNode(parse_unary())
    else:
        return core.parse_expr(tokens)
