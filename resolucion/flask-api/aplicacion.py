from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return """<p> API Flask </p>
			  <a href="/edificios">Edificios</a>
			  <br>
			  <a href="/departamentos">Departamentos</a>
    	   """

@app.route("/edificios")
def obtener_edificio():
    r = requests.get("http://localhost:8000/api/edificios/",
            auth=('sdgarcia6', '1'))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("edificios-obtenidos.html", edificios=edificios,
    numero_edificios=numero_edificios)


@app.route("/departamentos")
def obtener_departamento():
    r = requests.get("http://localhost:8000/api/departamentos/",
            auth=('sdgarcia6', '1'))
    datos = json.loads(r.content)['results']
    numero_departamentos = json.loads(r.content)['count']
    departamentos = []
    for d in datos:
        departamentos.append({'nombre_propietario':d['nombre_propietario'], 'costo':d['costo'], 
        'cantidad_cuartos':d['cantidad_cuartos'],'edificio': obtener_nombre_edificio(d['edificio'])})

    return render_template("departamentos-obtenidos.html", departamentos=departamentos,
    numero_departamentos=numero_departamentos)

def obtener_nombre_edificio(url):
    r = requests.get(url, auth=('sdgarcia6', '1'))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio

