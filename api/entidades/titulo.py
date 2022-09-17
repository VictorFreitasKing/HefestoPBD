class Titulo():
    def __init__(self, codigoNFS, codigoRecepcionista, valor, vencimento, data_baixa, codigo=0):
        self.__codigo = codigo
        self.__codigoNFS = codigoNFS
        self.__codigoRecepcionista = codigoRecepcionista
        self.__valor = valor
        self.__vencimento = vencimento
        self.__data_baixa = data_baixa


    @property
    def codigo(self):
        return self.__codigo

    @property
    def codigoNFS(self):
        return self.__codigoNFS

    @property
    def codigoRecepcionista(self):
        return self.__codigoRecepcionista

    @property
    def data_baixa(self):
        return self.__data_baixa

    @property
    def valor(self):
        return self.__valor

    @property
    def vencimento(self):
        return self.__vencimento

    @vencimento.setter
    def vencimento(self, vencimento):
         self.__vencimento = vencimento

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            codigoNFS = self.__codigoNFS,
            codigoRecepcionista = self.__codigoRecepcionista,
            valor=self.__valor,
            vencimento=self.__vencimento,
            data_baixa = self.__data_baixa


        )
