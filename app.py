import re
import json
from flask import Flask, render_template, url_for, request, redirect, jsonify
from static.project_files.password_security import Password
from static.project_files.display_code import code
import csv

app = Flask(__name__)


# Functions for rendering HTML templates
@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/<string:page_name>", methods=["POST", "GET"])
def html_page(page_name):
    return render_template(page_name)


# Functions for Contact Me form
def write_to_file(data):
    with open("./database.txt", "a") as db:
        db.write(
            f"[\nEmail:\n{data['email']}\nName:\n{data['name']}\nMessage:\n{data['message']}\n]\n"
        )


def write_to_csv(data):
    with open("./database.csv", "a", newline="") as db:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        csv_writer = csv.writer(
            db, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([email, name, message])


@app.route("/contact_form", methods=["POST", "GET"])
def contact_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thank_you.html")
        except:
            return "Database Error occured"
    else:
        return "Request Error occured"


# Functions for passwordcheck demo
def get_color(pass_strength: str) -> str:
    if pass_strength == "Very Poor":
        return "red"
    elif pass_strength == "Poor":
        return "orangered"
    elif pass_strength == "Alright":
        return "orange"
    elif pass_strength == "Good":
        return "lightgreen"
    elif pass_strength == "Very Good":
        return "limegreen"
    elif pass_strength == "Amazing":
        return "deepskyblue"


@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        try:
            data = request.form["name"]
            if len(data) > 0:
                pswd = Password()
                pswd.config(data)
                strength = pswd.get_password_strength()
                color = get_color(strength)
                display = f'<span id="security_results" style="color: {color};">{strength}</span>'
                return display
            else:
                return '<span id="security_results" style="color: #ffffff;">N/A</span>'
        except:
            keys = request.form
            return keys
    else:
        return "Submission Error occured"


# Functions for displaying and hiding preformatted code
@app.route("/show_code", methods=["POST"])
def show_code():
    if request.method == "POST":
        try:
            data = request.form
            display = f'\
            <button\
            class="button primary"\
            hx-post="/hide_code"\
            hx-target="#{data.get("code")}"\
            hx-vals=\'{{"code": "{data.get("code")}"}}\'>\
            Hide Code\
            </button>\
            <pre style="margin-top: 10px;">{code[data.get("code")]}</pre>'
            return display
        except:
            return "Display Error occured"
    else:
        return "Submission Error occured"


@app.route("/hide_code", methods=["POST"])
def hide_code():
    if request.method == "POST":
        try:
            data = request.form
            display = f'\
            <button\
            class="button primary"\
            hx-post="/show_code"\
            hx-target="#{data.get("code")}"\
            hx-swap="show:top"\
            hx-vals=\'{{"code": "{data.get("code")}"}}\'>\
            Show Code\
            </button>'
            return display
        except:
            return "Display Error occured"
    else:
        return "Submission Error occured"


# functions for showing more text
@app.route("/show_text", methods=["GET"])
def show_text():
    if request.method == "GET":
        try:
            display = f'\
            {code.get("About")}\
            <button\
            class="button"\
            style="padding: 0 15px"\
            hx-get="/hide_text"\
            hx-target="#more_about"\
            >\
            Hide\
            </button>'
            return display
        except:
            return "Display Error occured"
    else:
        return "Submission Error occured"


@app.route("/hide_text", methods=["GET"])
def hide_text():
    if request.method == "GET":
        try:
            display = f'\
            <button\
            class="button"\
            style="padding: 0 15px"\
            hx-get="/show_text"\
            hx-target="#more_about"\
            >\
            Show More\
            </button>'
            return display
        except:
            return "Display Error occured"
    else:
        return "Submission Error occured"
