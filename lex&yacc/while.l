%{
	#include "y.tab.h"
	#include<stdio.h>
	extern int yyerror(char* e);
	extern int yylval;
%}
let [a-zA-Z]+
dig [0-9]+
condn (<=|>=|<|>|==|!=)
%%

"while"|"if" { return KW;}
{dig}+ { return NUM;}
{let}({let}|{dig})* { return VAR;}
[(]* { return OB;}
[)]* { return CB;}
[{]* { return OCB;}
[}]* { return CCB;}
[;] { return SC;}
[ + | - | * | / | %]+ { return OP;}
[=] { return ASG;}
{condn} { return COND;}

%%

extern int yywrap(){
	return 1;
}



