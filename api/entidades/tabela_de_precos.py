class Tabela_de_preco():
    def __init__(self, codigoServico, preco, inicio, fim, codigo=0):
        self.__codigo = codigo
        self.__codigoServico = codigoServico
        self.__preco = preco
        self.__inicio = inicio
        self.__fim = fim

    @property
    def codigo(self):
        return self.__codigo

    @property
    def codigoChefe(self):
        return self.__codigoServico

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def marca(self, inicio):
        self.__inicio = inicio

    @property
    def fim(self):
        return self.__fim

    @fim.setter
    def fim(self, fim):
        self.__fim = fim

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            codigoChefe = self.__codigoServico,
            placa = self.__preco,
            marca = self.__inicio,
            modelo = self.__fim
        )
