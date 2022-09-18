from ..entidades import titulo
from ..database import db

nome_tabela = "titulos"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                  "codigoNFS INTEGER references notas_fiscais_servico(codigo) UNIQUE," \
                  "codigoRecepcionista INTEGER references recepcionistas(codigo) UNIQUE," \
                  "valor REAL," \
                  "vencimento Date," \
                  "data_baixa Date"
    comandoSQL += ");"

    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(titulo):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL +="codigoNFS," \
                "codigoRecepcionista," \
                "valor," \
                "vencimento"
    comandoSQL +=") values ("
    comandoSQL += "'" + str(titulo.codigoNFS) + "'," \
                "'" + str(titulo.codigoRecepcionista) + "'," \
                "'" + str(titulo.valor) + "'," \
                "'" + str(titulo.vencimento) + "'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return titulo

def editar(codigo, titulo):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "codigoNFS = '" + str(titulo.codigoNFS) + "', " \
                "codigoRecepcionista = '" + str(titulo.codigoRecepcionista) + "', " \
                "valor = '" + str(titulo.valor) + "'," \
                "vencimento = '" + str(titulo.vencimento) + "'," \
                "data_baixa = '" + str(titulo.data_baixa) + "'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return titulo

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(titulo.Titulo(codigo=data_manager[0], codigoNFS=data_manager[1], codigoRecepcionista=data_manager[2], valor=data_manager[3], vencimento=data_manager[4], data_baixa=data_manager[5]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return titulo.Titulo(codigo=data_manager[0], codigoNFS=data_manager[1], codigoRecepcionista=data_manager[2], valor=data_manager[3], vencimento=data_manager[4], data_baixa=data_manager[5])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return titulo.Titulo(codigo=data_manager[0], codigoNFS=data_manager[1], codigoRecepcionista=data_manager[2], valor=data_manager[3], vencimento=data_manager[4], data_baixa=data_manager[5])
    else:
        return None