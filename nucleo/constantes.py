# ============================================================
# MENFA PVT
# Constantes técnicas del sistema
# ============================================================

"""
Este módulo contiene constantes físicas y factores de conversión
utilizados por MENFA PVT.

IMPORTANTE:
Las constantes se mantienen separadas de las ecuaciones para
facilitar su revisión, validación y mantenimiento.
"""


# ============================================================
# CONSTANTES FÍSICAS FUNDAMENTALES
# ============================================================

GRAVEDAD_ESTANDAR = 9.80665          # m/s²

CONSTANTE_GASES = 8.314462618        # J/(mol·K)

PRESION_ESTANDAR_PA = 101325.0       # Pa

TEMPERATURA_ESTANDAR_K = 288.15      # K (15 °C)


# ============================================================
# CONVERSIONES DE PRESIÓN
# ============================================================

PA_POR_KPA = 1000.0

PA_POR_BAR = 100000.0

PA_POR_PSI = 6894.757293168

PSI_POR_BAR = 14.5037737738

BAR_POR_PSI = 0.0689475729317


# ============================================================
# CONVERSIONES DE TEMPERATURA
# ============================================================

CELSIUS_A_KELVIN = 273.15


# ============================================================
# CONVERSIONES DE VOLUMEN
# ============================================================

LITROS_POR_M3 = 1000.0

LITROS_POR_BARRIL = 158.987294928

M3_POR_BARRIL = 0.158987294928

PIES3_POR_M3 = 35.3146667215


# ============================================================
# CONVERSIONES DE LONGITUD
# ============================================================

METROS_POR_PIE = 0.3048

PIES_POR_METRO = 3.28083989501


# ============================================================
# CONVERSIONES DE CAUDAL
# ============================================================

SEGUNDOS_POR_DIA = 86400.0


# ============================================================
# RANGOS GENERALES DE VALIDACIÓN
# ============================================================

TEMPERATURA_MINIMA_K = 100.0

TEMPERATURA_MAXIMA_K = 1000.0

PRESION_MINIMA_PA = 100.0

PRESION_MAXIMA_PA = 100000000.0
