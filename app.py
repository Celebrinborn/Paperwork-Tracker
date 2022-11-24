from dataclasses import dataclass
import uuid
from datetime import datetime
import typing
from flask import Flask
import flask
import os

# Database

# documents have:
    # ID - GUID
    # Datetime - Datetime
    # Category
    # Box - references box.ID
    # Expiration Date (tax, warranty, other)
    # Scans - list of file directories


# boxes have:
    # ID - GUID
    # Friendly Name (Adjitive + Noun)
    # Location

@dataclass
class Box:
    ID: str
    Created: datetime
    FriendlyName: str
    Location: str

@dataclass
class Document:
    ID: str
    Created: datetime
    Category: str
    Box: str # box id
    ExpirationDate: datetime
    Scans: list[str]

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return flask.render_template('index.html')

@app.route("/NewBox")
def NewBox():
    pass

@app.route("/NewDoc")
def NewDoc():
    pass

@app.route("/ViewBoxes")
def ViewBoxes():
    pass

@app.route("/ViewDoc")
def ViewDoc():
    pass

@app.route("/Search")
def Search():
    pass

@app.route("/MoveBox")
def MoveBox():
    pass

@app.route("/DestroyBox")
def DestoryBox():
    pass
# new box, new doc, view boxes, view docs