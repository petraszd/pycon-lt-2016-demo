from ply import lex

from pyconltlisp import lexerrules


lexer = lex.lex(module=lexerrules)
lexer.input("(a 1 b 2)")
for x in lexer:
    print(x)
