from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://gitkmvhthnlnhg:71d2b868373e45d75d00ab9e73ae17476bac22df8ca85b919016e3967426c519@ec2-184-72-239-186.compute-1.amazonaws.com:5432/dc7vpvjksm002t
"
# Not secure, I know. Just practicing for project
heroku = Heroku(app)
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "<h1>Welcome</h1>"


if __name__ == '__main__':
    app.debug = True
    app.run()