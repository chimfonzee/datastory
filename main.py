from antlr4 import *
from DataStoryLexer import DataStoryLexer
from DataStoryParser import DataStoryParser
from DataStoryListener import DataStoryListener

input_stream = FileStream('test3.txt')
lexer = DataStoryLexer(input_stream)
stream = CommonTokenStream(lexer)

walker = ParseTreeWalker()
parser = DataStoryParser(stream)
tree = parser.prog()

def print_tree(tree, lev):
    print((" " * lev) + "|- " + str(tree))
    if not isinstance(tree, TerminalNode):
        for c in tree.getChildren():
            print_tree(c, lev + 1)

print_tree(tree, 0)