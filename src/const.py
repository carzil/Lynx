#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
KEYWORDS = ["def", "return",
            "int", "float", "string", "array", "assoc",
            "namespace", "block", "struct", "typedef",
            "class", "public", "private",
            "import", "from", "as",
            "while", "for", "in", "break", "continue",
            "and", "or", "xor",
            "if", "else", "elseif", "switch", "case"
            ]
TYPES = ["int", "long", "float", "complex",
         "string",
         "assoc", "array", "tuple", "list"]

OPERATORS = [
             "+", "-", "*", "/", "//", "%", "**", "++", "--",
             "&", "|", ">>", "<<",
             "=", "+=", "-=", "*=", "/=", "//=", "%=", "**=", "&=", "|=",
             "==", "<", ">", "!=", "<=", ">=",
             ".", ",", ";", ":", "->" 
             ]
UNOPS = ["++", "--", "-"]

DEBUG = False

PRECEDENCE = {
              "<": 10,
              ">": 10,
              ">=": 10,
              "<=": 10,
              "==": 10,
              "+": 20,
              "-": 20,
              "*": 30,
              "/": 30,
              "**": 40
              }
