import ply.lex as lex
import ply.yacc as yacc

# 1️⃣ Definir tokens
tokens = ('AND', 'OR', 'NOT', 'BOOLEAN', 'LPAREN', 'RPAREN')

t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = ' \t'  # Ignorar espacios y tabulaciones

# Reconocer booleanos (1 y 0)
def t_BOOLEAN(t):
    r'[01]'
    t.value = int(t.value)
    return t

# Manejo de errores
def t_error(t):
    print(f"Carácter no válido: {t.value[0]}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# 2️⃣ Reglas de la gramática (BNF)
def p_expr_andor(p):
    '''expr : expr AND term
            | expr OR term'''
    p[0] = p[1] and p[3] if p[2] == 'AND' else p[1] or p[3]

def p_expr_term(p):
    'expr : term'
    p[0] = p[1]

def p_term_not(p):
    'term : NOT factor'
    p[0] = not p[2]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_boolean(p):
    'factor : BOOLEAN'
    p[0] = p[1]

def p_factor_parens(p):
    'factor : LPAREN expr RPAREN'
    p[0] = p[2]

# Manejo de errores de sintaxis
def p_error(p):
    print("Expresión inválida")
    exit(1)

# Construcción del parser
parser = yacc.yacc()

# 3️⃣ Entrada de prueba
while True:
    try:
        entrada = input("Ingresa una expresión lógica: ")
        resultado = parser.parse(entrada)
        print("Expresión válida")
    except Exception:
        print("Expresión inválida")
