#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
class Ly_AST_Node(object):
    pass         

class Ly_AST_Constant(object):
    constant = True

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
            s += "    " + str(i) + ";\n"            
        return str(s[:-1])    

    
class Ly_AST_TypeNode(Ly_AST_Node):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return " -> " + str(self.value)  
    
class Ly_AST_NumberNode(Ly_AST_Node, Ly_AST_Constant):
    def __init__(self, value, type):
        self.value = value
        self.type = type
        
    def run(self):
        return int(self.value)
    
    def __repr__(self):
        return str(self.value) + " -> " + str(self.type)
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_NumberNode) and self.value == obj.value 

class Ly_AST_StringNode(Ly_AST_Node, Ly_AST_Constant):
    def __init__(self, value):
        self.value = value
        self.type = Ly_AST_TypeNode("string")
    
    def __repr__(self):
        return "'" + str(self.value)[1:-1] + "'"
        
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_StringNode) and self.value == obj.value
    
class Ly_AST_ListNode(Ly_AST_Node, Ly_AST_Constant):
    def __init__(self, values):
        self.values = values
        
    def __repr__(self):
        return str(self.values)
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_ListNode) and self.values == obj.values
         
class Ly_AST_TupleNode(Ly_AST_Node, Ly_AST_Constant):
    def __init__(self, values):
        self.values = values
        
    def __repr__(self):
        return str(self.values)
    
    def __eq__(self, obj):
        return isinstance(obj, Ly_AST_TupleNode) and self.values == obj.values
         
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

class Ly_AST_FunctionNode(Ly_AST_Node):
    def __init__(self, name, args, rtype, body):
        self.name = name
        if args:
            self.args = args
        else:
            self.args = ""
        self.body = body
        self.rtype = rtype
    
    def __repr__(self):
        return "def " + str(self.name) + "(" + ", ".join(map(str, self.args)) + ")" + str(self.rtype) + " {\n" + str(self.body) + "\n}"

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

class Ly_AST_ElseIfNode(Ly_AST_Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    
    def __repr__(self):
        return "elseif (" + str(self.condition) + ") {\n" + str(self.body) + "\n} "

class Ly_AST_IfNode(Ly_AST_Node):
    def __init__(self, condition, body, t_else=None, elseifs=None):
        self.condition = condition
        self.body = body
        self.t_else = t_else
        self.elseifs = elseifs
        
    def __repr__(self):
        s = "if " + "(" + str(self.condition) + ")" + "\n{\n" + str(self.body) + "\n} "
        if self.t_else:
            s += str(self.t_else)
        if self.elseifs:
            s += "\n".join(map(str, self.elseifs))
        return s
        

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
        return "while (" + str(self.condition) + ") => {\n" + str(self.body) + "\n}"

class Ly_AST_ForNode(Ly_AST_Node):
    def __init__(self, loop_var, condition, step, body):
        self.loop_var = loop_var
        self.condition = condition
        self.step = step
        self.body = body
        
    def __repr__(self):
        return "for (" + str(self.loop_var) + "; " + str(self.condition) + "; " +\
               str(self.step) + ")\n{\n" + str(self.body) + "\n}"

class Ly_AST_AssignNode(Ly_AST_Node):
    def __init__(self, name, value, ttype):
        self.name = name
        self.value = value
        self.type = ttype
        
    def __repr__(self):
        return str(self.name) + str(self.type) + " = " + str(self.value)
        
class Ly_AST_Assign2Node(Ly_AST_Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __repr__(self):
        return str(self.name) + " = " + str(self.value)

class Ly_AST_AddAssignNode(Ly_AST_Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __repr__(self):
        return str(self.name) + " += " + str(self.value)

class Ly_AST_SubAssignNode(Ly_AST_Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __repr__(self):
        return str(self.name) + " -= " + str(self.value)

class Ly_AST_DivAssignNode(Ly_AST_Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __repr__(self):
        return str(self.name) + " /= " + str(self.value)
    
class Ly_AST_Div2AssignNode(Ly_AST_Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __repr__(self):
        return str(self.name) + " //= " + str(self.value)

class Ly_AST_MulAssignNode(Ly_AST_Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __repr__(self):
        return str(self.name) + " *= " + str(self.value)

class Ly_AST_PowAssignNode(Ly_AST_Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __repr__(self):
        return str(self.name) + " **= " + str(self.value)
        
class Ly_AST_NamespaceNode(Ly_AST_Node):
    def __init__(self, name, body):
        self.name = name
        self.body = body
    
    def __repr__(self): 
        return "namespace %s {\n\t%s\n}" % (str(self.name), "\n\t".join(str(self.body).split("\n")))
        
class Ly_AST_CodeBlock(Ly_AST_Node):
    def __init__(self, code):
        self.code = code
        
class Ly_AST_ImportNode(Ly_AST_Node):
    def __init__(self, m_name, t_as, t_from):
        self.m_name = m_name
        self.t_as = t_as
        self.t_from = t_from       
        
class Ly_AST_ReturnNode(Ly_AST_Node):
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return "return " + str(self.value) 
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
        return "not" + str(self.obj)

class Ly_AST_BinNotNode(Ly_AST_Node):
    def __init__(self, obj):
        self.obj = obj
        
    def __repr__(self):
        return "!" + str(self.obj)
    
class Ly_AST_AndNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def __repr__(self):
        return "(" + str(self.right) + ") and (" + str(self.left) + ")"

class Ly_AST_OrNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def __repr__(self):
        return "(" + str(self.right) + ") or (" + str(self.left) + ")"

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
    
class Ly_AST_Div2Node(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l

    def run(self):
        l = self.left.run()
        r = self.right.run()
        return r // l

    def __repr__(self):
        return "(" + str(self.right) + ") / (" + str(self.left) + ")"

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

class Ly_AST_BinAndNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def __repr__(self):
        return "(" + str(self.right) + ") & (" + str(self.left) + ")"

class Ly_AST_BinOrNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def __repr__(self):
        return "(" + str(self.right) + ") | (" + str(self.left) + ")"
    
class Ly_AST_BinXorNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def __repr__(self):
        return "(" + str(self.right) + ") ^ (" + str(self.left) + ")"

class Ly_AST_BinShlNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def __repr__(self):
        return "(" + str(self.right) + ") shl (" + str(self.left) + ")"

class Ly_AST_BinShrNode(Ly_AST_Node):
    def __init__(self, r, l):
        self.right = r
        self.left = l
        
    def __repr__(self):
        return "(" + str(self.right) + ") shr (" + str(self.left) + ")"

class Ly_AST_VarProtoNode(Ly_AST_Node):
    def __init__(self, name, ttype):
        self.name = name
        self.type = ttype
        
    def __repr__(self):
        return str(self.name) + str(self.type)
