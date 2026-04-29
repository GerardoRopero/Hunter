"""
Environment.py
~~~~~~~~~~~~~~
Maneja los entornos (scopes) de variables y funciones del intérprete Hunter.
Las funciones matemáticas están en stdlib.hxh escrita en Hunter puro.
Las funciones de sistema (archivos) están aquí porque requieren acceso al SO.
"""

import os


# ─────────────────────────────────────────────
#  MANEJO DE ARCHIVOS
# ─────────────────────────────────────────────

def hunter_abrir(ruta: str, modo: str = "r"):
    """Lee un archivo y devuelve su contenido como string."""
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
    """Escribe contenido en un archivo. Si existe lo sobreescribe."""
    try:
        with open(ruta, mode="w", encoding="utf-8") as fh:
            fh.write(str(contenido))
    except Exception as exc:
        raise RuntimeError(f"Error al escribir archivo: {exc}")


def hunter_agregar(ruta: str, contenido: str):
    """Agrega contenido al final de un archivo sin borrar lo anterior."""
    try:
        with open(ruta, mode="a", encoding="utf-8") as fh:
            fh.write(str(contenido))
    except Exception as exc:
        raise RuntimeError(f"Error al agregar al archivo: {exc}")


def hunter_existe(ruta: str) -> bool:
    """Devuelve True si el archivo existe, False si no."""
    return os.path.isfile(ruta)


def hunter_lineas(ruta: str) -> list:
    """Lee un archivo y devuelve una lista con cada línea."""
    try:
        with open(ruta, encoding="utf-8") as fh:
            return [linea.rstrip("\n") for linea in fh.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Archivo no encontrado: '{ruta}'")


# ─────────────────────────────────────────────
#  ENVIRONMENT
# ─────────────────────────────────────────────

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


# ─────────────────────────────────────────────
#  GRAFICACIÓN
# ─────────────────────────────────────────────


# ─────────────────────────────────────────────
#  GRAFICACIÓN
#  Todas las funciones guardan la imagen en
#  disco porque el entorno no tiene pantalla.
# ─────────────────────────────────────────────

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def hunter_grafica_guardar(xs, ys, ruta, titulo="", etiqueta_x="", etiqueta_y=""):
    """Grafica una línea y guarda la imagen en disco."""
    try:
        plt.figure()
        plt.plot(xs, ys, marker='o')
        plt.title(titulo)
        plt.xlabel(etiqueta_x)
        plt.ylabel(etiqueta_y)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(ruta)
        plt.close()
        print(f"Grafica guardada en: {ruta}")
    except Exception as exc:
        raise RuntimeError(f"Error al graficar: {exc}")


def hunter_grafica_puntos_guardar(xs, ys, ruta, titulo="", etiqueta_x="", etiqueta_y=""):
    """Grafica puntos dispersos y guarda la imagen."""
    try:
        plt.figure()
        plt.scatter(xs, ys)
        plt.title(titulo)
        plt.xlabel(etiqueta_x)
        plt.ylabel(etiqueta_y)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(ruta)
        plt.close()
        print(f"Grafica guardada en: {ruta}")
    except Exception as exc:
        raise RuntimeError(f"Error al graficar: {exc}")


def hunter_grafica_barras_guardar(etiquetas, valores, ruta, titulo="", etiqueta_x="", etiqueta_y=""):
    """Grafica barras y guarda la imagen."""
    try:
        plt.figure()
        plt.bar(etiquetas, valores)
        plt.title(titulo)
        plt.xlabel(etiqueta_x)
        plt.ylabel(etiqueta_y)
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig(ruta)
        plt.close()
        print(f"Grafica guardada en: {ruta}")
    except Exception as exc:
        raise RuntimeError(f"Error al graficar: {exc}")


def hunter_grafica_histograma_guardar(datos, bins, ruta, titulo="", etiqueta_x="", etiqueta_y=""):
    """Grafica un histograma y guarda la imagen."""
    try:
        plt.figure()
        plt.hist(datos, bins=bins)
        plt.title(titulo)
        plt.xlabel(etiqueta_x)
        plt.ylabel(etiqueta_y)
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig(ruta)
        plt.close()
        print(f"Grafica guardada en: {ruta}")
    except Exception as exc:
        raise RuntimeError(f"Error al graficar: {exc}")


def hunter_grafica_dos_lineas_guardar(xs, ys1, ys2, etiq1, etiq2, ruta, titulo="", etiqueta_x="", etiqueta_y=""):
    """Grafica dos líneas comparadas y guarda la imagen."""
    try:
        plt.figure()
        plt.plot(xs, ys1, marker='o', label=etiq1)
        plt.plot(xs, ys2, marker='s', label=etiq2)
        plt.title(titulo)
        plt.xlabel(etiqueta_x)
        plt.ylabel(etiqueta_y)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(ruta)
        plt.close()
        print(f"Grafica guardada en: {ruta}")
    except Exception as exc:
        raise RuntimeError(f"Error al graficar: {exc}")


# ─────────────────────────────────────────────
#  LECTURA DE CSV
# ─────────────────────────────────────────────

def hunter_leer_csv(ruta: str) -> list:
    """
    Lee un archivo CSV y devuelve una lista de listas.
    La primera fila se trata como encabezados y se omite.
    Cada fila siguiente es una lista de valores.
    Los números se convierten automáticamente a int o float.
    """
    try:
        filas = []
        with open(ruta, encoding="utf-8") as fh:
            lineas = fh.readlines()
        # saltar encabezado (primera línea)
        for linea in lineas[1:]:
            linea = linea.strip()
            if linea == "":
                continue
            celdas = linea.split(",")
            fila   = []
            for celda in celdas:
                celda = celda.strip()
                try:
                    if "." in celda:
                        fila.append(float(celda))
                    else:
                        fila.append(int(celda))
                except ValueError:
                    fila.append(celda)
            filas.append(fila)
        return filas
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV no encontrado: '{ruta}'")
    except Exception as exc:
        raise RuntimeError(f"Error al leer CSV: {exc}")


def hunter_csv_columna(datos: list, col: int) -> list:
    """Extrae una columna específica de los datos del CSV."""
    return [fila[col] for fila in datos]


def hunter_leer_csv_encabezados(ruta: str) -> list:
    """Devuelve solo los encabezados del CSV como lista de strings."""
    try:
        with open(ruta, encoding="utf-8") as fh:
            primera = fh.readline().strip()
        return [h.strip() for h in primera.split(",")]
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV no encontrado: '{ruta}'")
