import fire

def greeting(name="world"):
  return print("Hello " + name)

if __name__ == "__main__":
  fire.Fire(greeting)