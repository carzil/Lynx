#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
class Ly_AST_Node(object):
    pass
    
class Ly_AST_Number(Ly_AST_Node):
    def __init__(self, value):
        self.value = value

class Ly_AST_String(Ly_AST_Node):
    def __init__(self, value):
        self.value = value
    
class Ly_AST_Identifier(Ly_AST_Node):
    def __init__(self, id):
        self.id = id
    
class Ly_AST_VariablePrototype(Ly_AST_Node):
    def __init__(self, id, type)
        self.id = id
        self.type = type

class Ly_AST_BinaryOperator(Ly_AST_Node):
    def __init__(self, op, r_opd, l_opd, type, is_users=False):
        self.op = op
        self.r_opd = r_opd
        self.l_opd = l_opd
        self.type = type

class Ly_AST_UnaryOperator(Ly_AST_Node):
    def __init__(self, op, opd, type, is_users=False):
        self.op = op
        self.opd = opd
        self.type = type

class Ly_AST_Call(Ly_AST_Node):
    def __init__(self, name, args, types, type):
        self.name = name
        self.args = args
        self.types = types
        self.type = type

class Ly_AST_Prototype(Ly_AST_Node):
    def __init__(self, name, args, types, type):
       self.name = name
       self.args = args
       self.types = types
       self.type = type

class Ly_AST_Function(Ly_AST_Node):
    def __init__(self, name, body, type):
        self.name = name
        self.body = body

class Ly_AST_Class(Ly_AST_Node):
    def __init__(self, name, pub_funcs, priv_funcs, pub_props, priv_props):
        self.pub_functions = pub_functions
        self.priv_functions = priv_functions
        self.pub_props = pub_props
        self.priv_props = priv_props

class Ly_AST_Struct(Ly_AST_Node):
    def __init__(self, name, props):
        self.name = name
        self.props = props

class Ly_AST_else(Ly_AST_Node):
    def __init__(self, body):
        self.body = body
    
class Ly_AST_if(Ly_AST_Node):
    def __init__(self, condition, body, t_else=None, elseif=None):
        self.condition = condition
        self.body = body
        self.t_else = t_else
        self.elseif = elseif

class Ly_AST_elseif(Ly_AST_Node):
    def __init__(self, contion, body):
        self.condition = condition
        self.body = body

class Ly_AST_switch(Ly_AST_Node):
    def __init__(self, var, cases, default):
        self.var = var
        self.cases = cases

class Ly_AST_case(Ly_AST_Node):
    def __init__(self, value, body):
        self.value = value
        self.body = body

class Ly_AST_while(Ly_AST_Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class Ly_AST_for(Ly_AST_Node):
    def __init__(self, loop_var, value, condition, step, body):
        self.loop_var = loop_var
        self.value = value
        self.condition = condition
        self.step = step

class Ly_AST_Declaration(Ly_AST_Node):
    def __init__(self, var, value, type):
        self.var = var
        self.value = value
        self.type = type
        

