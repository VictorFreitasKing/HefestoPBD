from api.entidades import nota_fiscal_servico
from api.database import db

nome_tabela = "notas_fiscais_servico"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key," \
                  "codigoOS INTEGER references ordens_servico(codigo)," \
                  "codigoFaturista INTEGER references faturistas(codigo)," \
                  "data_emissao Date," \
                  "total REAL"
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(nota_fiscal_servico):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigoOS," \
                  "codigoFaturista," \
                  "data_emissao," \
                  "total"
    comandoSQL +=") values ("
    comandoSQL += "'" + str(nota_fiscal_servico.codigoOS) + "'," \
                "'" + str(nota_fiscal_servico.codigoFaturista) + "'," \
                "'" + str(nota_fiscal_servico.data_emissao) + "'," \
                "'" + str(nota_fiscal_servico.total) + "'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return nota_fiscal_servico

def editar(codigo, nota_fiscal_servico):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "codigoOS = '" + str(nota_fiscal_servico.codigoOS) + "', " \
                "codigoFaturista = '" + str(nota_fiscal_servico.codigoFaturista) + "'," \
                "data_emissao = '" + str(nota_fiscal_servico.data_emissao) + "'," \
                "total = '" + str(nota_fiscal_servico.total) + "'"
    comandoSQL += " where codigo='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return nota_fiscal_servico

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(nota_fiscal_servico.Nota_Fiscal_Servico(codigo=data_manager[0], codigoOS=data_manager[1], codigoFaturista=data_manager[2], data_emissao=data_manager[3], total=data_manager[4]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return nota_fiscal_servico.Nota_Fiscal_Servico(codigo=data_manager[0], codigoOS=data_manager[1], codigoFaturista=data_manager[2], data_emissao=data_manager[3], total=data_manager[4])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return nota_fiscal_servico.Nota_Fiscal_Servico(codigo=data_manager[0], codigoOS=data_manager[1], codigoFaturista=data_manager[2], data_emissao=data_manager[3], total=data_manager[4])
    else:
        return None