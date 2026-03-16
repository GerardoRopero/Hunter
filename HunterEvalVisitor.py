"""
HunterEvalVisitor.py
~~~~~~~~~~~~~~~~~~~~
Visitor que recorre el árbol sintáctico de Hunter y ejecuta cada nodo
directamente, sin generar código Python intermedio.
"""

from HunterParser  import HunterParser
from HunterVisitor import HunterVisitor
from Environment   import Environment, HunterFunction, ReturnException


class HunterEvalVisitor(HunterVisitor):

    def __init__(self):
        self._global_env = Environment()
        self._env        = self._global_env

    # ── Utilidad de entorno ────────────────────────────────────────────────
    def _push(self) -> Environment:
        self._env = self._env.child()
        return self._env

    def _pop(self):
        self._env = self._env._parent

    # ─────────────────────────────────────────────────────────────────────
    #  PROGRAMA
    # ─────────────────────────────────────────────────────────────────────
    def visitProgram(self, ctx: HunterParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    # ─────────────────────────────────────────────────────────────────────
    #  STATEMENTS
    # ─────────────────────────────────────────────────────────────────────
    def visitStatement(self, ctx: HunterParser.StatementContext):
        for child in ctx.getChildren():
            if hasattr(child, "getRuleIndex"):
                return self.visit(child)

    # ── Assignments ────────────────────────────────────────────────────────
    def visitSimpleAssign(self, ctx: HunterParser.SimpleAssignContext):
        value = self.visit(ctx.expr())
        self._env.assign(ctx.ID().getText(), value)

    def visitPlusAssign(self, ctx: HunterParser.PlusAssignContext):
        name  = ctx.ID().getText()
        value = self._env.get(name) + self.visit(ctx.expr())
        self._env.assign(name, value)

    def visitMinusAssign(self, ctx: HunterParser.MinusAssignContext):
        name  = ctx.ID().getText()
        value = self._env.get(name) - self.visit(ctx.expr())
        self._env.assign(name, value)

    def visitStarAssign(self, ctx: HunterParser.StarAssignContext):
        name  = ctx.ID().getText()
        value = self._env.get(name) * self.visit(ctx.expr())
        self._env.assign(name, value)

    def visitSlashAssign(self, ctx: HunterParser.SlashAssignContext):
        name  = ctx.ID().getText()
        value = self._env.get(name) / self.visit(ctx.expr())
        self._env.assign(name, value)

    # ── Print ──────────────────────────────────────────────────────────────
    def visitPrintStmt(self, ctx: HunterParser.PrintStmtContext):
        args = []
        if ctx.exprList():
            args = [self.visit(e) for e in ctx.exprList().expr()]
        print(*args)

    # ── If / elif / else ───────────────────────────────────────────────────
    def visitIfStmt(self, ctx: HunterParser.IfStmtContext):
        if self.visit(ctx.expr()):
            return self._exec_block(ctx.block())

        for elif_clause in ctx.elifClause():
            if self.visit(elif_clause.expr()):
                return self._exec_block(elif_clause.block())

        if ctx.elseClause():
            return self._exec_block(ctx.elseClause().block())

    # ── While ──────────────────────────────────────────────────────────────
    def visitWhileStmt(self, ctx: HunterParser.WhileStmtContext):
        while self.visit(ctx.expr()):
            self._exec_block(ctx.block())

    # ── For ────────────────────────────────────────────────────────────────
    def visitForRange(self, ctx: HunterParser.ForRangeContext):
        var      = ctx.ID().getText()
        iterable = self.visit(ctx.rangeExpr())
        for val in iterable:
            self._push()
            self._env.set(var, val)
            try:
                self._exec_block_raw(ctx.block())
            finally:
                self._pop()

    def visitForIter(self, ctx: HunterParser.ForIterContext):
        var      = ctx.ID(0).getText()
        iterable = self._env.get(ctx.ID(1).getText())
        for val in iterable:
            self._push()
            self._env.set(var, val)
            try:
                self._exec_block_raw(ctx.block())
            finally:
                self._pop()

    def visitRangeOne(self, ctx: HunterParser.RangeOneContext):
        return range(int(self.visit(ctx.expr(0))))

    def visitRangeTwo(self, ctx: HunterParser.RangeTwoContext):
        return range(int(self.visit(ctx.expr(0))),
                     int(self.visit(ctx.expr(1))))

    def visitRangeThree(self, ctx: HunterParser.RangeThreeContext):
        return range(int(self.visit(ctx.expr(0))),
                     int(self.visit(ctx.expr(1))),
                     int(self.visit(ctx.expr(2))))

    # ── Return ─────────────────────────────────────────────────────────────
    def visitReturnStmt(self, ctx: HunterParser.ReturnStmtContext):
        value = self.visit(ctx.expr()) if ctx.expr() else None
        raise ReturnException(value)

    # ── Function definition ────────────────────────────────────────────────
    def visitFuncDef(self, ctx: HunterParser.FuncDefContext):
        name   = ctx.ID().getText()
        params = []
        if ctx.paramList():
            params = [t.getText() for t in ctx.paramList().ID()]
        self._env.define_function(name, params, ctx.block(), self._env)

    # ── Expression statement ───────────────────────────────────────────────
    def visitExprStmt(self, ctx: HunterParser.ExprStmtContext):
        self.visit(ctx.expr())

    # ── Block helpers ──────────────────────────────────────────────────────
    def _exec_block(self, ctx: HunterParser.BlockContext):
        """Ejecuta un bloque en un scope nuevo."""
        self._push()
        try:
            self._exec_block_raw(ctx)
        finally:
            self._pop()

    def _exec_block_raw(self, ctx: HunterParser.BlockContext):
        """Ejecuta un bloque sin crear un scope nuevo (for lo gestiona)."""
        for stmt in ctx.statement():
            self.visit(stmt)

    # ─────────────────────────────────────────────────────────────────────
    #  EXPRESIONES
    # ─────────────────────────────────────────────────────────────────────
    def visitExpr(self, ctx: HunterParser.ExprContext):
        return self.visit(ctx.orExpr())

    def visitOrExpr(self, ctx: HunterParser.OrExprContext):
        result = self.visit(ctx.andExpr(0))
        for i in range(1, len(ctx.andExpr())):
            result = result or self.visit(ctx.andExpr(i))
        return result

    def visitAndExpr(self, ctx: HunterParser.AndExprContext):
        result = self.visit(ctx.notExpr(0))
        for i in range(1, len(ctx.notExpr())):
            result = result and self.visit(ctx.notExpr(i))
        return result

    def visitNotExpr(self, ctx: HunterParser.NotExprContext):
        if ctx.NOT():
            return not self.visit(ctx.notExpr())
        return self.visit(ctx.compareExpr())

    def visitCompareExpr(self, ctx: HunterParser.CompareExprContext):
        children  = list(ctx.getChildren())
        add_exprs = ctx.addExpr()
        ops       = [c.getText() for c in children if not hasattr(c, "getRuleIndex")]
        result    = self.visit(add_exprs[0])
        for op, rhs_ctx in zip(ops, add_exprs[1:]):
            rhs = self.visit(rhs_ctx)
            result = self._compare(result, op, rhs)
        return result

    def _compare(self, left, op: str, right):
        if op == "==": return left == right
        if op == "!=": return left != right
        if op == "<" : return left <  right
        if op == "<=": return left <= right
        if op == ">" : return left >  right
        if op == ">=": return left >= right
        raise RuntimeError(f"Operador desconocido: {op}")

    def visitAddExpr(self, ctx: HunterParser.AddExprContext):
        children  = list(ctx.getChildren())
        mul_exprs = ctx.mulExpr()
        ops       = [c.getText() for c in children if not hasattr(c, "getRuleIndex")]
        result    = self.visit(mul_exprs[0])
        for op, operand in zip(ops, mul_exprs[1:]):
            val = self.visit(operand)
            if op == "+": result = result + val
            else:         result = result - val
        return result

    def visitMulExpr(self, ctx: HunterParser.MulExprContext):
        children    = list(ctx.getChildren())
        unary_exprs = ctx.unaryExpr()
        ops         = [c.getText() for c in children if not hasattr(c, "getRuleIndex")]
        result      = self.visit(unary_exprs[0])
        for op, operand in zip(ops, unary_exprs[1:]):
            val = self.visit(operand)
            if   op == "*" : result = result * val
            elif op == "/" : result = result / val
            elif op == "//": result = result // val
            elif op == "%" : result = result % val
        return result

    def visitUnaryMinus(self, ctx: HunterParser.UnaryMinusContext):
        return -self.visit(ctx.unaryExpr())

    def visitUnaryPlus(self, ctx: HunterParser.UnaryPlusContext):
        return +self.visit(ctx.unaryExpr())

    def visitUnaryPass(self, ctx: HunterParser.UnaryPassContext):
        return self.visit(ctx.powerExpr())

    def visitPowerExpr(self, ctx: HunterParser.PowerExprContext):
        primaries = ctx.primaryExpr()
        result    = self.visit(primaries[-1])
        for p in reversed(primaries[:-1]):
            result = self.visit(p) ** result
        return result

    # ── Primary expressions ────────────────────────────────────────────────
    def visitIntLit(self, ctx: HunterParser.IntLitContext):
        return int(ctx.INT_LIT().getText())

    def visitFloatLit(self, ctx: HunterParser.FloatLitContext):
        return float(ctx.FLOAT_LIT().getText())

    def visitStringLit(self, ctx: HunterParser.StringLitContext):
        raw = ctx.STRING_LIT().getText()
        # quitar comillas y procesar escapes
        return raw[1:-1].encode().decode("unicode_escape")

    def visitBoolLit(self, ctx: HunterParser.BoolLitContext):
        return ctx.BOOL_LIT().getText() == "True"

    def visitNoneLit(self, ctx: HunterParser.NoneLitContext):
        return None

    def visitIdentifier(self, ctx: HunterParser.IdentifierContext):
        return self._env.get(ctx.ID().getText())

    def visitParen(self, ctx: HunterParser.ParenContext):
        return self.visit(ctx.expr())

    def visitIndexAccess(self, ctx: HunterParser.IndexAccessContext):
        lst = self._env.get(ctx.ID().getText())
        idx = int(self.visit(ctx.expr()))
        return lst[idx]

    def visitListExpr(self, ctx: HunterParser.ListExprContext):
        return self.visit(ctx.listLit())

    def visitListLit(self, ctx: HunterParser.ListLitContext):
        if ctx.exprList():
            return [self.visit(e) for e in ctx.exprList().expr()]
        return []

    def visitExprList(self, ctx: HunterParser.ExprListContext):
        return [self.visit(e) for e in ctx.expr()]

    # ── Llamada a función ──────────────────────────────────────────────────
    def visitFuncCall(self, ctx: HunterParser.FuncCallContext):
        name = ctx.ID().getText()
        args = []
        if ctx.exprList():
            args = [self.visit(e) for e in ctx.exprList().expr()]

        func = self._env.get(name)

        # función nativa de Python (e.g. print registrada como builtin)
        if callable(func) and not isinstance(func, HunterFunction):
            return func(*args)

        if not isinstance(func, HunterFunction):
            raise TypeError(f"'{name}' no es una función")

        if len(args) != len(func.params):
            raise TypeError(
                f"'{name}' espera {len(func.params)} argumentos, "
                f"recibió {len(args)}"
            )

        # Crear scope de la función sobre su closure
        call_env  = func.closure.child()
        saved_env = self._env
        self._env = call_env

        for param, arg in zip(func.params, args):
            self._env.set(param, arg)

        result = None
        try:
            for stmt in func.body_ctx.statement():
                self.visit(stmt)
        except ReturnException as ret:
            result = ret.value
        finally:
            self._env = saved_env

        return result
