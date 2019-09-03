from settings import mongo_server, mongo_tasks
from datetime import datetime


class Task(object):
    def __init__(self):
        self.title = ""
        self.type = ""
        self.description = ""
        self.datetime = datetime.now()
        # self.duration = []

    def save(self):
        save = {
            "title": self.title,
            "type": self.type,
            "description": self.description,
            "datetime": self.datetime
        }

        if [i for i in mongo_tasks.find({"datetime": self.datetime})] is []:
            return mongo_tasks.insert(save)
        else:
            return mongo_tasks.update({"datetime": self.datetime}, {"$set": save})

    def delete(self):
        return mongo_tasks.delete_one({"datetime": self.datetime})
