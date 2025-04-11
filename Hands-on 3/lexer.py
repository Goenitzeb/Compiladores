import ply.lex as lex

# Definir los tokens
tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN')

# Expresiones regulares para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# Expresión regular para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convertir el valor a entero
    return t

# Ignorar espacios en blanco
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()
