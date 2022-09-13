class Produto():
    def __init__(self, descricao, codigo=0):
        self.__codigo = codigo
        self.__descricao = descricao
#peça no ER, referenciamos como produto por ser mais condizendo com notas fiscais n tenho nem ideia de como fazer isso kkkkkk

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
