from flask import Flask, render_template, request

app = Flask(__name__)

provincias = {
    "01": "Azuay",
    "02": "Bolívar",
    "03": "Cañar",
    "04": "Carchi",
    "05": "Cotopaxi",
    "06": "Chimborazo",
    "07": "El Oro",
    "08": "Esmeraldas",
    "09": "Guayas",
    "10": "Imbabura",
    "11": "Loja",
    "12": "Los Ríos",
    "13": "Manabí",
    "14": "Morona Santiago",
    "15": "Napo",
    "16": "Pastaza",
    "17": "Pichincha",
    "18": "Tungurahua",
    "19": "Zamora Chinchipe",
    "20": "Galápagos",
    "21": "Sucumbíos",
    "22": "Orellana",
    "23": "Santo Domingo de los Tsáchilas",
    "24": "Santa Elena"
}

def validar_cedula(cedula):
    if len(cedula) != 10 or not cedula.isdigit():
        return False

    provincia = int(cedula[:2])
    if provincia < 1 or provincia > 24:
        return False

    tercer_digito = int(cedula[2])
    if tercer_digito >= 6:
        return False

    suma = 0

    for i in range(9):
        numero = int(cedula[i])

        if i % 2 == 0:
            numero *= 2
            if numero > 9:
                numero -= 9

        suma += numero

    digito_verificador = (10 - (suma % 10)) % 10

    return digito_verificador == int(cedula[9])

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""

    if request.method == "POST":
        cedula = request.form["cedula"]

        if validar_cedula(cedula):
            codigo_provincia = cedula[:2]
            provincia = provincias.get(codigo_provincia, "Desconocida")

            mensaje = f"✅ Cédula válida. Provincia: {provincia}"
        else:
            mensaje = "❌ Cédula inválida"

    return render_template("index.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)