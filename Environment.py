"""
Environment.py

Maneja los entornos (scopes) de variables y funciones del intérprete Hunter.
escritas en Hunter puro.
"""

# ─────────────────────────────────────────────
#  MANEJO DE ARCHIVOS
# ─────────────────────────────────────────────

def hunter_abrir(ruta: str, modo: str = "r"):
    """
    Abre un archivo y devuelve su contenido.
    modo "r" → lectura
    modo "w" → escritura (borra el contenido anterior)
    modo "a" → append (agrega al final)
    """
    try:
        with open(ruta, mode=modo, encoding="utf-8") as fh:
            if modo == "r":
                return fh.read()
            return None
    except FileNotFoundError:
        raise FileNotFoundError(f"Archivo no encontrado: '{ruta}'")
    except Exception as exc:
        raise RuntimeError(f"Error al abrir archivo: {exc}")


def hunter_escribir(ruta: str, contenido: str):
    """
    Escribe contenido en un archivo.
    Si el archivo no existe lo crea.
    Si existe borra el contenido anterior.
    """
    try:
        with open(ruta, mode="w", encoding="utf-8") as fh:
            fh.write(str(contenido))
    except Exception as exc:
        raise RuntimeError(f"Error al escribir archivo: {exc}")


def hunter_agregar(ruta: str, contenido: str):
    """
    Agrega contenido al final de un archivo sin borrar lo anterior.
    Si el archivo no existe lo crea.
    """
    try:
        with open(ruta, mode="a", encoding="utf-8") as fh:
            fh.write(str(contenido))
    except Exception as exc:
        raise RuntimeError(f"Error al agregar al archivo: {exc}")


def hunter_existe(ruta: str) -> bool:
    """
    Devuelve True si el archivo existe, False si no.
    """
    import os
    return os.path.isfile(ruta)


def hunter_lineas(ruta: str) -> list:
    """
    Lee un archivo y devuelve una lista donde cada
    elemento es una línea del archivo.
    """
    try:
        with open(ruta, encoding="utf-8") as fh:
            return [linea.rstrip("\n") for linea in fh.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Archivo no encontrado: '{ruta}'")

class Environment:
    def __init__(self, parent=None):
        self._store  = {}
        self._parent = parent

    def get(self, name: str):
        if name in self._store:
            return self._store[name]
        if self._parent is not None:
            return self._parent.get(name)
        raise NameError(f"Variable no definida: '{name}'")

    def set(self, name: str, value):
        self._store[name] = value

    def assign(self, name: str, value):
        if name in self._store:
            self._store[name] = value
        elif self._parent is not None:
            try:
                self._parent.assign(name, value)
            except NameError:
                self._store[name] = value
        else:
            self._store[name] = value

    def define_function(self, name: str, params: list, body_ctx, closure):
        self._store[name] = HunterFunction(name, params, body_ctx, closure)

    def get_function(self, name: str):
        val = self.get(name)
        if not isinstance(val, HunterFunction):
            raise TypeError(f"'{name}' no es una función")
        return val

    def child(self):
        return Environment(parent=self)

    def __repr__(self):
        return f"Environment({self._store}, parent={self._parent is not None})"


class HunterFunction:
    def __init__(self, name: str, params: list, body_ctx, closure):
        self.name     = name
        self.params   = params
        self.body_ctx = body_ctx
        self.closure  = closure

    def __repr__(self):
        return f"<función Hunter '{self.name}({', '.join(self.params)})'>"


class ReturnException(Exception):
    def __init__(self, value):
        self.value = value
