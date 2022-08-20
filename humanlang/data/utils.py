from json import loads
from .data import learn, data
def learn_json(file: str) -> None:
  with open(file, 'r') as f:
    learn(loads(f.read()))

def check_data(word: str):
  '''
  Check if a word is in the data
  '''
  try:
    data[word]
    return True
  except:
    return False

def get_data():
  '''
  A simple function to get the current data
  '''
  return data
