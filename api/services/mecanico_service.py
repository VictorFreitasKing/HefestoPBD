from ..entidades import mecanico
from ..database import db

nome_tabela = "mecanicos"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                "matriculaFuncionario INTEGER references funcionarios(matricula) UNIQUE," \
                "especialidade varchar(20)"
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(mecanico):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "matriculaFuncionario," \
                "especialidade"
    comandoSQL +=") values ("
    comandoSQL += "'"+str(mecanico.matriculaFuncionario)+"'," \
                "'"+str(mecanico.especialidade)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return mecanico

def editar(codigo, mecanico):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "nome = '"+ str(mecanico.nome) +"', " \
                "matriculaFuncionario = '"+str(mecanico.matriculaFuncionario)+"'," \
                "especialidade = '"+str(mecanico.especialidade)+"'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return mecanico

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(mecanico.Mecanico(codigo=data_manager[0], matriculaFuncionario=data_manager[1], especialidade=data_manager[2]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return mecanico.Mecanico(codigo=data_manager[0], matriculaFuncionario=data_manager[1], especialidade=data_manager[2])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return mecanico.Mecanico(codigo=data_manager[0], matriculaFuncionario=data_manager[1], especialidade=data_manager[2])
    else:
        return None