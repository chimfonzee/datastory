grammar DataStory;
prog: func* expr* EOF ;

func: FUNC ID LPAREN (DTYPE ID (COMMA DTYPE ID)*)? RPAREN LCURL expr* (RET (val | condition)?)? RCURL ;

expr: initialize
    | assignment
    | control
    | loop
    | output
    | COMMENT
    | func_call
    | draw_call ;

draw_call: DRAW LPAREN val COMMA val COMMA val COMMA STR RPAREN ;
initialize: DTYPE ID ASSIGN_OP (val | condition) ;
assignment: ID ASSIGN_OP (val | condition) ;

control: IF LPAREN condition RPAREN LCURL expr* RCURL elif* else? ;
elif: ELIF LPAREN condition RPAREN LCURL expr* RCURL ;
else: ELSE LCURL expr* RCURL ;

loop: FOR LPAREN (initialize | assignment) COMMA condition COMMA assignment RPAREN LCURL expr* RCURL
    | WHILE LPAREN condition RPAREN LCURL expr* RCURL ;

output: PRINT LPAREN (val | condition) RPAREN ;

val: LPAREN val RPAREN
    | val POW_OP val
    | val (MUL_OP | DIV_OP) val
    | val (ADD_OP | SUB_OP) val
    | val index
    | val AND_DOP val
    | val OR_DOP val
    | input_call
    | func_call
    | read_call
    | ID
    | STR
    | INT
    | FLOAT ;
condition: LPAREN condition RPAREN
    | NOT_OP condition
    | condition AND_OP condition
    | condition OR_OP condition
    | val LT_OP val
    | val GT_OP val
    | val LTEQ_OP val
    | val GTEQ_OP val
    | val EQ_OP val
    | val NEQ_OP val
    | condition index
    | func_call
    | ID
    | TRUE
    | FALSE ;
index: LBRACK (val | val COLON val) RBRACK ;
func_call: ID LPAREN (val (COMMA val)*)? RPAREN ;
input_call: INPUT LPAREN val RPAREN ;
read_call: READ LPAREN val COMMA condition RPAREN ;

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
    | 'column'
    | 'string'
    | 'float'
    | 'int'
    | 'bool' ;
READ: 'read' ;
INT: [0-9][0-9]* ;
FLOAT: [0-9]+.[0-9]+ (SCIENTIFIC [1-9][0-9]*)? ;
SCIENTIFIC: 'E' [+-] ;
STR: '"' ~[\n"]* '"' ;
TRUE: 'true' ;
FALSE: 'false' ;
ADD_OP: '+' ;
SUB_OP: '-' ;
MUL_OP: '*' ;
DIV_OP: '/' ;
POW_OP: '^' ;
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

WS: (' ' | '\t')+ -> skip ;
NEWLINE: [\r\n]+ -> skip ;
COMMENT: '#' ~( '\r' | '\n' )* ;
