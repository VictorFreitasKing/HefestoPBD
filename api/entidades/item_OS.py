class Veiculo():
    def __init__(self, codigoOS, codigoServico, codigoMecanico, preco, status, codigo=0):
        self.__codigo = codigo
        self.__codigoOS = codigoOS
        self.__codigoServico = codigoServico
        self.__codigoMecanico = codigoMecanico
        self.__preco = preco
        self.__status = status

    @property
    def codigo(self):
        return self.__codigo

    @property
    def codigoOS(self):
        return self.__codigoOS

    @property
    def codigoServico(self):
        return self.__codigoServico

    @property
    def codigoMecanico(self):
        return self.__codigoMecanico

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status


    def toJson(self):
        return dict(
            codigo = self.__codigo,
            codigoOS = self.__codigoOS,
            codigoServico = self.__codigoServico,
            codigoMecanico = self.__codigoMecanico,
            preco = self.__preco,
            status = self.__status
        )
