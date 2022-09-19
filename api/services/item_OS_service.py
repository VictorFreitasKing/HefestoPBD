from api.entidades import item_OS
from api.database import db

nome_tabela = "items_OS"

def criar_tabela():
    #Montando comando SQL  codigoOS, codigoServico, codigoMecanico, preco, status, codigo=0
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                  "codigoOS INTEGER references ordens_servico(codigo)," \
                  "codigoServico INTEGER references servicos(codigo)," \
                  "codigoMecanico INTEGER references mecanicos(codigo)," \
                  "preco REAL," \
                  "status varchar(8)"
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
    comandoSQL += "codigoOS = '"+str(item_OS.codigoOS)+"'," \
                "codigoServico = '" + str(item_OS.codigoServico) + "'," \
                "codigoMecanico = '" + str(item_OS.codigoMecanico) + "'," \
                "preco = '"+str(item_OS.preco)+"'," \
                "status = '"+str(item_OS.status)+""
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
        lista.append(item_OS.Item_OS(codigo=data_manager[0], codigoOS=data_manager[1], codigoServico=data_manager[2], codigoMecanico=data_manager[3], preco=data_manager[4], status=data_manager[5]))
        data_manager = cursor.fetchone()
    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return item_OS.Item_OS(codigo=data_manager[0], codigoOS=data_manager[1], codigoServico=data_manager[2], codigoMecanico=data_manager[3], preco=data_manager[4], status=data_manager[5])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return item_OS.Item_OS(codigo=data_manager[0], codigoOS=data_manager[1], codigoServico=data_manager[2], codigoMecanico=data_manager[3], preco=data_manager[4], status=data_manager[5])
    else:
        return None