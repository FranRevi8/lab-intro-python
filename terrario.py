from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

class Terrario:
    def __init__(self, nombre, ancho, largo):
        self.nombre = nombre
        self.ancho = ancho
        self.largo = largo
        self.habitantes = []

    def agregar_habitante(self, serpiente):
        self.habitantes.append(serpiente)

    def area_terrario(self):
        return self.largo * self.ancho
    
    def mostrar_serpientes(self):
        for serpiente in self.habitantes:
            print(f'Serpiente {serpiente.nombre}.')

    def guardar(self, archivo):
        with open(archivo, 'w') as f:
            json.dump(self.__dict__, f, default=lambda o: o.__dict__, indent=4)
    
class Serpiente:
    def __init__(self, nombre, longitud, especie):
        self.nombre = nombre
        self.longitud = longitud
        self.especie = especie

    def deslizarse(self):
        print(f'La serpiente {self.nombre} se está deslizando.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre_terrario = request.form.get('nombre_terrario')
    ancho = request.form.get('ancho')
    largo = request.form.get('largo')
    nombre_serpiente = request.form.get('nombre_serpiente')
    longitud = request.form.get('longitud')
    especie = request.form.get('especie')

    terrario = Terrario(nombre_terrario, ancho, largo)
    serpiente = Serpiente(nombre_serpiente, longitud, especie)
    terrario.agregar_habitante(serpiente)
    terrario.guardar('terrario.json')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

terrario1 = Terrario("Primer terrario", 35, 60)

kobra = Serpiente("Kobra", 170, "kobrasium serpenticus")
casca = Serpiente("Cascabel", 125, "cascabellum serpenticus")

terrario1.agregar_habitante(kobra)
terrario1.agregar_habitante(casca)

print(f'El área del terrario es {terrario1.area_terrario()} cm.')

kobra.deslizarse()
casca.deslizarse()

terrario1.mostrar_serpientes()







