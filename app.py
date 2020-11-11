from flask import Flask, jsonify, render_template, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import os

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

developer = os.getenv("DEVELOPER", "Me")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)

def vowels(string): 
    vocales ="aeiouAEIOU"
    count = 0
    for char in string:
        if char in vocales: 
            count = count + 1
    return count

def consonants(string): 
    string = string.replace(" ", "")
    return len(string) - vowels(string)

def updomn(string): 
    c = 1
    new = ""
    for char in string:
        if c == 1: 
            new += char.upper()
            c = c - 1
        else: 
            new += char.lower()
            c = c + 1
    return new

def naive(string): 
    new = ""
    new = string.replace("a", "@")
    new = new.replace("e", "3")
    new = new.replace("i", "!")
    new = new.replace("o", "0")
    new = new.replace("u", ")")
    return new

def cambio(string: str): 
    diccionario = {} #diccionario
    if string == "": 
        return diccionario
    else: 
        diccionario['Original'] = string
        diccionario['Reverse'] = string[::-1]
        diccionario['Len'] = len(string)
        diccionario['Vowels'] = vowels(string)
        diccionario['Consonants'] = consonants(string)
        diccionario['UPPER'] = string.upper()
        diccionario['lower'] = string.lower()
        diccionario['UpDoWn'] = updomn(string)
        diccionario['Naive'] = naive(string)
        return diccionario
    print(diccionario)

@app.route("/", methods = ["GET", "POST"])
def index(): 
    string = ""
    image = url_for('static', filename='profile.jpg')
    string = request.args.get("qwerty", "")
    diccionario = cambio(string)
    print(string)
    print(diccionario)
    return render_template("index.html", image = image, result = diccionario)
    """
    if request.method == 'POST':
        string = request.form['string']
        print(string)
        dict = cambio(string)
        return render_template('index.html', image = image, string = string)
    """
    #return render_template('index.html', image = image, string = string)

if __name__ == "__main__":
    debug = False
    if environment == "development" or environment == "local":
        debug = True
    app.run(host="0.0.0.0", debug=debug, port=5000)
