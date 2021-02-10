from flask import Flask
from flask_restx import Api, fields, Resource

app = Flask(__name__)

api = Api(app, version='1.0', title='RestX Example',
    description='RestX Example Description',
)


class TodoDAO(Resource):

    def get_data(self):
        return todo

ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details'),
    'task2': fields.String(required=True, description='The task details')
})

@ns.doc("bismillah content")
@ns.route('/', methods=['POST'])
def bismillah():
    return TodoDAO.get_data()


if __name__ == '__main__':
    app.run()