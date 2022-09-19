from api.entidades import cliente
from api.database import db

nome_tabela = "clientes"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                "nome varchar(50)," \
                "cpf varchar(11) UNIQUE," \
                "rg varchar(7) UNIQUE," \
                "telefone varchar(11)," \
                "celular varchar(11)," \
                "pais varchar(15)," \
                "estado varchar(15)," \
                "cidade varchar(15)," \
                "bairro varchar(15)," \
                "logradouro varchar(30)," \
                "tipo varchar(15)"

    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(cliente):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "nome," \
                "cpf," \
                "rg," \
                "telefone," \
                "celular," \
                "pais," \
                "estado," \
                "cidade," \
                "bairro," \
                "logradouro," \
                "tipo"
    comandoSQL +=") values ("
    comandoSQL += "'"+str(cliente.nome)+"'," \
                "'"+str(cliente.cpf)+"'," \
                "'"+str(cliente.rg)+"'," \
                "'"+str(cliente.telefone)+"'," \
                "'"+str(cliente.celular)+"'," \
                "'"+str(cliente.pais)+"'," \
                "'"+str(cliente.estado)+"'," \
                "'"+str(cliente.cidade)+"'," \
                "'"+str(cliente.bairro)+"'," \
                "'"+str(cliente.logradouro)+"'," \
                "'"+str(cliente.tipo)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return cliente

def editar(codigo, cliente):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "nome = '"+ str(cliente.nome) +"', " \
                "cpf = '"+str(cliente.cpf)+"'," \
                "rg = '"+str(cliente.rg)+"'," \
                "telefone = '"+str(cliente.telefone)+"'," \
                "celular = '"+str(cliente.celular)+"'," \
                "pais = '"+str(cliente.pais)+"'," \
                "estado = '"+str(cliente.estado)+"'," \
                "cidade = '"+str(cliente.cidade)+"'," \
                "bairro = '"+str(cliente.bairro)+"'," \
                "logradouro = '"+str(cliente.logradouro)+"'," \
                "tipo = '"+str(cliente.tipo)+"'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return cliente

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(cliente.Cliente(codigo=data_manager[0], nome=data_manager[1], cpf=data_manager[2],  rg=data_manager[3], telefone=data_manager[4], celular=data_manager[5], pais=data_manager[6], estado=data_manager[7],cidade=data_manager[8], bairro=data_manager[9], logradouro=data_manager[10], tipo=data_manager[11]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return cliente.Cliente(codigo=data_manager[0], nome=data_manager[1], cpf=data_manager[2],  rg=data_manager[3], telefone=data_manager[4], celular=data_manager[5], pais=data_manager[6], estado=data_manager[7],cidade=data_manager[8], bairro=data_manager[9], logradouro=data_manager[10], tipo=data_manager[11])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return cliente.Cliente(codigo=data_manager[0], nome=data_manager[1], cpf=data_manager[2],  rg=data_manager[3], telefone=data_manager[4], celular=data_manager[5], pais=data_manager[6], estado=data_manager[7],cidade=data_manager[8], bairro=data_manager[9], logradouro=data_manager[10], tipo=data_manager[11])
    else:
        return None