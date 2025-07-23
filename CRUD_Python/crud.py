from Database.functions import functions
from Tabelas.recinto import recinto
from Tabelas.cuidador import cuidador
from Tabelas.especie import especie

db = functions(
    host="yane-2.local",
    user="root",
    password="12345678",
    database="zoologicoo"
)

recinto1 = recinto(1, "Do lado da entrada", 30)
db.criar("recinto", recinto1)
db.listar("recinto")

cuidador1 = cuidador("Fernanda Lemos", "12345678900", "(85) 99999-9999")
db.criar("cuidador", cuidador1)
db.listar("cuidador")

especie1 = especie("Lehonysys Fulanys", "Leão", "Savana africana")
db.criar("especie", especie1)
db.listar("especie")