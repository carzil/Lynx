#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from const import PRECEDENCE as PREC
from lexer.tokens import Ly_SpecCharToken, Ly_IdentifierToken
from errors.parser import Ly_SyntaxError
from ly_ast import Ly_AST_LTNode, Ly_AST_LENode, Ly_AST_GTNode, Ly_AST_GENode, Ly_AST_NENode, Ly_AST_EQNode,\
                   Ly_AST_AddNode, Ly_AST_SubNode, Ly_AST_MulNode, Ly_AST_DivNode, Ly_AST_PowNode, Ly_AST_ModNode,\
                   Ly_AST_DecNode, Ly_AST_IncNode, Ly_AST_NegNode, Ly_AST_IdentifierNode
import core
                   
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
    
def parse_binary(tokens, LHS, prec):
    """
    @bug: running of expression '3 * (3 + 1) * 3 + 1 * 4 - 40 > 0' return 37, instead of True
    """
    while True:
        p = getPrecedence(tokens)
        if p < prec:
            return LHS
        token = tokens.current()
        op = bop.get(token.value, -1)
        if op == -1:
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "invalid operator")
        tokens.next()
        RHS = core.parse_expr(tokens)
        np = getPrecedence(tokens)
        if p < np:
            RHS = parse_binary(tokens, RHS, prec + 1)
        LHS = op(LHS, RHS)
        
def parse_unary(tokens, name=None):
    if name == None:
        token = tokens.current()
        if token.value == "++":
            a = Ly_AST_IncNode
        elif token.value == "--":
            a = Ly_AST_DecNode
        elif token.value == "-":
            a = Ly_AST_NegNode
        else:
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "invalid operator")
        token = tokens.next()
        if isinstance(token, Ly_IdentifierToken):
            return a(Ly_AST_IdentifierNode(token.value))
        else:
            Ly_SyntaxError(token.file, token.line, token.pos, token.string,\
                           "operand of increment or decrement must be a name")
    else:
        token = tokens.current()
        if token.value == "++":
            tokens.next()
            return Ly_AST_IncNode(name)
        elif token.value == "--":
            tokens.next()
            return Ly_AST_DecNode(name)
        else:
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "invalid operator")
