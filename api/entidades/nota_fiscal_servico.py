class Nota_Fiscal_Servico():
    def __init__(self, codigoOS, codigoFaturista, data_emissao, total, codigo=0):
        self.__codigo = codigo
        self.__codigoOS = codigoOS
        self.__codigoFaturista = codigoFaturista
        self.__data_emissao = data_emissao
        self.__total = total


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

    @property
    def data_emissao(self):
        return self.__data_emissao

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            codigoOS = self.__codigoOS,
            codigoFaturista = self.__codigoFaturista,
            data_emissao=self.__data_emissao,
            total = self.__total
        )
