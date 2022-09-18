class Etapa_Servico():
    def __init__(self, codigoServico, descricao, ordem, codigo=0):
        self.__codigo = codigo
        self.__codigoServico = codigoServico
        self.__descricao = descricao
        self.__ordem = ordem

    @property
    def codigo(self):
        return self.__codigo

    @property
    def codigoServico(self):
        return self.__codigoServico

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def ordem(self):
        return self.__ordem

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            codigoServico = self.__codigoServico,
            descricao = self.__descricao
        )
