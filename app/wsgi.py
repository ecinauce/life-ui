from flask import Flask, jsonify
from settings import mongo_tasks
app = Flask(__name__)


@app.route('/api/')
def hello_world():
    return 'Accessing API URL'


@app.route('/api/tasks')
def tasks():
    output = {"tasks": [i for i in mongo_tasks.find({})]}
    return jsonify(output)


@app.route('/api/tasks/save', methods=['POST'])
def task_save():
    input =