from flask import Flask, render_template
import os
app = Flask(__name__)
 
 
@app.route('/')
def hello_whale():
    test = os.getenv("test")
    return "{test} hello there!"
 
if __name__ == '__main__':
    app.run(host='0.0.0.0')
