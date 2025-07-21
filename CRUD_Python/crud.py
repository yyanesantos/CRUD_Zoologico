from Database.functions import functions
from Tabelas.recinto import recinto

db = functions(
    host="yane-2.local",
    user="root",
    password="12345678",
    database="zoologicoo"
)

recinto = recinto(1, "Do lado da entrada", 30)
db.criar("recinto", recinto)
db.listar("recinto")
