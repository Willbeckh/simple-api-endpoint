from flask import Flask, render_template
import requests

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


# get json file
profiles_url = "https://raw.githubusercontent.com/HarunMbaabu/Flask-and-Docker-Application-Domo/main/students.json"

#api route
@app.route('/')
def get_current_data():
    api_response = requests.get(profiles_url)
    json_dict = api_response.json()
    # data = jsonify(json_dict)
    return render_template('index.html', students=json_dict)
