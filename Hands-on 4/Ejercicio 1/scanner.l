%{
#include "parser.tab.h" // Se incluye el encabezado generado por
#include <string.h> // Para manejo de cadenas (strdup)
#include <stdlib.h> // Para funciones estándar
%}
%%
"int" { return INT; } // Re
[a-zA-Z_][a-zA-Z0-9_]* { yylval.str = strdup(yytext); return ID; } // Rec
";" { return PUNTOYCOMA; } // Re
[ \t\n]+ ; // I
. { return yytext[0]; } // Re
%%

int yywrap() {
    return 1;
}