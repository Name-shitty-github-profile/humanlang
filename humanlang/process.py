from .data import data
def process_conv(conv: str, *, debug = False) -> list:
  e: list = []
  if debug is False: advice: bool = False
  for i in conv.replace("?", '').replace("!", '').replace(',', '').replace('.', '').lower().split('\n'):
    da = process_line(i)
    if type(da) is dict:
      if debug is False:
        if advice is False:
          da = "Invalid learning data | enable debug for traceback"
        else:
          da = "I had an error while processing your thing with my data"
      else:
        da = f"Invalid learning data\nData : {da}"
    e.append(da)
  return e

def check(l: str, dat: dict) -> bool:
  try:
    dat[l]
    return True
  except:
    return False

def process_line(line: str):
  dat = None
  for word in line.split(' '):
    if dat is None:
      if word not in data:
        return f"I'm sorry, I don't know, what you are saying by saying {line}.\nWord : {word}\nDat : {str(dat)}"
      else:
        dat = data[word]
    else:
      if check(word, dat) is False:
        if check('$$$set', dat) is True:
          return process_set(dat)
        return f"I'm sorry, I don't know, what you are saying by saying {line}.\nWord : {word}\nDat : {str(dat)}"
      dat = dat[word]
      if type(dat) is str:
        return dat
  if type(dat) is dict:
    return process_set(dat)
  return dat

def process_set(dat: dict):
  set: str = dat['$$$set']
  if set == '$$$func':
    return dat['$$$func'](dat['$$$argument'])
  return set
