from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') 
def index():
    data = {"name" : "Magi Boss", "age" : 19, "salary" : "5000"}
    return render_template("index.html", mydata = data)

@app.route('/about')
def about():
    products = ["เสื้อผ้า", "เตารีด", "ผ้าห่ม"]
    return render_template("about.html", myproduct = products)

@app.route('/admin')
def profile():
    # ชื่อ อายุ
    username = "Bell"
    return render_template("admin.html", username = username)

@app.route('/sendData')
def signupForm():
    fname = request.args.get('fname')
    description = request.args.get('description')
    return render_template("thankyou.html", data={"name":fname, "description":description})

if __name__ == "__main__":
    app.run(debug=True)