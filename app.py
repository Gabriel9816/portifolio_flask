import datetime
from flask import Flask,  render_template, request

app = Flask(__name__)
name_list = []


def remove_duplicates(lista):
    empty_list = []
    for i in lista:
        if i not in empty_list:
            empty_list.append(i)
    empty_list.sort()
    return empty_list



@app.route('/', methods=["GET", "POST"])
def hello():
    teacher = "Alex"
    students_list = ["Mauricio", "Caio", "Toshiba"]
    if request.method == "GET":
        return render_template("index.html", teacher=teacher, students_list=students_list)
    if request.method == "POST":
        name = request.form.get('name')
        name_list.append(name)
        lista = remove_duplicates(name_list)
        return render_template("index.html", teacher=teacher, students_list=students_list, name=name, name_list=lista)

@app.route("/plan")
def teaching_plan():
    return render_template("plan.html")

@app.route("/hello")
def initial_template():
    return "<h1>Hello, World!</h1>"

@app.route("/calculator", methods=["GET", "POST"])
def simple_calculator():
    if request.method == "GET":
        return render_template("calculator.html")
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
        return render_template("calculator.html", result=result, binnary=binnary, mensage=mensage)
@app.route("/calculatoralpha", methods=["GET", "POST"])
def alphanum_calculator():
    if request.method == "GET":
        return render_template("calculatoralpha.html")
    if request.method == "POST":
        expression = request.form.get('expression')
        try:
            binnary = ''.join(format(ord(caractere), '08b') for caractere in expression)
            size = len(binnary)
            separator = 480
            array_2d = [[binnary[n:n + separator]] for n in range(0, size, separator) if n < size]
            mensage = False
        except:
            mensage = True
            binnary = None
        return render_template("calculatoralpha.html", binnary=array_2d, mensage=mensage)