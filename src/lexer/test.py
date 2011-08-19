#!/usr/bin/python
#(c) Andreev Alexander (aka Carzil) 2011
import unittest
import main
import tokens

class Lynx_Tester(unittest.TestCase):
    def setUp(self):
        pass
    def test_operators(self):
        toks = main.get_tokens("1 + 2 * 3 & 2 >> 1 - - 3;", "C:\\hello.ly")
        for i in toks:
            self.assertIsInstance(i, tokens.Ly_Token, "One of returning values of main.get_tokens isn't instance of Ly_Token!")
            print(i)
unittest.main()