from ..entidades import titulo
from ..database import db

nome_tabela = "titulos"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                "data_baixa varchar(10)"\
                "valor varchar(11)," \
                "vencimento varchar(15)," \
                "codigoRecepcionista INTEGER references recepcionistas(codigo) UNIQUE" \
                "codigoNFS INTEGER references notas_fiscais_servico(codigo) UNIQUE"
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(titulos):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL +="data_baixa" \
                "codigoNFS," \
                "valor," \
                "codigoRecepcionista," \
                "vencimento" 
    comandoSQL +=") values ("
    comandoSQL += "'"+str(titulos.data_baixa)+"'," \
                "'"+str(titulos.codigoNFS)+"'," \
                "'" + str(titulos.valor) + "'," \
                "'" + str(titulos.codigoRecepcionista) + "'," \
                "'"+str(titulos.vencimento)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return titulos

def editar(codigo, titulos):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "data_baixa = '"+ str(titulos.data_baixa) +"', " \
                "codigoRecepcionista = '"+ str(titulos.codigoRecepcionista) +"', " \
                "codigoNFS = '"+str(titulos.codigoNFS)+"'," \
                "valor = '" + str(titulos.valor) + "'," \
                "vencimento = '"+str(titulos.vencimento)+"'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return titulos

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(titulo.titulos(codigo=data_manager[0], codigoNFS=data_manager[1], codigoRecepcionista=data_manager[2], valor=data_manager[3], vencimento=data_manager[4], data_baixa=data_manager[5]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return titulo.titulos(codigo=data_manager[0], codigoNFS=data_manager[1], codigoRecepcionista=data_manager[2], valor=data_manager[3], vencimento=data_manager[4], data_baixa=data_manager[5])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return titulo.titulos(codigo=data_manager[0], codigoNFS=data_manager[1], codigoRecepcionista=data_manager[2], valor=data_manager[3], vencimento=data_manager[4], data_baixa=data_manager[5])
    else:
        return None