from api.entidades import auxiliar_de_faturista
from api.database import db

nome_tabela = "auxiliares_de_faturistas"

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

def cadastrar(auxiliar_de_faturista):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "matriculaFuncionario"
    comandoSQL +=") values ("
    comandoSQL += "'"+str(auxiliar_de_faturista.matriculaFuncionario)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return auxiliar_de_faturista

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(auxiliar_de_faturista.Auxiliar_de_Faturista(codigo=data_manager[0], matriculaFuncionario=data_manager[1]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return auxiliar_de_faturista.Auxiliar_de_Faturista(codigo=data_manager[0], matriculaFuncionario=data_manager[1])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return auxiliar_de_faturista.Auxiliar_de_Faturista(codigo=data_manager[0], matriculaFuncionario=data_manager[1])
    else:
        return None