class Mecanico():
    def __init__(self, matriculaFuncionario, especialidade, codigo=0):
        self.__codigo = codigo
        self.__matriculaFuncionario = matriculaFuncionario
        self.__especialidade = especialidade

    @property
    def codigo(self):
        return self.__codigo

    @property
    def matriculaFuncionario(self):
        return self.__matriculaFuncionario

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        self.__especialidade = especialidade

    def toJson(self):
        return dict(
            codigo = self.__codigo,
            matriculaFuncionario = self.__matriculaFuncionario,
            especialidade = self.__especialidade
        )
