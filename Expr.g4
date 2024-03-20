grammar Expr;
//Main program structure
program : statement+;

//Statements definition
statement: create_table_statement | drop_table_statement | add_column_statement | remove_column_statement | insert_statement | update_statement| delete_statement | select_statement;

//Table definition
create_table_statement: 'create_table' IDENTIFIER '(' column_def_list+ ')';
drop_table_statement: 'drop_table' IDENTIFIER;
add_column_statement: 'add_column' IDENTIFIER '(' column_def ')';
remove_column_statement: 'remove_column' IDENTIFIER IDENTIFIER;

//Column definition
column_def_list: column_def ','*;
column_def: IDENTIFIER data_type;


//Data Types
data_type: 'int' | 'string' | 'bool' | 'date';

//Data Manipulation
insert_statement: 'insert_into' IDENTIFIER '(' identifier_list ')' 'values' '(' value_list ')';
update_statement: 'update' IDENTIFIER 'set' assignment_list where_clause;
delete_statement: 'delete_from' IDENTIFIER where_clause;
select_statement: 'select' selection 'from' IDENTIFIER join_clause where_clause;

//Clauses --> WHERE, JOIN & Conditions
where_clause: 'where' condition;
join_clause: 'join' IDENTIFIER 'on' condition;
condition: expression logical_operator expression;
logical_operator: 'and' | 'or';

//Expressions & Values
expression: IDENTIFIER | value;
value: numerical_literal | string_literal | boolean_literal | 'null';
identifier_list: IDENTIFIER ','*;
value_list: value ','*;
assignment_list: IDENTIFIER '=' value ;
selection: '*' | identifier_list;

//Literals
numerical_literal: '-' DIGIT+;
string_literal: '"' ~('\\' | '"')* '"';
boolean_literal: 'true' | 'false';

//Tokens
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
DIGIT: [0-9];
NEWLINE : [\r\n]+ -> skip;
SPACE : ' ' -> skip;