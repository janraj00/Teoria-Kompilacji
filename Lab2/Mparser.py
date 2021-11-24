from Lab1 import scanner
import ply.yacc as yacc

tokens = scanner.tokens
precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSE'),
    ('right', 'MULASSIGN', 'DIVASSIGN', 'SUBASSIGN', 'ADDASSIGN'),
    ('nonassoc', '<', '>', 'GE', 'LE', 'EQ', 'NEQ'),
    ('left', '+', '-'),
    ('left', 'DOTADD', 'DOTSUB'),
    ('left', '*', '/'),
    ('left', 'DOTMUL', 'DOTDIV'),
    ('right', 'UMINUS'),
    ('left', "'"),
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_start(p):
    """start :
            | instructions"""


def p_instructions(p):
    """ instructions : instruction
                    |  instruction instructions
                    | '{' instructions '}'"""


def p_instruction(p):
    """ instruction : instruction_if
                | instruction_for
                | instruction_while
                | expr ';'
                | instruction_returns';'
                | instruction_assign ';'
                | instruction_print ';'
                | BREAK ';'
                | CONTINUE ';'"""


def p_instruction_return(p):
    """ instruction_return : RETURN
                        | RETURN expr"""


def p_print_statement(p):
    """ instruction_print : PRINT printables"""


def p_printables(p):
    """ printables : printable
                | printables ',' printable"""


def p_printable(p):
    """ printable : expr
                | STRING"""


def p_assign_statement(p):
    """assignstatement : assignable '=' expr
                        | assignable ASSIGNPLUS expr
                        | assignable ASSIGNMINUS expr
                        | assignable ASSIGNTIMES expr
                        | assignable ASSIGNDIVIDE expr"""


def p_assignable(p):
    """assignable : ID
                    | matrixaccess"""


def p_matrix_access(p):
    """matrixaccess : ID '[' expr ',' expr ']'"""


def p_expr(p):
    """expr : assignable
            | INTNUMBER
            | FLOATNUMBER
            | '[' matrixinitializer ']'
            | specialmatrixword '(' expr ')'
            | '-' expr %prec UNARY
            | expr "\'"
            | '(' expr ')'
            | expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr
            | expr MPLUS expr
            | expr MMINUS expr
            | expr MTIMES expr
            | expr MDIVIDE expr
            | expr EQ expr
            | expr NEQ expr
            | expr '>' expr
            | expr '<' expr
            | expr LEQ expr
            | expr GEQ expr
            """


def p_special_matrix_word(p):
    """specialmatrixword : ZEROS
                            | ONES
                            | EYE"""


def p_if_statement(p):
    """ifstatement : IF '(' expr ')' morestatements %prec IFX
                    | IF '(' expr ')' morestatements ELSE morestatements"""


def p_loop(p):
    """loop : forloop
            | whileloop"""


def p_for_loop(p):
    """forloop : FOR ID '=' rangeoperator morestatements"""


def p_while_loop(p):
    """whileloop : WHILE '(' expr ')' morestatements"""


def p_range_op(p):
    """rangeoperator : expr ':' expr """


def p_matrix_initializer(p):
    """matrixinitializer : '[' innerlist  ']'
                        | matrixinitializer ',' '[' innerlist ']' """


def p_innerlist(p):
    """innerlist : expr
                | innerlist ',' expr"""


parser = yacc.yacc()
