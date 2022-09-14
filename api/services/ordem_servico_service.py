from ..entidades import ordem_servico
from ..database import db

nome_tabela = "ordem_servicos"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                "entrada varchar(10)," \
                "saida varchar(10)," \
                "total varchar(15)," \
                "codigoMecanico INTEGER references mecanicos(codigo) UNIQUE"\
                "codigoVeiculos INTEGER references veiculos(codigo) UNIQUE"
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(ordem_servicos):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigoMecanico," \
                "codigoVeiculo," \
                "entrada," \
                "saida," \
                "total"
    comandoSQL +=") values ("
    comandoSQL += "'"+str(ordem_servicos.codigoMecanico)+"'," \
                "'" + str(ordem_servicos.codigoVeiculo) + "'," \
                "'" + str(ordem_servicos.entrada) + "'," \
                "'" + str(ordem_servicos.saida) + "',"\             
                "'"+str(ordem_servicos.total)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return ordem_servicos

def editar(codigo, veiculos):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "entrada = '"+ str(ordem_servico.entrada) +"', " \
                "codigoChefe = '"+str(ordem_servico.codigoMecanico)+"'," \
                "codigoChefe = '" + str(ordem_servico.codigoVeiculo) + "'," \
                "placa = '" + str(ordem_servico.saida) + "'," \
                "modelo = '"+str(ordem_servico.total)+"'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return ordem_servico

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(ordem_servico.ordem_servico(codigo=data_manager[0], codigoMecanico=data_manager[1], codigoVeiculo=data_manager[2], entrada=data_manager[3], saida=data_manager[4], total=data_manager[5]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return ordem_servico.ordem_servico(codigo=data_manager[0], codigoMecanico=data_manager[1], codigoVeiculo=data_manager[2], entrada=data_manager[3], saida=data_manager[4], total=data_manager[5])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return ordem_servico.ordem_servico(codigo=data_manager[0], codigoMecanico=data_manager[1], codigoVeiculo=data_manager[2], entrada=data_manager[3], saida=data_manager[4], total=data_manager[5])
    else:
        return None