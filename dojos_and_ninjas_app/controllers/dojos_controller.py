from flask import render_template, request, redirect
from dojos_and_ninjas_app import app
from dojos_and_ninjas_app.models.dojo import Dojo

@app.route( "/" )
def displayLogin():
    return redirect ('/dojos')

@app.route( "/dojos", method = ["GET"] )
def loginPage():
    currentDojosInDataBase = User.get_all_dojos()
    print(currentUsersInTable)
    return render_template("dojo.html", dojos = currentDojosInDataBase )










