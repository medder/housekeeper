# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api

from housekeeper.views.test import Test_V

app = Flask(__name__)
api = Api()

api.add_resource(Test_V, '/api/test/')

api.init_app(app)
