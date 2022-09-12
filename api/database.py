import psycopg2

url = 'localhost'
db = 'HefestoDB'
usuario = 'postgres'
senha = 'root'

db = psycopg2.connect(
    host = url,
    database = db,
    user = usuario,
    password = senha
)