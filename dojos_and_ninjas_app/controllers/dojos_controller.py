from flask import render_template, request, redirect
from dojos_and_ninjas_app import app
from dojos_and_ninjas_app.models.Dojo import Dojo
from dojos_and_ninjas_app.models.Ninja import Ninja

@app.route( "/" )
def displayLogin():
    return redirect ('/dojos')

@app.route( "/dojos", methods = ["GET"] )
def loginPage():
    currentDojosInDataBase = Dojo.get_all_dojos()
    return render_template("dojo.html", dojos = currentDojosInDataBase )

@app.route( "/dojos/create", methods = ["POST"] )
def createNewDojos():
    print("First request form: ", request.form)
    Dojo.addNewDojo(request.form)
    return redirect('/dojos')

@app.route( "/dojo/ninjas/<id>", methods = ["GET"])
def listOfNinjas(id):
    data = {
        "id" : id
    }
    showDojoNinjas = Dojo.ninjasInDojo(id)
    print("Ninjas: ", showDojoNinjas)
    return render_template("dojoshow.html", dojos = showDojoNinjas)


