import ply.lex as lex
import ply.yacc as yacc

# Definir tokens
tokens = ('AND', 'OR', 'NOT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'NUMBER', 'BOOL')

# Definición de los tokens
t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# BOOLEANOS 0 y 1
def t_BOOL(t):
    r'[01]'
    t.value = int(t.value)  # Convertir '0' o '1' a entero
    return t

# Números (para expresiones aritméticas)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Carácter no válido: {t.value[0]}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# 📌 **Precedencia de operadores** para evitar conflictos shift/reduce
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('nonassoc', 'BOOL', 'NUMBER'),  # Evita confusiones entre booleanos y números
    ('nonassoc', 'LPAREN', 'RPAREN')  # Permite el uso de paréntesis
)

# 📌 **Reglas de la gramática**
def p_expr_addsub(p):
    '''expr : expr PLUS term
            | expr MINUS term'''
    p[0] = p[1] + p[3] if p[2] == '+' else p[1] - p[3]

def p_expr_term(p):
    'expr : term'
    p[0] = p[1]

def p_term_muldiv(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    p[0] = p[1] * p[3] if p[2] == '*' else p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_parens(p):
    'factor : LPAREN expr RPAREN'
    p[0] = p[2]

def p_factor_logical(p):
    'factor : logical'
    p[0] = p[1]

def p_logical_andor(p):
    '''logical : logical AND logical
               | logical OR logical'''
    p[0] = p[1] and p[3] if p[2] == 'AND' else p[1] or p[3]

def p_logical_not(p):
    'logical : NOT logical'
    p[0] = not p[2]

def p_logical_bool(p):
    'logical : BOOL'
    p[0] = bool(p[1])

def p_logical_number(p):
    'logical : NUMBER'
    p[0] = p[1]  # Permite usar números en expresiones lógicas

def p_error(p):
    print("Expresión inválida")
    if p:  
        parser.restart()  # Reiniciar el parser para evitar bucles infinitos
    exit(1)

# Construcción del parser
parser = yacc.yacc()

# 📌 **Ejecutar el analizador**
while True:
    try:
        entrada = input("Ingresa una expresión aritmética y lógica combinada: ")
        if not entrada.strip():
            continue  # Evita procesar entradas vacías
        resultado = parser.parse(entrada)
        if resultado is not None:  # Solo imprimir si hay un resultado válido
            print("Expresión válida")
    except Exception:
        print("Expresión inválida")
