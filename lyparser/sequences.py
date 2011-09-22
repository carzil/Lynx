#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from ast import Ly_AST_ArrNode, Ly_AST_DictNode, Ly_AST_IndexingNode, Ly_AST_SliceNode, Ly_AST_SetNode
from lyerrors.parser import Ly_SyntaxError
from lylexer.tokens import Ly_EOFToken
import core

def parse_arr(tokens):
    values = []
    token = tokens.current()
    while token.value != "]":
        token = tokens.next()
        if token.value == "]":
            break
        if token.value == "[":
            res = parse_arr(tokens)
        else:
            res = core.parse_expr(tokens)
        values.append(res)
        token = tokens.current()
        tokens.expect(",", "]", next=False, msg="missed comma in array definition")
    tokens.expect("]", next=False, msg="missed closing bracket in array definition")
    tokens.next()
    return Ly_AST_ArrNode(values)

def parse_dict(tokens):
    values = []
    keys = []
    token = tokens.current()
    flg = False
    while token.value != "}":
        token = tokens.next()
        if token.value == "}":
            break
        if token.value == "{":
            res = parse_dict(tokens)
        else:
            res = core.parse_primary(tokens)
        keys.append(res)
        token = tokens.current()
        if token.value != ":" and not flg:
            return parse_set(tokens, keys[0])
        elif token.value != ":" and flg:
            if isinstance(tokens, Ly_EOFToken):
                Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missed colon in dictionary definition")
        token = tokens.next()
        if token.value == "{":
            res = parse_dict(tokens)
        else:
            res = core.parse_primary(tokens)
        values.append(res)
        tokens.expect(",", "}", next=False, msg="missed comma in dictionary definition")
    token = tokens.next()
    tokens.expect("}", next=False, msg="missed closing bracket in dictionary definition")
    tokens.next()
    return Ly_AST_DictNode(keys, values)
        
def parse_set(tokens, fv):
    values = [fv]
    token = tokens.current()
    while token.value != "}":
        token = tokens.next()
        if token.value == "}":
            break
        res = core.parse_primary(tokens)
        if res not in values:
            values.append(res)
        token = tokens.current()
        tokens.expect(",", "}", next=False, msg="missed closing brace in set definition")
    tokens.expect("}", next=False, msg="missed closing bracket in set definition")
    token = tokens.next()
    return Ly_AST_SetNode(values)