# Generated from Hunter.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .HunterParser import HunterParser
else:
    from HunterParser import HunterParser

# This class defines a complete listener for a parse tree produced by HunterParser.
class HunterListener(ParseTreeListener):

    # Enter a parse tree produced by HunterParser#program.
    def enterProgram(self, ctx:HunterParser.ProgramContext):
        pass

    # Exit a parse tree produced by HunterParser#program.
    def exitProgram(self, ctx:HunterParser.ProgramContext):
        pass


    # Enter a parse tree produced by HunterParser#statement.
    def enterStatement(self, ctx:HunterParser.StatementContext):
        pass

    # Exit a parse tree produced by HunterParser#statement.
    def exitStatement(self, ctx:HunterParser.StatementContext):
        pass


    # Enter a parse tree produced by HunterParser#SimpleAssign.
    def enterSimpleAssign(self, ctx:HunterParser.SimpleAssignContext):
        pass

    # Exit a parse tree produced by HunterParser#SimpleAssign.
    def exitSimpleAssign(self, ctx:HunterParser.SimpleAssignContext):
        pass


    # Enter a parse tree produced by HunterParser#PlusAssign.
    def enterPlusAssign(self, ctx:HunterParser.PlusAssignContext):
        pass

    # Exit a parse tree produced by HunterParser#PlusAssign.
    def exitPlusAssign(self, ctx:HunterParser.PlusAssignContext):
        pass


    # Enter a parse tree produced by HunterParser#MinusAssign.
    def enterMinusAssign(self, ctx:HunterParser.MinusAssignContext):
        pass

    # Exit a parse tree produced by HunterParser#MinusAssign.
    def exitMinusAssign(self, ctx:HunterParser.MinusAssignContext):
        pass


    # Enter a parse tree produced by HunterParser#StarAssign.
    def enterStarAssign(self, ctx:HunterParser.StarAssignContext):
        pass

    # Exit a parse tree produced by HunterParser#StarAssign.
    def exitStarAssign(self, ctx:HunterParser.StarAssignContext):
        pass


    # Enter a parse tree produced by HunterParser#SlashAssign.
    def enterSlashAssign(self, ctx:HunterParser.SlashAssignContext):
        pass

    # Exit a parse tree produced by HunterParser#SlashAssign.
    def exitSlashAssign(self, ctx:HunterParser.SlashAssignContext):
        pass


    # Enter a parse tree produced by HunterParser#printStmt.
    def enterPrintStmt(self, ctx:HunterParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by HunterParser#printStmt.
    def exitPrintStmt(self, ctx:HunterParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by HunterParser#ifStmt.
    def enterIfStmt(self, ctx:HunterParser.IfStmtContext):
        pass

    # Exit a parse tree produced by HunterParser#ifStmt.
    def exitIfStmt(self, ctx:HunterParser.IfStmtContext):
        pass


    # Enter a parse tree produced by HunterParser#elifClause.
    def enterElifClause(self, ctx:HunterParser.ElifClauseContext):
        pass

    # Exit a parse tree produced by HunterParser#elifClause.
    def exitElifClause(self, ctx:HunterParser.ElifClauseContext):
        pass


    # Enter a parse tree produced by HunterParser#elseClause.
    def enterElseClause(self, ctx:HunterParser.ElseClauseContext):
        pass

    # Exit a parse tree produced by HunterParser#elseClause.
    def exitElseClause(self, ctx:HunterParser.ElseClauseContext):
        pass


    # Enter a parse tree produced by HunterParser#whileStmt.
    def enterWhileStmt(self, ctx:HunterParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by HunterParser#whileStmt.
    def exitWhileStmt(self, ctx:HunterParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by HunterParser#ForRange.
    def enterForRange(self, ctx:HunterParser.ForRangeContext):
        pass

    # Exit a parse tree produced by HunterParser#ForRange.
    def exitForRange(self, ctx:HunterParser.ForRangeContext):
        pass


    # Enter a parse tree produced by HunterParser#ForIter.
    def enterForIter(self, ctx:HunterParser.ForIterContext):
        pass

    # Exit a parse tree produced by HunterParser#ForIter.
    def exitForIter(self, ctx:HunterParser.ForIterContext):
        pass


    # Enter a parse tree produced by HunterParser#RangeOne.
    def enterRangeOne(self, ctx:HunterParser.RangeOneContext):
        pass

    # Exit a parse tree produced by HunterParser#RangeOne.
    def exitRangeOne(self, ctx:HunterParser.RangeOneContext):
        pass


    # Enter a parse tree produced by HunterParser#RangeTwo.
    def enterRangeTwo(self, ctx:HunterParser.RangeTwoContext):
        pass

    # Exit a parse tree produced by HunterParser#RangeTwo.
    def exitRangeTwo(self, ctx:HunterParser.RangeTwoContext):
        pass


    # Enter a parse tree produced by HunterParser#RangeThree.
    def enterRangeThree(self, ctx:HunterParser.RangeThreeContext):
        pass

    # Exit a parse tree produced by HunterParser#RangeThree.
    def exitRangeThree(self, ctx:HunterParser.RangeThreeContext):
        pass


    # Enter a parse tree produced by HunterParser#returnStmt.
    def enterReturnStmt(self, ctx:HunterParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by HunterParser#returnStmt.
    def exitReturnStmt(self, ctx:HunterParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by HunterParser#funcDef.
    def enterFuncDef(self, ctx:HunterParser.FuncDefContext):
        pass

    # Exit a parse tree produced by HunterParser#funcDef.
    def exitFuncDef(self, ctx:HunterParser.FuncDefContext):
        pass


    # Enter a parse tree produced by HunterParser#paramList.
    def enterParamList(self, ctx:HunterParser.ParamListContext):
        pass

    # Exit a parse tree produced by HunterParser#paramList.
    def exitParamList(self, ctx:HunterParser.ParamListContext):
        pass


    # Enter a parse tree produced by HunterParser#exprStmt.
    def enterExprStmt(self, ctx:HunterParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by HunterParser#exprStmt.
    def exitExprStmt(self, ctx:HunterParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by HunterParser#block.
    def enterBlock(self, ctx:HunterParser.BlockContext):
        pass

    # Exit a parse tree produced by HunterParser#block.
    def exitBlock(self, ctx:HunterParser.BlockContext):
        pass


    # Enter a parse tree produced by HunterParser#exprList.
    def enterExprList(self, ctx:HunterParser.ExprListContext):
        pass

    # Exit a parse tree produced by HunterParser#exprList.
    def exitExprList(self, ctx:HunterParser.ExprListContext):
        pass


    # Enter a parse tree produced by HunterParser#expr.
    def enterExpr(self, ctx:HunterParser.ExprContext):
        pass

    # Exit a parse tree produced by HunterParser#expr.
    def exitExpr(self, ctx:HunterParser.ExprContext):
        pass


    # Enter a parse tree produced by HunterParser#orExpr.
    def enterOrExpr(self, ctx:HunterParser.OrExprContext):
        pass

    # Exit a parse tree produced by HunterParser#orExpr.
    def exitOrExpr(self, ctx:HunterParser.OrExprContext):
        pass


    # Enter a parse tree produced by HunterParser#andExpr.
    def enterAndExpr(self, ctx:HunterParser.AndExprContext):
        pass

    # Exit a parse tree produced by HunterParser#andExpr.
    def exitAndExpr(self, ctx:HunterParser.AndExprContext):
        pass


    # Enter a parse tree produced by HunterParser#notExpr.
    def enterNotExpr(self, ctx:HunterParser.NotExprContext):
        pass

    # Exit a parse tree produced by HunterParser#notExpr.
    def exitNotExpr(self, ctx:HunterParser.NotExprContext):
        pass


    # Enter a parse tree produced by HunterParser#compareExpr.
    def enterCompareExpr(self, ctx:HunterParser.CompareExprContext):
        pass

    # Exit a parse tree produced by HunterParser#compareExpr.
    def exitCompareExpr(self, ctx:HunterParser.CompareExprContext):
        pass


    # Enter a parse tree produced by HunterParser#addExpr.
    def enterAddExpr(self, ctx:HunterParser.AddExprContext):
        pass

    # Exit a parse tree produced by HunterParser#addExpr.
    def exitAddExpr(self, ctx:HunterParser.AddExprContext):
        pass


    # Enter a parse tree produced by HunterParser#mulExpr.
    def enterMulExpr(self, ctx:HunterParser.MulExprContext):
        pass

    # Exit a parse tree produced by HunterParser#mulExpr.
    def exitMulExpr(self, ctx:HunterParser.MulExprContext):
        pass


    # Enter a parse tree produced by HunterParser#UnaryMinus.
    def enterUnaryMinus(self, ctx:HunterParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by HunterParser#UnaryMinus.
    def exitUnaryMinus(self, ctx:HunterParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by HunterParser#UnaryPlus.
    def enterUnaryPlus(self, ctx:HunterParser.UnaryPlusContext):
        pass

    # Exit a parse tree produced by HunterParser#UnaryPlus.
    def exitUnaryPlus(self, ctx:HunterParser.UnaryPlusContext):
        pass


    # Enter a parse tree produced by HunterParser#UnaryPass.
    def enterUnaryPass(self, ctx:HunterParser.UnaryPassContext):
        pass

    # Exit a parse tree produced by HunterParser#UnaryPass.
    def exitUnaryPass(self, ctx:HunterParser.UnaryPassContext):
        pass


    # Enter a parse tree produced by HunterParser#powerExpr.
    def enterPowerExpr(self, ctx:HunterParser.PowerExprContext):
        pass

    # Exit a parse tree produced by HunterParser#powerExpr.
    def exitPowerExpr(self, ctx:HunterParser.PowerExprContext):
        pass


    # Enter a parse tree produced by HunterParser#IntLit.
    def enterIntLit(self, ctx:HunterParser.IntLitContext):
        pass

    # Exit a parse tree produced by HunterParser#IntLit.
    def exitIntLit(self, ctx:HunterParser.IntLitContext):
        pass


    # Enter a parse tree produced by HunterParser#FloatLit.
    def enterFloatLit(self, ctx:HunterParser.FloatLitContext):
        pass

    # Exit a parse tree produced by HunterParser#FloatLit.
    def exitFloatLit(self, ctx:HunterParser.FloatLitContext):
        pass


    # Enter a parse tree produced by HunterParser#StringLit.
    def enterStringLit(self, ctx:HunterParser.StringLitContext):
        pass

    # Exit a parse tree produced by HunterParser#StringLit.
    def exitStringLit(self, ctx:HunterParser.StringLitContext):
        pass


    # Enter a parse tree produced by HunterParser#BoolLit.
    def enterBoolLit(self, ctx:HunterParser.BoolLitContext):
        pass

    # Exit a parse tree produced by HunterParser#BoolLit.
    def exitBoolLit(self, ctx:HunterParser.BoolLitContext):
        pass


    # Enter a parse tree produced by HunterParser#NoneLit.
    def enterNoneLit(self, ctx:HunterParser.NoneLitContext):
        pass

    # Exit a parse tree produced by HunterParser#NoneLit.
    def exitNoneLit(self, ctx:HunterParser.NoneLitContext):
        pass


    # Enter a parse tree produced by HunterParser#FuncCall.
    def enterFuncCall(self, ctx:HunterParser.FuncCallContext):
        pass

    # Exit a parse tree produced by HunterParser#FuncCall.
    def exitFuncCall(self, ctx:HunterParser.FuncCallContext):
        pass


    # Enter a parse tree produced by HunterParser#IndexAccess.
    def enterIndexAccess(self, ctx:HunterParser.IndexAccessContext):
        pass

    # Exit a parse tree produced by HunterParser#IndexAccess.
    def exitIndexAccess(self, ctx:HunterParser.IndexAccessContext):
        pass


    # Enter a parse tree produced by HunterParser#Identifier.
    def enterIdentifier(self, ctx:HunterParser.IdentifierContext):
        pass

    # Exit a parse tree produced by HunterParser#Identifier.
    def exitIdentifier(self, ctx:HunterParser.IdentifierContext):
        pass


    # Enter a parse tree produced by HunterParser#Paren.
    def enterParen(self, ctx:HunterParser.ParenContext):
        pass

    # Exit a parse tree produced by HunterParser#Paren.
    def exitParen(self, ctx:HunterParser.ParenContext):
        pass


    # Enter a parse tree produced by HunterParser#ListExpr.
    def enterListExpr(self, ctx:HunterParser.ListExprContext):
        pass

    # Exit a parse tree produced by HunterParser#ListExpr.
    def exitListExpr(self, ctx:HunterParser.ListExprContext):
        pass


    # Enter a parse tree produced by HunterParser#listLit.
    def enterListLit(self, ctx:HunterParser.ListLitContext):
        pass

    # Exit a parse tree produced by HunterParser#listLit.
    def exitListLit(self, ctx:HunterParser.ListLitContext):
        pass



del HunterParser