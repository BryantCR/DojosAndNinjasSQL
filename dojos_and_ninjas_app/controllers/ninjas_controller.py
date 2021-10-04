from flask import render_template, request, redirect
from dojos_and_ninjas_app import app
from dojos_and_ninjas_app.models.Ninja import Ninja
from dojos_and_ninjas_app.models.Dojo import Dojo


@app.route( "/ninjas", methods = ["GET"]  )
def addNewNinja():
    currentDojosInDataBase = Dojo.get_all_dojos()
    print("Dojos in objects ", currentDojosInDataBase)
    return render_template("ninja.html", dojos = currentDojosInDataBase )

@app.route( "/ninjas/create", methods = ["POST"] )
def createNewNinja():
    #Ninja.addNewNinja(request.form)
    data = {
            "dojos_id" : request.form["dojos_id"],
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "age" : request.form['age']
        }
    newNinja = Ninja.addNewNinja(data)
    return redirect("/")

