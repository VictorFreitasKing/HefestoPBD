#Produto = PEça no ER
class Produto():
    def __init__(self, descricao, codigo=0):
        self.__codigo = codigo
        self.__descricao = descricao

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            descricao = self.__descricao
        )
