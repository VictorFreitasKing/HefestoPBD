from api.entidades import veiculo
from api.database import db

nome_tabela = "veiculos"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                "codigoCliente INTEGER references clientes(codigo)," \
                "placa varchar(11)," \
                "marca varchar(11)," \
                "modelo varchar(15)"
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(veiculo):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigoCliente," \
                "placa," \
                "marca," \
                "modelo" 
    comandoSQL +=") values ("
    comandoSQL += "'"+str(veiculo.codigoCliente)+"'," \
                "'" + str(veiculo.placa) + "'," \
                "'" + str(veiculo.marca) + "'," \
                "'"+str(veiculo.modelo)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return veiculo

def editar(codigo, veiculo):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "marca = '"+ str(veiculo.marca) +"', " \
                "codigoCliente = '"+str(veiculo.codigoChefe)+"'," \
                "placa = '" + str(veiculo.placa) + "'," \
                "modelo = '"+str(veiculo.modelo)+"'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return veiculo

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(veiculo.Veiculo(codigo=data_manager[0], codigoCliente=data_manager[1], marca=data_manager[2], placa=data_manager[3], modelo=data_manager[4]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return veiculo.Veiculo(codigo=data_manager[0], codigoCliente=data_manager[1], marca=data_manager[2], placa=data_manager[3], modelo=data_manager[4])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return veiculo.Veiculo(codigo=data_manager[0], codigoCliente=data_manager[1], marca=data_manager[2], placa=data_manager[3], modelo=data_manager[4])
    else:
        return None