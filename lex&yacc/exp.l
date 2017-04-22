%{
	#include<stdio.h>
	#include "y.tab.h"
	extern int yylval;
	extern int yyerror(char* e);
%}

let [a-zA-Z]+
dig [0-9]+

%%

{dig}+ { return NUM;}
{let}({let}|{dig})* { return VAR;}
[+|-|*|/] { return OP;}
[=] { return ASG;}

%% 
extern int yywrap()
{
	return 1;
}


