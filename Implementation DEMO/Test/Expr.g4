grammar Expr;

// Parser rules
program: codeBlock+ EOF;

codeBlock: variableAssignment+ statement*;

statement: arrayStatement | linkedListStatement | stackStatement | queueStatement | printStatement;

arrayDefinition: 'ARRAY' '[' (var | NAME)* (',' (var | NAME))* ']';

linkedListDefinition: 'LINKEDLIST' '[' ']';

stackDefinition: 'STACK' '[' (INT | NAME) ']';

queueDefinition: 'QUEUE' '[' (INT | NAME) ']';

variableAssignment: NAME '=' arrayDefinition EOL
                  | NAME '=' linkedListDefinition EOL
                  | NAME '=' stackDefinition EOL
                  | NAME '=' queueDefinition EOL
                  | NAME '=' search
                  | NAME '=' popStack
                  | NAME '=' dequeueQueue
                  | NAME '=' peek
                  | NAME '=' isFull
                  | NAME '=' isEmpty
                  | NAME '=' var EOL
                  | NAME '=' NAME EOL;

arrayStatement: insert| insertAt | delete | search | sortArray ;

linkedListStatement: insert | delete | search ;

stackStatement: pushStack | popStack | peek | isFull | isEmpty ;

queueStatement: enqueueQueue | dequeueQueue | peek | isFull | isEmpty ;

printStatement: 'PRINT' NAME EOL;

// Array operations
sortArray: 'SORT' NAME ('ASCENDING' | 'DESCENDING') EOL; // Corrected ascending/descending

// Array and Linked list operations
insert: 'INSERT' '[' (var | NAME) ']' 'INTO' NAME EOL;
delete: 'DELETE' '[' (var | NAME) ']' 'FROM' NAME EOL;
search: 'SEARCH' '[' (var | NAME) ']' 'IN' NAME EOL;
insertAt: 'INSERT' '[' (var | NAME) ']' 'INTO' NAME 'AT' INT EOL;

// Stack operations
pushStack: 'PUSH' '[' (var | NAME) ']' 'INTO' NAME EOL;
popStack: 'POP' 'FROM' NAME EOL;

// Queue operations
enqueueQueue: 'ENQUEUE' '[' (var | NAME) ']' 'INTO' NAME EOL;
dequeueQueue: 'DEQUEUE' 'FROM' NAME EOL;

// Stack and Queue operations
isFull: NAME 'IS' 'FULL' EOL;
isEmpty: NAME 'IS' 'EMPTY' EOL;
peek: 'PEEK' NAME EOL;

// variableTypes
var: INT | FLOAT | CHAR | STRING | BOOL;

// Lexer rules
INT: [0-9]+;
FLOAT: [0-9][.][0-9]+;
CHAR: ['][a-zA-Z0-9]['];
STRING: ['][a-zA-Z0-9][a-zA-Z0-9]+['];
WS: [ \t\r\n]+ -> skip;
NAME: [a-zA-Z][a-zA-Z0-9_]*;
EOL: ';';
BOOL: 'TRUE' | 'FALSE';


// Comments
COMMENT: '//' ~[\r\n]* -> skip;