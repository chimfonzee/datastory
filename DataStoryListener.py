# Generated from DataStory.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DataStoryParser import DataStoryParser
else:
    from DataStoryParser import DataStoryParser

# This class defines a complete listener for a parse tree produced by DataStoryParser.
class DataStoryListener(ParseTreeListener):

    # Enter a parse tree produced by DataStoryParser#prog.
    def enterProg(self, ctx:DataStoryParser.ProgContext):
        pass

    # Exit a parse tree produced by DataStoryParser#prog.
    def exitProg(self, ctx:DataStoryParser.ProgContext):
        pass


    # Enter a parse tree produced by DataStoryParser#func.
    def enterFunc(self, ctx:DataStoryParser.FuncContext):
        pass

    # Exit a parse tree produced by DataStoryParser#func.
    def exitFunc(self, ctx:DataStoryParser.FuncContext):
        pass


    # Enter a parse tree produced by DataStoryParser#expr.
    def enterExpr(self, ctx:DataStoryParser.ExprContext):
        pass

    # Exit a parse tree produced by DataStoryParser#expr.
    def exitExpr(self, ctx:DataStoryParser.ExprContext):
        pass


    # Enter a parse tree produced by DataStoryParser#draw_call.
    def enterDraw_call(self, ctx:DataStoryParser.Draw_callContext):
        pass

    # Exit a parse tree produced by DataStoryParser#draw_call.
    def exitDraw_call(self, ctx:DataStoryParser.Draw_callContext):
        pass


    # Enter a parse tree produced by DataStoryParser#initialize.
    def enterInitialize(self, ctx:DataStoryParser.InitializeContext):
        pass

    # Exit a parse tree produced by DataStoryParser#initialize.
    def exitInitialize(self, ctx:DataStoryParser.InitializeContext):
        pass


    # Enter a parse tree produced by DataStoryParser#assignment.
    def enterAssignment(self, ctx:DataStoryParser.AssignmentContext):
        pass

    # Exit a parse tree produced by DataStoryParser#assignment.
    def exitAssignment(self, ctx:DataStoryParser.AssignmentContext):
        pass


    # Enter a parse tree produced by DataStoryParser#control.
    def enterControl(self, ctx:DataStoryParser.ControlContext):
        pass

    # Exit a parse tree produced by DataStoryParser#control.
    def exitControl(self, ctx:DataStoryParser.ControlContext):
        pass


    # Enter a parse tree produced by DataStoryParser#elif.
    def enterElif(self, ctx:DataStoryParser.ElifContext):
        pass

    # Exit a parse tree produced by DataStoryParser#elif.
    def exitElif(self, ctx:DataStoryParser.ElifContext):
        pass


    # Enter a parse tree produced by DataStoryParser#else.
    def enterElse(self, ctx:DataStoryParser.ElseContext):
        pass

    # Exit a parse tree produced by DataStoryParser#else.
    def exitElse(self, ctx:DataStoryParser.ElseContext):
        pass


    # Enter a parse tree produced by DataStoryParser#loop.
    def enterLoop(self, ctx:DataStoryParser.LoopContext):
        pass

    # Exit a parse tree produced by DataStoryParser#loop.
    def exitLoop(self, ctx:DataStoryParser.LoopContext):
        pass


    # Enter a parse tree produced by DataStoryParser#output.
    def enterOutput(self, ctx:DataStoryParser.OutputContext):
        pass

    # Exit a parse tree produced by DataStoryParser#output.
    def exitOutput(self, ctx:DataStoryParser.OutputContext):
        pass


    # Enter a parse tree produced by DataStoryParser#val.
    def enterVal(self, ctx:DataStoryParser.ValContext):
        pass

    # Exit a parse tree produced by DataStoryParser#val.
    def exitVal(self, ctx:DataStoryParser.ValContext):
        pass


    # Enter a parse tree produced by DataStoryParser#condition.
    def enterCondition(self, ctx:DataStoryParser.ConditionContext):
        pass

    # Exit a parse tree produced by DataStoryParser#condition.
    def exitCondition(self, ctx:DataStoryParser.ConditionContext):
        pass


    # Enter a parse tree produced by DataStoryParser#index.
    def enterIndex(self, ctx:DataStoryParser.IndexContext):
        pass

    # Exit a parse tree produced by DataStoryParser#index.
    def exitIndex(self, ctx:DataStoryParser.IndexContext):
        pass


    # Enter a parse tree produced by DataStoryParser#func_call.
    def enterFunc_call(self, ctx:DataStoryParser.Func_callContext):
        pass

    # Exit a parse tree produced by DataStoryParser#func_call.
    def exitFunc_call(self, ctx:DataStoryParser.Func_callContext):
        pass


    # Enter a parse tree produced by DataStoryParser#input_call.
    def enterInput_call(self, ctx:DataStoryParser.Input_callContext):
        pass

    # Exit a parse tree produced by DataStoryParser#input_call.
    def exitInput_call(self, ctx:DataStoryParser.Input_callContext):
        pass


    # Enter a parse tree produced by DataStoryParser#read_call.
    def enterRead_call(self, ctx:DataStoryParser.Read_callContext):
        pass

    # Exit a parse tree produced by DataStoryParser#read_call.
    def exitRead_call(self, ctx:DataStoryParser.Read_callContext):
        pass



del DataStoryParser