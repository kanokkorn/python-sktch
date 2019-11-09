import json

def main():
  agent_id_1 = {
    'agent_1': {
      'name': 'yukimori ai',
      'trait': 'supportive'
    }
  }
  json_write(agent_id_1)

def json_write(data):
  with open('data.json', 'w') as write:
    json.dump(data, write)

if __name__ == '__main__':
  main()
