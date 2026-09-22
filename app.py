import streamlit as st


# ============================================================
# CONFIGURACIÓN GENERAL DE LA APLICACIÓN
# ============================================================

st.set_page_config(
    page_title="MENFA PVT",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# INFORMACIÓN DEL SISTEMA
# ============================================================

VERSION = "0.1.0"
NOMBRE_SISTEMA = "MENFA PVT"
DESCRIPCION = "Sistema de Caracterización y Análisis PVT"


# ============================================================
# ENCABEZADO
# ============================================================

st.title("🛢️ MENFA PVT")

st.subheader(
    "Sistema de Caracterización y Análisis PVT"
)

st.write(
    "Plataforma modular para el análisis de propiedades "
    "de fluidos de petróleo y gas."
)


# ============================================================
# ESTADO DEL SISTEMA
# ============================================================

st.divider()

columna1, columna2, columna3 = st.columns(3)

with columna1:
    st.metric(
        label="Estado del sistema",
        value="OPERATIVO"
    )

with columna2:
    st.metric(
        label="Versión",
        value=VERSION
    )

with columna3:
    st.metric(
        label="Módulos activos",
        value="0"
    )


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

st.divider()

st.header("Módulos")

st.info(
    "El sistema se encuentra en etapa inicial de desarrollo. "
    "Los módulos serán incorporados progresivamente."
)


st.markdown(
    """
    ### Próximos módulos

    **01 — Gestión de Fluidos**  
    Creación, edición y almacenamiento de fluidos.

    **02 — Componentes**  
    Base de datos de componentes hidrocarbonados.

    **03 — Propiedades PVT**  
    Cálculo de propiedades mediante correlaciones.

    **04 — Ecuaciones de Estado**  
    Modelado termodinámico mediante EOS.

    **05 — Equilibrio de Fases**  
    Cálculos de equilibrio líquido-vapor.

    **06 — Envolvente de Fases**  
    Análisis del comportamiento de fases.

    **07 — Laboratorio PVT**  
    Gestión y comparación de datos experimentales.

    **08 — Escenarios**  
    Simulación y análisis de sensibilidad.

    **09 — Informes**  
    Generación de informes técnicos.
    """
)


# ============================================================
# PIE DE APLICACIÓN
# ============================================================

st.divider()

st.caption(
    f"{NOMBRE_SISTEMA} | Versión {VERSION} | MENFA Capacitaciones"
)
