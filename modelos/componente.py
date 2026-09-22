# ============================================================
# MENFA PVT
# Modelo de componente
# ============================================================

from dataclasses import dataclass


@dataclass
class Componente:
    """
    Representa un componente de una mezcla PVT.
    """

    nombre: str
    formula: str
    peso_molecular: float
    temperatura_critica: float
    presion_critica: float
    factor_acenico: float
    densidad: float | None = None
    numero_componente: str | None = None

    def descripcion(self) -> str:
        """
        Devuelve una descripción resumida
        del componente.
        """

        return (
            f"{self.nombre} ({self.formula})"
        )
