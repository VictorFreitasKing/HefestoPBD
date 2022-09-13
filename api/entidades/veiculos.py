class Veiculo():
    def __init__(self, codigoChefe, placa, marca, modelo, codigo=0):
        self.__codigo = codigo
        self.__codigoChefe = codigoChefe
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def codigoChefe(self):
        return self.__codigoChefe

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            codigoChefe = self.__codigoChefe,
            placa = self.__placa,
            marca = self.__marca,
            modelo = self.__modelo
        )
