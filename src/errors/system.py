#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
M = "It is fatal error. Please contact with Lynx support team for more information!" 
def Ly_SystemError(msg):
    print("SystemError:", msg)
    print(M)
    
def Ly_IOError(msg):
    print("IOError:", msg)