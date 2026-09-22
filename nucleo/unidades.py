# ============================================================
# MENFA PVT
# Conversión de unidades
# ============================================================

from nucleo.constantes import (
    PA_POR_KPA,
    PA_POR_BAR,
    PA_POR_PSI,
    PSI_POR_BAR,
    BAR_POR_PSI,
    CELSIUS_A_KELVIN,
    M3_POR_BARRIL,
    PIES3_POR_M3,
    METROS_POR_PIE,
)


# ============================================================
# PRESIÓN
# ============================================================

def psi_a_pa(presion_psi: float) -> float:
    """Convierte psi a Pa."""
    return presion_psi * PA_POR_PSI


def pa_a_psi(presion_pa: float) -> float:
    """Convierte Pa a psi."""
    return presion_pa / PA_POR_PSI


def bar_a_pa(presion_bar: float) -> float:
    """Convierte bar a Pa."""
    return presion_bar * PA_POR_BAR


def pa_a_bar(presion_pa: float) -> float:
    """Convierte Pa a bar."""
    return presion_pa / PA_POR_BAR


def kpa_a_pa(presion_kpa: float) -> float:
    """Convierte kPa a Pa."""
    return presion_kpa * PA_POR_KPA


def pa_a_kpa(presion_pa: float) -> float:
    """Convierte Pa a kPa."""
    return presion_pa / PA_POR_KPA


def psi_a_bar(presion_psi: float) -> float:
    """Convierte psi a bar."""
    return presion_psi * BAR_POR_PSI


def bar_a_psi(presion_bar: float) -> float:
    """Convierte bar a psi."""
    return presion_bar * PSI_POR_BAR


# ============================================================
# TEMPERATURA
# ============================================================

def celsius_a_kelvin(temperatura_c: float) -> float:
    """Convierte °C a K."""
    return temperatura_c + CELSIUS_A_KELVIN


def kelvin_a_celsius(temperatura_k: float) -> float:
    """Convierte K a °C."""
    return temperatura_k - CELSIUS_A_KELVIN


def fahrenheit_a_celsius(temperatura_f: float) -> float:
    """Convierte °F a °C."""
    return (temperatura_f - 32.0) * 5.0 / 9.0


def celsius_a_fahrenheit(temperatura_c: float) -> float:
    """Convierte °C a °F."""
    return temperatura_c * 9.0 / 5.0 + 32.0


def fahrenheit_a_kelvin(temperatura_f: float) -> float:
    """Convierte °F a K."""
    celsius = fahrenheit_a_celsius(temperatura_f)
    return celsius_a_kelvin(celsius)


def kelvin_a_fahrenheit(temperatura_k: float) -> float:
    """Convierte K a °F."""
    celsius = kelvin_a_celsius(temperatura_k)
    return celsius_a_fahrenheit(celsius)


# ============================================================
# VOLUMEN
# ============================================================

def barril_a_m3(volumen_barril: float) -> float:
    """Convierte barriles a m³."""
    return volumen_barril * M3_POR_BARRIL


def m3_a_barril(volumen_m3: float) -> float:
    """Convierte m³ a barriles."""
    return volumen_m3 / M3_POR_BARRIL


def m3_a_pies3(volumen_m3: float) -> float:
    """Convierte m³ a pies cúbicos."""
    return volumen_m3 * PIES3_POR_M3


def pies3_a_m3(volumen_pies3: float) -> float:
    """Convierte pies cúbicos a m³."""
    return volumen_pies3 / PIES3_POR_M3


# ============================================================
# LONGITUD
# ============================================================

def pie_a_metro(longitud_pie: float) -> float:
    """Convierte pies a metros."""
    return longitud_pie * METROS_POR_PIE


def metro_a_pie(longitud_metro: float) -> float:
    """Convierte metros a pies."""
    return longitud_metro / METROS_POR_PIE
