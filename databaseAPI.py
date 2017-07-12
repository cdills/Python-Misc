### RestfulAPI for interacting with sqlite3 with additional support for iOS ###

import sys
import sqlite3
from flask import Flask, g, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
database = "C:\\sqlite3\\users.db" #Will create if noexist

class userprefs(): #Define empty string for argument objects. Not sure if required.
    arg1 = "" 
    arg2 = ""
    udid = ""


class AddUser(Resource): #Updates DB with arguments from POST. Returns posted arguments
    def post(self):
        try:
            global args
            global p1
            # Parse the arguments
            parser = reqparse.RequestParser()

            parser.add_argument('arg1', type=str)
            parser.add_argument('arg2', type=str)
            parser.add_argument('udid', type=str, help='unique device ID')
            args = parser.parse_args()

            newUser = userprefs()
            newUser.arg1 = args['arg1']
            newUser.arg2 = args['arg2']
            newUser.udid = args['udid']
   

            with sqlite3.connect(database) as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO users (id,arg1,arg2,udid) VALUE (Null, \"{newUser.arg1}\", \"{newUser.arg2}\", \"{newUser.udid}\")")
                con.commit()

            return {'1': args['arg1'], '2': args['arg2'], 'udid': args['udid']}

        except Exception as e:
            return {'error': str(e)}

class RemoveUser(Resource): #Removes entry from DB for matching user ID from POST. Returns user ID
    def post(self):
        try:
            global args
            global p1
            # Parse the arguments
            parser = reqparse.RequestParser()

            parser.add_argument('udid', type=str, help='unique device ID')
            args = parser.parse_args()

            newUser = userprefs()

            newUser.udid = args['udid']


            with sqlite3.connect(database) as con:
                cur = con.cursor()
                cur.execute(f"DELETE FROM users WHERE udid = \"{newUser.udid}\"") #Will delete ALL matching entries.
                con.commit()

            return {'udid': args['udid']}

        except Exception as e:
            return {'error': str(e)}

api.add_resource(AddUser, '/AddUser') #Adds the functions to the specified URL for API
api.add_resource(RemoveUser, '/RemoveUser') #Adds the functions to the specified URL for API

def create_connection(db_file): #Creates DB connection, returns connection object
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)

    return None

def create_table(conn, create_table_sql): #Creates table with specified query and connection object.
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)

def main():

    sql_create_user_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        arg1 text NOT NULL,
                                        arg2 text,
                                        UDID text
                                    ); """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create user table
        create_table(conn, sql_create_user_table)

    else:
        print("Error! cannot create the database connection.")

    app.run(debug=False) #Starts the API listening on localhost:5000


if __name__ == "__main__":
    sys.exit(main())
