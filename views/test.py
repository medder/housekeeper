# -*- coding: utf-8 -*-

from flask_restful import Resource


class Test_V(Resource):
    '''
        test restful api
    '''
    def get(self, token):
        if token != 'p0o9i8u7y6':
            return 'You have not rights.'

        return 'Hello, This is a beautiful world.'
