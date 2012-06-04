#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import ply.yacc as yacc
import ast
from lylexer.lexer import LyLexer
from lyerrors.parser import Ly_SyntaxError

class LyParser(object):
    def __init__(self, filename):
        self.filename = filename
        self.tokenizer = LyLexer(filename)
        self.fopen = open(filename)
        self.tokenizer.build()
        self.tokens = self.tokenizer.tokens
        self.parser = yacc.yacc(module=self)
             
    def parse(self):
        return self.parser.parse(lexer=self.tokenizer, debug=1)

#Main
    def p_program(self, p):
        """program : input
        """
        p[0] = ast.Ly_AST_ModuleNode(p[1])
    
    def p_input(self, p):
        """input : op
                 | input op
                 |
        """
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        elif len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = []
        
    def p_op(self, p):
        """op : expr SEMICOLON
              | stmt SEMICOLON
        """
        p[0] = p[1]
        
#Statements
    def p_stmt(self, p):
        """stmt : def_stmt
                | if_stmt
                | call_stmt
                | while_stmt
                | for_stmt
                | assign"""
        p[0] = p[1]
        
    def p_if_stmt(self, p):
        """
        if_stmt : IF expr THEN code_block elseifs_stmts else_stmt
                | IF LPAR expr RPAR code_block elseifs_stmts else_stmt
        """
        if len(p) == 7:
            p[0] = ast.Ly_AST_IfNode(p[2], p[4], p[6], p[5])
        else:
            p[0] = ast.Ly_AST_IfNode(p[3], p[5], p[7], p[6])
            
    def p_elseifs_stmts(self, p):
        """
        elseifs_stmts : elseifs_stmts elseif_stmt
                      | elseif_stmt
                      | 
        """
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        elif len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = []
            
    def p_elseif_stmt(self, p):
        """
        elseif_stmt : ELSEIF expr THEN code_block
                    | ELSEIF LPAR expr RPAR code_block
        """
        if len(p) == 5:
            p[0] = ast.Ly_AST_ElseIfNode(p[2], p[4], p[5], p[6])
        else:
            p[0] = ast.Ly_AST_ElseIfNode(p[3], p[5], p[6], p[7])
            
    def p_else_stmt(self, p):
        """
        else_stmt : ELSE THEN code_block
                  | ELSE code_block
        """
        if len(p) == 4:
            p[0] = ast.Ly_AST_ElseNode(p[3])
        else:
            p[0] = ast.Ly_AST_ElseNode(p[2]) 
        
    def p_stmt_while(self, p):
        """
        while_stmt : WHILE LPAR expr RPAR code_block
                   | WHILE LPAR expr RPAR THEN code_block
        """
        if len(p) == 6:
            p[0] = ast.Ly_AST_WhileNode(p[3], p[5])
        else:
            p[0] = ast.Ly_AST_WhileNode(p[3], p[6])
            
    def p_stmt_for(self, p):
        """
        for_stmt : FOR LPAR assign SEMICOLON expr SEMICOLON expr RPAR code_block
                 | FOR LPAR expr SEMICOLON expr SEMICOLON expr RPAR THEN code_block
        """
        if len(p) == 10: 
            p[0] = ast.Ly_AST_ForNode(p[3], p[5], p[7], p[9])
        else:
            p[0] = ast.Ly_AST_ForNode(p[3], p[5], p[7], p[10])
            
    def p_stmt_fdef(self, p):
        """
        def_stmt : DEF ID LPAR var_prototypes_list RPAR TYPEIS type THEN code_block
                     | DEF ID LPAR var_prototypes_list RPAR TYPEIS type code_block
        """
        if len(p) == 10:
            p[0] = ast.Ly_AST_FunctionNode(p[2], p[4], p[7], p[9])
        else:
            p[0] = ast.Ly_AST_FunctionNode(p[2], p[4], p[7], p[8])
            
    def p_vpl(self, p):
        """var_prototypes_list : var_prototypes_list COMMA var_prototype
                               | var_prototype
        """
        if len(p) == 4:
            p[0] = p[1] + [p[3]]
        else:
            p[0] = [p[1]]
            
    def p_var_proto(self, p):
        """
        var_prototype : ID TYPEIS type
        """
        p[0] = ast.Ly_AST_VarProtoNode(p[1], p[3])
        
    def p_call_stmt(self, p):
        """call_stmt : ID LPAR RPAR
                     | ID LPAR args_list RPAR
        """
        if len(p) == 4:
            p[0] = ast.Ly_AST_CallNode(p[1], [])
        else:
            p[0] = ast.Ly_AST_CallNode(p[1], p[3])
        
    def p_assign_stmt(self, p):
        """
        assign : ID TYPEIS type EQUAL expr
               | assign_left EQUAL expr
               | assign_left PE expr
               | assign_left ME expr
               | assign_left SE expr
               | assign_left DSE expr
               | assign_left AE expr
               | assign_left DAE expr
        """
        if len(p) == 6:
            p[0] = ast.Ly_AST_AssignNode(p[1], p[5], p[3])
        else:
            if p[2] == "+=":
                p[0] = ast.Ly_AST_AddAssignNode(p[1], p[3])
            elif p[2] == "-=":
                p[0] = ast.Ly_AST_SubAssignNode(p[1], p[3])
            elif p[2] == "*=":
                p[0] = ast.Ly_AST_MulAssignNode(p[1], p[3])
            elif p[2] == "/=":
                p[0] = ast.Ly_AST_DivAssignNode(p[1], p[3])
            elif p[2] == "//=":
                p[0] = ast.Ly_AST_Div2AssignNode(p[1], p[3])
            elif p[2] == "**=":
                p[0] = ast.Ly_AST_PowAssignNode(p[1], p[3])
            else:
                p[0] = ast.Ly_AST_Assign2Node(p[1], p[3])
                
    def p_assign_left(self, p):
        """assign_left : ID
                       | index_expr
        """
        p[0] = p[1]
        
    def p_args_list(self, p):
        """args_list : expr
                     | args_list COMMA expr
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

#Expressions        
    def p_expr(self, p):
        """expr : par_expr
                | test
                | return_expr
                | index_expr
        """
        p[0] = p[1]
        
    def p_index_expr(self, p):
        """
        index_expr : ID LSQB expr RSQB
        """
        p[0] = ast.Ly_AST_IndexingNode(p[1], p[3])
        
    def p_test(self, p):
        """test : test AND cmp
                | test OR cmp 
                | cmp
        """
        if len(p) == 4:
            if p[2] == "and":
                p[0] = ast.Ly_AST_AndNode(p[1], p[3])
            elif p[2] == "or":
                p[0] = ast.Ly_AST_OrNode(p[1], p[3])
        else:
            p[0] = p[1]
            
    def p_cmp(self, p):
        """cmp : cmp LT cmp_expr
               | cmp GT cmp_expr
               | cmp LE cmp_expr
               | cmp GE cmp_expr
               | cmp NE cmp_expr
               | cmp DEQUAL cmp_expr
               | cmp_expr
        """
        if len(p) == 4:
            if p[2] == "<":
                p[0] = ast.Ly_AST_LTNode(p[1], p[3])
            elif p[2] == ">":
                p[0] = ast.Ly_AST_GTNode(p[1], p[3])
            elif p[2] == "<=":
                p[0] = ast.Ly_AST_LENode(p[1], p[3])
            elif p[2] == ">=":
                p[0] = ast.Ly_AST_GENode(p[1], p[3])
            elif p[2] == "!=":
                p[0] = ast.Ly_AST_NENode(p[1], p[3])
            elif p[2] == "==":
                p[0] = ast.Ly_AST_EQNode(p[1], p[3])
        else:
            p[0] = p[1]
    
    def p_cmp_expr(self, p):
        """
        cmp_expr : or
        """
        p[0] = p[1]
            
    def p_or_expr(self, p):
        """or : or BOR xor
              | xor
        """
        if len(p) == 4:
            p[0] = ast.Ly_AST_BinOrNode(p[1], p[3])
        else:
            p[0] = p[1]
        
    def p_xor_expr(self, p):
        """xor : xor BXOR and
               | and
        """
        if len(p) == 4:
            p[0] = ast.Ly_AST_BinXorNode(p[1], p[3])
        else:
            p[0] = p[1]
            
    def p_and_expr(self, p):
        """and : and BAND shift
               | shift
        """
        if len(p) == 4:
            p[0] = ast.Ly_AST_BinAndNode(p[1], p[3])
        else:
            p[0] = p[1]
    
    def p_shift_expr(self, p):
        """shift : and SHIFTLEFT shift
                 | and SHIFTRIGTH shift
                 | arith
        """
        if len(p) == 4:
            if p[2] == "shl":
                p[0] = ast.Ly_AST_BinShlNode(p[1], p[3])
            else:
                p[0] = ast.Ly_AST_BinShrNode(p[1], p[3])
        else:
            p[0] = p[1]

    def p_par_expr(self, p):
        """par_expr : LPAR arith RPAR
        """
        p[0] = p[2]

    def p_arith(self, p):
        """arith : arith PLUS term
                 | arith MINUS term
                 | term"""
        if len(p) == 4:
            if str(p[2]) == "+":
                p[0] = ast.Ly_AST_AddNode(p[1], p[3])
            elif str(p[2]) == "-":
                p[0] = ast.Ly_AST_SubNode(p[1], p[3])
        else:
            p[0] = p[1]
            
    
    def p_term(self, p): 
        """term : term MUL factor
                | term DIV factor
                | term MOD factor
                | term POW factor
                | term DIV2 factor
                | factor"""
        if len(p) == 4:
            if str(p[2]) == "*":
                p[0] = ast.Ly_AST_MulNode(p[1], p[3])
            elif str(p[2]) == "%":
                p[0] = ast.Ly_AST_ModNode(p[1], p[3])
            elif str(p[2]) == "//":
                p[0] = ast.Ly_AST_DivNode(p[1], p[3])
            elif str(p[2]) == "/":
                p[0] = ast.Ly_AST_Div2Node(p[1], p[3])
            elif str(p[2]) == "**":
                p[0] = ast.Ly_AST_PowNode(p[1], p[3])
        else:
            p[0] = p[1]
            
    def p_factor(self, p):
        """factor : atom 
                  | EMARK atom
                  | MINUS atom
                  | PLUS atom
                  | NOT atom
        """
        if len(p) == 3:
            if p[1] == "!":
                p[0] = ast.Ly_AST_BinNotNode(p[2])
            elif p[1] == "-":
                p[0] = ast.Ly_AST_NegNode(p[2])
            elif p[1] == "not":
                p[0] = ast.Ly_AST_NotNode(p[2])
            else:
                p[0] = p[2]
        else:
            p[0] = p[1]
            
    def p_atom(self, p):
        """atom : primary
                | call_stmt
        """
        p[0] = p[1]

    def p_primary(self, p):
        """primary : ID
                   | NUMBER
                   | FLOAT
                   | STRING
                   | list_def
        """
        p[0] = p[1]
                
#Other  

    def p_list_def(self, p):
        """list_def : LSQB RSQB
                    | LSQB primary_list RSQB
        """
        if len(p) == 4:
            p[0] = ast.Ly_AST_ListNode(p[2])
        else:
            p[0] = ast.Ly_AST_ListNode([])
        
    def p_primary_list(self, p):
        """primary_list : primary
                        | primary_list COMMA primary
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]
    
    def p_type(self, p):
        """type : TINT
                | TLONG
                | TFLOAT
                | ARRAY
                | TUPLE
                | CINT
                | CLONG
                | CFLOAT
        """
        p[0] = ast.Ly_AST_TypeNode(p[1])
        
    def p_code_block(self, p):
        """
        code_block : LBRACE input RBRACE
        """
        p[0] = ast.Ly_AST_CodeNode(p[2])
        
    def p_return(self, p):
        """
        return_expr : RETURN test
        """
        p[0] = ast.Ly_AST_ReturnNode(p[2])
    
    def p_error(self, p):
        Ly_SyntaxError(self.filename, p.lineno, [p.lexpos], self.fopen.readlines()[p.lineno - 1], "syntax error")

if __name__ == "__main__":
    #p = LyParser("../../examples/all.ly")
    p = LyParser("../hello.ly")
    print(p.parse())
