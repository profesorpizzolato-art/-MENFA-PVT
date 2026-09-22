# ============================================================
# MENFA PVT
# Modelo de fluido
# ============================================================

from dataclasses import dataclass, field

from nucleo.validadores import validar_composicion


@dataclass
class Fluido:
    """
    Representa un fluido PVT compuesto por varios componentes.
    """

    nombre: str
    composicion: dict[str, float] = field(
        default_factory=dict
    )

    temperatura: float | None = None
    presion: float | None = None

    descripcion: str = ""

    def validar(self) -> None:
        """
        Valida la composición del fluido.
        """

        validar_composicion(
            self.composicion
        )

    def fraccion(
        self,
        componente: str,
    ) -> float:
        """
        Devuelve la fracción molar de un componente.
        """

        return self.composicion.get(
            componente,
            0.0,
        )

    def numero_componentes(self) -> int:
        """
        Devuelve la cantidad de componentes.
        """

        return len(self.composicion)

    def suma_composicion(self) -> float:
        """
        Devuelve la suma de las fracciones molares.
        """

        return sum(
            self.composicion.values()
        )
