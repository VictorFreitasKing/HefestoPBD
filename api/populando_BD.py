from database import db
from .entidades import funcionario
from .services import funcionario_service

def Popular():
    funcionario_service.cadastrar(
        funcionario.Funcionario(
            nome="",
            cpf="",
            rg="",
            telefone="",
            celular="",
            pais="",
            estado="",
            cidade="",
            bairro="",
            logradouro="",
            data_admissao="01/01/2000",
            data_demissao="",
            salario=2500,
            senha="",
            urlImagem=""
        )
    )
