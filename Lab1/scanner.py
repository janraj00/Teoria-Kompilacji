import sys
import ply.lex as lex

reserved = {
    'if': 'IF',
    'for': 'FOR',
    'else': 'ELSE',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'PRINT',
}

tokens = ['DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV', 'ADDASSIGN', 'SUBASSIGN',
          'MULASSIGN', DIVASSIGN]

literals = "=+-*/()[]{}<>:,';"
t_ignore = ' \t'
t_COMMENT = r'\#*'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("line %d: illegal character '%s'" % (t.lineno, t.value[0]))
    t.lexer.skip(1)


lexer = lex.lex()
fh = None
try:
    fh = open(sys.argv[1] if len(sys.argv) > 1 else "plik.ini", "r");
    lexer.input(fh.read())
    for token in lexer:
        print("line %d: %s(%s)" % (token.lineno, token.type, token.value))
except:
    print("open error\n")
