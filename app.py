from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://gitkmvhthnlnhg:71d2b868373e45d75d00ab9e73ae17476bac22df8ca85b919016e3967426c519@ec2-184-72-239-186.compute-1.amazonaws.com:5432/dc7vpvjksm002t"
# Not secure, I know. Just practicing for project

heroku = Heroku(app)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/collections', methods=['POST'])
def collections():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        reg = User(email)
        db.session.add(reg)
        db.session.commit()
        return render_template('success.html')
    return render_template('home.html')

@app.route('/return_emails', methods=['GET'])
def return_emails():
    all_emails = db.session.query(User.email).all()
    return jsonify(all_emails)

if __name__ == '__main__':
    app.debug = True
    app.run()