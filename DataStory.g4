grammar DataStory;
prog: func* expr* EOF ;

func: FUNC ID LPAREN arglist? RPAREN LCURL expr* (RET (val | condition))? RCURL ;
arglist: DTYPE ID COMMA arglist | DTYPE ID ;

expr: initialize
    | assignment
    | control
    | loop
    | output
    | COMMENT 
    | func_call
    | print_call
    | draw_call ;

print_call: PRINT LPAREN val RPAREN ;
draw_call: DRAW LPAREN val COMMA val COMMA val COMMA STR RPAREN ;
initialize: DTYPE assignment ;
assignment: ID ASSIGN_OP (val | condition) ;

control: IF LPAREN condition RPAREN LCURL expr* RCURL elif* else? ;
elif: ELIF LPAREN condition RPAREN LCURL expr* RCURL ;
else: ELSE LCURL expr* RCURL ;

loop: FOR LPAREN initialize COMMA condition COMMA assignment RPAREN LCURL expr* RCURL
    | WHILE LPAREN condition RPAREN LCURL expr* RCURL ;

output: PRINT LPAREN (val | condition) RPAREN ;

val: LPAREN val RPAREN
    | val ADD_OP val
    | val SUB_OP val
    | val MUL_OP val
    | val DIV_OP val
    | val AND_DOP val
    | val OR_DOP val
    | func_call
    | ID slicing*
    | STR
    | INT
    | FLOAT
    | INPUT LPAREN STR RPAREN
    | draw_call ;
condition: NOT_OP condition
    | LPAREN condition RPAREN
    | condition AND_OP condition
    | condition OR_OP condition
    | val LT_OP val
    | val GT_OP val
    | val LTEQ_OP val
    | val GTEQ_OP val
    | val EQ_OP val
    | val NEQ_OP val
    | func_call
    | ID slicing*
    | TRUE
    | FALSE ;
slicing: LBRACK val RBRACK
    | LBRACK val COLON val RBRACK ;
func_call: ID LPAREN idlist RPAREN ;
idlist: ID COMMA idlist | ID ;

FOR: 'for' ;
IF: 'if' ;
ELSE: 'else' ;
ELIF: 'elif' ;
NULL: 'null' ;
WHILE: 'while' ;
FUNC: 'func' ;
RET: 'return' ;
PRINT: 'print' ;
DRAW: 'draw' ;
INPUT: 'input' ;
DTYPE: 'table'
    | 'chart'
    | 'dataset'
    | 'row'
    | 'column'
    | 'story'
    | 'string'
    | 'float'
    | 'int'
    | 'struct' ;
INT: [0-9][0-9]* ;
FLOAT: [0-9]+.[0-9]+ ;
STR: '"' ~["]* '"' ;
TRUE: 'true' ;
FALSE: 'false' ;
ADD_OP: '+' ;
SUB_OP: '-' ;
MUL_OP: '*' ;
DIV_OP: '/' ;
EQ_OP: '==' ;
NEQ_OP: '!=' ;
LTEQ_OP: '<=' ;
GTEQ_OP: '>=' ;
LT_OP: '<' ;
GT_OP: '>' ;
AND_DOP: '&' ;
OR_DOP: '|' ;
AND_OP: '&&' ;
OR_OP: '||' ;
NOT_OP: '!' ;
ASSIGN_OP: '=' ;
LPAREN: '(' ;
RPAREN: ')' ;
LCURL: '{' ;
RCURL: '}' ;
LBRACK: '[' ;
RBRACK: ']' ;
COMMA: ',' ;
COLON: ':' ;
ID: [A-Za-z][_A-Za-z0-9]* ;

WS : (' ' | '\t')+ -> skip ;
NEWLINE: [\r\n]+ -> skip ;
COMMENT: '#' ~( '\r' | '\n' )* ;
