class Veiculo():
    def __init__(self, codigoOS, codigoFaturista, total, data_emissao, codigo=0):
        self.__codigo = codigo
        self.__codigoOS = codigoOS
        self.__codigoFaturista = codigoFaturista
        self.__total = total
        self.__data_emissao = data_emissao

    @property
    def codigo(self):
        return self.__codigo

    @property
    def codigoOS(self):
        return self.__codigoOS

    @property
    def codigoFaturista(self):
        return self.__codigoFaturista

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        self.__total = total

    @property
    def data_emissao(self):
        return self.__data_emissao

    # @data_emissao.setter
    # def data_emissao(self, data_emissao):
    #     self.__data_emissao = data_emissao

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            codigoOS = self.__codigoOS,
            codigoFaturista = self.__codigoFaturista,
            total = self.__total,
            data_emissao = self.__data_emissao
        )
