emotion: str = 'I don\'t have feelings, I cannot feel good or feel bad'

hru: dict = {
  "are": {
     "you": {
      "$$$set": emotion,
      'today': emotion
    }
  }
}

data: dict = {
  "$$$set": "hi",
  'how': hru
}

hello: dict = {
  "hi": data,
  "hello": data,
  'yo': data,
  'how': hru
}
