class Lojas_Conveniadas():
    def __init__(self, logradouro, bairron, cidade, pais, estado, IE, cnpj, razao_social, codigo=0):
        self.__codigo = codigo

        self.__logradouro = logradouro
        self.__bairron = bairron
        self.__cidade = cidade
        self.__pais = pais
        self.__estado = estado
        self.__IE = IE
        self.__cnpj = cnpj
        self.__razao_social = razao_social


    @property
    def codigo(self):
        return self.__codigo

    @property
    def logradouro(self):
        return self.__logradouro

    @property
    def bairron(self):
        return self.__bairron

    @bairron.setter
    def bairron(self, bairron):
        self.__bairron = bairron

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, pais):
        self.__pais = pais

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def IE(self):
        return self.__IE

    @IE.setter
    def IE(self, IE):
        self.__IE = IE

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def razao_social(self):
        return self.__razao_social

    @razao_social.setter
    def razao_social(self, razao_social):
        self.__razao_social = razao_social

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            logradouro = self.__logradouro,
            bairron = self.__bairron,
            cidade = self.__cidade,
            pais = self.__pais,
            estado = self.__estado,
            IE = self.__IE,
            cnpj = self.__cnpj,
            razao_social = self.__razao_social

        )
