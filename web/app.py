from flask import Flask, render_template
import os
app = Flask(__name__)
 
 
@app.route('/')
def hello_whale():
    test = os.environ
    return f"{test} hello there!"
 
if __name__ == '__main__':
    app.run(host='0.0.0.0')
