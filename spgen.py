#!/usr/bin/env python3

"""
Nombre del Script: spgen.py
Descripción: Simple Page Generator (SPGen) -  is a simple tool that automates the creation of static pages using Jinja2 template files and JSON data.
Autor: Pablo Vargas <pablo.vargas@itu.uncu.edu.ar>
Fecha de Creación: 27/08/2023
Versión: 1.0
Licensed under the Apache License, Version 2.0 (the "License");
"""

import json
from jinja2 import Environment, FileSystemLoader

# Leer los archivos JSON como antes
with open('config/general_data.json', 'r') as file:
    general_data = json.load(file)

with open('config/table_data.json', 'r') as file:
    table_data = json.load(file)

# Configurar Jinja2
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template/plantilla.html')

# Renderizar la plantilla con los datos
html_output = template.render(
    general_data=general_data,
    table_data=table_data
)

# Escribir el resultado en un archivo HTML
with open('docs/index.html', 'w') as file:
    file.write(html_output)

print("Archivo HTML generado exitosamente.")
