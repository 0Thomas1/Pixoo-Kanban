import util
from mongoModel import MongoModel
from pixooDriver import PixooDriver 


# init_pixoo() function
def init_pixoo():
  pixoo = PixooDriver(util.enum['PIXOO_IP'])
  return pixoo

# init_model() function
def init_model(name):
  model = MongoModel('kanban', name)
  if model.client is None:
    print('Failed to connect to MongoDB')
    exit(1)
  return model

pixoo = init_pixoo()
mongo = init_model('USER_NAME')

def main():  
  while True:
    try:
      pixoo.draw_all_tasks(mongo.in_progress,"In Progress")
      pixoo.draw_all_tasks(mongo.todo,"To Do")

    except KeyboardInterrupt:
      print('[!] Exiting...')
      pixoo.revert_display()
      exit(0)

if __name__ == "__main__":
  main() 

  