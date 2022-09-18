class Loja_Conveniada():
    def __init__(self, razao_social, cnpj, IE, pais, estado, cidade, bairro, logradouro, inicio_vigencia, fim_vigencia, codigo=0):
        self.__codigo = codigo
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__IE = IE
        self.__pais = pais
        self.__estado = estado
        self.__cidade = cidade
        self.__bairro = bairro
        self.__logradouro = logradouro
        self.__inicio_vigencia = inicio_vigencia
        self.__fim_vigencia = fim_vigencia

    @property
    def codigo(self):
        return self.__codigo

    @property
    def razao_social(self):
        return self.__razao_social

    @razao_social.setter
    def razao_social(self, razao_social):
        self.__razao_social = razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def IE(self):
        return self.__IE

    @IE.setter
    def IE(self, IE):
        self.__IE = IE

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self,pais):
        self.__pais = pais

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def logradouro(self):
        return self.__logradouro

    @logradouro.setter
    def logradouro(self, logradouro):
        self.__logradouro = logradouro

    @property
    def inicio_vigencia (self):
        return self.__inicio_vigencia

    @inicio_vigencia.setter
    def inicio_vigencia(self, inicio_vigencia):
        self.__inicio_vigencia = inicio_vigencia

    @property
    def fim_vigencia(self):
        return self.__fim_vigencia

    @fim_vigencia.setter
    def fim_vigencia(self, fim_vigencia):
        self.__fim_vigencia = fim_vigencia

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            razao_social = self.__razao_social,
            cnpj = self.__cnpj,
            IE = self.__IE,
            pais = self.__pais,
            estado = self.__estado,
            cidade = self.__cidade,
            bairro = self.__bairro ,
            logradouro = self.__logradouro,
            inicio_vigencia = self.__inicio_vigencia,
            fim_vigencia = self.__fim_vigencia
        )
