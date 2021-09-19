tokens = (
    'NUMBER',
    'SYMBOL',
    'S_BEGIN',
    'S_END',
)
t_ignore = '\t\n '


def t_error(t):
    print("Lexer error")
    t.lexer.skip(1)


def t_S_BEGIN(t):
    r'\('
    t.value = ''
    return t


def t_S_END(t):
    r'\)'
    t.value = ''
    return t


def t_SYMBOL(t):
    r'[^\d\s()][^\s()]*'
    return t


def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t
