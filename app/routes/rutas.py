from flask import Blueprint, render_template

from app.modelos.personajes import Personaje

from app.db import db

import requests

bp_nombres = Blueprint('bp_nombres', __name__)


@bp_nombres.route("/")
def index():
    morty = db.Personaje.find({}).sort("name", 1)
    return render_template("index.html", morty=morty)
