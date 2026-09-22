# ============================================================
# MENFA PVT
# Modelo de mezcla
# ============================================================

from dataclasses import dataclass

from modelos.componente import Componente
from modelos.fluido import Fluido


@dataclass
class ComponenteMezcla:
    """
    Representa un componente dentro de una mezcla PVT.
    """

    componente: Componente
    fraccion_molar: float


class MezclaPVT:
    """
    Representa una mezcla termodinámica formada
    por componentes y sus fracciones molares.
    """

    def __init__(
        self,
        fluido: Fluido,
        biblioteca: dict[str, Componente],
    ):

        self.fluido = fluido
        self.biblioteca = biblioteca

        self.componentes: list[
            ComponenteMezcla
        ] = []

        self._construir()

    def _construir(self) -> None:
        """
        Construye la mezcla utilizando la biblioteca
        de componentes.
        """

        self.componentes = []

        for nombre, fraccion in (
            self.fluido.composicion.items()
        ):

            if fraccion <= 0:
                continue

            if nombre not in self.biblioteca:
                raise ValueError(
                    f"El componente '{nombre}' "
                    "no existe en la biblioteca."
                )

            componente = self.biblioteca[nombre]

            self.componentes.append(
                ComponenteMezcla(
                    componente=componente,
                    fraccion_molar=fraccion,
                )
            )

    def peso_molecular_mezcla(self) -> float:
        """
        Calcula el peso molecular promedio
        de la mezcla.

        PMmezcla = Σ(xi * PMi)
        """

        return sum(
            item.fraccion_molar
            * item.componente.peso_molecular
            for item in self.componentes
        )

    def numero_componentes(self) -> int:
        """
        Cantidad de componentes activos.
        """

        return len(self.componentes)

    def componentes_activos(
        self,
    ) -> list[ComponenteMezcla]:
        """
        Devuelve los componentes con
        fracción molar mayor que cero.
        """

        return self.componentes
