import datetime
from flask import Flask,  render_template, request
from random import random
import numpy
import cv2
import os
import pandas as pd
import flask_sqlalchemy
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from zipfile import ZipFile
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
name_list = []
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://alex22:Fg#6u2t5HpYT.DT@db4free.net:3306/tads_dw1"
# db = SQLAlchemy(app)


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
        expression = expression.replace(
            '÷', '/').replace('𝗑', '*').replace(',', '.')
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
            binnary = ''.join(format(ord(caractere), '08b')
                              for caractere in expression)
            size = len(binnary)
            separator = 480
            array_2d = [[binnary[n:n + separator]]
                        for n in range(0, size, separator) if n < size]
            mensage = False
        except:
            mensage = True
            binnary = None
        return render_template("calculatoralpha.html", binnary=array_2d, mensage=mensage)


@app.route("/pixel")
def pixel():
    def row(): return [
        f'#{round(random() * 0xffffff):06X}' for _ in range(512)]
    col = [row() for _ in range(512)]
    return render_template("pixel.html", colors=col)


@app.route("/gallery", methods=["GET", "POST"])
def gallery_form():
    path_prefix = './' if os.path.exists('./static') else 'tads/'
    path = f'{path_prefix}static/img/gallery'
    if request.method == "GET":
        for image_name in os.listdir(path):
            os.remove(f'{path}/{image_name}')
        return render_template("gallery.html")
    if request.method == "POST":
        try:
            buffer_file = request.files['input-file-image']
            bytes_array = numpy.frombuffer(buffer_file.read(), numpy.uint8)
            image: numpy.ndarray = cv2.imdecode(bytes_array, cv2.IMREAD_COLOR)
            cv2.imwrite(f'{path}/image_{datetime.now()}.jpg', image)

            if os.path.exists(f'{path}/photos.zip'):
                os.remove(f'{path}/photos.zip')

            with ZipFile(f'{path}/photos.zip', 'w') as zip_obj:
                images_list = os.listdir(path)
                images_list.remove('photos.zip')
                for image_name in images_list:
                    zip_obj.write(f'{path}/{image_name}')

            images_list = os.listdir(path)
            images_list.remove('photos.zip')
            return render_template("gallery.html", images_list=images_list, zip_file_exists=True)
        except:
            return render_template("gallery.html")


@app.route("/array2d", methods=["GET", "POST"])
def pixel_transposition():
    if request.method == "GET":
        return render_template("array2d.html")
    if request.method == "POST":
        try:
            buffer_file = request.files['input-file-image']
            bytes_array = numpy.frombuffer(buffer_file.read(), numpy.uint8)
            image: numpy.ndarray = cv2.imdecode(bytes_array, cv2.IMREAD_COLOR)

            def rgb_to_hex(row): return [
                f'#{pixel[2]:02X}{pixel[1]:02X}{pixel[0]:02X}' for pixel in row]
            matriz = [rgb_to_hex(row) for row in image]

            return render_template("array2d.html", image=matriz)
        except:
            return render_template("array2d.html")


@app.route("/apiteti", methods=["POST"])
def apitoken():
    token = 'abc'
    if request.method == 'POST':
        tokenForm = request.form.get('token')
        if tokenForm == token:
            return render_template("apiteti.html", MSN="sucess")
        return render_template("apiteti.html", MSN="invalid")


@app.route("/triangule", methods=["GET", "POST"])
def triangule():
    if request.method == "GET":
        return render_template("triangulo.html")
    if request.method == "POST":
        ladoA = request.form.get('ladoA')
        ladoB = request.form.get('ladoB')
        ladoC = request.form.get('ladoC')
    return render_template("triangulo.html")


@app.route("/teste")
def teste():
    return render_template("teste.html")

# ---------------cursos--------------------
# class curso(db):
#     curso_id = db.Column(db.Integer, primary_key=True)
#     curso_nome = db.Column(db.String(45))
#     curso_descricao = db.Column(db.String(45))
#     curso_carga_horaria = db.Column(db.Integer)

#     def __init__(self, curso_id, curso_nome, curso_descricao, curso_carga_horaria):
#         self.curso_id = curso_id
#         self.curso_nome = curso_nome
#         self.curso_descricao = curso_descricao
#         self.curso_carga_horaria = curso_carga_horaria


# @app.route("/cursos")
# def cursos():
#     lista_de_cursos = cursos.query.all()
#     return render_template("cursos.html", lista_de_cursos=lista_de_cursos)

# ---------------cursos--------------------
# ---------------fazendo conexão com o banco --------------------
@app.route("/bd", methods=["GET", "POST"])
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


# ------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
