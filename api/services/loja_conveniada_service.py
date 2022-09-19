from api.entidades import loja_conveniada
from api.database import db

nome_tabela = "lojas_conveniadas"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
#  eeee eu n sei se ta certo a parte do codigoChefe 
    comandoSQL += "codigo serial primary key," \
                "razao_social varchar(20) UNIQUE," \
                "cnpj varchar(14) UNIQUE," \
                "IE varchar(11)," \
                "pais varchar(15)," \
                "estado varchar(15)," \
                "cidade varchar(15)," \
                "bairro varchar(15)," \
                "logradouro varchar(30)," \
                "inicio_vigencia Date," \
                "fim_vigencia Date"
    comandoSQL += ");"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(loja_conveniada):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "razao_social," \
                "cnpj," \
                "IE," \
                "pais," \
                "estado," \
                "cidade," \
                "bairro," \
                "logradouro," \
                "inicio_vigencia," \
                "fim_vigencia"
    comandoSQL +=") values ("
    comandoSQL +="'" + str(loja_conveniada.razao_social) + "'," \
                "'" + str(loja_conveniada.cnpj) + "'," \
                "'" + str(loja_conveniada.IE) + "'," \
                "'" + str(loja_conveniada.pais) + "'," \
                "'" + str(loja_conveniada.estado) + "'," \
                "'" + str(loja_conveniada.cidade) + "'," \
                "'" + str(loja_conveniada.bairro) + "'," \
                "'" + str(loja_conveniada.logradouro) + "'," \
                "'" + str(loja_conveniada.inicio_vigencia) + "'," \
                "'" + str(loja_conveniada.fim_vigencia) + "'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return loja_conveniada

def editar(codigo, loja_conveniada):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL +="razao_social = '"+str(loja_conveniada.razao_social)+"'," \
                "cnpj = '"+str(loja_conveniada.cnpj)+"'," \
                "IE = '"+str(loja_conveniada.IE)+"'," \
                "pais = '"+str(loja_conveniada.pais)+"'," \
                "estado = '"+str(loja_conveniada.estado)+"'," \
                "cidade = '"+str(loja_conveniada.cidade)+"'," \
                "bairro = '"+str(loja_conveniada.bairro)+"'," \
                "logradouro = '"+str(loja_conveniada.logradouro)+"'" \
                "inicio_vigencia = '"+str(loja_conveniada.inicio_vigencia)+"'" \
                "fim_vigencia = '"+str(loja_conveniada.fi)+"'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return loja_conveniada

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(loja_conveniada.Loja_Conveniada(codigo=data_manager[0], razao_social=data_manager[1], cnpj=data_manager[2], IE=data_manager[3], pais=data_manager[4], estado=data_manager[5], cidade=data_manager[6], bairro=data_manager[7], logradouro=data_manager[8], inicio_vigencia=data_manager[9], fim_vigencia=data_manager[10]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return loja_conveniada.Loja_Conveniada(codigo=data_manager[0], razao_social=data_manager[1], cnpj=data_manager[2], IE=data_manager[3], pais=data_manager[4], estado=data_manager[5], cidade=data_manager[6], bairro=data_manager[7], logradouro=data_manager[8], inicio_vigencia=data_manager[9], fim_vigencia=data_manager[10])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return loja_conveniada.Loja_Conveniada(codigo=data_manager[0], razao_social=data_manager[1], cnpj=data_manager[2], IE=data_manager[3], pais=data_manager[4], estado=data_manager[5], cidade=data_manager[6], bairro=data_manager[7], logradouro=data_manager[8], inicio_vigencia=data_manager[9], fim_vigencia=data_manager[10])
    else:
        return None