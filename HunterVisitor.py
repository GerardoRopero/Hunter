# Generated from Hunter.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .HunterParser import HunterParser
else:
    from HunterParser import HunterParser

# This class defines a complete generic visitor for a parse tree produced by HunterParser.

class HunterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HunterParser#program.
    def visitProgram(self, ctx:HunterParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#statement.
    def visitStatement(self, ctx:HunterParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#SimpleAssign.
    def visitSimpleAssign(self, ctx:HunterParser.SimpleAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#PlusAssign.
    def visitPlusAssign(self, ctx:HunterParser.PlusAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#MinusAssign.
    def visitMinusAssign(self, ctx:HunterParser.MinusAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#StarAssign.
    def visitStarAssign(self, ctx:HunterParser.StarAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#SlashAssign.
    def visitSlashAssign(self, ctx:HunterParser.SlashAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#printStmt.
    def visitPrintStmt(self, ctx:HunterParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#ifStmt.
    def visitIfStmt(self, ctx:HunterParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#elifClause.
    def visitElifClause(self, ctx:HunterParser.ElifClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#elseClause.
    def visitElseClause(self, ctx:HunterParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#whileStmt.
    def visitWhileStmt(self, ctx:HunterParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#ForRange.
    def visitForRange(self, ctx:HunterParser.ForRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#ForIter.
    def visitForIter(self, ctx:HunterParser.ForIterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#RangeOne.
    def visitRangeOne(self, ctx:HunterParser.RangeOneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#RangeTwo.
    def visitRangeTwo(self, ctx:HunterParser.RangeTwoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#RangeThree.
    def visitRangeThree(self, ctx:HunterParser.RangeThreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#returnStmt.
    def visitReturnStmt(self, ctx:HunterParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#funcDef.
    def visitFuncDef(self, ctx:HunterParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#paramList.
    def visitParamList(self, ctx:HunterParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#exprStmt.
    def visitExprStmt(self, ctx:HunterParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#block.
    def visitBlock(self, ctx:HunterParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#exprList.
    def visitExprList(self, ctx:HunterParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#expr.
    def visitExpr(self, ctx:HunterParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#orExpr.
    def visitOrExpr(self, ctx:HunterParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#andExpr.
    def visitAndExpr(self, ctx:HunterParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#notExpr.
    def visitNotExpr(self, ctx:HunterParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#compareExpr.
    def visitCompareExpr(self, ctx:HunterParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#addExpr.
    def visitAddExpr(self, ctx:HunterParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#mulExpr.
    def visitMulExpr(self, ctx:HunterParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:HunterParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#UnaryPlus.
    def visitUnaryPlus(self, ctx:HunterParser.UnaryPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#UnaryPass.
    def visitUnaryPass(self, ctx:HunterParser.UnaryPassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#powerExpr.
    def visitPowerExpr(self, ctx:HunterParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#IntLit.
    def visitIntLit(self, ctx:HunterParser.IntLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#FloatLit.
    def visitFloatLit(self, ctx:HunterParser.FloatLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#StringLit.
    def visitStringLit(self, ctx:HunterParser.StringLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#BoolLit.
    def visitBoolLit(self, ctx:HunterParser.BoolLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#NoneLit.
    def visitNoneLit(self, ctx:HunterParser.NoneLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#FuncCall.
    def visitFuncCall(self, ctx:HunterParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#IndexAccess.
    def visitIndexAccess(self, ctx:HunterParser.IndexAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#Identifier.
    def visitIdentifier(self, ctx:HunterParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#Paren.
    def visitParen(self, ctx:HunterParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#ListExpr.
    def visitListExpr(self, ctx:HunterParser.ListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HunterParser#listLit.
    def visitListLit(self, ctx:HunterParser.ListLitContext):
        return self.visitChildren(ctx)



del HunterParser