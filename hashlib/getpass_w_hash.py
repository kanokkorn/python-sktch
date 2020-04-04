import hashlib
import getpass

# username
user_list = ['alpaca', 'badger', 'capybara']

# somepassword
hash_val = '3c6fd36b1d006a1c4037ccca3d17793abfa764130007e14635a61f64'

def login():
  user = str(input('username:')) 
  while user not in user_list:
    user = str(input('No username found. try again\nusername:')) 
  for i in range(1, 5):
    pwd = getpass.getpass('password:')
    if hashlib.sha224(pwd.encode('ascii')).hexdigest() == hash_val and i <= 3:
      print('Login successful\nWelcome {}!'.format(user))
      break
    elif i <= 3:
      print('[{}] wrong password'.format(i))
    else:
      print('3 attemped, terminated')

if __name__ == "__main__":
  login()