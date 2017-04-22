%{
	#include<stdio.h>
	#include "y.tab.h"
	extern int yyparse();
	extern int yyerror(char* e);
	extern int yylex();

%}

%token NUM
%token VAR
%token OP
%token ASG
%start s

%%

s : VAR ASG exp {
	printf("Valid syntax\n");
	exit(0);
}

exp :	exp OP exp |
		exp OP VAR |
		NUM OP NUM |
		VAR OP VAR |
		VAR OP NUM |
		NUM OP VAR
		VAR |
		NUM |
		s
;
%%

int main()
{
	yyparse();
}

extern int yyerror(char* e)
{
	printf("Syntax error!");
}
		