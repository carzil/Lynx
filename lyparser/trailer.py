#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from lyerrors.parser import Ly_SyntaxError
from lylexer.tokens import Ly_EOFToken
from ast import Ly_AST_DottedIdentifierNode, Ly_AST_IdentifierNode
from ast import Ly_AST_SliceNode, Ly_AST_IndexingNode, Ly_AST_CallNode
import core

def parse_dotted_name(tokens, obj):
    res = Ly_AST_IdentifierNode(tokens.next().value)
    tokens.next()
    return Ly_AST_DottedIdentifierNode(obj, res)

def parse_indexing(tokens, obj):
    token = tokens.next()
    if token.value != ":":
        res = core.parse_primary(tokens)
        token = tokens.current()
        if token.value == ":":
            token = tokens.next()
            if token.value == "]":
                tokens.next()
                return Ly_AST_SliceNode(obj, res, "")
            else:
                res2 = core.parse_primary(tokens)
                token = tokens.current()
                if token.value != "]":
                    tokens.expect("]")
                    tokens.next()
                    return Ly_AST_SliceNode(obj, res, res2)
                else:
                    tokens.next()
                    return Ly_AST_SliceNode(obj, res, res2)
        elif token.value == "]":
            tokens.next()
            return Ly_AST_IndexingNode(obj, res)
        elif token.value:
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "invalid syntax")
            
def parse_call(tokens, obj):
    token = tokens.current()
    args = []
    while token.value != ")":
        token = tokens.next()
        if isinstance(token, Ly_EOFToken):
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
        if token.value == ")":
            tokens.next()
            break
        res = core.parse_primary(tokens)
        tokens.expect(",", ")", msg="missing comma in function call", next=False)
        token = tokens.current()
        if token.value == ",":
            args.append(res)
        elif token.value == ")":
            args.append(res)
            tokens.next()
            break
    return Ly_AST_CallNode(obj, args)

def parse_trailer(tokens, obj):
    tok = tokens.current()
    while tok.value in ["[", "(", "."] and tok.value:
        if tok.value == "[":
            obj = parse_indexing(tokens, obj)
        elif tok.value == "(":
            obj = parse_call(tokens, obj)
        elif tok.value == ".":
            obj = parse_dotted_name(tokens, obj)
        tok = tokens.current()
    return obj
