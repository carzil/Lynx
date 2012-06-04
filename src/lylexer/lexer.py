#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import ply.lex as lex
from lyerrors.lexer import Ly_SyntaxError

class LyLexer(object):
    reserved = {"if": "IF",
            "else": "ELSE",
            "elseif": "ELSEIF",
            "switch": "SWITCH",
            "case": "CASE",
            "default": "DEFAULT",
            "while": "WHILE",
            "for": "FOR",
            "def": "DEF",
            "generator": "GENERATOR",
            "class": "CLASS",
            "struct": "STRUCT",
            "public": "PUBLIC",
            "private": "PRIVATE",
            "int": "TINT",
            "long": "TLONG",
            "float": "TFLOAT",
            "array": "ARRAY",
            "const array": "TUPLE",
            "const int": "CINT",
            "const long": "CLONG",
            "const float": "CFLOAT",
            "namespace": "NAMESPACE",
            "import": "IMPORT",
            "as": "AS",
            "and": "AND",
            "or": "OR",
            "return": "RETURN",
            "shl": "SHIFTLEFT",
            "shr": "SHIFTRIGTH",
            "not": "NOT"
    }

    tokens = ["ID",
          "NUMBER",
          "STRING",
          "PLUS",
          "MINUS",
          "MUL",
          "DIV",
          "POW",
          "FLOAT",
          "MOD",
          "DIV2",
          "TYPEIS",
          "THEN",
          "LPAR",
          "RPAR",
          "LSQB",
          "RSQB",
          "LBRACE",
          "RBRACE",
          "COLON",
          "DOT",
          "COMMA",
          "AMPER",
          "SEMICOLON",
          "LT",
          "GT",
          "LE",
          "GE",
          "DEQUAL",
          "NE",
          "EQUAL",
          "CIRCUMFLEXUS",
          "EMARK",
          "BAND",
          "BNOT",
          "BOR",
          "BXOR",
          "PE",
          "ME",
          "SE",
          "DSE",
          "AE",
          "DAE"
    ] + list(reserved.values())
    
    def t_NUMBER(self, t):
        r"\d+"
        #r"\d+.{0,1}\d+(l|L){0,2}"
        t.value = int(t.value)
        return t
    
    def t_FLOAT(self, t):
        r"\d+.\d+"
        t.value = float(t.value)
        return t
    
    t_STRING = r'\"([^\\\n]|(\\.))*?\"'
    t_PLUS = r"\+"
    t_MINUS = r"-"
    t_MUL = r"\*"
    t_DIV = r"/"
    t_POW = r"\*\*"
    t_MOD = r"\%"
    t_DIV2 = r"//"
    t_LPAR = r"\("
    t_RPAR = r"\)"
    t_LSQB = r"\["
    t_RSQB = r"\]"
    t_LBRACE = r"\{"
    t_RBRACE = r"\}"
    t_SEMICOLON = r";"
    t_COLON = r":"
    t_DOT = r"\."
    t_COMMA = r"\,"
    t_LT = r"\<"
    t_GT = r"\>"
    t_LE = r"\<\="
    t_GE = r"\>\="
    t_DEQUAL = r"\=\="
    t_NE = r"\!\="
    t_EQUAL = r"\="
    t_CIRCUMFLEXUS = r"\^"
    t_EMARK = r"\!"
    t_TYPEIS = r"\-\>"
    t_THEN = r"=\>"
    t_BAND = r"\&"
    t_BOR = r"\|"
    t_BXOR = r"\^"
    t_PE = r"\+\="
    t_ME = r"\+\="
    t_SE = r"\/\="
    t_DSE = r"\//\="
    t_AE = r"\*\="
    t_DAE = r"\*\*\="
    t_ignore = " \t"
    
    def __init__(self, filename):
        self.file = filename
        self.text = open(filename).read()
    
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'ID')
        return t
    
    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += 1
        
    def t_COMMENT(self, t):
        r"\#.*"
        pass
    
    def t_error(self, t):
        Ly_SyntaxError(self.file, t.lexer.lineno, "invalid character: '%s'" % (t.value[0],))
        t.lexer.skip(1)
    
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.lexer.input(self.text)
        
    def token(self):
        return self.lexer.token()
            

if __name__ == "__main__":
    lexer = LyLexer("../../examples/all.ly")
    lexer.build()
    for i in lexer.parse():
        print(i)
