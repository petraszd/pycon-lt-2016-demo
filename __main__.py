import sys

from ply import lex, yacc

from pyconltlisp import lexerrules
from pyconltlisp import parserrules
from pyconltlisp.enviroment import Enviroment


lexer = lex.lex(module=lexerrules)

parser_walker = parserrules.ParserWalker()
parser = yacc.yacc(module=parser_walker, debug=False, write_tables=False)

with open(sys.argv[1], 'r') as f:
    code = f.read()
parser.parse(code, lexer=lexer)

enviroment = Enviroment()
parser_walker.root.evaluate(enviroment)
