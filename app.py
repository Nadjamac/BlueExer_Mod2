from flask import flask, render_templates, request 

app = flask(__name__)# instanciando 

@app.route("/")# criando rota
def index():
    return render_templates("index.html")
