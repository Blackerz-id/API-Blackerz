from flask import Flask
from flask_restful import Api

from src.searchbot import resouce
from src.allbot import resource2
from src.submitbot import resource3

app = Flask(__name__)
api = Api(app)

api.add_resource(resouce, "/api/v1/bots/<int:id>")
api.add_resource(resource2, "/api/v1/bots/all")
api.add_resource(resource3, "/api/v1/bots/submit/<int:id>")

if __name__ == "__main__":
  app.run()
