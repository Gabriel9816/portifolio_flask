import datetime
from flask import Flask,  render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route("/plano-de-ensino")
def teaching_plan():
    return render_template("plan.html")

@app.route("/", methods=["GET", "POST"])
def simple_calculator():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        expression = request.form.get('expression')
        expression = expression.replace('÷','/').replace('𝗑', '*').replace(',', '.')
        try:
            result = eval(expression)
            binnary = bin(int(result)).removeprefix('0b')
            mensage = None
        except:
            mensage = 'Verifique se digitou corretamente'
            result = binnary = None
        return render_template("index.html", result=result, binnary=binnary, mensage=mensage)
