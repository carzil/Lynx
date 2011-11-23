#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from lexer.tokens import Ly_IdentifierToken
from const import TYPES
from ly_ast import Ly_AST_TypeNode
from errors.parser import Ly_SyntaxError
import logging
from const import DEBUG

log = logging.getLogger("lynx.parser.types")
f = logging.Formatter("[%(name)s] %(asctime)s: %(message)s (%(levelname)s)")
sh = logging.StreamHandler()
sh.setFormatter(f)
log.addHandler(sh)
if DEBUG:
    log.setLevel(logging.DEBUG) 

def parse_type(tokens):
    log.debug("lynx.parser.types.parse_type")
    type = ""
    token = tokens.current()
    
    while isinstance(token, Ly_IdentifierToken):
        type += token.value + " "
        token = tokens.next()
        
    if type[:-1] in TYPES:
        return Ly_AST_TypeNode(type[:-1])
    else:
        Ly_SyntaxError(token.file, token.line, token.pos, token.string,
                       "unexpected type '" + token.value + "'!")
        return -1