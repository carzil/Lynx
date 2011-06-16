#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011

class Ly_Number(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, obj):
        return isinstance(obj, Ly_Number) and self.value == obj.value
    
    def __ne__(self, obj):
        return isinstance(obj, Ly_Number) and self.value != obj.value

    def __repr__(self):
        return "<Ly_Number(" + str(self.value)  + ")>"

class Ly_Identifier(object):
    def __init__(self, id):
        self.id = id

    def __eq__(self, obj):
        return isinstance(obj, Ly_Identifier) and self.id == obj.id

    def __ne__(self, obj):
        return isinstance(obj, Ly_Identifier) and self.id != obj.id

    def __repr__(self):
        return "<Ly_Identifier('" + self.id  + "')>"

class Ly_SpecChar(object):
    def __init__(self, char):
        self.char = char

    def __eq__(self, obj):
        return isinstance(obj, Ly_SpecChar) and self.char == obj.char

    def __ne__(self, obj):
        return isinstance(obj, Ly_SpecChar) and self.char != obj.char
    
    def __repr__(self):
        return "<Ly_SpecChar('" + self.char  + "')>"

class Ly_Comment(object):
    def __init__(self, comment):
        self.comment = comment

    def __eq__(self, obj):
        return isinstance(obj, Ly_Comment) and self.comment == obj.comment

    def __ne__(self, obj):
        return isinstance(obj, Ly_Comment) and self.comment != obj.commet

    def __repr__(self):
        return "<Ly_SpecComment('" + self.comment  + "')>"

class Ly_EOF(object):
    def __ne__(self, obj):
        return isinstance(obj, Ly_EOF)

    def __eq__(self, obj):
        return isinstance(obj, Ly_EOF)

    def __repr__(self):
        return "<Ly_EOF()>"


