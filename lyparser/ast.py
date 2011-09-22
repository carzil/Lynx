#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
class Ly_AST_Node(object):
    pass

class Ly_AST_ModuleNode(Ly_AST_Node):
    def __init__(self, code):
        self.code = code
    
    def run(self):
        res = []
        for i in self.code:
            res.append(i.run())
        return res
    
    def __repr__(self):
        s = ""
        for i in self.code:
            s += str(i) + ";\n"            
        return str(s[:-1])    
    
class Ly_AST_CodeNode(Ly_AST_Node):
    def __init__(self, code):
        self.code = code
        
    def run(self):
        res = []
        for i in self.code:
            res.append(i.run())
        return res
    
    def __repr__(self):
        s = ""
        for i in self.code:
            s += str(i) + ";\n"            
        return str(s[:-1])    

    
class Ly_AST_TypeNode(Ly_AST_Node):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return str(self.value)    
    
class Ly_AST_NumberNode(Ly_AST_Node):
    def __init__(self, value, type):
        self.value = value
        self.type = type
        
    def run(self):
        return int(self.value)
    
    def __repr__(self):
        return str(self.value) + " -> " + str(self.type)
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_NumberNode) and self.value == obj.value 

class Ly_AST_StringNode(Ly_AST_Node):
    def __init__(self, value):
        self.value = value
        self.type = Ly_AST_TypeNode("string")
    
    def __repr__(self):
        return "'" + str(self.value)[1:-1] + "'"
        
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_StringNode) and self.value == obj.value
    
class Ly_AST_ArrNode(Ly_AST_Node):
    def __init__(self, values):
        self.values = values
        
    def __repr__(self):
        return str(self.values)
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_ArrNode) and self.values == obj.values
         
class Ly_AST_DictNode(Ly_AST_Node):
    def __init__(self, keys, values):
        self.values = values
        self.keys = keys
        
    def __repr__(self):
        res = "{"
        for i in range(len(self.keys)):
            res += str(self.keys[i]) + ": " + str(self.values[i]) + ", "
        res = res[:-2]
        res += "}"
        return res
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_DictNode) and self.keys == obj.keys and self.values == obj.values
            
class Ly_AST_SetNode(Ly_AST_Node):
    def __init__(self, vals):
        self.values = vals
        
    def __repr__(self):
        return "{" + str(self.values)[1:-1] + "}"
        
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_NumberNode) and self.values == obj.values
    
class Ly_AST_IdentifierNode(Ly_AST_Node):
    def __init__(self, id):
        self.id = id
    
    def __repr__(self):
        return str(self.id)
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_NumberNode) and self.id == obj.id
    
class Ly_AST_DottedIdentifierNode(Ly_AST_Node):
    def __init__(self, parent, id):
        self.parent = parent
        self.id = id
    
    def __repr__(self):
        return str(self.parent) + "." + str(self.id)
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_NumberNode) and self.id == obj.id

class Ly_AST_ArgumentNode(Ly_AST_Node):
    def __init__(self, id, type):
        self.id = id
        self.type = type
        
    def __repr__(self):
        return str(self.id) + " -> " + str(self.type)
    
class Ly_AST_ArgumentDefaultNode(Ly_AST_Node):
    def __init__(self, id, type, value):
        self.id = id
        self.type = type
        
    def __repr__(self):
        return str(self.id) + " -> " + str(self.type)

class Ly_AST_KeywordArgumentsNode(Ly_AST_Node):
    def __init__(self, id, type):
        self.id = id
        self.type = type
        
    def __repr__(self):
        return str(self.id) + " -> " + str(self.type)
    
class Ly_AST_MultipleArgumentsNode(Ly_AST_Node):
    def __init__(self, id, type):
        self.id = id
        self.type = type
        
    def __repr__(self):
        return str(self.id) + " -> " + str(self.type)

class Ly_AST_IndexingNode(Ly_AST_Node):
    def __init__(self, name, index):
        self.name = name
        self.index = index
        
    def __repr__(self):
        return str(self.name) + "[" + str(self.index) + "]"

class Ly_AST_SliceNode(Ly_AST_Node):
    def __init__(self, name, start, stop):
        self.name = name
        self.start = start
        self.stop = stop
        
    def __repr__(self):
        return str(self.name) + "[" + str(self.start) + ":" + str(self.stop) + "]"

