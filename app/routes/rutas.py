from flask import Blueprint, render_template

from app.modelos.personajes import Personaje

from app.db import db

import requests

bp_nombres = Blueprint('bp_nombres', __name__)


@bp_nombres.route("/")
def index():
    morty = db.Personaje.find({}).sort("name", 1)
    return render_template("index.html", morty=morty)

@bp_nombres.route("/datos/<int:id>")
def datos(id):
    detalles = db.Personaje.find({'id': id})
    return render_template('detalles.html', detalles=detalles)


@bp_nombres.route("/capítulo/<int:id>")
def deta_cap(id):
    captituloss = db.Capitulo.find({'id': id}).sort("name", 1)

    return render_template('capitulos.html', captituloss=captituloss)



@bp_nombres.route("/insertp")
def insert_personajes():
    for a in range(1, 22):
        url = "https://rickandmortyapi.com/api/character?page=" + str(a)
        datos = requests.get(url).json()

        for lise in datos['results']:
            llenado_personaje = Personaje(
                lise['id'],
                lise['name'],
                lise['status'],
                lise['species'],
                lise['type'],
                lise['gender'],
                lise['image'],
            )
            db.Personaje.insert_one(llenado_personaje.to_json())

    return "Se Insertaron los datos , REGRESE A INDEX"



#Usamos el range donde especificamos la lista de capitulos a insertar en la BD
#EL API Consta de 51 CAPITULOS por eso usamos un IF donde si supera el valor no muestra un mensaje
#Consideramos registrar 14 capitulos para este ejercicio
#Tal y como sugiere la diapositiva solo mostramos los PERSONAJES,type,dimension

@bp_nombres.route("/insertc")
def insert_capitulos():
    from app.modelos.capitulo import Capitulo
    from app.db import db

    link = "https://rickandmortyapi.com/api/episode/"

    for numerador in range(1, 15):
        url = link + str(numerador)

        if numerador >=52:
            print("Este capitulo no EXISTE")
        else:
            datos = requests.get(url).json()

            for a in datos['characters']:
                nombres = a
                mirar = requests.get(nombres).json()
                nommbre = mirar['name']
                tyypo = mirar['type']
                fotoss = mirar['image']
                if mirar['location']["url"] == "":
                    print("htts:sae")
                else:
                    mirar['location']["url"]
                    localidad = mirar['location']["url"]
                local_dato = requests.get(localidad).json()
                r = requests.get(localidad)
                # print(local_dato)
                if r.status_code == "404":
                    print("ERROR")
                else:
                    llenado_capitulo = Capitulo(numerador, nommbre, tyypo, local_dato['dimension'], fotoss)
                    db.Capitulo.insert_one(llenado_capitulo.to_json())

                print("--------")
    return "Se Insertaron los capitulos, busque en la url de esta Forma /capítulo/1"
