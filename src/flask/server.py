from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Values(Resource):
    def get(self):
        return [ "value1", "value2" ]

api.add_resource(Values, "/api/values")

if __name__ == "__main__":
    app.run(port=9001)