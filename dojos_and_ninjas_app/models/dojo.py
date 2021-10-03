from dojos_and_ninjas_app.config.MySQLConnection import connectToMySQL
from dojos_and_ninjas_app import app 
from datetime import date, datetime

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
        query = "INSERT INTO dojos (dojos_id, dojos_name, created_at, updated_at) VALUES ( %(dojos_id)d, %(dojos_name)s, SYSDATE(), SYSDATE());"
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
        user_data = []

        #for users in result:
            #user_data.append(User(user['id'],user['first_name'], user['last_name'], user['email'],user['created_at'],user['updated_at']))
        print("End of the get_one_dojo method***********************************")
        return result

    @classmethod
    def deleteDojo(cls, data ):
        query = "DELETE FROM dojos WHERE dojos_id = %(id)s;"
        return connectToMySQL('users_shema').query_db( query, data )