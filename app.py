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

from nucleo.unidades import (
    psi_a_bar,
    bar_a_psi,
    celsius_a_kelvin,
    kelvin_a_celsius,
    barril_a_m3,
    m3_a_barril,
    pie_a_metro,
    metro_a_pie,
)


# ============================================================
# CONFIGURACIÓN
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
        value="1",
    )


# ============================================================
# MÓDULOS
# ============================================================

st.divider()

st.header("Módulos")

modulos = [
    ("00", "Núcleo del Sistema", "Activo"),
    ("01", "Gestión de Fluidos", "En desarrollo"),
    ("02", "Componentes", "Planificado"),
    ("03", "Propiedades PVT", "Planificado"),
    ("04", "Ecuaciones de Estado", "Planificado"),
    ("05", "Equilibrio de Fases", "Planificado"),
    ("06", "Envolvente de Fases", "Planificado"),
    ("07", "Laboratorio PVT", "Planificado"),
    ("08", "Escenarios", "Planificado"),
    ("09", "Informes", "Planificado"),
]

for numero, nombre, estado in modulos:
    if estado == "Activo":
        st.success(f"**{numero} — {nombre}** | {estado}")
    elif estado == "En desarrollo":
        st.warning(f"**{numero} — {nombre}** | {estado}")
    else:
        st.info(f"**{numero} — {nombre}** | {estado}")


# ============================================================
# HERRAMIENTAS
# ============================================================

st.divider()

st.header("Herramientas")

st.subheader("Conversor de Unidades")

tipo_conversion = st.selectbox(
    "Tipo de conversión",
    [
        "Presión",
        "Temperatura",
        "Volumen",
        "Longitud",
    ],
)


# ============================================================
# PRESIÓN
# ============================================================

if tipo_conversion == "Presión":

    valor = st.number_input(
        "Valor",
        min_value=0.0,
        value=100.0,
        step=1.0,
    )

    unidad = st.selectbox(
        "Unidad de origen",
        ["psi", "bar"],
    )

    if unidad == "psi":

        resultado = psi_a_bar(valor)

        st.success(
            f"{valor:.4f} psi = {resultado:.4f} bar"
        )

    else:

        resultado = bar_a_psi(valor)

        st.success(
            f"{valor:.4f} bar = {resultado:.4f} psi"
        )


# ============================================================
# TEMPERATURA
# ============================================================

elif tipo_conversion == "Temperatura":

    valor = st.number_input(
        "Valor",
        value=25.0,
        step=1.0,
    )

    unidad = st.selectbox(
        "Unidad de origen",
        ["°C", "K"],
    )

    if unidad == "°C":

        resultado = celsius_a_kelvin(valor)

        st.success(
            f"{valor:.2f} °C = {resultado:.2f} K"
        )

    else:

        resultado = kelvin_a_celsius(valor)

        st.success(
            f"{valor:.2f} K = {resultado:.2f} °C"
        )


# ============================================================
# VOLUMEN
# ============================================================

elif tipo_conversion == "Volumen":

    valor = st.number_input(
        "Valor",
        min_value=0.0,
        value=1.0,
        step=1.0,
    )

    unidad = st.selectbox(
        "Unidad de origen",
        ["bbl", "m³"],
    )

    if unidad == "bbl":

        resultado = barril_a_m3(valor)

        st.success(
            f"{valor:.4f} bbl = {resultado:.6f} m³"
        )

    else:

        resultado = m3_a_barril(valor)

        st.success(
            f"{valor:.4f} m³ = {resultado:.4f} bbl"
        )


# ============================================================
# LONGITUD
# ============================================================

elif tipo_conversion == "Longitud":

    valor = st.number_input(
        "Valor",
        min_value=0.0,
        value=1.0,
        step=1.0,
    )

    unidad = st.selectbox(
        "Unidad de origen",
        ["ft", "m"],
    )

    if unidad == "ft":

        resultado = pie_a_metro(valor)

        st.success(
            f"{valor:.4f} ft = {resultado:.4f} m"
        )

    else:

        resultado = metro_a_pie(valor)

        st.success(
            f"{valor:.4f} m = {resultado:.4f} ft"
        )


# ============================================================
# PIE
# ============================================================

st.divider()

st.caption(
    f"{NOMBRE_SISTEMA} | Versión {VERSION} | {EMPRESA}"
)
