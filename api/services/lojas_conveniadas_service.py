from ..entidades import loja_conveniada
from ..database import db

nome_tabela = "lojas_conveniadas"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
#  eeee eu n sei se ta certo a parte do codigoChefe 
    comandoSQL += "codigo serial primary key," \
                "cnpj varchar(7) UNIQUE," \
                "razao_social varchar(11)," \
                "IE varchar(11)," \
                "pais varchar(15)," \
                "estado varchar(15)," \
                "cidade varchar(15)," \
                "bairro varchar(15)," \
                "logradouro varchar(30)"

    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(oficina):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "cnpj," \
                "razao_social," \
                "IE," \
                "pais," \
                "estado," \
                "cidade," \
                "bairro," \
                "logradouro"
    comandoSQL +=") values ("
    comandoSQL +="'" + str(loja_conveniada.cnpj) + "'," \
                "'" + str(loja_conveniada.razao_social) + "'," \
                "'" + str(loja_conveniada.IE) + "'," \
                "'" + str(loja_conveniada.pais) + "'," \
                "'" + str(loja_conveniada.estado) + "'," \
                "'" + str(loja_conveniada.cidade) + "'," \
                "'" + str(loja_conveniada.bairro) + "'," \
                "'" + str(loja_conveniada.logradouro) + "'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return loja_conveniada

def editar(codigo, lojas_conveniadas):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL +="cnpj = '"+str(lojas_conveniadas.cnpj)+"'," \
                "razao_social = '"+str(lojas_conveniadas.razao_social)+"'," \
                "IE = '"+str(lojas_conveniadas.IE)+"'," \
                "pais = '"+str(lojas_conveniadas.pais)+"'," \
                "estado = '"+str(lojas_conveniadas.estado)+"'," \
                "cidade = '"+str(lojas_conveniadas.cidade)+"'," \
                "bairro = '"+str(lojas_conveniadas.bairro)+"'," \
                "logradouro = '"+str(lojas_conveniadas.logradouro)+"'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return lojas_conveniadas

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(loja_conveniada.Lojas_Conveniadas(codigo=data_manager[0], cnpj=data_manager[1], razao_social=data_manager[2], IE=data_manager[3], pais=data_manager[4], estado=data_manager[5], cidade=data_manager[6], bairro=data_manager[7], logradouro=data_manager[8]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return loja_conveniada.Lojas_Conveniadas(codigo=data_manager[0], cnpj=data_manager[1], razao_social=data_manager[2], IE=data_manager[3], pais=data_manager[4], estado=data_manager[5], cidade=data_manager[6], bairro=data_manager[7], logradouro=data_manager[8])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return loja_conveniada.Lojas_Conveniadas(codigo=data_manager[0], cnpj=data_manager[1], razao_social=data_manager[2], IE=data_manager[3], pais=data_manager[4], estado=data_manager[5], cidade=data_manager[6], bairro=data_manager[7], logradouro=data_manager[8])
    else:
        return None