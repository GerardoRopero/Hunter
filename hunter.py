#!/usr/bin/env python3
"""
hunter.py  –  Intérprete del lenguaje Hunter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ejecuta archivos .hxh directamente, sin generar ningún archivo .py intermedio.

Uso
---
    python hunter.py <archivo.hxh>
    python hunter.py <archivo.hxh> --verbose
"""

import argparse
import os
import sys

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.DiagnosticErrorListener import DiagnosticErrorListener

from IndentLexer        import IndentLexer
from HunterParser       import HunterParser
from HunterEvalVisitor  import HunterEvalVisitor


def run(source: str, verbose: bool = False):
    input_stream = InputStream(source)

    # Lexing
    lexer = IndentLexer(input_stream)
    lexer.addErrorListener(DiagnosticErrorListener())
    tokens = CommonTokenStream(lexer)

    # Parsing
    parser = HunterParser(tokens)
    parser.addErrorListener(DiagnosticErrorListener())
    tree = parser.program()

    if verbose:
        print("─── Parse Tree ───────────────────────────────")
        print(tree.toStringTree(recog=parser))
        print("──────────────────────────────────────────────\n")

    # Ejecución directa
    interpreter = HunterEvalVisitor()
    interpreter.visit(tree)


def main():
    ap = argparse.ArgumentParser(description="Intérprete Hunter — ejecuta archivos .hxh directamente")
    ap.add_argument("source",          help="Archivo fuente .hxh")
    ap.add_argument("-v", "--verbose", action="store_true", help="Muestra el árbol de análisis")
    args = ap.parse_args()

    if not os.path.isfile(args.source):
        print(f"Error: '{args.source}' no encontrado.", file=sys.stderr)
        sys.exit(1)

    with open(args.source, encoding="utf-8") as fh:
        source_text = fh.read()

    try:
        run(source_text, verbose=args.verbose)
    except Exception as exc:
        print(f"\nError en tiempo de ejecución: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
