import datetime
from datetime import date
import requests
import time


# Some variables that will be used in making calls to the APIs
location_name = 'Houston, TX'
location_coords = { 'x': '29.7199', 'y': '-95.3422' }
request_params = { 'token': '##AccessToken##'}

def post(to_send):
    # Send the response to the group
        post_params = { 'bot_id' : '##BOT_ID##', 'text': to_send }
        requests.post('https://api.groupme.com/v3/bots/post', params = post_params)


def datediff(today):
    try:
      nextmonthdate = today.replace(month=today.month+1, day=1)
    except ValueError:
      if today.month == 12:
        nextmonthdate = today.replace(year=today.year+1, month=1, day=1)
      else:
        raise

    delta = nextmonthdate - today


    if delta.days == 2:
        post("2 days until rent is due.")
    elif delta.days == 1:
        post("1 days until rent is due.")
    elif today.day==1:
        post("RENT IS DUE TODAY.")
    else:
        return

if __name__ == "__main__":
    #today = date(2018, 7, 20)
    today = datetime.date.today()
    datediff(today)

