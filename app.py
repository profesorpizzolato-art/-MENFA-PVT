import streamlit as st

from nucleo.configuracion import (
    NOMBRE_SISTEMA,
    NOMBRE_COMPLETO,
    DESCRIPCION,
    VERSION,
    EMPRESA,
    ICONO,
    DISEÑO_PAGINA,
    MENU_LATERAL_ABIERTO,
)

# ============================================================
# CONFIGURACIÓN DE STREAMLIT
# ============================================================

st.set_page_config(
    page_title=NOMBRE_SISTEMA,
    page_icon=ICONO,
    layout=DISEÑO_PAGINA,
    initial_sidebar_state=(
        "expanded"
        if MENU_LATERAL_ABIERTO
        else "collapsed"
    ),
)

# ============================================================
# ENCABEZADO
# ============================================================

st.title(f"{ICONO} {NOMBRE_SISTEMA}")

st.subheader(NOMBRE_COMPLETO)

st.write(DESCRIPCION)

# ============================================================
# ESTADO DEL SISTEMA
# ============================================================

st.divider()

columna1, columna2, columna3 = st.columns(3)

with columna1:
    st.metric(
        label="Estado del sistema",
        value="OPERATIVO",
    )

with columna2:
    st.metric(
        label="Versión",
        value=VERSION,
    )

with columna3:
    st.metric(
        label="Módulos activos",
        value="0",
    )

# ============================================================
# MÓDULOS
# ============================================================

st.divider()

st.header("Módulos")

st.info(
    "MENFA PVT se encuentra en etapa inicial de desarrollo. "
    "Los módulos serán incorporados progresivamente."
)

modulos = [
    ("01", "Gestión de Fluidos"),
    ("02", "Componentes"),
    ("03", "Propiedades PVT"),
    ("04", "Ecuaciones de Estado"),
    ("05", "Equilibrio de Fases"),
    ("06", "Envolvente de Fases"),
    ("07", "Laboratorio PVT"),
    ("08", "Escenarios"),
    ("09", "Informes"),
]

for numero, nombre in modulos:
    st.write(f"**{numero} — {nombre}**")

# ============================================================
# PIE DE APLICACIÓN
# ============================================================

st.divider()

st.caption(
    f"{NOMBRE_SISTEMA} | Versión {VERSION} | {EMPRESA}"
)
