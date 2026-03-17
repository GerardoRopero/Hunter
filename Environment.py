"""
Environment.py
~~~~~~~~~~~~~~
Maneja los entornos (scopes) de variables y funciones del intérprete Hunter.
Las funciones matemáticas ya no están aquí, están en stdlib.hxh
escritas en Hunter puro.
"""


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
