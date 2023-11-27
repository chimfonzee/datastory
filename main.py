import sys

from antlr4 import *
from DataStoryLexer import DataStoryLexer
from DataStoryParser import DataStoryParser
from DataStoryListener import DataStoryListener
from DataStoryVisitor import DataStoryVisitor

def print_tree(tree, lev):
        print((" " * lev) + "|- " + str(tree))
        if not isinstance(tree, TerminalNode):
            for c in tree.getChildren():
                print_tree(c, lev + 1)

try:
    argslen = len(sys.argv)
    if argslen < 2:
        print('Please input source file as argument')
    else:
        source_file = sys.argv[1]
        to_parse_tree = argslen >= 3 and sys.argv[2] == "tree"

        input_stream = FileStream(source_file)
        lexer = DataStoryLexer(input_stream)
        stream = CommonTokenStream(lexer)

        parser = DataStoryParser(stream)
        visitor = DataStoryVisitor()
        tree = parser.prog()
    
        if to_parse_tree:
            print_tree(tree, 0)
        else:
            visitor.visit(tree)
except Exception as e:
    print(e)
