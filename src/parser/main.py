#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from lexer.main import Tokens
from lexer.tokens import Ly_EOFToken
from ly_ast import Ly_AST_ModuleNode
from core import parse_expr
from errors.system import Ly_SystemError
import time 

def main(*filenames):
    start_time = time.time()
    programm = []
    for i in filenames:
        if isinstance(i, str):
            res = __parse_file(i)
            if res != -1:
                programm.append(res)
            else:
                return -1
        else:
            Ly_SystemError("all arguments of lynx.parser.main.main must be str, not", type(i))
            return -1
    if len(filenames) > 1:
        print(len(filenames), "files parsed in", str(time.time() - start_time)[0:5], "sec")
    else:
        print(1, "file parsed in", str(time.time() - start_time)[0:5], "sec")
    
    return programm
            
def __parse_file(filename):
    tokens = Tokens(filename)
    tok = tokens.current()
    programm = []
    while not isinstance(tok, Ly_EOFToken):
        tok = tokens.current()
        res = parse_expr(tokens)
        if not res:
            pass
        elif res != -1:
            programm.append(res)
        else:
            exit(1)
    return Ly_AST_ModuleNode(programm)
