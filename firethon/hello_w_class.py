import fire

# python hello_w_class.py hello username
class greeting(object):
  def hello(self, name):
    return print(f'Hello from python-fire {name}!')
  
  def random_quote(self, num):
    self.quote_list = [
      'Two things are infinite: the universe and human stupidity; and Im not sure about the universe',
      'Ever tried. Ever failed. No matter. Try Again. Fail again. Fail better.',
      'Always do whatever is next.'
    ]
    return print(self.quote_list[num])

if __name__ == "__main__":
  fire.Fire(greeting)