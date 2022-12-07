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
