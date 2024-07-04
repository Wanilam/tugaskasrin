from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods =["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = "jaya"
        password = "1234"
        
        input_username = request.form.get("username")
        input_password= request.form.get("password")
        
        if input_username == username and input_password == password :
            return redirect(url_for("departemen"))
        else :
             return redirect(url_for("login"))
        
@app.route("/departemen")
def departemen():
    return render_template("departemen.html")

@app.route("/karyawan")
def karyawan():
    return render_template("karyawan.html")

@app.route("/proyek")
def proyek():
    return render_template("proyek.html")

@app.route("/gaji")
def gaji():
    return render_template("gaji.html")