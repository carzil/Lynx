#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import ly_ast as ast
import errors.parser
import types
import logging
from const import DEBUG

log = logging.getLogger("lynx.parser.numbers")
f = logging.Formatter("[%(name)s] %(asctime)s: %(message)s (%(levelname)s)")
sh = logging.StreamHandler()
sh.setFormatter(f)
log.addHandler(sh)
if DEBUG:
    log.setLevel(logging.DEBUG)

def parse_num_type(value):
    log.debug("lynx.parser.numbers.parse_num_type")
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
    log.debug("lynx.parser.number.parse_number")
    value = tokens.current().value
    token = tokens.next()
    if token.value != "->":
        res = parse_num_type(value)
        if res != -1:
            return ast.Ly_AST_NumberNode(value, res)
        errors.parser.Ly_SyntaxError(token.file, token.line, token.pos, token.string,
                                     "unexpected number '" + token.value + "'!")
        return -1
    token = tokens.next()
    res = types.parse_type(tokens)
    if res != -1:
        return ast.Ly_AST_NumberNode(value, res)
    else:
        return -1