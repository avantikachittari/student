# Refactored: Use CRUD naming (read, create) in InfoModel
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')

api = Api(app)

# --- Model class for InfoDb with CRUD naming ---
class InfoModel:
    def __init__(self):
        self.data = [
            {
                "FirstName": "John",
                "LastName": "Mortensen",
                "DOB": "October 21",
                "Residence": "San Diego",
                "Email": "jmortensen@powayusd.com",
                "Owns_Cars": ["2015-Fusion", "2011-Ranger", "2003-Excursion", "1997-F350", "1969-Cadillac", "2015-Kuboto-3301"]
            },
            {
                "FirstName": "Shane",
                "LastName": "Lopez",
                "DOB": "February 27",
                "Residence": "San Diego",
                "Email": "slopez@powayusd.com",
                "Owns_Cars": ["2021-Insight"]
            }
        ]

    def read(self):
        return self.data

    def create(self, entry):
        self.data.append(entry)

# Instantiate the model
info_model = InfoModel()

# --- API Resource ---
class DataAPI(Resource):
    def get(self):
        return jsonify(info_model.read())

    def post(self):
        # Add a new entry to InfoDb
        entry = request.get_json()
        if not entry:
            return {"error": "No data provided"}, 400
        info_model.create(entry)
        return {"message": "Entry added successfully", "entry": entry}, 201

api.add_resource(DataAPI, '/api/data')

# Wee can use @app.route for HTML endpoints, this will be style for Admin UI
@app.route('/')
def say_hello():
    html_content = """
    <html>
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h2>Hello, World!</h2>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(port=5001)