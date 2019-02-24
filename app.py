from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sammy:sammy@localhost:5432/sammy'
db = SQLAlchemy(app)


class car(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    year = db.Column(db.Integer)

@app.route('/', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        mycar = car(name=request.form['car'], year=request.form['year'])
        db.session.add(mycar)
        db.session.commit()
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)