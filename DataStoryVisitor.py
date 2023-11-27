# Generated from DataStory.g4 by ANTLR 4.13.1
import requests
from bs4 import BeautifulSoup
import webbrowser
import tempfile
import os
from antlr4 import *
if "." in __name__:
    from .DataStoryParser import DataStoryParser
else:
    from DataStoryParser import DataStoryParser

# This class defines a complete generic visitor for a parse tree produced by DataStoryParser.

class DataStoryVisitor(ParseTreeVisitor):

    TRANSLATION = {
        'int': int,
        'float': float,
        'string': str,
        'column': list,
        'table': dict,
        'bool': bool
    }
    URL = "http://localhost:8000/analytics/generate_chart"
    temp_store = {}
    data_store = {}
    sign_store = {}


    # Helper to extract specific text
    def getText(self, ctx):
        return ctx.getSymbol().text


    # Helper to raise exception
    def raiseException(self, ctx, message):
        raise Exception(f'Exception at line {ctx.start.line}: {message}')


    # Helper to check if assignment is allowed
    def allowedDataTypes(self, val, data_type):
        return type(val) == self.TRANSLATION[data_type] \
            or (type(val) == int and self.TRANSLATION[data_type] == float)


    # Helper to cast input to appropriate values
    def castInput(self, val):
        try:
            ret = float(val)
        except:
            return val
        else:
            try:
                return int(val)
            except:
                return ret


    # Visit a parse tree produced by DataStoryParser#prog.
    def visitProg(self, ctx:DataStoryParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataStoryParser#func.
    def visitFunc(self, ctx:DataStoryParser.FuncContext):
        args = [(self.getText(dtype), self.getText(id)) for dtype, id in zip(ctx.DTYPE(), ctx.ID()[1:])]
        self.sign_store[self.getText(ctx.ID(0))] = [args, ctx.expr()]


    # Visit a parse tree produced by DataStoryParser#expr.
    def visitExpr(self, ctx:DataStoryParser.ExprContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by DataStoryParser#draw_call.
    def visitDraw_call(self, ctx:DataStoryParser.Draw_callContext):
        data = {
            'table': self.visit(ctx.val(0)),
            'y-axis': self.visit(ctx.val(1)),
            'x-axis': self.visit(ctx.val(2))
        }
        res = requests.post(url=self.URL, json=data)
        soup = BeautifulSoup(res.content.decode("utf-8"), "html.parser")
        _path = os.path.abspath('temp.html')
        url = "file://" + "\\\\wsl.localhost\\Ubuntu" + _path
        with open(_path, 'w+') as f:
            f.write(str(soup))
        webbrowser.register("edge", None, webbrowser.BackgroundBrowser("/mnt/c/Program\ Files\ \(x86\)/Microsoft/Edge/Application/msedge.exe"))
        webbrowser.open_new(url)

    # Visit a parse tree produced by DataStoryParser#initialize.
    def visitInitialize(self, ctx:DataStoryParser.InitializeContext):
        children = ctx.getChildren()
        data_type = self.getText(next(children))
        var = self.getText(next(children))
        _ = next(children)
        val = self.visit(next(children))
        
        if self.allowedDataTypes(val, data_type):
            self.data_store[var] = [data_type, val]
        else:
            self.raiseException(ctx, f'{val} is not type {data_type}')
        # print(self.data_store)


    # Visit a parse tree produced by DataStoryParser#assignment.
    def visitAssignment(self, ctx:DataStoryParser.AssignmentContext):
        children = ctx.getChildren()
        var = self.getText(next(children))
        _ = next(children)
        data = self.data_store.get(var)

        if data == None:
            self.raiseException(ctx, f'unknown variable "{var}" is being referenced')

        data_type = data[0]
        val = self.visit(next(children))

        if self.allowedDataTypes(val, data_type):
            self.data_store[var].pop()
            self.data_store[var].append(val)
        else:
            self.raiseException(ctx, f'{val} is not type {data_type}')
        # print(self.data_store)


    # Visit a parse tree produced by DataStoryParser#control.
    def visitControl(self, ctx:DataStoryParser.ControlContext):
        condition = ctx.condition()
        if self.visit(condition):
            temp_store = self.data_store.copy()
            for expr in ctx.expr():
                self.visit(expr)
            self.data_store = temp_store
        else:
            chosen = False
            for elif_ in ctx.elif_():
                chosen = self.visit(elif_)
                if chosen:
                    break
            if not chosen and (else_:=ctx.else_()) != None:
                self.visit(else_)


    # Visit a parse tree produced by DataStoryParser#elif.
    def visitElif(self, ctx:DataStoryParser.ElifContext):
        condition = ctx.condition()
        if ret:=self.visit(condition):
            temp_store = self.data_store.copy()
            for expr in ctx.expr():
                self.visit(expr)
            self.data_store = temp_store
        return ret


    # Visit a parse tree produced by DataStoryParser#else.
    def visitElse(self, ctx:DataStoryParser.ElseContext):
        temp_store = self.data_store.copy()
        print(temp_store)
        self.visitChildren(ctx)
        print(self.data_store)
        self.data_store = temp_store


    # Visit a parse tree produced by DataStoryParser#loop.
    def visitLoop(self, ctx:DataStoryParser.LoopContext):
        temp_store = self.data_store.copy()
        if ctx.FOR():
            if (init:=ctx.initialize()) != None:
                self.visit(init)
            else:
                self.visit(ctx.assignment(0))
            
            while self.visit(ctx.condition()):
                for expr in ctx.expr():
                    self.visit(expr)
                self.visit(ctx.assignment(1))
        else:
            while self.visit(ctx.condition()):
                for expr in ctx.expr():
                    self.visit(expr)
        self.data_store = temp_store


    # Visit a parse tree produced by DataStoryParser#output.
    def visitOutput(self, ctx:DataStoryParser.OutputContext):
        print(self.visit(ctx.val()))


    # Visit a parse tree produced by DataStoryParser#val.
    def visitVal(self, ctx:DataStoryParser.ValContext):
        if ctx.LPAREN() != None:
            return self.visit(ctx.val(0))
        elif ctx.AND_DOP() != None:
            first = self.visit(ctx.val(0))
            second = self.visit(ctx.val(1))
            first_type = type(first)
            second_type = type(second)

            if isinstance(first, dict):
                if isinstance(second, dict):
                    return {**first, **second}
                elif isinstance(second, list):
                    return {**first, '_second': second}
            elif isinstance(first, list) and isinstance(second, list):
                return {'_first': first, '_second': second}
            else:
                self.raiseException(ctx, f'trying to join types {first_type} and {second_type}')
        elif ctx.OR_DOP() != None:
            first = self.visit(ctx.val(0))
            second = self.visit(ctx.val(1))
            print(first)
            print(second)
            first_type = type(first)
            second_type = type(second)

            if isinstance(first, list) and isinstance(second, list):
                return first + second
            elif isinstance(first, dict) and isinstance(second, dict):
                if len(first) < len(second):
                    self.raiseException(ctx, f'table to append has more columns')
                ret = {**first}
                for fkey, skey in zip(first, second):
                    ret[fkey] + second[skey]
                return ret
        elif ctx.POW_OP() != None:
            return self.visit(ctx.val(0)) ** self.visit(ctx.val(1))    
        elif ctx.ADD_OP() != None:
            return self.visit(ctx.val(0)) + self.visit(ctx.val(1))
        elif ctx.SUB_OP() != None:
            return self.visit(ctx.val(0)) - self.visit(ctx.val(1))
        elif ctx.MUL_OP() != None:
            return self.visit(ctx.val(0)) * self.visit(ctx.val(1))
        elif ctx.DIV_OP() != None:
            return self.visit(ctx.val(0)) / self.visit(ctx.val(1))
        elif ctx.INT() != None:
            return int(self.getText(ctx.getChild(0)))
        elif ctx.FLOAT() != None:
            return float(self.getText(ctx.getChild(0)))
        elif ctx.STR() != None:
            return self.getText(ctx.getChild(0)).strip('\"')
        elif (_id:=ctx.ID()) != None:
            try:
                return self.data_store[_id.getSymbol().text][1]
            except KeyError:
                self.raiseException(ctx, f'unknown variable "{_id}" is being referenced') 
            # try:
            #     if (slice:=ctx.val(0)) == None:
            #         return self.data_store[_id.getSymbol().text][1]
            #     print(slice)
            #     start, end = self.visit(slice)
            #     if end != None:
            #         return self.data_store[_id.getSymbol().text][1][start:end]
            # except KeyError:
            #     self.raiseException(ctx, f'unknown variable "{_id}" is being referenced') 
            # except IndexError:
            #     self.raiseException(ctx, f'column index out of range using {start}, {end}')
            # except TypeError:
            #     self.raiseException(ctx, f'trying to get data using {start}, {end} as indices')
        elif (input_call:=ctx.input_call()) != None:
            return self.castInput(self.visit(input_call))
        elif (read_call:=ctx.read_call()) != None:
            return self.visit(read_call)
        elif (index:=ctx.index()) != None:
            try:
                start, end = self.visit(index)
                if end != None:
                    return self.visit(ctx.val(0))[start:end]
                return self.visit(ctx.val(0))[start]
            except IndexError:
                self.raiseException(ctx, f'column index out of range using {start}, {end}')
            except TypeError:
                self.raiseException(ctx, f'trying to get data using {start}, {end} as indices')


    # Visit a parse tree produced by DataStoryParser#condition.
    def visitCondition(self, ctx:DataStoryParser.ConditionContext):
        if ctx.LPAREN() != None:
            return self.visit(ctx.condition(0))
        elif ctx.AND_OP() != None:
            return self.visit(ctx.condition(0)) and self.visit(ctx.condition(1))
        elif ctx.OR_OP() != None:
            return self.visit(ctx.condition(0)) or self.visit(ctx.condition(1))
        elif ctx.NOT_OP() != None:
            return not self.visit(ctx.condition(0))
        elif ctx.LT_OP() != None:
            return self.visit(ctx.val(0)) < self.visit(ctx.val(1))
        elif ctx.GT_OP() != None:
            return self.visit(ctx.val(0)) > self.visit(ctx.val(1))
        elif ctx.LTEQ_OP() != None:
            return self.visit(ctx.val(0)) <= self.visit(ctx.val(1))
        elif ctx.GTEQ_OP() != None:
            return self.visit(ctx.val(0)) >= self.visit(ctx.val(1))
        elif ctx.EQ_OP() != None:
            return self.visit(ctx.val(0)) == self.visit(ctx.val(1))
        elif ctx.NEQ_OP() != None:
            return self.visit(ctx.val(0)) != self.visit(ctx.val(1))
        elif ctx.TRUE() != None:
            return True
        elif ctx.FALSE() != None:
            return False
        elif (_id:=ctx.ID()) != None:
            try:
                return self.data_store[_id.getSymbol().text][1]
            except KeyError:
                self.raiseException(ctx, f'unknown variable "{_id}" is being referenced')
            # try:
            #     if (slicing:=ctx.slicing()) == None:
            #         return self.data_store[_id.getSymbol().text][1]
            #     start, end = self.visit(slicing)
            #     if end != None:
            #         return self.data_store[_id.getSymbol().text][1][start:end]
            # except KeyError:
            #     self.raiseException(ctx, f'unknown variable "{_id}" is being referenced') 
            # except IndexError:
            #     self.raiseException(ctx, f'column index out of range using {start}, {end}')
            # except TypeError:
            #     self.raiseException(ctx, f'trying to get data using {start}, {end} as indices')
        elif (index:=ctx.index()) != None:
            try:
                start, end = self.visit(index)
                if end != None:
                    return self.visit(ctx.val(0))[start:end]
                return self.visit(ctx.val(0))[start] 
            except IndexError:
                self.raiseException(ctx, f'column index out of range using {start}, {end}')
            except TypeError:
                self.raiseException(ctx, f'trying to get data using {start}, {end} as indices')

    # Visit a parse tree produced by DataStoryParser#index.
    def visitIndex(self, ctx:DataStoryParser.IndexContext):
        if (right:=ctx.val(1)) != None:
            return self.visit(ctx.val(0)), self.visit(right)
        return self.visit(ctx.val(0)), None


    # Visit a parse tree produced by DataStoryParser#func_call.
    def visitFunc_call(self, ctx:DataStoryParser.Func_callContext):
        func_store = {}
        func_id = self.getText(ctx.ID())
        func = self.sign_store.get(func_id)

        if func == None:
            self.raiseException(ctx, f'unknown function "{func_id}" is being referenced')

        for var, val in zip(func[0], ctx.val()):
            try:
                val = self.visit(val)
                func_store[var[1]] = [var[0], self.TRANSLATION[var[0]](val)]
            except Exception:
                self.raiseException(ctx, f'{val} is not type {var[0]}')
        temp_store = self.data_store
        self.data_store = func_store
        # print(func_store)

        for expr in func[1]:
            self.visit(expr)
        self.data_store = temp_store


    # Visit a parse tree produced by DataStoryParser#input_call.
    def visitInput_call(self, ctx:DataStoryParser.Input_callContext):
        return input(f'{self.visit(ctx.val())} ')


    # Visit a parse tree produced by DataStoryParser#read_call.
    def visitRead_call(self, ctx:DataStoryParser.Read_callContext):
        with open(self.visit(ctx.val()), 'r') as file:
            lines = file.readlines()
            headers = []
            index = 0

            if self.visit(ctx.condition()):
                headers = lines[0].strip().split(',')
                index = 1
            else:
                headers = range(0, len(lines[0].strip().split(',')))
                index = 0
            
            table = {key: [] for key in headers}
            for line in lines[index:]:
                for header, data in zip(headers, line.split(',')):
                    table[header].append(self.castInput(data))

            return table
                

del DataStoryParser
