%{
#include "parser.tab.h"
#include <string.h>
#include <stdlib.h>
%}
%%
"func" { return FUNC; }
[0-9]+ { yylval.str = strdup(yytext); return ID; }  // ← esta línea es clave
[a-zA-Z_][a-zA-Z0-9_]* { yylval.str = strdup(yytext); return ID; }
"(" { return PARIZQ; }
")" { return PARDER; }
";" { return PUNTOYCOMA; }
"," { return COMA; }
[ \t\r\n]+ ;  
. { return yytext[0]; }
%%
int yywrap() {
    return 1;
}
