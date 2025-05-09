%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int yylex(void); // Declaración de la función léxica
int yyerror(char *s) { 
    printf("Error: %s\n", s); 
    return 0; 
} // Manejador de errores sintácticos

#define MAX_ID 100 // Tamaño máximo de la tabla de símbolos
char *tabla[MAX_ID]; // Arreglo para nombres de variables
int tipos[MAX_ID]; // Arreglo para guardar el tipo de cada variable
int ntabla = 0; // Contador de identificadores registrados

void agregar_tipo(char *id, int tipo) {
    for (int i = 0; i < ntabla; i++)
        if (strcmp(tabla[i], id) == 0) return; // No se vuelve a declarar
    tabla[ntabla] = strdup(id); // Copia el nombre del identificador
    tipos[ntabla++] = tipo; // Registra su tipo (en este caso 0)
}

int buscar_tipo(char *id) {
    for (int i = 0; i < ntabla; i++)
        if (strcmp(tabla[i], id) == 0) return tipos[i]; // Retorna tipo si lo encuentra
    return -1; // Retorna -1 si no está registrado
}

int existe(char *id) {
    for (int i = 0; i < ntabla; i++)
        if (strcmp(tabla[i], id) == 0) return 1; // Verifica existencia del identificador
    return 0; // No encontrado
}
%}

%union { char *str; } // Asociación del tipo de dato para los tokens

%token <str> ID // Token para identificadores
%token INT IGUAL PUNTOYCOMA // Tokens para palabra clave, '=' y ';'

%%

programa:
    sentencias
;

sentencias:
    sentencia
  | sentencias sentencia
;

sentencia:
    INT ID PUNTOYCOMA { agregar_tipo($2, 0); }
  | ID IGUAL ID PUNTOYCOMA {
        if (!existe($1) || !existe($3))
            printf("Error: identificador no declarado\n");
        else if (buscar_tipo($1) != buscar_tipo($3))
            printf("Error: tipos incompatibles\n");
    }
;

%%

int main() {
    return yyparse();
}