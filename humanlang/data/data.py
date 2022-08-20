data: dict = {"hello": {"world": "Your code is working !"}}

def learn(words: dict) -> None:
  """
  A normal dict that will merge into the data<br>
  Exemple
  ```python
  // conv
  hello world !
  // data
  {"hello" : {"world": "Your code is working !"}}
  //code
  from humanlang import learn, process_conv as pv
  learn({"hello" : {"world": "Your code is working !"}})
  conv = "hello world !"
  print("Human : " + conv)
  print("Bot : " + pv(conv))
  //console
  Human : hello world !
  Bot : Your code is working !
  ```
  """
  global data
  data = merge(data, words)
  return None

def merge(big_dict: dict, small_dict: dict) -> dict:
  for i in small_dict:
    if check(i, big_dict):
      e = big_dict[i]
      if type(e) is dict and type(small_dict[i]) is dict:
        big_dict[i] = merge(e, small_dict[i])
    else:
      big_dict[i] = small_dict[i]
  return big_dict

def check(l: str, dat: dict) -> bool:
  try:
    dat[l]
    return True
  except:
    return False
