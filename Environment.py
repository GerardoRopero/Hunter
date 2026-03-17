"""
Environment.py
~~~~~~~~~~~~~~
Maneja los entornos (scopes) de variables y funciones del intérprete Hunter.
Incluye implementación desde cero de:
  - Funciones trigonométricas (sin, cos, tan)
  - Raíz cuadrada (sqrt)
  - Valor absoluto (abs)
  - Logaritmos (log, log2, log10)
  - Exponencial (exp)
Sin usar ninguna librería externa.
"""


# ─────────────────────────────────────────────
#  CONSTANTES MATEMÁTICAS
# ─────────────────────────────────────────────

PI  = 3.14159265358979323846
E   = 2.71828182845904523536


# ─────────────────────────────────────────────
#  FUNCIONES AUXILIARES INTERNAS
# ─────────────────────────────────────────────

def _factorial(n: int) -> int:
    """Factorial iterativo de n."""
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def _normalizar_angulo(x: float) -> float:
    """
    Reduce x al rango [-π, π] para que la serie de Taylor
    converja más rápido y con mayor precisión.
    """
    dos_pi = 2.0 * PI
    x = x % dos_pi
    if x > PI:
        x -= dos_pi
    return x


# ─────────────────────────────────────────────
#  TRIGONOMÉTRICAS (Series de Taylor)
# ─────────────────────────────────────────────

def hunter_sin(x: float, terminos: int = 20) -> float:
    """
    Seno usando serie de Taylor:
    sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + ...
    """
    x         = _normalizar_angulo(x)
    resultado = 0.0
    for n in range(terminos):
        exponente  = 2 * n + 1
        signo      = (-1) ** n
        resultado += signo * (x ** exponente) / _factorial(exponente)
    return resultado


def hunter_cos(x: float, terminos: int = 20) -> float:
    """
    Coseno usando serie de Taylor:
    cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ...
    """
    x         = _normalizar_angulo(x)
    resultado = 0.0
    for n in range(terminos):
        exponente  = 2 * n
        signo      = (-1) ** n
        resultado += signo * (x ** exponente) / _factorial(exponente)
    return resultado


def hunter_tan(x: float) -> float:
    """Tangente = sin(x) / cos(x)"""
    cos_x = hunter_cos(x)
    if cos_x < 0:
        cos_x_abs = -cos_x
    else:
        cos_x_abs = cos_x
    if cos_x_abs < 1e-10:
        raise ZeroDivisionError("tan(x) no está definida para este valor")
    return hunter_sin(x) / cos_x


# ─────────────────────────────────────────────
#  RAÍZ CUADRADA (Método de Newton-Raphson)
# ─────────────────────────────────────────────

def hunter_sqrt(x: float) -> float:
    """
    Raíz cuadrada usando el método de Newton-Raphson:
      estimado = (estimado + x / estimado) / 2
    Converge muy rápido, en ~50 iteraciones es extremadamente preciso.
    """
    if x < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    if x == 0:
        return 0.0
    estimado = x / 2.0
    for _ in range(50):
        estimado = (estimado + x / estimado) / 2.0
    return estimado


# ─────────────────────────────────────────────
#  VALOR ABSOLUTO
# ─────────────────────────────────────────────

def hunter_abs(x: float) -> float:
    """Valor absoluto de x."""
    if x < 0:
        return -x
    return x


# ─────────────────────────────────────────────
#  EXPONENCIAL (Serie de Taylor)
# ─────────────────────────────────────────────

def hunter_exp(x: float, terminos: int = 50) -> float:
    """
    e^x usando serie de Taylor:
    e^x = 1 + x + x²/2! + x³/3! + x⁴/4! + ...
    """
    resultado = 0.0
    for n in range(terminos):
        resultado += (x ** n) / _factorial(n)
    return resultado


# ─────────────────────────────────────────────
#  LOGARITMOS
# ─────────────────────────────────────────────

def hunter_log(x: float, terminos: int = 1000) -> float:
    """
    Logaritmo natural ln(x) usando la serie de Taylor.
    Usa la identidad: ln(x) = 2 * arctanh((x-1)/(x+1))
    que converge para todo x > 0 y es más estable que
    la serie directa.

    arctanh(y) = y + y³/3 + y⁵/5 + y⁷/7 + ...
    """
    if x <= 0:
        raise ValueError("El logaritmo no está definido para x <= 0")
    if x == 1:
        return 0.0

    # Reducción de rango: si x es muy grande o muy pequeño
    # usamos ln(x) = ln(x/E^k) + k para acercar x a 1
    k = 0
    while x > 2.0:
        x  = x / E
        k += 1
    while x < 0.5:
        x  = x * E
        k -= 1

    # Serie: ln(x) = 2 * arctanh((x-1)/(x+1))
    y         = (x - 1.0) / (x + 1.0)
    y2        = y * y
    resultado = 0.0
    termino   = y
    for n in range(terminos):
        resultado += termino / (2 * n + 1)
        termino   *= y2

    return 2.0 * resultado + k


def hunter_log2(x: float) -> float:
    """
    Logaritmo en base 2.
    log2(x) = ln(x) / ln(2)
    """
    return hunter_log(x) / hunter_log(2.0)


def hunter_log10(x: float) -> float:
    """
    Logaritmo en base 10.
    log10(x) = ln(x) / ln(10)
    """
    return hunter_log(x) / hunter_log(10.0)


def hunter_logb(x: float, base: float) -> float:
    """
    Logaritmo en base arbitraria.
    logb(x, base) = ln(x) / ln(base)
    """
    if base <= 0 or base == 1:
        raise ValueError("La base del logaritmo debe ser positiva y distinta de 1")
    return hunter_log(x) / hunter_log(base)


# ─────────────────────────────────────────────
#  ENVIRONMENT
# ─────────────────────────────────────────────

class Environment:
    def __init__(self, parent=None):
        self._store  = {}
        self._parent = parent

    # ── Variables ─────────────────────────────────────────────────────────
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

    # ── Funciones ─────────────────────────────────────────────────────────
    def define_function(self, name: str, params: list, body_ctx, closure):
        self._store[name] = HunterFunction(name, params, body_ctx, closure)

    def get_function(self, name: str):
        val = self.get(name)
        if not isinstance(val, HunterFunction):
            raise TypeError(f"'{name}' no es una función")
        return val

    # ── Utilidades ────────────────────────────────────────────────────────
    def child(self):
        return Environment(parent=self)

    def __repr__(self):
        return f"Environment({self._store}, parent={self._parent is not None})"


class HunterFunction:
    def __init__(self, name: str, params: list, body_ctx, closure: Environment):
        self.name     = name
        self.params   = params
        self.body_ctx = body_ctx
        self.closure  = closure

    def __repr__(self):
        return f"<función Hunter '{self.name}({', '.join(self.params)})'>"


class ReturnException(Exception):
    def __init__(self, value):
        self.value = value
