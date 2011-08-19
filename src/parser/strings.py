#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from ly_ast import Ly_AST_StringNode
import logging
from const import DEBUG

log = logging.getLogger("lynx.parser.strings")
f = logging.Formatter("[%(name)s] %(asctime)s: %(message)s (%(levelname)s)")
sh = logging.StreamHandler()
sh.setFormatter(f)
log.addHandler(sh)
if DEBUG:
    log.setLevel(logging.DEBUG)

def parse_string(tokens):
    log.debug("lynx.parser.strings.parse_string")
    value = tokens.current().value
    tokens.next()
    return Ly_AST_StringNode(value)