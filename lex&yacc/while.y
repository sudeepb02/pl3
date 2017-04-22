%{
	#include<stdio.h>
	extern int yyparse();
	extern int yylex();
	extern int yyerror(char* e);
%}

%token NUM
%token VAR
%token COND
%token KW
%token OB
%token CB
%token OCB
%token CCB
%token SC
%token OP
%token ASG
%start S
%%

S : KW OB test CB OCB stmt CCB {
	printf("Valid Syntax\n");
}

test : 	VAR COND VAR |
	VAR COND NUM |
	VAR |
	'1' |
	'0'

stmt :	exp SC | stmt stmt | S

exp : 	VAR ASG exp |
	exp OP exp |
	VAR OP VAR |
	NUM OP NUM |
	VAR OP NUM |
	VAR |
	NUM

%%
int main()
{
	yyparse();
}

extern int yyerror(char* e)
{
	printf("Syntax error!\n");
}

