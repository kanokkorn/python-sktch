import json

def getdata():
  user = str(input('username:'))
  data = str(input('data:'))
  payload = {'username':user, 'data':data}
  return payload

def json_write(data):
  with open('data.json', 'w') as write:
    json.dump(data, write)

if __name__ == '__main__':
  print(getdata())