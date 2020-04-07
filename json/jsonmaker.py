import json

def main():
  json_write()

def json_write(data):
  with open('data.json', 'w') as write:
    json.dump(data, write)

if __name__ == '__main__':
  main()