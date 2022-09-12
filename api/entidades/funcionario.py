class Funcionario():
    def __init__(self, nome, cpf, rg, telefone, celular, pais, estado, cidade, bairro, logradouro, data_admissao, data_demissao, salario, senha,  matricula=0):
        self.__matricula = matricula
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__telefone = telefone
        self.__celular = celular
        self.__pais = pais
        self.__estado = estado
        self.__cidade = cidade
        self.__bairro = bairro
        self.__logradouro = logradouro
        self.__data_admissao = data_admissao
        self.__data_demissao = data_demissao
        self.__salario = salario
        self.__senha = senha

    @property
    def matricula(self):
        return self.__matricula

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def rg(self):
        return self.__rg

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular):
        self.__celular = celular

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
    def data_admissao(self):
        return self.__data_admissao

    @data_admissao.setter
    def data_admissao(self, data_admissao):
        self.__data_admissao = data_admissao

    @property
    def data_demissao(self):
        return self.__data_demissao

    @data_demissao.setter
    def data_demissao(self, data_demissao):
        self.__data_demissao = data_demissao

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    def toJson(self):
        return dict(
            matricula = self.__matricula,
            nome = self.__nome,
            cpf = self.__cpf,
            rg = self.__rg,
            telefone = self.__telefone,
            celular = self.__celular,
            pais = self.__pais,
            estado = self.__estado,
            cidade = self.__cidade,
            bairro = self.__bairro,
            logradouro = self.__logradouro,
            data_admissao = self.__data_admissao,
            data_demissao = self.__data_demissao,
            salario = self.__salario,
            senha = self.__senha
        )
