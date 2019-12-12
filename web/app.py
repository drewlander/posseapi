from flask import Flask, render_template
import os
import pymysql
app = Flask(__name__)
 

def get_database_connection():
    dbhost = os.environ['DB_HOST']
    dbuser = os.environ['DB_USER']
    dbpass = os.environ['DB_PASS']
    dbname = os.environ['DB_NAME']
    db = pymysql.connect(dbhost, dbuser, dbpass, dbname)
    return db

@app.route('/')
def hello_whale():
    db = get_database_connection()
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    db.close()
    return f"Version is {data}"
 
if __name__ == '__main__':
    app.run(host='0.0.0.0')
