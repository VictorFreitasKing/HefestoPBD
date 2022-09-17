from ..entidades import item_OS
from ..database import db

nome_tabela = "item_OS"

def criar_tabela():
    #Montando comando SQL  codigoOS, codigoServico, codigoMecanico, preco, status, codigo=0
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                "preco varchar(10)," \
                "status varchar(8)," \
                "codigoServico INTEGER references servicos(codigo) UNIQUE," \
                "codigoOS INTEGER references ordem_servicos(codigo) UNIQUE," \
                "codigoMecanico INTEGER references mecanicos(codigo) UNIQUE"
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(item_OS):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigoOS,"\
                  "codigoServico,"\
                  "codigoMecanico," \
                  "preco," \
                  "status"
    comandoSQL +=") values ("
    comandoSQL += "'"+str(item_OS.codigoOS)+"'," \
                "'" + str(item_OS.codigoServico) + "'," \
                "'" + str(item_OS.codigoMecanico) + "'," \
                "'" + str(item_OS.preco) + "'," \
                "'"+str(item_OS.status)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return item_OS

def editar(codigo, item_OS):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "preco = '" + str(item_OS.preco) + "'," \
                "codigoOS = '"+str(item_OS.codigoOS)+"'," \
                "codigoServico = '" + str(item_OS.codigoServico) + "'," \
                "codigoMecanico = '" + str(item_OS.codigoMecanico) + "'," \
                "status = '"+str(item_OS.status)+"'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return item_OS

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(item_OS.item_OS(codigo=data_manager[0], codigoOS=data_manager[1], codigoServico=data_manager[2], codigoMecanico=data_manager[3], preco=data_manager[4], status=data_manager[5]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return item_OS.item_OS(codigo=data_manager[0], codigoOS=data_manager[1], codigoServico=data_manager[2], codigoMecanico=data_manager[3], preco=data_manager[4], status=data_manager[5])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return item_OS.item_OS(codigo=data_manager[0], codigoOS=data_manager[1], codigoServico=data_manager[2], codigoMecanico=data_manager[3], preco=data_manager[4], status=data_manager[5])
    else:
        return None