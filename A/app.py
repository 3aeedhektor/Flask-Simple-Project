from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.sqlite3'

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    city = db.Column(db.String(50))

with app.app_context():
    db.drop_all()
    db.create_all()

    u1 = User(full_name='Alfreds Futterkiste', city='Berlin')
    db.session.add(u1)
    db.session.commit()

    u2 = User(full_name='LILA-Supermercado', city='Barquisimeto')
    db.session.add(u2)
    db.session.commit()

    u3 = User(full_name='Vaffeljernet', city='Arhus')
    db.session.add(u3)
    db.session.commit()

    u4 = User(full_name='White Clover Markets', city='Seattle')
    db.session.add(u4)
    db.session.commit()

    u5 = User(full_name='Wolski', city='	Walla')
    db.session.add(u5)
    db.session.commit()

#Router
#home
@app.route('/')
@app.route('/home')
def home():
    users = User.query.all()
    return render_template('home.html', users = users)

#about
@app.route('/about')
def about():
    return render_template('about.html')

#detail
@app.route('/detail/<int:user_id>')
def detail(user_id):
    user = User.query.get(user_id)
    return render_template('detail.html', user=user)
#delete
@app.route('/delete/<int:user_id>')
def delete(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
