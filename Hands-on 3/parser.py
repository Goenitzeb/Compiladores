import ply.yacc as yacc
from lexer import tokens  # Importar los tokens del lexer

# Definición de la gramática en BNF

def p_expr_plus_minus(p):
    '''expr : expr PLUS term
            | expr MINUS term'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1] - p[3]

def p_expr_term(p):
    'expr : term'
    p[0] = p[1]

def p_term_times_divide(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    else:
        p[0] = p[1] / p[3] if p[3] != 0 else float('inf')  # Evitar división entre 0

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expr RPAREN'
    p[0] = p[2]  # Evaluar la expresión dentro de paréntesis

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Expresión inválida")

# Construir el parser
parser = yacc.yacc()
