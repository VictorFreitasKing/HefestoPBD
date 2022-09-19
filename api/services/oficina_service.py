from api.entidades import oficina
from api.database import db

nome_tabela = "oficinas"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
#  eeee eu n sei se ta certo a parte do codigoChefe 
    comandoSQL += "codigo serial primary key," \
                "codigoChefe INTEGER references chefes(codigo)," \
                "razao_social varchar(30)," \
                "cnpj varchar(14) UNIQUE," \
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
    comandoSQL += "codigoChefe," \
                "razao_social," \
                "cnpj," \
                "IE," \
                "pais," \
                "estado," \
                "cidade," \
                "bairro," \
                "logradouro"

    comandoSQL +=") values ("
    comandoSQL +="'" + str(oficina.codigoChefe) + "'," \
                "'" + str(oficina.razao_social) + "'," \
                "'" + str(oficina.cnpj) + "'," \
                "'" + str(oficina.IE) + "'," \
                "'" + str(oficina.pais) + "'," \
                "'" + str(oficina.estado) + "'," \
                "'" + str(oficina.cidade) + "'," \
                "'" + str(oficina.bairro) + "'," \
                "'" + str(oficina.logradouro) + "'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return oficina

def editar(codigo, oficina):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL +="codigoChefe = '"+str(oficina.cnpj)+"'," \
                "razao_social = '"+str(oficina.razao_social)+"'," \
                "cnpj = '"+str(oficina.IE)+"'," \
                "IE = '"+str(oficina.IE)+"'," \
                "pais = '"+str(oficina.pais)+"'," \
                "estado = '"+str(oficina.estado)+"'," \
                "cidade = '"+str(oficina.cidade)+"'," \
                "bairro = '"+str(oficina.bairro)+"'," \
                "logradouro = '"+str(oficina.logradouro)+"'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return oficina

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(oficina.Oficina(codigo=data_manager[0], codigoChefe=data_manager[1], razao_social=data_manager[2], cnpj=data_manager[3], IE=data_manager[4], pais=data_manager[5], estado=data_manager[6], cidade=data_manager[7], bairro=data_manager[8], logradouro=data_manager[9]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return oficina.Oficina(codigo=data_manager[0], codigoChefe=data_manager[1], razao_social=data_manager[2], cnpj=data_manager[3], IE=data_manager[4], pais=data_manager[5], estado=data_manager[6], cidade=data_manager[7], bairro=data_manager[8], logradouro=data_manager[9])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return oficina.Oficina(codigo=data_manager[0], codigoChefe=data_manager[1], razao_social=data_manager[2], cnpj=data_manager[3], IE=data_manager[4], pais=data_manager[5], estado=data_manager[6], cidade=data_manager[7], bairro=data_manager[8], logradouro=data_manager[9])
    else:
        return None