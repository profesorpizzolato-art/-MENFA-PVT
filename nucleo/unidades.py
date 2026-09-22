# ============================================================
# MENFA PVT
# Conversión de unidades
# ============================================================

from nucleo.constantes import (
    PA_POR_KPA,
    PA_POR_BAR,
    PA_POR_MPA,
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
    return presion_psi * PA_POR_PSI


def pa_a_psi(presion_pa: float) -> float:
    return presion_pa / PA_POR_PSI


def bar_a_pa(presion_bar: float) -> float:
    return presion_bar * PA_POR_BAR


def pa_a_bar(presion_pa: float) -> float:
    return presion_pa / PA_POR_BAR


def mpa_a_pa(presion_mpa: float) -> float:
    return presion_mpa * PA_POR_MPA


def pa_a_mpa(presion_pa: float) -> float:
    return presion_pa / PA_POR_MPA


def kpa_a_pa(presion_kpa: float) -> float:
    return presion_kpa * PA_POR_KPA


def pa_a_kpa(presion_pa: float) -> float:
    return presion_pa / PA_POR_KPA


def psi_a_bar(presion_psi: float) -> float:
    return presion_psi * BAR_POR_PSI


def bar_a_psi(presion_bar: float) -> float:
    return presion_bar * PSI_POR_BAR


# ============================================================
# TEMPERATURA
# ============================================================

def celsius_a_kelvin(temperatura_c: float) -> float:
    return temperatura_c + CELSIUS_A_KELVIN


def kelvin_a_celsius(temperatura_k: float) -> float:
    return temperatura_k - CELSIUS_A_KELVIN


def fahrenheit_a_celsius(temperatura_f: float) -> float:
    return (temperatura_f - 32.0) * 5.0 / 9.0


def celsius_a_fahrenheit(temperatura_c: float) -> float:
    return temperatura_c * 9.0 / 5.0 + 32.0


def fahrenheit_a_kelvin(temperatura_f: float) -> float:
    return celsius_a_kelvin(
        fahrenheit_a_celsius(temperatura_f)
    )


def kelvin_a_fahrenheit(temperatura_k: float) -> float:
    return celsius_a_fahrenheit(
        kelvin_a_celsius(temperatura_k)
    )


# ============================================================
# VOLUMEN
# ============================================================

def barril_a_m3(volumen_barril: float) -> float:
    return volumen_barril * M3_POR_BARRIL


def m3_a_barril(volumen_m3: float) -> float:
    return volumen_m3 / M3_POR_BARRIL


def m3_a_pies3(volumen_m3: float) -> float:
    return volumen_m3 * PIES3_POR_M3


def pies3_a_m3(volumen_pies3: float) -> float:
    return volumen_pies3 / PIES3_POR_M3


# ============================================================
# LONGITUD
# ============================================================

def pie_a_metro(longitud_pie: float) -> float:
    return longitud_pie * METROS_POR_PIE


def metro_a_pie(longitud_metro: float) -> float:
    return longitud_metro / METROS_POR_PIE
