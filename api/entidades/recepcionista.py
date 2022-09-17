class Recepicionista():
    def __init__(self, matriculaFuncionario, codigo=0):
        self.__codigo = codigo
        self.__matriculaFuncionario = matriculaFuncionario

    @property
    def codigo(self):
        return self.__codigo

    @property
    def matriculaFuncionario(self):
        return self.__matriculaFuncionario

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            matriculaFuncionario = self.__matriculaFuncionario
        )