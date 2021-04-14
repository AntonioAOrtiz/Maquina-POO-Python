class Maquina(object):

    __cantidadDeMaquinasFabricadas:int=0

    def __init__(self,marca:str,modelo:str):
        self._marca:str=marca
        self._modelo:str=modelo
        self._numeroDeSerie=0

    def getMarca(self)->str:
        return self._marca

    def getModelo(self)->str:
        return self._modelo 

    def getNumeroDeSerie(self)->int:
        return self._numeroDeSerie           

    def getCantidadDeMaquinasFabricadas(self)->int:
        return Maquina.__cantidadDeMaquinasFabricadas

    def __str__(self) -> str:
        tmp_str=f"{{Marca: {self._marca}; modelo: {self._modelo}; NS: {self._numeroDeSerie} }}"
        return tmp_str 