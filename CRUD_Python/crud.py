from Database.functions import functions
from Tabelas.recinto import recinto
from Tabelas.cuidador import cuidador
from CRUD.crud_recinto import criar_recinto
from Tabelas.especie import especie
from CRUD.crud_animal import criar_animal
from CRUD.crud_eventosEducativos import criar_evento
from datetime import datetime
from Tabelas.eventosEducativos import eventosEducativos
from Tabelas.animal import animal
from CRUD.crud_animal import criar_animal


db = functions(
    host="yane-2.local",
    user="root",
    password="12345678",
    database="zoologicoo"
)


recinto1 = recinto(2, "Do lado da entrada", 30)
criar_recinto(2, "Do lado da entrada", 30)
db.listar("recinto")

cuidador1 = cuidador("Fernanda Lemos", "12345678900", "(85) 99999-9999")
db.criar("cuidador", cuidador1)
db.listar("cuidador")

especie1 = especie("Lehonysys Fulanys", "Leão", "Savana africana")
db.criar("especie", especie1)
db.listar("especie")

evento = eventosEducativos(1, "Parque em ação", "2025-07-08", 1)
criar_evento(11, "Leões por todo o lado!", "2025-07-23", 60000)
db.listar("eventosEducativos")

animal = animal(1, "ricardo", "2025-07-08", "F", "Lehonysys Fulanys", 1)
criar_animal(2, "ricardo", "2025-07-08", "F", "Lehonysys Fulanys", 1)
db.listar("animal")

