from pymongo import MongoClient
from bson.objectid import ObjectId
import util

class MongoModel:
  def __init__(self, db_name, username, uri=util.enum['MONGO_URI']):
    self.client = MongoClient(uri)
    self.db = self.client[db_name]
    self.tasks = self.db["tasks"]
    self.username = username
    self.todo = list(self.get_task_by_status("todo"))
    self.in_progress = list(self.get_task_by_status("inProgress"))



  def find_tasks_by_user(self):
    user = self.db["users"].find_one({"username":self.username})
    task_ids = user["tasks"]
    tasks = []
    for task_id in task_ids:
      task = self.tasks.find_one({"_id":ObjectId(task_id)},{"title": 1,"description": 1, "taskStatus": 1})
      tasks.append(task)
    return tasks

  def get_task_by_status(self, status):
    return self.tasks.find({"taskStatus": status},{'title': 1, 'description':1, 'taskStatus':1, 'updatedAt':1})
  


  

# Example usage:
# model = MongoModel('test_db', 'test_collection')
# model.insert_one({'name': 'John', 'age': 30})
# print(model.find_one({'name': 'John'}))
