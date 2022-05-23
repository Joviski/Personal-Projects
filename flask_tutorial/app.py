from flask import Flask, render_template, url_for, request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from datetime import datetime

app = Flask(__name__)
api= Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db= SQLAlchemy(app)


class Todo(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    content= db.Column(db.String(200), nullable=False)
    date_created= db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def hello_world():  # put application's code here
    if request.method == 'POST':
        task_content= request.form['content']
        new_task= Todo(content= task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding the task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks= tasks)

@app.route("/delete/<int:id>/")
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting the task.'

@app.route("/update/<int:id>/", methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == "POST":
        task.content= request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating the task."
    else:
        return render_template('update.html', task=task)


class HelloWorld(Resource):
    def get(self):
        return {'data': 'Hello, World'}

class HelloName(Resource):
    def get(self,name):
        return {'data': f'Hello, {name}'}

api.add_resource(HelloWorld, "/helloworld")
api.add_resource(HelloName,"/helloworld/<string:name>")

#====================================================
task_post_args= reqparse.RequestParser()
task_post_args.add_argument('content',type=str, required=True, help="Task content is required")

resource_fields= {
    'id': fields.Integer,
    'content': fields.String,
    'date_created': fields.DateTime
}

class ToDos(Resource):
    @marshal_with(resource_fields)
    def get(self, todo_id):
        todos= Todo.query.filter_by(id=todo_id).first()
        if not todos:
            abort(404, message= "Couldn't find task")
        return todos


    @marshal_with(resource_fields)
    def put(self, todo_id):
        todos = Todo.query.filter_by(id=todo_id).first()
        args = task_post_args.parse_args()
        if not todos:
            abort(409, message="Task does not exist")
        if args['content']:
            todos.content = args['content']
        try:
            db.session.commit()
            return todos , 201
        except:
            return 'There was an issue adding the task'

    @marshal_with(resource_fields)
    def delete(self, todo_id):
        todos = Todo.query.filter_by(id=todo_id).first()
        if not todos:
            abort(404, message="Couldn't find task")
        db.session.delete(todos)

        return todos, 204

class ToDoList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        tasks= Todo.query.all()
        todos= {}

        return tasks

    @marshal_with(resource_fields)
    def post(self):
        args = task_post_args.parse_args()

        task_content = args['content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return new_task, 201
        except:
            return 'There was an issue adding the task'


api.add_resource(ToDos, '/todos/<int:todo_id>')
api.add_resource(ToDoList,'/todos')



if __name__ == '__main__':
    app.run(debug=True)


