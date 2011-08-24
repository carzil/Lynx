#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from ly_ast import Ly_AST_ArrNode, Ly_AST_DictNode, Ly_AST_IndexingNode, Ly_AST_SliceNode,\
                   Ly_AST_SetNode
from errors.parser import Ly_SyntaxError
from lexer.tokens import Ly_EOFToken
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
        if res != -1:
            values.append(res)
        else:
            return -1
        token = tokens.current()
        if token.value != "," and token.value != "]":
            if isinstance(tokens, Ly_EOFToken):
                Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
                return -1
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missed comma in array definition")
            return -1
    if token.value != "]":
        if isinstance(tokens, Ly_EOFToken):
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
            return -1
        Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missing closing bracket in array definition")
        return -1
    token = tokens.next()
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
            res = core.parse_expr(tokens)
        if res != -1:
            keys.append(res)
        else:
            return -1
        token = tokens.current()
        if token.value != ":" and not flg:
            return parse_set(tokens, keys[0])
        elif token.value != ":" and flg:
            if isinstance(tokens, Ly_EOFToken):
                Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
                return -1
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missed colon in dictionary definition")
            return -1
        token = tokens.next()
        if token.value == "{":
            res = parse_dict(tokens)
        else:
            res = core.parse_expr(tokens)
        if res != -1:
            values.append(res)
        else:
            return -1
        token = tokens.current()
        if token.value != "," and token.value != "}":
            if isinstance(tokens, Ly_EOFToken):
                Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
                return -1
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missed comma in dictionary definition")
            return -1
    if token.value != "}":
        if isinstance(tokens, Ly_EOFToken):
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
            return -1
        Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missing closing brace in dictionary definition")
        return -1
    token = tokens.next()
    return Ly_AST_DictNode(keys, values)
        
def parse_set(tokens, fv):
    values = [fv]
    token = tokens.current()
    while token.value != "}":
        token = tokens.next()
        if token.value == "}":
            break
        res = core.parse_expr(tokens)
        if res != -1:
            if res not in values:
                values.append(res)
        else:
            return -1
        token = tokens.current()
        if token.value != "," and token.value != "}":
            if isinstance(tokens, Ly_EOFToken):
                Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
                return -1
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missed comma in set definition")
            return -1
    if token.value != "}":
        if isinstance(tokens, Ly_EOFToken):
            Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
            return -1
        Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missing closing brace in set definition")
        return -1
    token = tokens.next()
    return Ly_AST_SetNode(values)

def parse_indexing(tokens, obj):
    token = tokens.next()
    if token.value != ":":
        res = core.parse_expr(tokens)
        if res != -1:
            token = tokens.current()
            if token.value == ":":
                token = tokens.next()
                if token.value == "]":
                    tokens.next()
                    return Ly_AST_SliceNode(obj, res, "")
                else:
                    res2 = core.parse_expr(tokens)
                    if res != -1: 
                        token = tokens.current()
                        if token.value != "]":
                            if tokens.next() != "]":
                                Ly_SyntaxError(token.file, token.line, token.pos, token.string, "invalid syntax")
                                return -1
                            else:
                                tokens.next()
                                return Ly_AST_SliceNode(obj, res, res2)
                        else:
                            tokens.next()
                            return Ly_AST_SliceNode(obj, res, res2)
            elif token.value == "]":
                tokens.next()
                return Ly_AST_IndexingNode(obj, res)
            else:
                Ly_SyntaxError(token.file, token.line, token.pos, token.string, "invalid syntax")
                return -1
        else:
            return -1
