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

literals = "=+-*/()[]{}<>:,';"
tokens = list(reserved.values()) + [
    'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV', 
    'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
    'LESSEREQUAL', 'GREATEREQUAL', 'EQUAL', 'NOTEQUAL',
    'ID', 'INTNUM', 'FLOAT', 'STRING',
    'COMMENT',
]

t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='
t_LESSEREQUAL = r'<='
t_GREATEREQUAL = r'>='
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_INTNUM = r'\d+'
t_FLOAT = r'(\d+(\.\d*)?|\.\d+)([eE][-]?\d+)?'
t_STRING = r'\"(\\.|[^"\\])*\"'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("(%d): illegal character '%s'" % (t.lineno, t.value[0]))
    t.lexer.skip(1)


lexer = lex.lex()
