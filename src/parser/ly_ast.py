#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
class Ly_AST_Node(object):
    pass
    
class Ly_AST_TypeNode(Ly_AST_Node):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return "type: '" + self.value + "'"    
    
class Ly_AST_NumberNode(Ly_AST_Node):
    def __init__(self, value, type):
        self.value = value
        self.type = type
    
    def __repr__(self):
        return "<Number " + self.value + ", " + str(self.type) + ">"
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_NumberNode) and self.value == obj.value 

class Ly_AST_StringNode(Ly_AST_Node):
    def __init__(self, value):
        self.value = value
        self.type = Ly_AST_TypeNode("string")
    
    def __repr__(self):
        return "<String " + self.value + ", " + str(self.type) + ">"
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_StringNode) and self.value == obj.value
    
class Ly_AST_ArrNode(Ly_AST_Node):
    def __init__(self, values):
        self.values = values
        
    def __repr__(self):
        return "<Array, values: " + str([i for i in self.values]) + ">"
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_ArrNode) and self.values == obj.values
         
class Ly_AST_DictNode(Ly_AST_Node):
    def __init__(self, keys, values):
        self.values = values
        self.keys = keys
        
    def __repr__(self):
        return "<Associative array, keys: " + str(self.keys) + ", values: " + str(self.values) + ">"
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_DictNode) and self.keys == obj.keys and self.values == obj.values
        
class Ly_AST_TupleNode(Ly_AST_Node):
    def __init__(self, values):
        self.values = values
    
    def __repr__(self):
        return "<Tuple  " + str(self.values) + ">"
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_NumberNode) and self.values == obj.values
    
class Ly_AST_SetNode(Ly_AST_Node):
    def __init__(self, vals):
        self.values = vals
        
    def __repr__(self):
        return "<Set " + str(self.values) + ">"
        
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_NumberNode) and self.values == obj.values
class Ly_AST_IdentifierNode(Ly_AST_Node):
    def __init__(self, id):
        self.id = id
    
    def __repr__(self):
        return "<Identifier '" + self.id + "'>"
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_NumberNode) and self.id == obj.id
    
class Ly_AST_ArgumentNode(Ly_AST_Node):
    def __init__(self, id, type, spec="normal"):
        self.id = id
        self.type = type
        self.spec = spec
        
    def __repr__(self):
        return "<Argument '" + self.id + "'>"

class Ly_AST_BinaryOperatorNode(Ly_AST_Node):
    def __init__(self, op, r_opd, l_opd, type, is_users=False):
        self.op = op
        self.r_opd = r_opd
        self.l_opd = l_opd
        self.type = type

class Ly_AST_UnaryOperatorNode(Ly_AST_Node):
    def __init__(self, op, opd, type, is_users=False):
        self.op = op
        self.opd = opd
        self.type = type

class Ly_AST_CallNode(Ly_AST_Node):
    def __init__(self, name, args, types, type):
        self.name = name
        self.args = args
        self.types = types
        self.type = type

class Ly_AST_PrototypeNode(Ly_AST_Node):
    def __init__(self, name, args, ret_type, pub):
        self.name = name
        self.args = args
        self.ret_type = ret_type
        self.pub = pub

class Ly_AST_FunctionNode(Ly_AST_Node):
    def __init__(self, name, body, proto):
        self.proto = proto
        self.body = body

class Ly_AST_ClassNode(Ly_AST_Node):
    def __init__(self, name, parents, pub_funcs, priv_funcs, pub_props, priv_props):
        self.pub_functions = pub_funcs
        self.priv_functions = priv_funcs
        self.pub_props = pub_props
        self.priv_props = priv_props

class Ly_AST_StructNode(Ly_AST_Node):
    def __init__(self, name, props):
        self.name = name
        self.props = props

class Ly_AST_ElseNode(Ly_AST_Node):
    def __init__(self, body):
        self.body = body
    
class Ly_AST_IfNode(Ly_AST_Node):
    def __init__(self, condition, body, t_else=None, elseif=None):
        self.condition = condition
        self.body = body
        self.t_else = t_else
        self.elseif = elseif

class Ly_AST_ElseifNode(Ly_AST_Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class Ly_AST_SwitchNode(Ly_AST_Node):
    def __init__(self, var, cases, default):
        self.var = var
        self.cases = cases

class Ly_AST_CaseNode(Ly_AST_Node):
    def __init__(self, value, body):
        self.value = value
        self.body = body

class Ly_AST_WhileNode(Ly_AST_Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class Ly_AST_ForNode(Ly_AST_Node):
    def __init__(self, loop_var, value, condition, step, body):
        self.loop_var = loop_var
        self.value = value
        self.condition = condition
        self.step = step

class Ly_AST_AssignNode(Ly_AST_Node):
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type
        
class Ly_AST_TypeDefinitionNode(Ly_AST_Node):
    def __init__(self, t_name, t_body):
        self.t_name = t_name
        self.t_body = t_body
        
class Ly_AST_Namespace(Ly_AST_Node):
    def __init__(self, name, body):
        self.name = name
        self.body = body
        
class Ly_AST_CodeBlock(Ly_AST_Node):
    def __init__(self, code):
        self.code = code
        
class Ly_AST_ImportNode(Ly_AST_Node):
    def __init__(self, m_name, t_as, t_from):
        self.m_name = m_name
        self.t_as = t_as
        self.t_from = t_from       
        
class Ly_AST_ReturnDeclarationNode(Ly_AST_Node):
    def __init__(self, type):
        self.type = type
        
class Ly_AST_ReturnNode(Ly_AST_Node):
    def __init__(self, value, r_dec):
        self.value = value
        self.type = r_dec.value
