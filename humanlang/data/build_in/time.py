from datetime import datetime
import pytz

def ti(place):
  city = place.split('/')[1]
  return f'The current time in {city} is {datetime.now(pytz.timezone(place)).strftime("%H:%M:%S")}'

time: dict = {
  "what": {
    'is': {
      "the": {
        "time": {
          'in': {
            "$$$set": "In what???",
            'london': {
              "$$$set": "func",
              "$$$func": ti,
              "$$$argument": "Europe/London"
            }
          }
        }
      }
    }
  }
}
