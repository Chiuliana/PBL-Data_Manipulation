grammar Expr;

// Parser rules
program: statement*;

statement: arrayStatement | linkedListStatement | stackStatement | queueStatement;

arrayStatement: 'ARRAY' '[' INT (',' INT)* ']' (insertArray | deleteArray | searchArray | sortArray)? ;

linkedListStatement: 'LINKEDLIST' (insertLinkedList | deleteLinkedList | searchLinkedList)? ;

stackStatement: 'STACK' (pushStack | popStack | topStack | isEmptyStack)? ;

queueStatement: 'QUEUE' (enqueueQueue | dequeueQueue | peekQueue | isFullQueue | isNullQueue)? ;

// Array operations
insertArray: 'INSERT' '[' INT ']' 'INTO' 'ARRAY' '[' INT ']' ';';
deleteArray: 'DELETE' 'FROM' 'ARRAY' '[' INT ']' ';';
searchArray: 'SEARCH' 'ARRAY' '[' INT ']' 'FOR' INT ';';
sortArray: 'SORT' 'ARRAY' '[' INT ']' ('ASCENDING' | 'DESCENDING') ';'; // Corrected ascending/descending

// Linked list operations
insertLinkedList: 'INSERT' 'INTO' 'LINKEDLIST' '[' INT ']' 'VALUE' INT ';';
deleteLinkedList: 'DELETE' 'FROM' 'LINKEDLIST' '[' INT ']' ';';
searchLinkedList: 'SEARCH' 'LINKEDLIST' '[' INT ']' 'FOR' INT ';';

// Stack operations
pushStack: 'PUSH' INT 'TO' 'STACK' ';';
popStack: 'POP' 'FROM' 'STACK' ';';
topStack: 'TOP' 'ELEMENT' 'OF' 'STACK' ';';
isEmptyStack: 'CHECK' 'IF' 'STACK' 'IS' 'EMPTY' ';';

// Queue operations
enqueueQueue: 'ENQUEUE' INT 'TO' 'QUEUE' ';';
dequeueQueue: 'DEQUEUE' 'FROM' 'QUEUE' ';';
peekQueue: 'PEEK' 'FRONT' 'ELEMENT' 'OF' 'QUEUE' ';';
isFullQueue: 'CHECK' 'IF' 'QUEUE' 'IS' 'FULL' ';';
isNullQueue: 'CHECK' 'IF' 'QUEUE' 'IS' 'EMPTY' ';';

// Lexer rules
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;

// Comments
COMMENT: '//' ~[\r\n]* -> skip;