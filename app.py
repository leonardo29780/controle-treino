from flask import Flask, request

app = Flask(__name__)

treinos = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        distancia = request.form["distancia"]
        tempo = request.form["tempo"]

        treinos.append({
            "distancia": distancia,
            "tempo": tempo
        })

    html = "<h1>Controle de Treinos ⚽</h1>"

    html += """
    <form method="POST">
        Distância (km): <input name="distancia"><br><br>
        Tempo (min): <input name="tempo"><br><br>
        <button type="submit">Salvar</button>
    </form>
    <hr>
    """

    for treino in treinos:
        html += f"<p>{treino}</p>"

    return html


if __name__ == "__main__":
    app.run(debug=True)
