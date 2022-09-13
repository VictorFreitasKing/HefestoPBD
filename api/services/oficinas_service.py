from ..entidades import oficinas
from ..database import db

nome_tabela = "oficinas"

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
                "logradouro varchar(30)," \
                "codigoChefe INTEGER references chefes(codigo) UNIQUE"

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
                "logradouro," \
                "codigoChefe"
    comandoSQL +=") values ("
    comandoSQL +="'"+str(oficinas.cnpj)+"'," \
                "'"+str(oficinas.razao_social)+"'," \
                "'"+str(oficinas.IE)+"'," \
                "'"+str(oficinas.pais)+"'," \
                "'"+str(oficinas.estado)+"'," \
                "'"+str(oficinas.cidade)+"'," \
                "'"+str(oficinas.bairro)+"'," \
                "'"+str(oficinas.logradouro)+"'," \
                "'"+str(oficinas.codigoChefe)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return oficinas

def editar(codigo, oficinas):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL +="cnpj = '"+str(oficinas.cnpj)+"'," \
                "razao_social = '"+str(oficinas.razao_social)+"'," \
                "IE = '"+str(oficinas.IE)+"'," \
                "pais = '"+str(oficinas.pais)+"'," \
                "estado = '"+str(oficinas.estado)+"'," \
                "cidade = '"+str(oficinas.cidade)+"'," \
                "bairro = '"+str(oficinas.bairro)+"'," \
                "logradouro = '"+str(oficinas.logradouro)+"'," \
                "codigoChefe = '"+str(oficinas.codigoChefe)+"'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return oficinas

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(oficinas.Oficinas(codigo=data_manager[0], cnpj=data_manager[1], razao_social=data_manager[2], IE=data_manager[3], pais=data_manager[4], estado=data_manager[5],cidade=data_manager[6], bairro=data_manager[7], logradouro=data_manager[8], codigoChefe=data_manager[9]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return oficinas.Oficinas(codigo=data_manager[0], cnpj=data_manager[1], razao_social=data_manager[2], IE=data_manager[3], pais=data_manager[4], estado=data_manager[5],cidade=data_manager[6], bairro=data_manager[7], logradouro=data_manager[8], codigoChefe=data_manager[9])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return oficinas.Oficinas(codigo=data_manager[0], cnpj=data_manager[1], razao_social=data_manager[2], IE=data_manager[3], pais=data_manager[4], estado=data_manager[5],cidade=data_manager[6], bairro=data_manager[7], logradouro=data_manager[8], codigoChefe=data_manager[9])
    else:
        return None