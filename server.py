from flask  import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "Topsecreto"

@app.route( '/',methods=['GET'])
def pagPrincipal():
    if "contador" not in session:
        session["contador"] = 1
        default = f"{session['contador']} time"
        
    else:
        default = f"{session['contador']} times"
    
    if "visits" not in session:
        session["visits"] = 0
    else:
        session["visits"] += 1

    return render_template("index.html", default=default)

@app.route('/sumamasx', methods=['POST'])
def suma2():
    session["contador"] += session["tunumero"]
    return redirect('/')

@app.route( '/suma', methods=['POST'])
def vecesvisitado():
    
    if "contador" not in session:
        session["contador"] = 1
    else:
        session["contador"] += 1
    return redirect('/')

@app.route( '/limpiar', methods=['POST'])
def limpiando():
    session.clear()
    return redirect('/')

@app.route('/tunumero', methods=['POST'])
def ingresaNumero():
    if 'tunumero' not in session:
        session["tunumero"] = int(request.form["tunumero"])
    else:
        session["tunumero"] = int(request.form["tunumero"])
    return redirect('/')



if __name__=="__main__":
    app.run( debug=True )

























"""
#CODIGO CORRECTO
from flask  import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "Topsecreto"

@app.route( '/',methods=['GET'])
def pagPrincipal():
    if "contador" not in session:
        session["contador"] = 1
        default = f"{session['contador']} time"
        
    else:
        default = f"{session['contador']} times"

    return render_template("index.html", default=default)

@app.route('/suma2', methods=['POST'])
def suma2():
    session["contador"] += 2
    return redirect('/')

@app.route( '/suma', methods=['POST'])
def vecesvisitado():
    
    if "contador" not in session:
        print("SESION AQUI", session)
        session["contador"] = 1
        print("Ahora session que trae?", session)
    else:
        session["contador"] += 1
    return redirect('/')

@app.route( '/limpiar', methods=['POST'])
def limpiando():
    session.clear()
    return redirect('/')

@app.route('/tunumero', methods=['POST'])
def ingresaNumero():
    tuNumero = request.form["tunumero"]
    print(tuNumero)
    return redirect('/')


if __name__=="__main__":
    app.run( debug=True )


@app.route('/suma2', methods=['GET'])
def suma2():
    session["contador"] += 2
    return redirect('/')
"""