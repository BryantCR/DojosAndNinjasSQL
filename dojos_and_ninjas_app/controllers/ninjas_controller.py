from flask import render_template, request, redirect
from dojos_and_ninjas_app import app
from dojos_and_ninjas_app.models.Ninja import Ninja
from dojos_and_ninjas_app.models.Dojo import Dojo


@app.route( "/ninjas", methods = ["GET"]  )
def addNewNinja():
    currentDojosInDataBase = Dojo.get_all_dojos()
    print("Hola ", currentDojosInDataBase)
    return render_template("ninja.html", dojos = currentDojosInDataBase )

@app.route( "/ninjas/create", methods = ["POST"] )
def createNewNinja():
    data = {
            "id" : id,
            "dojos_name" : request.form['dojos_name'],
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "age" : request.form['age']
        }
    allDojos = Dojo.get_all_dojos()
    newNinja = Ninja.addNewNinja(data, id)
    print("Second request form: ", newNinja)
    return render_template ("ninja.html", ninjas = newNinja, dojos = allDojos, id = id )

@app.route( "/dojo/ninjas/<id>", methods = ["GET"])
def listOfNinjas(id):
    allDojos = Dojo.get_one_dojo(id)
    showDojoNinjas = Ninja.get_all_ninjas()
    print("Ninjas: ", showDojoNinjas)
    return render_template("dojoshow.html", ninjas = showDojoNinjas, dojos = allDojos )








