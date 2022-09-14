class ordem_servico():
    def __init__(self, codigoMecanico, codigoVeiculo, entrada, saida, total, codigo=0):
        self.__codigo = codigo
        self.__codigoMecanico = codigoMecanico
        self.__codigoVeiculo = codigoVeiculo
        self.__entrada = entrada
        self.__saida = saida
        self.__total = total

    @property
    def codigo(self):
        return self.__codigo

    @property
    def codigoMecanico(self):
        return self.__codigoMecanico

    @property
    def codigoVeiculo(self):
        return self.__codigoVeiculo

    @property
    def entrada(self):
        return self.__entrada

    @property
    def saida(self):
        return self.__saida

    @saida.setter
    def saida(self, saida):
        self.__saida = saida

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        self.__total = total

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            codigoChefe = self.__codigoMecanico,
            codigoVeiculo = self.__codigoVeiculo,
            placa = self.__entrada,
            marca = self.__saida,
            modelo = self.__total
        )
