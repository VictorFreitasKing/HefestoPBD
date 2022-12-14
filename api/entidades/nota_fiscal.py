class Nota_Fiscal():
    def __init__(self, codigo_loja_conveniada, numero, serie, codigoAuxiliarFaturista, codigoOS, total, codigo = 0):
        self.__codigo = codigo
        self.__codigo_loja_conveniada = codigo_loja_conveniada
        self.__numero = numero
        self.__serie = serie
        self.__codigoAuxiliarFaturista = codigoAuxiliarFaturista
        self.__codigoOS = codigoOS
        self.__total = total

    @property
    def codigo(self):
        return self.__codigo

    @property
    def codigo_loja_conveniada(self):
        return self.__codigo_loja_conveniada

    @codigo_loja_conveniada.setter
    def codigo_loja_conveniada(self, codigo):
        self.__codigo_loja_conveniada = codigo

    @property
    def numero(self):
        return self.__numero

    @property
    def serie(self):
        return self.__serie

    @property
    def codigoAuxiliarFaturista(self):
        return self.__codigoAuxiliarFaturista

    @codigoAuxiliarFaturista.setter
    def codigoAuxiliarFaturista(self, codigoAuxiliarFaturista):
        self.__codigoAuxiliarFaturista = codigoAuxiliarFaturista

    @property
    def codigoOS(self):
        return self.__codigoOS

    @codigoOS.setter
    def codigoOS(self, codigoOS):
        self.__codigoOS = codigoOS

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        self.__total = total

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            codigo_loja_conveniada = self.__codigoLojaConveniada,
            numero = self.__numero,
            serie = self.__serie,
            codigoAuxiliarFaturista = self.__codigoAuxiliarFaturista,
            codigoOS = self.__codigoOS,
            total = self.__total
        )
