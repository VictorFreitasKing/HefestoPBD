from ..entidades import itens_NF
from ..database import db

nome_tabela = "itens_NF"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                "quantidade varchar(11)," \
                "preco varchar(15)," \
                "codigoProduto INTEGER references produtos(codigo) UNIQUE"\
                "codigoNF INTEGER references notas_fiscais(codigo) UNIQUE"
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(itens_NF):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigoNF," \
                "quantidade," \
                "codigoProduto," \
                "preco" 
    comandoSQL +=") values ("
    comandoSQL += "'"+str(itens_NF.codigoNF)+"'," \
                "'" + str(itens_NF.quantidade) + "'," \
                "'" + str(itens_NF.codigoProduto) + "'," \
                "'"+str(itens_NF.preco)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return itens_NF

def editar(codigo, itens_NF):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "codigoProduto = '"+ str(itens_NF.codigoProduto) +"', " \
                "codigoNF = '"+str(itens_NF.codigoNF)+"'," \
                "quantidade = '" + str(itens_NF.quantidade) + "'," \
                "preco = '"+str(itens_NF.preco)+"'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return itens_NF

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(itens_NF.itens_NF(codigo=data_manager[0], codigoNF=data_manager[1], codigoProduto=data_manager[2], quantidade=data_manager[3], preco=data_manager[4]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return itens_NF.itens_NF(codigo=data_manager[0], codigoNF=data_manager[1], codigoProduto=data_manager[2], quantidade=data_manager[3], preco=data_manager[4])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return itens_NF.itens_NF(codigo=data_manager[0], codigoNF=data_manager[1], codigoProduto=data_manager[2], quantidade=data_manager[3], preco=data_manager[4])
    else:
        return None