from ..entidades import nota_fiscal_servico
from ..database import db

nome_tabela = "notas_fiscais_servico"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                  "data_emissao varchar(10)," \
                  "total varchar(15)," \
                  "codigoFaturista INTEGER references faturistas(codigo) UNIQUE" \
                  "codigoOS INTEGER references ordem_servico(codigo) UNIQUE"
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(notas_fiscais_servico):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigoOS," \
                "data_emissao," \
                "codigoFaturista," \
                "total" 
    comandoSQL +=") values ("
    comandoSQL += "'"+str(notas_fiscais_servico.codigoOS)+"'," \
                "'" + str(notas_fiscais_servico.data_emissao) + "'," \
                "'" + str(notas_fiscais_servico.codigoFaturista) + "'," \
                "'"+str(notas_fiscais_servico.total)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return notas_fiscais_servico

def editar(codigo, notas_fiscais_servico):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "codigoFaturista = '"+ str(notas_fiscais_servico.codigoFaturista) +"', " \
                "codigoOS = '"+str(notas_fiscais_servico.codigoOS)+"'," \
                "data_emissao = '" + str(notas_fiscais_servico.data_emissao) + "'," \
                "total = '"+str(notas_fiscais_servico.total)+"'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return notas_fiscais_servico

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(nota_fiscal_servico.notas_fiscais_servico(codigo=data_manager[0], codigoOS=data_manager[1], codigoFaturista=data_manager[2], data_emissao=data_manager[3], total=data_manager[4]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return nota_fiscal_servico.notas_fiscais_servico(codigo=data_manager[0], codigoOS=data_manager[1], codigoFaturista=data_manager[2], data_emissao=data_manager[3], total=data_manager[4])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return nota_fiscal_servico.notas_fiscais_servico(codigo=data_manager[0], codigoOS=data_manager[1], codigoFaturista=data_manager[2], data_emissao=data_manager[3], total=data_manager[4])
    else:
        return None