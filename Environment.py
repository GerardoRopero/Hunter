"""
Environment.py
~~~~~~~~~~~~~~
Maneja los entornos (scopes) de variables y funciones del intérprete Hunter.
Cada llamada a función o bloque crea un entorno hijo que hereda del padre.
"""


class Environment:
    def __init__(self, parent=None):
        self._store  = {}       # variables de este scope
        self._parent = parent   # scope padre (None = global)

    # ── Variables ──────────────────────────────────────────────────────────
    def get(self, name: str):
        if name in self._store:
            return self._store[name]
        if self._parent is not None:
            return self._parent.get(name)
        raise NameError(f"Variable no definida: '{name}'")

    def set(self, name: str, value):
        """Crea o actualiza la variable en el scope actual."""
        self._store[name] = value

    def assign(self, name: str, value):
        """
        Actualiza una variable ya existente buscando hacia arriba en la
        cadena de scopes.  Si no existe la crea en el scope actual.
        """
        if name in self._store:
            self._store[name] = value
        elif self._parent is not None:
            try:
                self._parent.assign(name, value)
            except NameError:
                self._store[name] = value
        else:
            self._store[name] = value

    # ── Funciones ─────────────────────────────────────────────────────────
    def define_function(self, name: str, params: list, body_ctx, closure):
        """Guarda la definición de una función."""
        self._store[name] = HunterFunction(name, params, body_ctx, closure)

    def get_function(self, name: str):
        val = self.get(name)
        if not isinstance(val, HunterFunction):
            raise TypeError(f"'{name}' no es una función")
        return val

    # ── Utilidades ────────────────────────────────────────────────────────
    def child(self):
        """Crea un entorno hijo que hereda de este."""
        return Environment(parent=self)

    def __repr__(self):
        return f"Environment({self._store}, parent={self._parent is not None})"


class HunterFunction:
    """Representa una función definida en código Hunter."""
    def __init__(self, name: str, params: list, body_ctx, closure: Environment):
        self.name      = name
        self.params    = params    # lista de strings con los nombres
        self.body_ctx  = body_ctx  # nodo BlockContext del parser
        self.closure   = closure   # entorno donde fue definida

    def __repr__(self):
        return f"<función Hunter '{self.name}({', '.join(self.params)})' >"


class ReturnException(Exception):
    """Se lanza con 'return' para salir de una función."""
    def __init__(self, value):
        self.value = value
