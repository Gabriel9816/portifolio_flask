import datetime
from flask import Flask,  render_template, request

app = Flask(__name__)
name_list = []

@app.route('/', methods=["GET", "POST"])
def hello():
    teacher = "Alex"
    students_list = ["Mauricio", "Caio", "Toshiba"]
    if request.method == "GET":
        return render_template("index.html", teacher=teacher, students_list=students_list)
    if request.method == "POST":
        name = request.form.get('Name')
        name_list.append(name)
        return render_template("index.html", teacher=teacher, students_list=students_list, name=name, name_list=name_list)

@app.route("/plano-de-ensino")
def teaching_plan():
    return render_template("plan.html")

@app.route("/initial-template")
def initial_template():
    return "<h1>Hello, World!</h1>"

