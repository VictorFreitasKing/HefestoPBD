from api.entidades import etapa_servico
from api.database import db

nome_tabela = "etapas_servico"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                "codigoServico INTEGER references servicos(codigo)," \
                "descricao varchar(30)"
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(etapa_servico):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigoServico," \
                "descricao"
    comandoSQL +=") values ("
    comandoSQL += "'"+str(etapa_servico.codigoServico)+"'," \
                "'"+str(etapa_servico.descricao)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return etapa_servico

def editar(codigo, etapa_servico):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "descricao = '"+ str(etapa_servico.codigoServico) +"', " \
                "descricao = '"+str(etapa_servico.descricao)+"',"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return etapa_servico

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(etapa_servico.Etapa_Servico(codigo=data_manager[0], codigoServico=data_manager[1], descricao=data_manager[2], ordem=data_manager[3]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return etapa_servico.etapa_servico(codigo=data_manager[0], codigoChefe=data_manager[1], descricao=data_manager[2])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return etapa_servico.etapa_servico(codigo=data_manager[0], codigoChefe=data_manager[1], descricao=data_manager[2])
    else:
        return None