class Itens_NF():
    def __init__(self, codigoNF, codigoProduto, quantidade, preco, codigo=0):
        self.__codigo = codigo
        self.__codigoNF = codigoNF
        self.__codigoProduto = codigoProduto
        self.__quantidade = quantidade
        self.__preco = preco

    @property
    def codigo(self):
        return self.__codigo

    @property
    def codigoNF(self):
        return self.__codigoNF

    @property
    def codigoProduto(self):
        return self.__codigoProduto

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            codigoNF = self.__codigoNF,
            codigoProduto = self.__codigoProduto,
            quantidade = self.__quantidade,
            preco = self.__preco
        )
