from dojos_and_ninjas_app.config.MySQLConnection import connectToMySQL
from dojos_and_ninjas_app import app 
from datetime import date, datetime
from dojos_and_ninjas_app.models.Ninja import Ninja


class Dojo:
    def __init__(self, dojos_id, dojos_name, created_at, updated_at):
        self.dojos_id = dojos_id
        self.dojos_name = dojos_name
        self.created_at = created_at
        self.updated_at = updated_at
        self.ninjas = []
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas").query_db( query )
        dojos = []
        for n in results:
            dojos.append( Dojo( n['dojos_id'], n['dojos_name'], n['created_at'], n['updated_at'] ) )
        return dojos

    @classmethod
    def addNewDojo(cls, data):
        query = "INSERT INTO dojos ( dojos_name, created_at, updated_at) VALUES ( %(dojos_name)s, SYSDATE(), SYSDATE());"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return result

    @classmethod
    def editDojoData(cls, data):
        query = "UPDATE users SET dojos_name = %(dojos_name)s, WHERE dojos_id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print("This come from editDojoData Method model: ", data)
        return result

    @classmethod
    def get_one_dojo(cls, id):
        print("from get_one_dojo method 1 **************************************")
        query  = "SELECT * FROM dojos WHERE dojos_id = %(id)s;"
        data = {
            "id" : id
        }
        result = connectToMySQL('dojos_and_ninjas').query_db( query, data )
        print("End of the get_one_dojo method***********************************")
        return result

    @classmethod
    def deleteDojo(cls, data ):
        query = "DELETE FROM dojos WHERE dojos_id = %(id)s;"
        return connectToMySQL('users_shema').query_db( query, data )

    @classmethod
    def ninjasInDojo(cls, id):
        query= "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.dojos_id WHERE dojos.dojos_id = %(id)s;"
        data = {
            "id" : id
        }
        results = connectToMySQL('dojos_and_ninjas').query_db( query , data )
        print("from ninjasInDojo: ", results)
        # dojos = []
        # for n in results:
        #     data = {
        #         'ninjas_id': n['ninjas_id'],
        #         'first_name': n['first_name'],
        #         'last_name': n['last_name'],
        #         'age': n['age'],
        #         'created_at': n['ninjas.created_at'],
        #         'updated_at': n['ninjas.updated_at']
        #     }
        #     dojos.ninjas.append( Ninja(data) )
        return results





