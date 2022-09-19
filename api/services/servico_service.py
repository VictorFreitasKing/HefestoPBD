from api.entidades import servico
from api.database import db

nome_tabela = "servicos"

def criar_tabela():
   #Montando comando SQL
   comandoSQL = "CREATE TABLE IF NOT EXISTS "
   comandoSQL += nome_tabela
   comandoSQL += "("
   comandoSQL += "codigo serial primary key," \
               "descricao varchar(60)"
   comandoSQL += ");"


   cursor = db.cursor()
   cursor.execute(comandoSQL)
   db.commit()
   cursor.close()

def cadastrar(servico):
   #Montando comando SQL
   comandoSQL = "insert into "
   comandoSQL += nome_tabela
   comandoSQL += "("
   comandoSQL += "descricao"
   comandoSQL +=") values ("
   comandoSQL += "'"+str(servico.descricao)+"'"
   comandoSQL += ");"

   #Executando comando no banco de dados
   cursor = db.cursor()
   cursor.execute(comandoSQL)
   db.commit()
   cursor.close()

   return servico

def editar(codigo, servico):
   #Montando comando SQL
   comandoSQL = "UPDATE "
   comandoSQL += nome_tabela
   comandoSQL += " SET "
   comandoSQL += "descricao = '"+ str(servico.descricao) +"'"
   comandoSQL += " where codigo='"+str(codigo)+"';"

   #Executando comando no banco de dados
   cursor = db.cursor()
   cursor.execute(comandoSQL)
   db.commit()
   cursor.close()
   return servico

def getAll():
   comandoSQL = "SELECT * FROM "+nome_tabela+";"
   cursor = db.cursor()
   cursor.execute(comandoSQL)
   lista = []
   data_manager = cursor.fetchone()
   if data_manager is None:
       return None
   while data_manager is not None:
       lista.append(servico.Servico(codigo=data_manager[0], descricao=data_manager[1]))
       data_manager = cursor.fetchone()

   return lista

def get(id):
   comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
   cursor = db.cursor()
   cursor.execute(comandoSQL)
   data_manager = cursor.fetchone()
   if data_manager:
       return servico.Servico(codigo=data_manager[0], descricao=data_manager[1])
   else:
       return None

def get_ultimo():
   comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
   cursor = db.cursor()
   cursor.execute(comandoSQL)
   data_manager = cursor.fetchone()
   if data_manager:
       return servico.servicos(codigo=data_manager[0], descricao=data_manager[1])
   else:
       return None
