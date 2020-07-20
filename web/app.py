from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from datetime import datetime
import os
import pymysql
import json
app = Flask(__name__)
auth = HTTPBasicAuth() 

def get_database_connection():
    dbhost = os.environ['DB_HOST']
    dbuser = os.environ['DB_USER']
    dbpass = os.environ['DB_PASS']
    dbname = os.environ['DB_NAME']
    dbport = int(os.environ['DB_PORT'])
    db = pymysql.connect(dbhost, dbuser, dbpass, dbname, port=dbport, autocommit=True)
    return db

@auth.verify_password
def verify_password(username, password):
    user = os.environ['AUTH_USER']
    userpass = os.environ['AUTH_PASS']
    if username == user and userpass == password:
        return True
    return False

@app.route('/')
def hello_whale():
    db = get_database_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * from possequotes")
    data = cursor.fetchone()
    db.close()
    return f"Version is {data}"

@app.route('/possequote', methods=['GET'])
def get_posse_quote():
    db = get_database_connection()
    cursor = db.cursor()
    sql = " select * \
    from possequotes order by RAND() limit 1"
    data = {}
    try:
        # Execute the SQL command
        cursor.execute(sql)
        data = cursor.fetchone()
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

        # disconnect from server
    db.close()
    return jsonify(data)

@app.route('/possequote', methods=['POST'])
#@auth.login_required
def add_posse_quote():
    quote =  json.loads(request.data)
    db = get_database_connection()
    cursor = db.cursor()
    #import pdb; pdb.set_trace()
    sql = f"INSERT INTO possequotes(date_added, quote) \
            VALUES('{datetime.now().date().isoformat()}', '{quote['quote']}');"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

        # disconnect from server
    db.close()
    return quote

if __name__ == '__main__':
    app.run(host='0.0.0.0')
