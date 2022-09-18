from ..entidades import funcionario
from ..database import db

nome_tabela = "funcionarios"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "matricula serial primary key," \
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
                  "data_admissao Date," \
                  "data_demissao Date," \
                  "salario Real," \
                  "senha varchar(40)," \
                  "urlImagem varchar(255)"

    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(funcionario):
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
                  "data_admissao," \
                  "data_demissao," \
                  "salario," \
                  "senha," \
                  "urlImagem"
    comandoSQL +=") values ("
    comandoSQL += "'"+str(funcionario.nome)+"'," \
                  "'"+str(funcionario.cpf)+"'," \
                  "'"+str(funcionario.rg)+"'," \
                  "'"+str(funcionario.telefone)+"'," \
                  "'"+str(funcionario.celular)+"'," \
                  "'"+str(funcionario.pais)+"'," \
                  "'"+str(funcionario.estado)+"'," \
                  "'"+str(funcionario.cidade)+"'," \
                  "'"+str(funcionario.bairro)+"'," \
                  "'"+str(funcionario.logradouro)+"'," \
                  "'"+str(funcionario.data_admissao)+"'," \
                  "'"+str(funcionario.data_demissao)+"'," \
                  ""+str(funcionario.salario)+"," \
                  "'"+str(funcionario.senha)+"'," \
                  "'"+str(funcionario.urlImagem)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return funcionario

def editar(matricula, funcionario):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "nome= '"+ str(funcionario.nome) +"', " \
                "cpf = '"+str(funcionario.cpf)+"'," \
                "rg = '"+str(funcionario.rg)+"'," \
                "telefone = '"+str(funcionario.telefone)+"'," \
                "celular = '"+str(funcionario.celular)+"'," \
                "pais = '"+str(funcionario.pais)+"'," \
                "estado = '"+str(funcionario.estado)+"'," \
                "cidade = '"+str(funcionario.cidade)+"'," \
                "bairro = '"+str(funcionario.bairro)+"'," \
                "logradouro = '"+str(funcionario.logradouro)+"'," \
                "data_admissao = '"+str(funcionario.data_admissao)+"'," \
                "data_demissao = '"+str(funcionario.data_demissao)+"'," \
                "salario = "+str(funcionario.salario)+"," \
                "senha = '"+str(funcionario.senha)+"'," \
                "urlImagem = '"+str(funcionario.urlImagem)+"'"
    comandoSQL += " where matricula='"+str(matricula)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return funcionario

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(funcionario.Funcionario(matricula=data_manager[0], nome=data_manager[1], cpf=data_manager[2],  rg=data_manager[3], telefone=data_manager[4], celular=data_manager[5], pais=data_manager[6], estado=data_manager[7],cidade=data_manager[8], bairro=data_manager[9], logradouro=data_manager[10], data_admissao=data_manager[11], data_demissao=data_manager[12], salario=data_manager[13], senha=data_manager[14], urlImagem=data_manager[15]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where matricula='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return funcionario.Funcionario(matricula=data_manager[0], nome=data_manager[1], cpf=data_manager[2],  rg=data_manager[3], telefone=data_manager[4], celular=data_manager[5], pais=data_manager[6], estado=data_manager[7],cidade=data_manager[8], bairro=data_manager[9], logradouro=data_manager[10], data_admissao=data_manager[11], data_demissao=data_manager[12], salario=data_manager[13], senha=data_manager[14], urlImagem=data_manager[15])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY matricula DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return funcionario.Funcionario(matricula=data_manager[0], nome=data_manager[1], cpf=data_manager[2],  rg=data_manager[3], telefone=data_manager[4], celular=data_manager[5], pais=data_manager[6], estado=data_manager[7],cidade=data_manager[8], bairro=data_manager[9], logradouro=data_manager[10], data_admissao=data_manager[11], data_demissao=data_manager[12], salario=data_manager[13], senha=data_manager[14], urlImagem=data_manager[15])
    else:
        return None