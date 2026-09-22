# ============================================================
# MENFA PVT
# Biblioteca de componentes
# ============================================================

from modelos.componente import Componente


# ============================================================
# HIDROCARBUROS LIVIANOS
# ============================================================

METANO = Componente(
    nombre="Metano",
    formula="CH4",
    peso_molecular=16.043,
    temperatura_critica=190.56,
    presion_critica=45.99,
    factor_acenico=0.0115,
    numero_componente="C1",
)


ETANO = Componente(
    nombre="Etano",
    formula="C2H6",
    peso_molecular=30.070,
    temperatura_critica=305.32,
    presion_critica=48.72,
    factor_acenico=0.0995,
    numero_componente="C2",
)


PROPANO = Componente(
    nombre="Propano",
    formula="C3H8",
    peso_molecular=44.097,
    temperatura_critica=369.83,
    presion_critica=42.48,
    factor_acenico=0.1524,
    numero_componente="C3",
)


ISOBUTANO = Componente(
    nombre="Isobutano",
    formula="i-C4H10",
    peso_molecular=58.124,
    temperatura_critica=407.81,
    presion_critica=36.48,
    factor_acenico=0.1840,
    numero_componente="i-C4",
)


N_BUTANO = Componente(
    nombre="n-Butano",
    formula="n-C4H10",
    peso_molecular=58.124,
    temperatura_critica=425.12,
    presion_critica=37.96,
    factor_acenico=0.2002,
    numero_componente="n-C4",
)


# ============================================================
# OTROS COMPONENTES
# ============================================================

DIOXIDO_CARBONO = Componente(
    nombre="Dióxido de carbono",
    formula="CO2",
    peso_molecular=44.010,
    temperatura_critica=304.13,
    presion_critica=73.77,
    factor_acenico=0.2239,
    numero_componente="CO2",
)


NITROGENO = Componente(
    nombre="Nitrógeno",
    formula="N2",
    peso_molecular=28.014,
    temperatura_critica=126.20,
    presion_critica=33.98,
    factor_acenico=0.0372,
    numero_componente="N2",
)


HIDROGENO_SULFURADO = Componente(
    nombre="Sulfuro de hidrógeno",
    formula="H2S",
    peso_molecular=34.081,
    temperatura_critica=373.53,
    presion_critica=89.63,
    factor_acenico=0.1005,
    numero_componente="H2S",
)


# ============================================================
# BIBLIOTECA
# ============================================================

BIBLIOTECA_COMPONENTES = {
    "C1": METANO,
    "C2": ETANO,
    "C3": PROPANO,
    "i-C4": ISOBUTANO,
    "n-C4": N_BUTANO,
    "CO2": DIOXIDO_CARBONO,
    "N2": NITROGENO,
    "H2S": HIDROGENO_SULFURADO,
}
