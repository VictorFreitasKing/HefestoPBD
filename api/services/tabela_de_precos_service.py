from api.entidades import tabela_de_precos
from api.database import db

nome_tabela = "tabelas_de_preco"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                "codigoServico INTEGER references servicos(codigo)," \
                "preco REAL," \
                "inicio Date," \
                "fim Date"
    comandoSQL += ");"

    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(tabela_de_precos):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigoServico," \
                "preco," \
                "inicio," \
                "fim"
    comandoSQL +=") values ("
    comandoSQL += "'"+str(tabela_de_precos.codigoServico)+"'," \
                "'" + str(tabela_de_precos.preco) + "'," \
                "'" + str(tabela_de_precos.inicio) + "'," \
                "'"+str(tabela_de_precos.fim)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return tabela_de_precos

def editar(codigo, tabela_de_precos):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "codigo serial primary key," \
                  "codigoServico = '"+str(tabela_de_precos.codigoServico)+"'," \
                  "preco = '"+str(tabela_de_precos.preco)+"'," \
                  "inicio = '"+str(tabela_de_precos.inicio)+"'," \
                  "fim = '"+str(tabela_de_precos.fim)+"'," \
                  "codigoServico INTEGER references servicos(codigo) UNIQUE"
    comandoSQL += " where codigo='" + str(codigo) + "';"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return tabela_de_precos

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(tabela_de_precos.Tabela_de_preco(codigo=data_manager[0], codigoServico=data_manager[1], preco=data_manager[2], inicio=data_manager[3], fim=data_manager[4]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return tabela_de_precos.Tabela_de_preco(codigo=data_manager[0], codigoServico=data_manager[1], preco=data_manager[2], inicio=data_manager[3], fim=data_manager[4])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return tabela_de_precos.Tabela_de_preco(codigo=data_manager[0], codigoServico=data_manager[1], preco=data_manager[2], inicio=data_manager[3], fim=data_manager[4])
    else:
        return None