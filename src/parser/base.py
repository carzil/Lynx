#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import core
from ly_ast import Ly_AST_IdentifierNode, Ly_AST_CodeNode, Ly_AST_IfNode, Ly_AST_WhileNode, Ly_AST_ForNode,\
                   Ly_AST_ElseNode
from lexer.tokens import Ly_EOFToken, Ly_IdentifierToken
from errors.parser import Ly_SyntaxError

def parse_else(tokens):
    token = tokens.next()
    if token.value == "else":
        token = tokens.next()
        if token.value != "{":
            return Ly_AST_ElseNode(Ly_AST_CodeNode(core.parse_expr(tokens)))
        else:
            body = []
            while token.value != "}":
                token = tokens.next()
                if token.value == "}":
                    break
                if isinstance(token, Ly_EOFToken):
                    Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
                res = core.parse_expr(tokens)
                body.append(res)
            tokens.next()
            return Ly_AST_ElseNode(Ly_AST_CodeNode(body))
    else:
        return
                

def parse_if(tokens):
    tokens.expect("(")
    tokens.next()
    res = core.parse_expr(tokens)
    tokens.expect(")", next=False, msg="missed opening parenthesis")
    token = tokens.next()
    if token.value != "{":
        res2 = core.parse_expr(tokens)
        res3 = parse_else(tokens)
        if res3 != None:
            return Ly_AST_IfNode(res, Ly_AST_CodeNode(res2), res3)
        elif res3 == None:
            return Ly_AST_IfNode(res, Ly_AST_CodeNode(res2), "")
    else:
        body = []
        while token.value != "}":
            token = tokens.next()
            if token.value == "}":
                break
            if isinstance(token, Ly_EOFToken):
                Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
            body.append(core.parse_expr(tokens))
        res3 = parse_else(tokens)
        if res != None:
            return Ly_AST_IfNode(res, Ly_AST_CodeNode(body), res3)
        elif res == None:
            return Ly_AST_IfNode(res, Ly_AST_CodeNode(body), "")
            
def parse_while(tokens):
    tokens.expect("(")
    tokens.next()
    res = core.parse_expr(tokens)
    tokens.expect(")", next=False, msg="missed closing parenthesis")
    token = tokens.next()
    if token.value != "{":
        return Ly_AST_WhileNode(res, Ly_AST_CodeNode([core.parse_expr(tokens)]))
    else:
        body = []
        while token.value != "}":
            token = tokens.next()
            if token.value == "}":
                break
            if isinstance(token, Ly_EOFToken):
                Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
            body.append(core.parse_expr(tokens))
        tokens.next()
        return Ly_AST_WhileNode(res, Ly_AST_CodeNode(body))
        
def parse_for(tokens):
    tokens.expect("(")
    token = tokens.next()
    if isinstance(token, Ly_IdentifierToken):
        loopv = Ly_AST_IdentifierNode(token.value)
    else:
        Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
    tokens.expect("=", msg="expected '=' in head for loop")
    tokens.next()
    value = core.parse_expr(tokens)
    tokens.expect(";", next=False)
    tokens.next()
    condition = core.parse_expr(tokens)
    tokens.expect(";", next=False)
    tokens.next()
    step = core.parse_expr(tokens)
    tokens.expect(")", next=False)
    token = tokens.next()
    if token.value != "{":
        return Ly_AST_ForNode(loopv, value, condition, step, Ly_AST_CodeNode([core.parse_expr(tokens)]))
    else:
        body = []
        while token.value != "}":
            token = tokens.next()
            if token.value == "}":
                break
            if isinstance(token, Ly_EOFToken):
                Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
            body.append(core.parse_expr(tokens))
        tokens.next()
        return Ly_AST_ForNode(loopv, value, condition, step, Ly_AST_CodeNode(body))
