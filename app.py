from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sammy:sammy@localhost/sammy'
db = SQLAlchemy(app)


class car(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    year = db.Column(db.Integer)

@app.route('/')
def main():
    return '<h1>this is main page</h1>'

if __name__ == '__main__':
    app.run(debug=True)