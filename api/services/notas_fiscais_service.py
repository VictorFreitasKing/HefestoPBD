from ..entidades import nota_fiscal
from ..database import db

nome_tabela = "notas_fiscais"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo_loja_conveniada INTEGER primary key UNIQUE references lojas_conveniadas(codigo)," \
                "numero varchar(9)," \
                "serie varchar(3)," \
                "codigoAuxiliarFaturista INTEGER references auxiliares_de_faturistas(codigo) UNIQUE," \
                "codigoOS INTEGER references ordem_servicos(codigo) UNIQUE,"\
                "total varchar(15)"
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(notas_fiscais):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo_loja_conveniada," \
                "numero,"\
                "serie," \
                "codigoAuxiliarFaturista," \
                "codigoOS"\
                "total"
    comandoSQL +=") values ("
    comandoSQL += "'"+str(notas_fiscais.codigo_loja_conveniada)+"'," \
                "'" + str(notas_fiscais.numero) + "'," \
                "'" + str(notas_fiscais.serie) + "',"\
                "'" + str(notas_fiscais.codigoAuxiliarFaturista) + "'," \
                "'" + str(notas_fiscais.codigoOS) + "'," \
                "'"+str(notas_fiscais.total)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return notas_fiscais

def editar(codigo, notas_fiscais):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "marca = '"+ str(notas_fiscais.marca) +"', " \
                "codigoChefe = '"+str(notas_fiscais.codigoChefe)+"'," \
                "placa = '" + str(notas_fiscais.placa) + "'," \
                "modelo = '"+str(notas_fiscais.modelo)+"'"
    comandoSQL += " where codigo(serie)='"+str(serie)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return notas_fiscais

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(nota_fiscal.notas_fiscais(codigo=data_manager[0], codigoChefe=data_manager[1], marca=data_manager[2], placa=data_manager[3], modelo=data_manager[4]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return nota_fiscal.notas_fiscais(codigo=data_manager[0], codigoChefe=data_manager[1], marca=data_manager[2], placa=data_manager[3], modelo=data_manager[4])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return nota_fiscal.notas_fiscais(codigo=data_manager[0], codigoChefe=data_manager[1], marca=data_manager[2], placa=data_manager[3], modelo=data_manager[4])
    else:
        return None