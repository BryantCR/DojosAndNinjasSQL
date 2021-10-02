from flask import Flask, render_template, request, redirect, session
from dojos_and_ninjas_app import app
from dojos_and_ninjas_app.controllers import ninjas_controller, dojos_controller

if __name__ == "__main__":
    app.run( debug = True )