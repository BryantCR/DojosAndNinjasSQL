from dojos_and_ninjas_app.confing.MySQLConnection import connectToMySQL
from dojos_and_ninjas_app import app 
from datetime import date, datetime

class Ninja:
    def __init__(self, ninjas_id, first_name, last_name, age, dojos_id, created_at, updated_at):
        self.ninjas_id = ninjas_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.dojos_id = dojos_id
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL("dojos_and_ninjas").query_db( query )
        ninjas = []
        for n in results:
            ninjas.append( Ninja( n['ninjas_id'], n['first_name'], n['last_name'], n['age'] ) )
        return ninjas

    @classmethod
    def get_one_ninja(cls, id):
        print("1")
        query  = "SELECT * FROM ninjas WHERE id = %(id)s;"
        data = {
            "id" : id
        }
        result = connectToMySQL('dojos_and_ninjas').query_db( query, data )
        #for users in result:
            #user_data.append(User(user['id'],user['first_name'], user['last_name'], user['email'],user['created_at'],user['updated_at']))
        print("2" )
        return result









