from api.entidades import nota_fiscal
from api.database import db

nome_tabela = "notas_fiscais"

def criar_tabela():
    #Montando comando SQL
    comandoSQL = "CREATE TABLE IF NOT EXISTS "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo serial primary key UNIQUE," \
                  "codigo_loja_conveniada INTEGER references lojas_conveniadas(codigo)," \
                  "numero varchar(9)," \
                  "serie varchar(3)," \
                  "codigoAuxiliarFaturista INTEGER references auxiliares_de_faturistas(codigo)," \
                  "codigoOS INTEGER references ordens_servico(codigo) UNIQUE,"\
                  "total REAL"
    comandoSQL += ");"


    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

def cadastrar(nota_fiscal):
    #Montando comando SQL
    comandoSQL = "insert into "
    comandoSQL += nome_tabela
    comandoSQL += "("
    comandoSQL += "codigo_loja_conveniada," \
                  "numero,"\
                  "serie," \
                  "codigoAuxiliarFaturista," \
                  "codigoOS,"\
                  "total"
    comandoSQL +=") values ("
    comandoSQL += "'"+str(nota_fiscal.codigo_loja_conveniada)+"'," \
                "'" + str(nota_fiscal.numero) + "'," \
                "'" + str(nota_fiscal.serie) + "',"\
                "'" + str(nota_fiscal.codigoAuxiliarFaturista) + "'," \
                "'" + str(nota_fiscal.codigoOS) + "'," \
                "'"+str(nota_fiscal.total)+"'"
    comandoSQL += ");"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()

    return nota_fiscal

def editar(codigo, nota_fiscal):
    #Montando comando SQL
    comandoSQL = "UPDATE "
    comandoSQL += nome_tabela
    comandoSQL += " SET "
    comandoSQL += "codigo_loja_conveniada = '"+ str(nota_fiscal.codigoLojaConveniada) +"', " \
                "numero = '"+str(nota_fiscal.numero)+"'," \
                "serie = '" + str(nota_fiscal.serie) + "'," \
                "codigoAuxiliarFaturista = '" + str(nota_fiscal.codigoAuxiliarFaturista) + "'," \
                "codigoOS = '" + str(nota_fiscal.codigoOS) + "'," \
                "total = '"+str(nota_fiscal.total)+"'"
    comandoSQL += " where codigo(serie)='"+str(codigo)+"';"

    #Executando comando no banco de dados
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    db.commit()
    cursor.close()
    return nota_fiscal

def getAll():
    comandoSQL = "SELECT * FROM "+nome_tabela+";"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    lista = []
    data_manager = cursor.fetchone()
    if data_manager is None:
        return None
    while data_manager is not None:
        lista.append(nota_fiscal.Nota_Fiscal(codigo=data_manager[0], codigoLojaConveniada=data_manager[1], numero=data_manager[2], serie=data_manager[3], codigoAuxiliarFaturista=data_manager[4], codigoOS=data_manager[5], total=[6]))
        data_manager = cursor.fetchone()

    return lista

def get(id):
    comandoSQL = "SELECT * from "+nome_tabela+" where codigo='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return nota_fiscal.Nota_Fiscal(codigo=data_manager[0], codigoLojaConveniada=data_manager[1], numero=data_manager[2], serie=data_manager[3], codigoAuxiliarFaturista=data_manager[4], codigoOS=data_manager[5], total=data_manager[4])
    else:
        return None

def get_ultimo():
    comandoSQL = "SELECT * from "+nome_tabela+" ORDER BY codigo DESC limit 1;"
    cursor = db.cursor()
    cursor.execute(comandoSQL)
    data_manager = cursor.fetchone()
    if data_manager:
        return nota_fiscal.Nota_Fiscal(codigo=data_manager[0], codigoLojaConveniada=data_manager[1], numero=data_manager[2], serie=data_manager[3], codigoAuxiliarFaturista=data_manager[4], codigoOS=data_manager[5], total=data_manager[4])
    else:
        return None