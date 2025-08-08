from pymongo import MongoClient
from bson.objectid import ObjectId
import util

class MongoModel:
  def __init__(self, username, uri=util.enum['MONGO_URI'], db_name=util.enum['DB_NAME']):
    self.client = MongoClient(uri)
    self.db = self.client[db_name]
    self.tasks = self.db["tasks"]
    self.username = username
   



  def find_tasks_by_user(self):
    user = self.db["users"].find_one({"username":self.username})
    task_ids = user["tasks"]
    tasks = []
    for task_id in task_ids:
      task = self.tasks.find_one({"_id":ObjectId(task_id)},{"title": 1,"description": 1, "taskStatus": 1})
      tasks.append(task)
    return tasks

  def get_task_by_status(self, status):
    res = list(self.tasks.find({"taskStatus": status},{'title': 1, 'description':1, 'taskStatus':1, 'updatedAt':1}))
    #print(status, res)
    return res


  

# Example usage:
# model = MongoModel('test_db', 'test_collection')
# model.insert_one({'name': 'John', 'age': 30})
# print(model.find_one({'name': 'John'}))
