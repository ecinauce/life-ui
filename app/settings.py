import pymongo

mongo_server = pymongo.MongoClient('localhost', 27017)
mongo_lifeui = mongo_server.lifeui
mongo_tasks = mongo_lifeui.tasks
