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
from nucleo.validadores import (
    validar_presion_pa,
    validar_temperatura_k,
    validar_fraccion,
    validar_composicion,
)
from datos.componentes.biblioteca import (
    BIBLIOTECA_COMPONENTES,
)
from modelos.fluido import Fluido
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
# ============================================================
# VALIDACIÓN DE DATOS
# ============================================================

st.divider()

st.header("Validación de Datos")

st.write(
    "Herramientas para verificar la consistencia "
    "de los datos ingresados al sistema."
)

tipo_validacion = st.selectbox(
    "Tipo de validación",
    [
        "Presión",
        "Temperatura",
        "Fracción",
        "Composición molar",
    ],
)


if tipo_validacion == "Presión":

    from nucleo.unidades import psi_a_pa

    presion = st.number_input(
        "Presión [psi]",
        min_value=0.0,
        value=100.0,
    )

    if st.button("Validar presión"):

        try:

            presion_pa = psi_a_pa(presion)

            validar_presion_pa(
                presion_pa
            )

            st.success(
                "✓ Presión válida."
            )

        except ValueError as error:

            st.error(
                f"✗ {error}"
            )


elif tipo_validacion == "Temperatura":

    from nucleo.unidades import celsius_a_kelvin

    temperatura = st.number_input(
        "Temperatura [°C]",
        value=25.0,
    )

    if st.button("Validar temperatura"):

        try:

            temperatura_k = (
                celsius_a_kelvin(
                    temperatura
                )
            )

            validar_temperatura_k(
                temperatura_k
            )

            st.success(
                "✓ Temperatura válida."
            )

        except ValueError as error:

            st.error(
                f"✗ {error}"
            )


elif tipo_validacion == "Fracción":

    fraccion = st.number_input(
        "Fracción",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
    )

    if st.button("Validar fracción"):

        try:

            validar_fraccion(
                fraccion
            )

            st.success(
                "✓ Fracción válida."
            )

        except ValueError as error:

            st.error(
                f"✗ {error}"
            )


elif tipo_validacion == "Composición molar":

    st.write(
        "Ingrese una composición simplificada."
    )

    c1 = st.number_input(
        "C1 — Metano",
        min_value=0.0,
        max_value=1.0,
        value=0.70,
    )

    c2 = st.number_input(
        "C2 — Etano",
        min_value=0.0,
        max_value=1.0,
        value=0.10,
    )

    c3 = st.number_input(
        "C3 — Propano",
        min_value=0.0,
        max_value=1.0,
        value=0.05,
    )

    c7 = st.number_input(
        "C7+",
        min_value=0.0,
        max_value=1.0,
        value=0.15,
    )

    composicion = {
        "C1": c1,
        "C2": c2,
        "C3": c3,
        "C7+": c7,
    }

    suma = sum(composicion.values())

    st.write(
        f"**Suma de fracciones:** "
        f"{suma:.6f}"
    )

    if st.button("Validar composición"):

        try:

            validar_composicion(
                composicion
            )

            st.success(
                "✓ Composición válida. "
                "La suma de las fracciones es 1."
            )

        except ValueError as error:

            st.error(
                f"✗ {error}"
            )
# ============================================================
# BIBLIOTECA DE COMPONENTES
# ============================================================

st.divider()

st.header("Biblioteca de Componentes")

componente_seleccionado = st.selectbox(
    "Seleccionar componente",
    list(BIBLIOTECA_COMPONENTES.keys()),
)

componente = BIBLIOTECA_COMPONENTES[
    componente_seleccionado
]

st.subheader(componente.nombre)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Fórmula",
        componente.formula,
    )

with col2:
    st.metric(
        "Peso molecular",
        f"{componente.peso_molecular:.3f} g/mol",
    )

with col3:
    st.metric(
        "Factor acéntrico",
        f"{componente.factor_acenico:.4f}",
    )

col4, col5 = st.columns(2)

with col4:
    st.metric(
        "Temperatura crítica",
        f"{componente.temperatura_critica:.2f} K",
    )

with col5:
    st.metric(
        "Presión crítica",
        f"{componente.presion_critica:.2f} bar",
    )
# ============================================================
# CONSTRUCTOR DE FLUIDO PVT
# ============================================================

st.divider()

st.header("Constructor de Fluido PVT")

st.write(
    "Defina la composición molar del fluido "
    "para crear un modelo PVT."
)

nombre_fluido = st.text_input(
    "Nombre del fluido",
    value="FLUIDO-MENFA-001",
)

st.subheader("Composición molar")

col1, col2 = st.columns(2)

with col1:

    fraccion_c1 = st.number_input(
        "C1 — Metano",
        min_value=0.0,
        max_value=1.0,
        value=0.70,
        step=0.01,
    )

    fraccion_c2 = st.number_input(
        "C2 — Etano",
        min_value=0.0,
        max_value=1.0,
        value=0.10,
        step=0.01,
    )

    fraccion_c3 = st.number_input(
        "C3 — Propano",
        min_value=0.0,
        max_value=1.0,
        value=0.05,
        step=0.01,
    )

    fraccion_i_c4 = st.number_input(
        "i-C4 — Isobutano",
        min_value=0.0,
        max_value=1.0,
        value=0.02,
        step=0.01,
    )

with col2:

    fraccion_n_c4 = st.number_input(
        "n-C4 — n-Butano",
        min_value=0.0,
        max_value=1.0,
        value=0.03,
        step=0.01,
    )

    fraccion_co2 = st.number_input(
        "CO2 — Dióxido de carbono",
        min_value=0.0,
        max_value=1.0,
        value=0.05,
        step=0.01,
    )

    fraccion_n2 = st.number_input(
        "N2 — Nitrógeno",
        min_value=0.0,
        max_value=1.0,
        value=0.00,
        step=0.01,
    )

    fraccion_h2s = st.number_input(
        "H2S — Sulfuro de hidrógeno",
        min_value=0.0,
        max_value=1.0,
        value=0.00,
        step=0.01,
    )


# ============================================================
# COMPOSICIÓN
# ============================================================

composicion = {
    "C1": fraccion_c1,
    "C2": fraccion_c2,
    "C3": fraccion_c3,
    "i-C4": fraccion_i_c4,
    "n-C4": fraccion_n_c4,
    "CO2": fraccion_co2,
    "N2": fraccion_n2,
    "H2S": fraccion_h2s,
}

suma = sum(
    composicion.values()
)

st.metric(
    "Suma de fracciones molares",
    f"{suma:.6f}",
)


# ============================================================
# CREACIÓN DEL FLUIDO
# ============================================================

if st.button(
    "Crear fluido PVT",
    type="primary",
):

    try:

        fluido = Fluido(
            nombre=nombre_fluido,
            composicion=composicion,
        )

        fluido.validar()

        st.success(
            f"Fluido **{fluido.nombre}** creado correctamente."
        )

        st.write(
            f"Componentes definidos: "
            f"**{fluido.numero_componentes()}**"
        )

        st.write(
            f"Suma de composición: "
            f"**{fluido.suma_composicion():.6f}**"
        )

        st.subheader(
            "Composición del fluido"
        )

        for componente, fraccion in (
            fluido.composicion.items()
        ):

            if fraccion > 0:

                st.write(
                    f"**{componente}** — "
                    f"{fraccion * 100:.3f} %"
                )

    except ValueError as error:

        st.error(
            f"No se pudo crear el fluido: {error}"
        )
