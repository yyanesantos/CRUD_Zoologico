from Database.functions import functions
from Tabelas.recinto import recinto
from Tabelas.cuidador import cuidador

db = functions(
    host="yane-2.local",
    user="root",
    password="12345678",
    database="zoologicoo"
)

recinto1 = recinto(1, "Do lado da entrada", 30)
db.criar("recinto", recinto)
db.listar("recinto")

cuidador1 = cuidador("Fernanda Lemos", "12345678900", "(85) 99999-9999")
db.criar("cuidador", cuidador1)
db.listar("cuidador")