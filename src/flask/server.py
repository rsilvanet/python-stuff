from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

values = []

class Values(Resource):

    def get(self):
        return values
    
    def post(self):
        values.append(request.json["value"])
        return values,201

api.add_resource(Values, "/api/values")

if __name__ == "__main__":
    app.run(port=9001)