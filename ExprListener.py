# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#create_table_statement.
    def enterCreate_table_statement(self, ctx:ExprParser.Create_table_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#create_table_statement.
    def exitCreate_table_statement(self, ctx:ExprParser.Create_table_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#drop_table_statement.
    def enterDrop_table_statement(self, ctx:ExprParser.Drop_table_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#drop_table_statement.
    def exitDrop_table_statement(self, ctx:ExprParser.Drop_table_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#add_column_statement.
    def enterAdd_column_statement(self, ctx:ExprParser.Add_column_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#add_column_statement.
    def exitAdd_column_statement(self, ctx:ExprParser.Add_column_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#remove_column_statement.
    def enterRemove_column_statement(self, ctx:ExprParser.Remove_column_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#remove_column_statement.
    def exitRemove_column_statement(self, ctx:ExprParser.Remove_column_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#column_def_list.
    def enterColumn_def_list(self, ctx:ExprParser.Column_def_listContext):
        pass

    # Exit a parse tree produced by ExprParser#column_def_list.
    def exitColumn_def_list(self, ctx:ExprParser.Column_def_listContext):
        pass


    # Enter a parse tree produced by ExprParser#column_def.
    def enterColumn_def(self, ctx:ExprParser.Column_defContext):
        pass

    # Exit a parse tree produced by ExprParser#column_def.
    def exitColumn_def(self, ctx:ExprParser.Column_defContext):
        pass


    # Enter a parse tree produced by ExprParser#data_type.
    def enterData_type(self, ctx:ExprParser.Data_typeContext):
        pass

    # Exit a parse tree produced by ExprParser#data_type.
    def exitData_type(self, ctx:ExprParser.Data_typeContext):
        pass


    # Enter a parse tree produced by ExprParser#insert_statement.
    def enterInsert_statement(self, ctx:ExprParser.Insert_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#insert_statement.
    def exitInsert_statement(self, ctx:ExprParser.Insert_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#update_statement.
    def enterUpdate_statement(self, ctx:ExprParser.Update_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#update_statement.
    def exitUpdate_statement(self, ctx:ExprParser.Update_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#delete_statement.
    def enterDelete_statement(self, ctx:ExprParser.Delete_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#delete_statement.
    def exitDelete_statement(self, ctx:ExprParser.Delete_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#select_statement.
    def enterSelect_statement(self, ctx:ExprParser.Select_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#select_statement.
    def exitSelect_statement(self, ctx:ExprParser.Select_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#where_clause.
    def enterWhere_clause(self, ctx:ExprParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by ExprParser#where_clause.
    def exitWhere_clause(self, ctx:ExprParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by ExprParser#join_clause.
    def enterJoin_clause(self, ctx:ExprParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by ExprParser#join_clause.
    def exitJoin_clause(self, ctx:ExprParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by ExprParser#condition.
    def enterCondition(self, ctx:ExprParser.ConditionContext):
        pass

    # Exit a parse tree produced by ExprParser#condition.
    def exitCondition(self, ctx:ExprParser.ConditionContext):
        pass


    # Enter a parse tree produced by ExprParser#logical_operator.
    def enterLogical_operator(self, ctx:ExprParser.Logical_operatorContext):
        pass

    # Exit a parse tree produced by ExprParser#logical_operator.
    def exitLogical_operator(self, ctx:ExprParser.Logical_operatorContext):
        pass


    # Enter a parse tree produced by ExprParser#expression.
    def enterExpression(self, ctx:ExprParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#expression.
    def exitExpression(self, ctx:ExprParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#value.
    def enterValue(self, ctx:ExprParser.ValueContext):
        pass

    # Exit a parse tree produced by ExprParser#value.
    def exitValue(self, ctx:ExprParser.ValueContext):
        pass


    # Enter a parse tree produced by ExprParser#identifier_list.
    def enterIdentifier_list(self, ctx:ExprParser.Identifier_listContext):
        pass

    # Exit a parse tree produced by ExprParser#identifier_list.
    def exitIdentifier_list(self, ctx:ExprParser.Identifier_listContext):
        pass


    # Enter a parse tree produced by ExprParser#value_list.
    def enterValue_list(self, ctx:ExprParser.Value_listContext):
        pass

    # Exit a parse tree produced by ExprParser#value_list.
    def exitValue_list(self, ctx:ExprParser.Value_listContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment_list.
    def enterAssignment_list(self, ctx:ExprParser.Assignment_listContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment_list.
    def exitAssignment_list(self, ctx:ExprParser.Assignment_listContext):
        pass


    # Enter a parse tree produced by ExprParser#selection.
    def enterSelection(self, ctx:ExprParser.SelectionContext):
        pass

    # Exit a parse tree produced by ExprParser#selection.
    def exitSelection(self, ctx:ExprParser.SelectionContext):
        pass


    # Enter a parse tree produced by ExprParser#numerical_literal.
    def enterNumerical_literal(self, ctx:ExprParser.Numerical_literalContext):
        pass

    # Exit a parse tree produced by ExprParser#numerical_literal.
    def exitNumerical_literal(self, ctx:ExprParser.Numerical_literalContext):
        pass


    # Enter a parse tree produced by ExprParser#string_literal.
    def enterString_literal(self, ctx:ExprParser.String_literalContext):
        pass

    # Exit a parse tree produced by ExprParser#string_literal.
    def exitString_literal(self, ctx:ExprParser.String_literalContext):
        pass


    # Enter a parse tree produced by ExprParser#boolean_literal.
    def enterBoolean_literal(self, ctx:ExprParser.Boolean_literalContext):
        pass

    # Exit a parse tree produced by ExprParser#boolean_literal.
    def exitBoolean_literal(self, ctx:ExprParser.Boolean_literalContext):
        pass



del ExprParser