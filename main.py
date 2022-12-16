import json
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

text = {

}


class Main(Resource):

    def post(self, text_id):
        parser = reqparse.RequestParser()
        parser.add_argument(type=str)
        text[text_id] = parser.parse_args()
        return text


api.add_resource(Main, "/api")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
