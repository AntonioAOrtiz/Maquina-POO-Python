from maquina import Maquina
from maquinaElectrica import MaquinaElectrica
from maquinaMecanica import MaquinaMecanica





def __main__():
    m2=MaquinaMecanica("La pava","pavo")
    print(m2)
    m3=MaquinaElectrica("La pava","pavo",8,200)
    print(m3)

if __name__=='__main__':
    __main__()
