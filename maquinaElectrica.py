from maquina import Maquina


class MaquinaElectrica(Maquina):

    __DEFAULT_VOLTAJE=None
    __MIN_VOLTAJE=10
    __MAX_VOLTAJE=400
    __DEFAULT_POTENCIA_ELECTRICA=__MIN_VOLTAJE
    __MIN_POTENCIA_ELECTRICA=700.0
    __MAX_POTENCIA_ELECTRICA=200000.0


    def __init__(self, marca: str, modelo: str,voltaje=None,potenciaElectrica=None):
        super().__init__(marca, modelo)
        self._voltaje=voltaje
        self._potenciaElectrica=potenciaElectrica
        if voltaje<self.__MIN_VOLTAJE or voltaje>self.__MAX_VOLTAJE:
            raise Exception("Error de voltaje,voltaje mínimo 10v y voltaje máximo 400v")
        elif potenciaElectrica <self.__MIN_POTENCIA_ELECTRICA or potenciaElectrica>self.__MAX_POTENCIA_ELECTRICA:
            raise Exception("Error de potencia, la potencia no debe ser menor a 700.0 kW ni mayor a 200.000kW")


    def getVoltaje(self):
        return self._voltaje    

    def getPotenciaElectrica(self):
        return self._potenciaElectrica    

    def __str__(self) -> str:
        tmp_str=super().__str__()
        tmp_str = tmp_str[:-1] + f"voltaje:{self._voltaje};potencia{self._potenciaElectrica} }}"
        return tmp_str