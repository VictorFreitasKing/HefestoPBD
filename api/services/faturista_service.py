from api.entidades import faturista
from api.database import db

nome_tabela = "faturistas"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                "matriculaFuncionario INTEGER references funcionarios(matricula) UNIQUE" 
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(faturista):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "matriculaFuncionario" 
    comandoSQL +=") values ("
    comandoSQL += "'"+str(faturista.matriculaFuncionario)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return faturista

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(faturista.Faturista(codigo=data_manager[0], matriculaFuncionario=data_manager[1]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return faturista.Faturista(codigo=data_manager[0], matriculaFuncionario=data_manager[1])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return faturista.Faturista(codigo=data_manager[0], matriculaFuncionario=data_manager[1])
    else:
        return None