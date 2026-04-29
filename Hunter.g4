grammar Hunter;

program
    : statement* EOF
    ;

statement
    : assignStmt         NEWLINE
    | printStmt          NEWLINE
    | ifStmt
    | whileStmt
    | forStmt
    | returnStmt         NEWLINE
    | funcDef
    | exprStmt           NEWLINE
    | NEWLINE
    ;

// ── Assignments ──────────────────────────────
assignStmt
    : ID ASSIGN expr                                                         # SimpleAssign
    | ID PLUS_ASSIGN  expr                                                   # PlusAssign
    | ID MINUS_ASSIGN expr                                                   # MinusAssign
    | ID STAR_ASSIGN  expr                                                   # StarAssign
    | ID SLASH_ASSIGN expr                                                   # SlashAssign
    | ID LBRACKET expr RBRACKET ASSIGN expr                                  # IndexAssign
    | ID LBRACKET expr RBRACKET LBRACKET expr RBRACKET ASSIGN expr           # IndexAssign2D
    ;

// ── Print ────────────────────────────────────
printStmt
    : PRINT LPAREN exprList? RPAREN
    ;

// ── If / elif / else ─────────────────────────
ifStmt
    : IF expr COLON NEWLINE block
      elifClause*
      elseClause?
    ;

elifClause
    : ELIF expr COLON NEWLINE block
    ;

elseClause
    : ELSE COLON NEWLINE block
    ;

// ── While ────────────────────────────────────
whileStmt
    : WHILE expr COLON NEWLINE block
    ;

// ── For ──────────────────────────────────────
// ForIter acepta cualquier expresión después de IN,
// incluyendo variables, listas literales y accesos a índice.
forStmt
    : FOR ID IN expr COLON NEWLINE block
    ;

// ── Return ───────────────────────────────────
returnStmt
    : RETURN expr?
    ;

// ── Function definition ──────────────────────
funcDef
    : DEF ID LPAREN paramList? RPAREN COLON NEWLINE block
    ;

paramList
    : ID (COMMA ID)*
    ;

// ── Expression statement ─────────────────────
exprStmt
    : expr
    ;

// ── Indented block ───────────────────────────
block
    : INDENT statement+ DEDENT
    ;

// ─────────────────────────────────────────────
//  EXPRESSIONS
// ─────────────────────────────────────────────

exprList
    : expr (COMMA expr)*
    ;

expr
    : orExpr
    ;

orExpr
    : andExpr (OR andExpr)*
    ;

andExpr
    : notExpr (AND notExpr)*
    ;

notExpr
    : NOT notExpr
    | compareExpr
    ;

compareExpr
    : addExpr ( (EQ | NEQ | LT | LE | GT | GE) addExpr )*
    ;

addExpr
    : mulExpr ( (PLUS | MINUS) mulExpr )*
    ;

mulExpr
    : unaryExpr ( (STAR | SLASH | DOUBLESLASH | PERCENT) unaryExpr )*
    ;

unaryExpr
    : MINUS unaryExpr                           # UnaryMinus
    | PLUS  unaryExpr                           # UnaryPlus
    | powerExpr                                 # UnaryPass
    ;

powerExpr
    : primaryExpr (DOUBLESTAR primaryExpr)*
    ;

primaryExpr
    : INT_LIT                                                       # IntLit
    | FLOAT_LIT                                                     # FloatLit
    | STRING_LIT                                                    # StringLit
    | BOOL_LIT                                                      # BoolLit
    | NONE_LIT                                                      # NoneLit
    | RANGE LPAREN expr RPAREN                                      # RangeOne
    | RANGE LPAREN expr COMMA expr RPAREN                           # RangeTwo
    | RANGE LPAREN expr COMMA expr COMMA expr RPAREN                # RangeThree
    | ID LPAREN exprList? RPAREN                                    # FuncCall
    | ID LBRACKET expr RBRACKET LBRACKET expr RBRACKET              # IndexAccess2D
    | ID LBRACKET expr RBRACKET                                     # IndexAccess
    | ID                                                            # Identifier
    | LPAREN expr RPAREN                                            # Paren
    | listLit                                                       # ListExpr
    ;

listLit
    : LBRACKET exprList? RBRACKET
    ;

// ─────────────────────────────────────────────
//  LEXER RULES
// ─────────────────────────────────────────────

IF          : 'if'    ;
ELIF        : 'elif'  ;
ELSE        : 'else'  ;
WHILE       : 'while' ;
FOR         : 'for'   ;
IN          : 'in'    ;
DEF         : 'def'   ;
RETURN      : 'return';
PRINT       : 'print' ;
RANGE       : 'range' ;
AND         : 'and'   ;
OR          : 'or'    ;
NOT         : 'not'   ;
BOOL_LIT    : 'True' | 'False' ;
NONE_LIT    : 'None'  ;

PLUS        : '+'  ;
MINUS       : '-'  ;
STAR        : '*'  ;
SLASH       : '/'  ;
DOUBLESLASH : '//' ;
PERCENT     : '%'  ;
DOUBLESTAR  : '**' ;

ASSIGN      : '='  ;
PLUS_ASSIGN : '+=' ;
MINUS_ASSIGN: '-=' ;
STAR_ASSIGN : '*=' ;
SLASH_ASSIGN: '/=' ;

EQ          : '==' ;
NEQ         : '!=' ;
LT          : '<'  ;
LE          : '<=' ;
GT          : '>'  ;
GE          : '>=' ;

LPAREN      : '('  ;
RPAREN      : ')'  ;
LBRACKET    : '['  ;
RBRACKET    : ']'  ;
COMMA       : ','  ;
COLON       : ':'  ;

ID          : [a-zA-Z_][a-zA-Z0-9_]* ;

INT_LIT     : [0-9]+ ;
FLOAT_LIT   : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;
STRING_LIT  : '"'  (~["\\\r\n] | '\\' .)*  '"'
            | '\'' (~['\\\r\n] | '\\' .)* '\''
            ;

INDENT      : '<INDENT>'  ;
DEDENT      : '<DEDENT>'  ;

COMMENT     : '#' ~[\r\n]* -> skip ;
WS          : [ \t]+       -> skip ;
NEWLINE     : ('\r'? '\n' | '\r') ;
