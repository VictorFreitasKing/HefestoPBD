from api.entidades import solicitacao_reboque
from api.database import db

nome_tabela = "solicitacoes_reboque"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                  "codigoCliente INTEGER references clientes(codigo)," \
                  "latitude varchar(11)," \
                  "longitude varchar(11)"
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(solicitacao_reboque):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigoCliente," \
                  "latitude," \
                  "longitude"
    comandoSQL +=") values ("
    comandoSQL += "'"+str(solicitacao_reboque.codigoCliente)+"'," \
                "'" + str(solicitacao_reboque.latitude) + "'," \
                "'"+str(solicitacao_reboque.longitude)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return solicitacao_reboque

def editar(codigo, solicitacao_reboque):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "codigoCliente = '"+ str(solicitacao_reboque.latitude) +"', " \
                  "latitude = '"+str(solicitacao_reboque.codigoCliente)+"'," \
                  "longitude = '" + str(solicitacao_reboque.longitude) + "',"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return solicitacao_reboque

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(solicitacao_reboque.Solicitacao_reboque(codigo=data_manager[0], codigoCliente=data_manager[1], latitude=data_manager[2], longitude=data_manager[3]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return solicitacao_reboque.Solicitacao_reboque(codigo=data_manager[0], codigoCliente=data_manager[1], latitude=data_manager[2], longitude=data_manager[3])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return solicitacao_reboque.Solicitacao_reboque(codigo=data_manager[0], codigoCliente=data_manager[1], latitude=data_manager[2], longitude=data_manager[3])
    else:
        return None