class Ly_AST_CallNode(Ly_AST_Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args
        
    def __repr__(self):
        s = str(self.name) + "("
        for i in self.args:
            s += str(i) + ", "
        if len(self.args) > 0:
            s = s[:-2] + ")"
        else:
            s = s + ")"
        return s

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
    
    def __repr__(self):
        return "else {\n" + str(self.body) + "\n}"

class Ly_AST_IfNode(Ly_AST_Node):
    def __init__(self, condition, body, t_else=None, elseif=None):
        self.condition = condition
        self.body = body
        self.t_else = t_else
        
    def __repr__(self):
        if self.t_else == None:
            return "if " + "(" + str(self.condition) + ")" + "\n{\n" + str(self.body) + "\n}"
        else:
            return "if " + "(" + str(self.condition) + ")" + "\n{\n" + str(self.body) + "\n} " + str(self.t_else)

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
        
    def __repr__(self):
        return "while (" + str(self.condition) + ")\n{\n" + str(self.body) + "\n}"

class Ly_AST_ForNode(Ly_AST_Node):
    def __init__(self, loop_var, value, condition, step, body):
        self.loop_var = loop_var
        self.value = value
        self.condition = condition
        self.step = step
        self.body = body
        
    def __repr__(self):
        return "for (" + str(self.loop_var) + " = " + str(self.value) + "; " + str(self.condition) + "; " +\
               str(self.step) + ")\n{\n" + str(self.body) + "\n}"

class Ly_AST_AssignNode(Ly_AST_Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __repr__(self):
        return str(self.name) + " = " + str(self.value)
        
class Ly_AST_MultipleAssignNode(Ly_AST_Node):
    def __init__(self, names, value):
        self.names = names
        self.value = value
        
    def __repr__(self):
        a = ""
        for i in range(len(self.names)):
            a += str(self.names[i]) + " = "
        a += str(self.value)
        return a
        
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
        
class Ly_AST_ReturnNode(Ly_AST_Node):
    def __init__(self, value, r_dec):
        self.value = value
        self.type = r_dec.value
        
class Ly_AST_IncNode(Ly_AST_Node):
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return str(self.name) + "++"

class Ly_AST_DecNode(Ly_AST_Node):
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return str(self.name) + "--"

class Ly_AST_NegNode(Ly_AST_Node):
    def __init__(self, obj):
        self.obj = obj
        
    def __repr__(self):
        return "-" + str(self.obj)

class Ly_AST_NotNode(Ly_AST_Node):
    def __init__(self, obj):
        self.obj = obj
        
    def __repr__(self):
        return "!" + str(self.obj)


class Ly_AST_AddNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def run(self): #Method 'run' is used only for debug
        l = self.left.run()
        r = self.right.run()
        return l + r

    def __repr__(self):
        return "(" + str(self.right) + ") + (" + str(self.left) + ")"
    
class Ly_AST_SubNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def run(self):
        l = self.left.run()
        r = self.right.run()
        return r - l

    def __repr__(self):
        return "(" + str(self.right) + ") - (" + str(self.left) + ")"
    
class Ly_AST_MulNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def run(self):
        l = self.left.run()
        r = self.right.run()
        return l * r

    def __repr__(self):
        return "(" + str(self.right) + ") * (" + str(self.left) + ")"
    
class Ly_AST_DivNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l

    def run(self):
        l = self.left.run()
        r = self.right.run()
        return r // l

    def __repr__(self):
        return "(" + str(self.right) + ") // (" + str(self.left) + ")"
    
class Ly_AST_ModNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def run(self):
        l = self.left.run()
        r = self.right.run()
        return l % r

    def __repr__(self):
        return "(" + str(self.right) + ") % (" + str(self.left) + ")"
    
class Ly_AST_PowNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def run(self):
        l = self.left.run()
        r = self.right.run()
        return l ** r

    def __repr__(self):
        return "(" + str(self.right) + ") ** (" + str(self.left) + ")"
    
class Ly_AST_EQNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def run(self):
        l = self.left.run()
        r = self.right.run()
        return l == r

    def __repr__(self):
        return "(" + str(self.right) + ") == (" + str(self.left) + ")"
    
class Ly_AST_LTNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def run(self):
        l = self.left.run()
        r = self.right.run()
        return l < r

    def __repr__(self):
        return "(" + str(self.right) + ") < (" + str(self.left) + ")"
    
class Ly_AST_LENode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def run(self):
        l = self.left.run()
        r = self.right.run()
        return l <= r

    def __repr__(self):
        return "(" + str(self.right) + ") <= (" + str(self.left) + ")"
    
class Ly_AST_NENode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def run(self):
        l = self.left.run()
        r = self.right.run()
        return l != r

    def __repr__(self):
        return "(" + str(self.right) + ") != (" + str(self.left) + ")"
    
class Ly_AST_GTNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def run(self):
        l = self.left.run()
        r = self.right.run()
        return l > r

    def __repr__(self):
        return "(" + str(self.right) + ") > (" + str(self.left) + ")"
    
class Ly_AST_GENode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def run(self):
        l = self.left.run()
        r = self.right.run()
        return l >= r

    def __repr__(self):
        return "(" + str(self.right) + ") >= (" + str(self.left) + ")"
