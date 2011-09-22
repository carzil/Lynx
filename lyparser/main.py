#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
from lylexer.main import Tokens
from lylexer.tokens import Ly_EOFToken
from ast import Ly_AST_ModuleNode
from core import parse_program
import time

def main(*filenames):
    start_time = time.time()
    programm = []
    for i in filenames:
        res = __parse_file(i)
        programm.append(res)
    if len(filenames) > 1:
        print(len(filenames), "files parsed in", str(time.time() - start_time)[0:5], "sec")
    else:
        print("1", "file parsed in", str(time.time() - start_time)[0:5], "sec")
    
    return programm
            
def __parse_file(filename):
    tokens = Tokens(filename)
    tok = tokens.current()
    programm = []
    while not isinstance(tok, Ly_EOFToken):
        tok = tokens.current()
        res = parse_program(tokens)
        if not res:
            pass
        else:
            programm.append(res)
    return Ly_AST_ModuleNode(programm)
