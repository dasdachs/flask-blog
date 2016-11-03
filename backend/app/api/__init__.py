from flask_restful import Api, Resource

api = Api(prefix='/api/v1')

class TodoItem(Resource):
    def get(self):
        return {'task': 'Say "Hello, World!"'}

api.add_resource(TodoItem, '/')
