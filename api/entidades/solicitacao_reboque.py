class Solicitacao_reboque():
    def __init__(self, codigoCliente, latitude, longitude, codigo=0):
        self.__codigo = codigo
        self.__codigoCliente = codigoCliente
        self.__latitude = latitude
        self.__longitude = longitude

    @property
    def codigo(self):
        return self.__codigo

    @property
    def codigoCliente(self):
        return self.__codigoCliente

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        self.__latitude = latitude

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude):
        self.__longitude = longitude


    def toJson(self):
        return dict(
            codigo = self.__codigo,
            codigoCliente = self.__codigoCliente,
            latitude = self.__latitude,
            longitude = self.__longitude
        )
