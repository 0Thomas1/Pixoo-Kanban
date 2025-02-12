import requests
import json
enum ={
  'PIXOO_IP' : '192.168.50.78'}#change to your pixoo ip

def request(url,body):
  response = requests.post(url, json.dumps(body))
  data = response.json()
  if data['error_code'] != 0:
    print(f"Error: {data['error_code']}")
    return None
  return data    


