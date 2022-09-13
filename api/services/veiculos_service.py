from ..entidades import veiculos
from ..database import db

nome_tabela = "veiculos"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                "placa varchar(11)," \
                "marca varchar(11)," \
                "modelo varchar(15)," \
                "codigoChefe INTEGER references chefes(codigo) UNIQUE"
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(veiculos):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigoChefe," \
                "placa," \
                "marca," \
                "modelo" 
    comandoSQL +=") values ("
    comandoSQL += "'"+str(veiculos.codigoChefe)+"'," \
                "'" + str(veiculos.placa) + "'," \
                "'" + str(veiculos.marca) + "'," \
                "'"+str(veiculos.modelo)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return veiculos

def editar(codigo, veiculos):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "marca = '"+ str(veiculos.marca) +"', " \
                "codigoChefe = '"+str(veiculos.codigoChefe)+"'," \
                "placa = '" + str(veiculos.placa) + "'," \
                "modelo = '"+str(veiculos.modelo)+"'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return veiculos

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(veiculos.veiculos(codigo=data_manager[0], codigoChefe=data_manager[1], marca=data_manager[3], placa=data_manager[4], modelo=data_manager[5]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return veiculos.veiculos(codigo=data_manager[0], codigoChefe=data_manager[1], marca=data_manager[3], placa=data_manager[4], modelo=data_manager[5])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return veiculos.veiculos(codigo=data_manager[0], codigoChefe=data_manager[1], marca=data_manager[3], placa=data_manager[4], modelo=data_manager[5])
    else:
        return None