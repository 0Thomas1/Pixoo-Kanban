import requests
import json
import os
import dotenv

dotenv.load_dotenv()
enum ={
  'PIXOO_IP' : os.getenv('PIXOO_IP'),
  'MONGO_URI' : os.getenv('MONGO_URL_'),
  'DB_NAME' : os.getenv('DB_NAME'),
  'USER_NAME' : os.getenv('USER_NAME')}

def request(url,body):
  response = requests.post(url, json.dumps(body))
  data = response.json()
  if data['error_code'] != 0:
    print(f"Error: {data['error_code']}")
    return None
  return data    

#parse date

