# ============================================================
# MENFA PVT
# Validadores del sistema
# ============================================================

from nucleo.constantes import (
    TEMPERATURA_MINIMA_K,
    TEMPERATURA_MAXIMA_K,
    PRESION_MINIMA_PA,
    PRESION_MAXIMA_PA,
)


# ============================================================
# VALIDACIÓN GENERAL
# ============================================================

def validar_numero(
    valor: float,
    nombre: str = "Valor",
) -> None:
    """
    Verifica que el valor sea numérico.
    """

    if not isinstance(valor, (int, float)):
        raise ValueError(
            f"{nombre} debe ser un valor numérico."
        )


def validar_positivo(
    valor: float,
    nombre: str = "Valor",
) -> None:
    """
    Verifica que el valor sea mayor que cero.
    """

    validar_numero(valor, nombre)

    if valor <= 0:
        raise ValueError(
            f"{nombre} debe ser mayor que cero."
        )


def validar_no_negativo(
    valor: float,
    nombre: str = "Valor",
) -> None:
    """
    Verifica que el valor sea mayor o igual a cero.
    """

    validar_numero(valor, nombre)

    if valor < 0:
        raise ValueError(
            f"{nombre} no puede ser negativo."
        )


# ============================================================
# PRESIÓN
# ============================================================

def validar_presion_pa(
    presion_pa: float,
) -> None:
    """
    Valida una presión expresada en Pa.
    """

    validar_numero(
        presion_pa,
        "Presión",
    )

    if presion_pa < PRESION_MINIMA_PA:
        raise ValueError(
            "La presión está por debajo del "
            "límite permitido."
        )

    if presion_pa > PRESION_MAXIMA_PA:
        raise ValueError(
            "La presión supera el "
            "límite permitido."
        )


# ============================================================
# TEMPERATURA
# ============================================================

def validar_temperatura_k(
    temperatura_k: float,
) -> None:
    """
    Valida una temperatura expresada en Kelvin.
    """

    validar_numero(
        temperatura_k,
        "Temperatura",
    )

    if temperatura_k < TEMPERATURA_MINIMA_K:
        raise ValueError(
            "La temperatura está por debajo "
            "del límite permitido."
        )

    if temperatura_k > TEMPERATURA_MAXIMA_K:
        raise ValueError(
            "La temperatura supera el "
            "límite permitido."
        )


# ============================================================
# FRACCIONES
# ============================================================

def validar_fraccion(
    fraccion: float,
    nombre: str = "Fracción",
) -> None:
    """
    Valida una fracción entre 0 y 1.
    """

    validar_numero(fraccion, nombre)

    if fraccion < 0 or fraccion > 1:
        raise ValueError(
            f"{nombre} debe estar entre 0 y 1."
        )


# ============================================================
# COMPOSICIÓN
# ============================================================

def validar_composicion(
    composicion: dict,
    tolerancia: float = 1e-6,
) -> None:
    """
    Valida una composición de fracciones molares.

    La suma de las fracciones debe ser aproximadamente 1.
    """

    if not isinstance(composicion, dict):
        raise ValueError(
            "La composición debe ser un diccionario."
        )

    if not composicion:
        raise ValueError(
            "La composición no puede estar vacía."
        )

    suma = 0.0

    for componente, fraccion in composicion.items():

        validar_fraccion(
            fraccion,
            f"Fracción de {componente}",
        )

        suma += fraccion

    if abs(suma - 1.0) > tolerancia:
        raise ValueError(
            "La suma de las fracciones molares "
            f"debe ser 1. Actualmente es {suma:.8f}."
        )


# ============================================================
# RANGO
# ============================================================

def validar_rango(
    valor: float,
    minimo: float,
    maximo: float,
    nombre: str = "Valor",
) -> None:
    """
    Verifica que un valor esté dentro de un rango.
    """

    validar_numero(valor, nombre)

    if valor < minimo or valor > maximo:
        raise ValueError(
            f"{nombre} debe estar entre "
            f"{minimo} y {maximo}."
        )
