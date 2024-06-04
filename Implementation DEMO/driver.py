from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener

def main():
    input_stream = FileStream("input.txt")
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.program()
    listener = ExprListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)





if __name__ == '__main__':
    main()