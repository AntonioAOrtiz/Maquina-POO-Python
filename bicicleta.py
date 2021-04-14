from fuerza import Fuerza
from desplazable import Desplazable
from maquinaMecanica import MaquinaMecanica


class Bicicleta(MaquinaMecanica, Desplazable):

    DEFAULT_RADIO_RUEDA = 33.0
    MIN_RADIO_RUEDA = 17.75
    MAX_RADIO_RUEDA = 36.85
    MAX_DESPLAZAMIENTO = 200.0

    def __init__(self, marca: str, modelo: str,radioRueda=None, fuerzaMotriz=Fuerza.Animal):
        super().__init__(marca, modelo, fuerzaMotriz=fuerzaMotriz)
        self._radioRueda:float = Bicicleta.DEFAULT_RADIO_RUEDA if radioRueda is None else radioRueda
        self._totalKilometros:float = 0
        if self._radioRueda< Bicicleta.MIN_RADIO_RUEDA or self._radioRueda> Bicicleta.MAX_RADIO_RUEDA:
            raise Exception("Error de valor en radio, el radio debe estar entre 17.75 y 36.85")


    def desplazar(self, kilometros: float):
        if kilometros < 0 or kilometros > Bicicleta.MAX_DESPLAZAMIENTO:
            raise Exception("Cantida de kilómetros negativa o excesiva")


    def getTotalKilometrosRecorridos(self) -> float:
        return super().getTotalKilometrosRecorridos()

    def getKilometrosSinRepostar(self) -> float:
        return super().getKilometrosSinRepostar()   

    def __str__(self) -> str:
        tmp_str = super().__str__()
        tmp_str= tmp_str[:-1]+ f"Radio:{self._radioRueda};Kilómetros:{self._totalKilometros} }}"   
        return tmp_str      