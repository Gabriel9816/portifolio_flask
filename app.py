import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/perfil')
def perfil():
    return render_template('perfil.html', utc_dt=datetime.datetime.utcnow())

@app.route('/semana3')
def semana3():
    return render_template('semana3.html', utc_dt=datetime.datetime.utcnow())