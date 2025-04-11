%{
#include <stdio.h>
%}

%%
"int"|"return"        { printf("KEYWORD %s\n", yytext); }
"//".*                { printf("COMMENT\n"); }
"/*"([^*]|\*+[^*/])*\*+"/" { printf("COMMENT\n"); }
\"([^\"\n])*\"        { printf("STRING\n"); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("IDENTIFIER %s\n", yytext); }
[0-9]+               { printf("NUMBER %s\n", yytext); }
[+\-*/=]             { printf("OPERATOR %s\n", yytext); }
[\(\)\{\}\;\,]       { printf("DELIMITER %s\n", yytext); }
[ \t\n]              { /* Ignorar espacios en blanco y saltos de línea */ }
.                    { printf("UNKNOWN %s\n", yytext); }
%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
