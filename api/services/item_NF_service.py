from ..entidades import item_NF
from ..database import db

nome_tabela = "itens_NF"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                  "codigoNF INTEGER references notas_fiscais(codigo)," \
                  "codigoProduto INTEGER references produtos(codigo)," \
                  "quantidade INTEGER," \
                  "preco REAL"
    comandoSQL += ");"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(item_NF):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigoNF," \
                  "codigoProduto," \
                  "quantidade," \
                  "preco"
    comandoSQL +=") values ("
    comandoSQL += "'" + str(item_NF.codigoNF) + "'," \
                "'" + str(item_NF.codigoProduto) + "'," \
                "'" + str(item_NF.quantidade) + "'," \
                "'" + str(item_NF.preco) + "'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return item_NF

def editar(codigo, item_NF):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "codigoNF = '" + str(item_NF.codigoNF) + "', " \
                "codigoProduto = '" + str(item_NF.codigoProduto) + "'," \
                "quantidade = '" + str(item_NF.quantidade) + "'," \
                "preco = '" + str(item_NF.preco) + "'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return item_NF

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(item_NF.Item_NF(codigo=data_manager[0], codigoNF=data_manager[1], codigoProduto=data_manager[2], quantidade=data_manager[3], preco=data_manager[4]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return item_NF.Item_NF(codigo=data_manager[0], codigoNF=data_manager[1], codigoProduto=data_manager[2], quantidade=data_manager[3], preco=data_manager[4])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return item_NF.Item_NF(codigo=data_manager[0], codigoNF=data_manager[1], codigoProduto=data_manager[2], quantidade=data_manager[3], preco=data_manager[4])
    else:
        return None