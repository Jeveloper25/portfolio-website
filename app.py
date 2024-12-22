import re
import json
from flask import Flask, render_template, url_for, request, redirect, jsonify
from static.project_files.password_security import Password
from static.project_files.display_code import code
import csv
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/<string:page_name>', methods=['POST', 'GET'])
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
     with open('./database.txt', 'a') as db:
            db.write(f"[\nEmail:\n{data['email']}\nName:\n{data['name']}\nMessage:\n{data['message']}\n]\n")

def write_to_csv(data):
     with open('./database.csv', 'a', newline='') as db:
            email = data['email']
            name = data['name']
            message = data['message']
            csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, name, message])

@app.route('/contact_form', methods=['POST', 'GET'])
def contact_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'Database Error occured'
    else:
        return 'Request Error occured'

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form['name']
            if len(data) > 0:
                pswd = Password()
                pswd.config(data)
                strength = pswd.get_password_strength()
                display = f"""<h3>Password Strength: {strength}</h3>"""
                return display
            else:
                 return"""<h3>Password Strength: N/A</h3>"""
        except:
            keys = request.form
            return keys
    else:
        return 'Submission Error occured'

@app.route('/show_code', methods=['POST'])
def show_code():
    if request.method == 'POST':
        try:
            data = request.get_json()
            display = code[data.get('code')]
            return """ It worked!"""
        except:
            return 'Display Error occured'
    else:
        return 'Submission Error occured'

               

# @app.route('/update', methods=['POST'])
# def update():
#     new_data = request.form.get('data')
#     return jsonify({'status': 'success'})


if __name__ == "__main__":
     app.run(debug=True)
    