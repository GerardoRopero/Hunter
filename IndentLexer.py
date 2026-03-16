"""
IndentLexer.py
~~~~~~~~~~~~~~
Wraps the ANTLR4-generated HunterLexer to inject INDENT / DEDENT tokens,
replicating Python-style significant indentation.
Compatible with antlr4-python3-runtime 4.13.0
"""

import collections
from antlr4 import Token
from antlr4.Token import CommonToken
from HunterLexer import HunterLexer


class IndentLexer(HunterLexer):

    NEWLINE_TOKEN = HunterLexer.NEWLINE
    INDENT_TOKEN  = HunterLexer.INDENT
    DEDENT_TOKEN  = HunterLexer.DEDENT
    EOF_TOKEN     = Token.EOF

    def __init__(self, input_stream):
        super().__init__(input_stream)
        self._indent_stack = [0]
        self._pending = collections.deque()
        self._last_token = None

    def nextToken(self):
        if self._pending:
            tok = self._pending.popleft()
            self._last_token = tok
            return tok

        tok = super().nextToken()

        if tok.type == self.NEWLINE_TOKEN:
            indent_tok = self._handle_newline(tok)
            if indent_tok is not None:
                self._last_token = indent_tok
                return indent_tok

        if tok.type == self.EOF_TOKEN:
            self._flush_dedents(tok)
            if self._pending:
                self._pending.append(tok)
                tok = self._pending.popleft()

        self._last_token = tok
        return tok

    def _handle_newline(self, nl_tok):
        next_indent    = self._peek_indent()
        current_indent = self._indent_stack[-1]

        self._pending.append(nl_tok)

        if next_indent > current_indent:
            self._indent_stack.append(next_indent)
            self._pending.append(self._make_token(self.INDENT_TOKEN, "<INDENT>", nl_tok))

        elif next_indent < current_indent:
            while self._indent_stack[-1] > next_indent:
                self._indent_stack.pop()
                self._pending.append(self._make_token(self.DEDENT_TOKEN, "<DEDENT>", nl_tok))
            if self._indent_stack[-1] != next_indent:
                raise IndentationError(
                    f"Unindent does not match any outer indentation level "
                    f"(line {nl_tok.line})"
                )

        return self._pending.popleft() if self._pending else None

    def _peek_indent(self) -> int:
        saved = self.inputStream.index
        i     = saved

        while True:
            indent = 0
            while i < self.inputStream.size:
                ch = chr(self.inputStream.LA(i - saved + 1))
                if ch in (' ', '\t'):
                    indent += 1
                    i += 1
                else:
                    break

            ch_at = chr(self.inputStream.LA(i - saved + 1)) if i < self.inputStream.size else ''

            if ch_at in ('\r', '\n'):
                i += 1
                if ch_at == '\r' and i < self.inputStream.size \
                        and chr(self.inputStream.LA(i - saved + 1)) == '\n':
                    i += 1
                continue

            if ch_at == '#':
                while i < self.inputStream.size \
                        and chr(self.inputStream.LA(i - saved + 1)) not in ('\r', '\n'):
                    i += 1
                continue

            break

        return indent

    def _flush_dedents(self, eof_tok):
        while len(self._indent_stack) > 1:
            self._indent_stack.pop()
            self._pending.append(self._make_token(self.DEDENT_TOKEN, "<DEDENT>", eof_tok))

    def _make_token(self, ttype: int, text: str, ref):
        tok            = CommonToken(source=ref.source, type=ttype, channel=Token.DEFAULT_CHANNEL, start=ref.start, stop=ref.stop)
        tok.line       = ref.line
        tok.column     = ref.column
        tok.tokenIndex = -1
        tok.text       = text
        return tok
