class notas_fiscais():
    def __init__(self, codigoOS, codigoAuxiliarFaturista, total, serie=0, codigo_loja_conveniada=0,numero=0):
        self.__numero = numero
        self.__codigo_loja_conveniada = codigo_loja_conveniada
        self.__codigoAuxiliarFaturista = codigoAuxiliarFaturista
        self.__codigoOS = codigoOS
        self.__serie = serie
        self.__total = total

    @property
    def numero(self):
        return self.__numero

    @property
    def codigo_loja_conveniada(self):
        return self.__codigo_loja_conveniada

    @property
    def serie(self):
        return self.__serie

    @property
    def codigoAuxiliarFaturista(self):
        return self.__codigoAuxiliarFaturista

    @property
    def codigoOS(self):
        return self.__codigoOS

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        self.__total = total

    def toJson(self):
        return dict(
            numero = self.__numero,
            codigocodigo_loja_conveniada = self.__codigo_loja_conveniada,
            serie= self.__serie,
            codigoAuxiliarFaturista = self.__codigoAuxiliarFaturista,
            codigoOS = self.__codigoOS,
            total = self.__total
        )
