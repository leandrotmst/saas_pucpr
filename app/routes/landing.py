from flask import Flask, render_template
import os


template_dir = os.path.abspath('app/templates')
app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def hello_world():
    return render_template('landing.html')
    

app.run(debug=True)