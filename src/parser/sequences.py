#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import ly_ast as ast
import errors.parser
import lexer.tokens
import core
import logging
from const import DEBUG
from lexer.tokens import Ly_EOFToken 

log = logging.getLogger("lynx.parser.sequences")
f = logging.Formatter("[%(name)s] %(asctime)s: %(message)s (%(levelname)s)")
sh = logging.StreamHandler()
sh.setFormatter(f)
log.addHandler(sh)
if DEBUG:
    log.setLevel(logging.DEBUG) 

def parse_arr(tokens):
    log.debug("lynx.parser.sequences.parse_arr")
    values = []
    token = tokens.current()
    while token.value != "]":
        token = tokens.next()
        if token.value == "]":
            break
        if token.value == "[":
            res = parse_arr(tokens)
        else:
            res = core.parse_primary(tokens)
        if res != -1:
            values.append(res)
        else:
            return -1
        token = tokens.current()
        if token.value != "," and token.value != "]":
            if isinstance(tokens, Ly_EOFToken):
                errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
                return -1
            errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missed comma in array definition")
            return -1
    if token.value != "]":
        if isinstance(tokens, Ly_EOFToken):
            errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
            return -1
        errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missing closing bracket in array definition")
        return -1
    token = tokens.next()
    return ast.Ly_AST_ArrNode(values)

def parse_tuple(tokens):
    log.debug("lynx.parser.sequences.parse_tuple")
    values = []
    token = tokens.current()
    while token.value != ")":
        token = tokens.next()
        if token.value == ")":
            break
        if token.value == "(":
            res = parse_tuple(tokens)
        else:
            res = core.parse_primary(tokens)
        if res != -1:
            values.append(res)
        else:
            return -1
        token = tokens.current()
        if token.value != "," and token.value != ")":
            if isinstance(tokens, Ly_EOFToken):
                errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
                return -1
            errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missed comma in tuple definition")
            return -1
    if token.value != ")":
        if isinstance(tokens, Ly_EOFToken):
            errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
            return -1
        errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missing closing parenthesis in tuple definition")
        return -1
    token = tokens.next()
    return ast.Ly_AST_TupleNode(values)

def parse_dict(tokens):
    '''
    This function parse Lynx dictionary
    @param tokens: <class lexer.main.Tokens>
    @return: <class ly_ast.Ly_AST_DictNode> or -1
    '''
    log.debug("lynx.parser.sequences.parse_dict")
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
        if res != -1:
            keys.append(res)
        else:
            return -1
        token = tokens.current()
        if token.value != ":" and not flg:
            return parse_set(tokens, keys[0])
        elif token.value != ":" and flg:
            if isinstance(tokens, Ly_EOFToken):
                errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
                return -1
            errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missed colon in dictionary definition")
            return -1
        token = tokens.next()
        if token.value == "{":
            res = parse_dict(tokens)
        else:
            res = core.parse_primary(tokens)
        if res != -1:
            values.append(res)
        else:
            return -1
        token = tokens.current()
        if token.value != "," and token.value != "}":
            if isinstance(tokens, Ly_EOFToken):
                errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
                return -1
            errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missed comma in dictionary definition")
            return -1
    if token.value != "}":
        if isinstance(tokens, Ly_EOFToken):
            errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
            return -1
        errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missing closing brace in dictionary definition")
        return -1
    token = tokens.next()
    return ast.Ly_AST_DictNode(keys, values)
        
def parse_set(tokens, fv):
    log.debug("lynx.parser.sequences.parse_set")
    values = [fv]
    token = tokens.current()
    while token.value != "}":
        token = tokens.next()
        if token.value == "}":
            break
        res = core.parse_primary(tokens)
        if res != -1:
            if res not in values:
                values.append(res)
        else:
            return -1
        token = tokens.current()
        if token.value != "," and token.value != "}":
            if isinstance(tokens, Ly_EOFToken):
                errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
                return -1
            errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missed comma in set definition")
            return -1
    if token.value != "}":
        if isinstance(tokens, Ly_EOFToken):
            errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "unexpected EOF")
            return -1
        errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string, "missing closing brace in set definition")
        return -1
    token = tokens.next()
    return ast.Ly_AST_SetNode(values)