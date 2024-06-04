# Generated from Expr.g4 by ANTLR 4.13.1
from Iuliana import LinkedList
from Iuliana import Stack
from Iuliana import Queue
from Iuliana import Array
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):
    class variable:
        def __init__(self, name):
            self.name = name
            self.value = None
            self.type = None

        def __str__(self):
            return f"{self.name} = {self.value} ({self.type})"

    def __init__(self):
        self.variables = []
        self.types = ['int', 'float', 'char', 'string', 'boolean', 'array', 'linkedlist', 'stack', 'queue']
        self.current_variable = None

    def add_variable(self, variable):
        for var in self.variables:
            if var.name == variable.name:
                var.value = variable.value
                var.type = variable.type
                return

        self.variables.append(variable)

    def get_var(self, name):
        for variable in self.variables:
            if variable.name == name:
                return variable
        return None

    def get_var_value(self, var):
        if var.INT():
            return int(var.INT().getText())
        elif var.FLOAT():
            return float(var.FLOAT().getText())
        elif var.CHAR():
            return var.CHAR().getText()
        elif var.STRING():
            return var.STRING().getText()
        elif var.BOOL():
            return var.BOOL().getText() == 'TRUE'
        else:
            raise Exception("Invalid type")

    def get_type(self, var):
        if var.INT():
            return 'int'
        elif var.FLOAT():
            return 'float'
        elif var.CHAR():
            return 'char'
        elif var.STRING():
            return 'string'
        elif var.BOOL():
            return 'boolean'
        else:
            raise Exception("Invalid type")

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Enter a parse tree produced by ExprParser#codeBlock.
    def enterCodeBlock(self, ctx:ExprParser.CodeBlockContext):
        pass

    # Exit a parse tree produced by ExprParser#codeBlock.
    def exitCodeBlock(self, ctx:ExprParser.CodeBlockContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#arrayDefinition.
    def enterArrayDefinition(self, ctx:ExprParser.ArrayDefinitionContext):
        if self.current_variable:
            self.current_variable.type = 'array'
            self.current_variable.value = Array()
            for child in ctx.children:
                if child in ctx.var():
                    self.current_variable.value.append(self.get_var_value(child))

                elif child in ctx.NAME():
                    var = self.get_var(child.getText())
                    if var:
                        self.current_variable.value.append(var.value)
                    else:
                        raise Exception("Variable not found")

    # Exit a parse tree produced by ExprParser#arrayDefinition.
    def exitArrayDefinition(self, ctx:ExprParser.ArrayDefinitionContext):
        pass


    # Enter a parse tree produced by ExprParser#linkedListDefinition.
    def enterLinkedListDefinition(self, ctx:ExprParser.LinkedListDefinitionContext):
        if self.current_variable:
            self.current_variable.type = 'linkedlist'
            self.current_variable.value = LinkedList()

    # Exit a parse tree produced by ExprParser#linkedListDefinition.
    def exitLinkedListDefinition(self, ctx:ExprParser.LinkedListDefinitionContext):
        pass


    # Enter a parse tree produced by ExprParser#stackDefinition.
    def enterStackDefinition(self, ctx:ExprParser.StackDefinitionContext):
        size = None
        if ctx.NAME():
            var = self.get_var(ctx.NAME().getText())
            if var and var.type == 'int':
                size = var.value
            else:
                raise Exception("Variable not found")

        if ctx.INT():
            size = int(ctx.INT().getText())

        if self.current_variable and size:
            self.current_variable.type = 'stack'
            self.current_variable.value = Stack(size)

    # Exit a parse tree produced by ExprParser#stackDefinition.
    def exitStackDefinition(self, ctx:ExprParser.StackDefinitionContext):
        pass


    # Enter a parse tree produced by ExprParser#queueDefinition.
    def enterQueueDefinition(self, ctx:ExprParser.QueueDefinitionContext):
        size = None
        if ctx.NAME():
            var = self.get_var(ctx.NAME().getText())
            if var and var.type == 'int':
                size = var.value
            else:
                raise Exception("Variable not found")

        if ctx.INT():
            size = int(ctx.INT().getText())

        if self.current_variable and size:
            self.current_variable.type = 'queue'
            self.current_variable.value = Queue(size)

    # Exit a parse tree produced by ExprParser#queueDefinition.
    def exitQueueDefinition(self, ctx:ExprParser.QueueDefinitionContext):
        pass


    # Enter a parse tree produced by ExprParser#variableAssignment.
    def enterVariableAssignment(self, ctx:ExprParser.VariableAssignmentContext):
        var_name = ctx.NAME()[0].getText()
        var = self.get_var(var_name)
        if var:
            self.current_variable = var
        else:
            self.current_variable = self.variable(var_name)

        if ctx.var():
            if ctx.var().INT():
                self.current_variable.value = int(ctx.var().INT().getText())
                self.current_variable.type = 'int'
            elif ctx.var().FLOAT():
                self.current_variable.value = float(ctx.var().FLOAT().getText())
                self.current_variable.type = 'float'
            elif ctx.var().CHAR():
                self.current_variable.value = ctx.var().CHAR().getText()
                self.current_variable.type = 'char'
            elif ctx.var().STRING():
                self.current_variable.value = ctx.var().STRING().getText()
                self.current_variable.type = 'string'
            elif ctx.var().BOOL():
                self.current_variable.value = ctx.var().BOOL().getText() == 'TRUE'
                self.current_variable.type = 'boolean'
            else:
                raise Exception("Invalid type")

        elif len(ctx.NAME()) == 2:
            var = self.get_var(ctx.NAME()[1].getText())
            if var:
                self.current_variable.value = var.value
                self.current_variable.type = var.type
            else:
                raise Exception("Variable not found")

    # Exit a parse tree produced by ExprParser#variableAssignment.
    def exitVariableAssignment(self, ctx:ExprParser.VariableAssignmentContext):
        self.add_variable(self.current_variable)
        self.current_variable = None


    # Enter a parse tree produced by ExprParser#arrayStatement.
    def enterArrayStatement(self, ctx:ExprParser.ArrayStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayStatement.
    def exitArrayStatement(self, ctx:ExprParser.ArrayStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#linkedListStatement.
    def enterLinkedListStatement(self, ctx:ExprParser.LinkedListStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#linkedListStatement.
    def exitLinkedListStatement(self, ctx:ExprParser.LinkedListStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#stackStatement.
    def enterStackStatement(self, ctx:ExprParser.StackStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#stackStatement.
    def exitStackStatement(self, ctx:ExprParser.StackStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#queueStatement.
    def enterQueueStatement(self, ctx:ExprParser.QueueStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#queueStatement.
    def exitQueueStatement(self, ctx:ExprParser.QueueStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#printStatement.
    def enterPrintStatement(self, ctx:ExprParser.PrintStatementContext):
        var_name = ctx.NAME().getText()
        var = self.get_var(var_name)

        if not var:
            raise Exception("Variable not found")

        print(var.value)

    # Exit a parse tree produced by ExprParser#printStatement.
    def exitPrintStatement(self, ctx:ExprParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#sortArray.
    def enterSortArray(self, ctx:ExprParser.SortArrayContext):
        order = 'DESCENDING' in ctx.getText()
        print(order)
        var_name = ctx.NAME().getText()
        var = self.get_var(var_name)

        if not var:
            raise Exception("Variable not found")

        var.value.sort(reverse=order)

    # Exit a parse tree produced by ExprParser#sortArray.
    def exitSortArray(self, ctx:ExprParser.SortArrayContext):
        pass


    # Enter a parse tree produced by ExprParser#insert.
    def enterInsert(self, ctx:ExprParser.InsertContext):
        if len(ctx.NAME()) == 2:
            var_name = ctx.NAME()[1].getText()
            assigned_var = self.get_var(ctx.NAME()[0].getText())

            if not assigned_var:
                raise Exception("Variable not found")

            value = assigned_var.value

        else:
            var_name = ctx.NAME()[0].getText()
            value = self.get_var_value(ctx.var())

        var = self.get_var(var_name)

        if not var:
            raise Exception("Variable not found")

        var.value.insert(value)

    # Exit a parse tree produced by ExprParser#insert.
    def exitInsert(self, ctx:ExprParser.InsertContext):
        pass


    # Enter a parse tree produced by ExprParser#delete.
    def enterDelete(self, ctx:ExprParser.DeleteContext):
        if len(ctx.NAME()) == 2:
            var_name = ctx.NAME()[1].getText()
            assigned_var = self.get_var(ctx.NAME()[0].getText())

            if not assigned_var:
                raise Exception("Variable not found")

            value = assigned_var.value

        else:
            var_name = ctx.NAME()[0].getText()
            value = self.get_var_value(ctx.var())

        var = self.get_var(var_name)

        if not var:
            raise Exception("Variable not found")

        var.value.remove(value)

    # Exit a parse tree produced by ExprParser#delete.
    def exitDelete(self, ctx:ExprParser.DeleteContext):
        pass


    # Enter a parse tree produced by ExprParser#search.
    def enterSearch(self, ctx:ExprParser.SearchContext):
        if len(ctx.NAME()) == 2:
            var_name = ctx.NAME()[1].getText()
            assigned_var = self.get_var(ctx.NAME()[0].getText())

            if not assigned_var:
                raise Exception("Variable not found")

            value = assigned_var.value
            type = assigned_var.type

        else:
            var_name = ctx.NAME()[0].getText()
            value = self.get_var_value(ctx.var())
            type = self.get_type(ctx.var())

        var = self.get_var(var_name)

        if not var:
            raise Exception("Variable not found")

        if self.current_variable:
            self.current_variable.type = type
            self.current_variable.value = var.value.search(value)

    # Exit a parse tree produced by ExprParser#search.
    def exitSearch(self, ctx:ExprParser.SearchContext):
        pass


    # Enter a parse tree produced by ExprParser#insertAt.
    def enterInsertAt(self, ctx:ExprParser.InsertAtContext):
        pass

    # Exit a parse tree produced by ExprParser#insertAt.
    def exitInsertAt(self, ctx:ExprParser.InsertAtContext):
        pass


    # Enter a parse tree produced by ExprParser#pushStack.
    def enterPushStack(self, ctx:ExprParser.PushStackContext):
        if len(ctx.NAME()) == 2:
            var_name = ctx.NAME()[1].getText()
            assigned_var = self.get_var(ctx.NAME()[0].getText())

            if not assigned_var:
                raise Exception("Variable not found")

            value = assigned_var.value

        else:
            var_name = ctx.NAME()[0].getText()
            value = self.get_var_value(ctx.var())

        var = self.get_var(var_name)

        if not var:
            raise Exception("Variable not found")

        var.value.push(value)

    # Exit a parse tree produced by ExprParser#pushStack.
    def exitPushStack(self, ctx:ExprParser.PushStackContext):
        pass


    # Enter a parse tree produced by ExprParser#popStack.
    def enterPopStack(self, ctx:ExprParser.PopStackContext):
        var_name = ctx.NAME().getText()
        var = self.get_var(var_name)
        value = var.value.pop()
        type = None

        if isinstance(value, int):
            type = 'int'
        elif isinstance(value, float):
            type = 'float'
        elif isinstance(value, str):
            if len(value) == 1:
                type = 'char'
            else:
                type = 'string'
        elif isinstance(value, bool):
            type = 'boolean'
        else:
            raise Exception("Invalid type")

        if not var:
            raise Exception("Variable not found")

        if self.current_variable:
            self.current_variable.type = type
            self.current_variable.value = value

    # Exit a parse tree produced by ExprParser#popStack.
    def exitPopStack(self, ctx:ExprParser.PopStackContext):
        pass


    # Enter a parse tree produced by ExprParser#enqueueQueue.
    def enterEnqueueQueue(self, ctx:ExprParser.EnqueueQueueContext):
        if len(ctx.NAME()) == 2:
            var_name = ctx.NAME()[1].getText()
            assigned_var = self.get_var(ctx.NAME()[0].getText())

            if not assigned_var:
                raise Exception("Variable not found")

            value = assigned_var.value

        else:
            var_name = ctx.NAME()[0].getText()
            value = self.get_var_value(ctx.var())

        var = self.get_var(var_name)

        if not var:
            raise Exception("Variable not found")

        var.value.enqueue(value)

    # Exit a parse tree produced by ExprParser#enqueueQueue.
    def exitEnqueueQueue(self, ctx:ExprParser.EnqueueQueueContext):
        pass


    # Enter a parse tree produced by ExprParser#dequeueQueue.
    def enterDequeueQueue(self, ctx:ExprParser.DequeueQueueContext):
        var_name = ctx.NAME().getText()
        var = self.get_var(var_name)
        value = var.value.dequeue()
        type = None

        if isinstance(value, int):
            type = 'int'
        elif isinstance(value, float):
            type = 'float'
        elif isinstance(value, str):
            if len(value) == 1:
                type = 'char'
            else:
                type = 'string'
        elif isinstance(value, bool):
            type = 'boolean'
        else:
            raise Exception("Invalid type")

        if not var:
            raise Exception("Variable not found")

        if self.current_variable:
            self.current_variable.type = type
            self.current_variable.value = value

    # Exit a parse tree produced by ExprParser#dequeueQueue.
    def exitDequeueQueue(self, ctx:ExprParser.DequeueQueueContext):
        pass


    # Enter a parse tree produced by ExprParser#isFull.
    def enterIsFull(self, ctx:ExprParser.IsFullContext):
        var_name = ctx.NAME().getText()
        var = self.get_var(var_name)

        if not var:
            raise Exception("Variable not found")

        if self.current_variable:
            self.current_variable.type = 'boolean'
            self.current_variable.value = var.value.is_full()

    # Exit a parse tree produced by ExprParser#isFull.
    def exitIsFull(self, ctx:ExprParser.IsFullContext):
        pass


    # Enter a parse tree produced by ExprParser#isEmpty.
    def enterIsEmpty(self, ctx:ExprParser.IsEmptyContext):
        var_name = ctx.NAME().getText()
        var = self.get_var(var_name)

        if not var:
            raise Exception("Variable not found")

        if self.current_variable:
            self.current_variable.type = 'boolean'
            self.current_variable.value = var.value.is_empty()

    # Exit a parse tree produced by ExprParser#isEmpty.
    def exitIsEmpty(self, ctx:ExprParser.IsEmptyContext):
        pass


    # Enter a parse tree produced by ExprParser#peek.
    def enterPeek(self, ctx:ExprParser.PeekContext):
        var_name = ctx.NAME().getText()
        var = self.get_var(var_name)

        if not var:
            raise Exception("Variable not found")

        if self.current_variable:
            self.current_variable.type = var.type
            self.current_variable.value = var.value.peek()

    # Exit a parse tree produced by ExprParser#peek.
    def exitPeek(self, ctx:ExprParser.PeekContext):
        pass


    # Enter a parse tree produced by ExprParser#var.
    def enterVar(self, ctx:ExprParser.VarContext):
        pass

    # Exit a parse tree produced by ExprParser#var.
    def exitVar(self, ctx:ExprParser.VarContext):
        pass



del ExprParser