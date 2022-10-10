from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sendData", methods=['POST'])
def sendData():
    numberphone = request.form["numberphone"]
    print(numberphone)
    print(5555)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)