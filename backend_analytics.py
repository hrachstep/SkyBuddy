import re
import airport_api
import twitter_api

def parse_message(msg):
    type = 0
    if re.search("\s*Hello\s*", msg, re.IGNORECASE):
        type = 1
    elif re.search("\s*Hi\s*", msg, re.IGNORECASE):
        type = 1
    elif re.search("\s*airport\s*", msg, re.IGNORECASE):
        if re.search("\s*dubai\s*", msg, re.IGNORECASE):
            type = 21
        else:
            type = 20
    elif re.search("\s*time\s*", msg, re.IGNORECASE):
        type = 31
    elif re.search("\s*weather\s*", msg, re.IGNORECASE):
        type = 41
    elif re.search("\s*traffic\s*", msg, re.IGNORECASE):
        type = 51
    elif re.search("thank", msg, re.IGNORECASE):
        type = 91
    elif re.search("flight", msg, re.IGNORECASE):
        type = 61
    
    else:
        type = 0
    
    return type

def send_message(type):
    msg = ""
    if type == 1:
        msg = "Hello Buddy hope you doing well :) I m here to help you before your flight\nSo which airport we are going today?"
    elif type == 20:
        msg = "Sorry Buddy but I currently do not support this airport, see you soon bye!"
    elif type == 21:
        msg = "Have a nice trip to Dubai Internatinal Airport, What is your concern just simply type, I can help you with following: \nMy flight\ntime\nweather\ntraffic"
    elif type == 31:
        data = airport_api.getRequest("time")
        msg = airport_api.parseRequest(data, "time")
        msg1 = "\nThank you for talking with me :) if you want anything else simply type"
        msg = msg + msg1
    elif type == 41:
        data = airport_api.getRequest("weather")
        msg = airport_api.parseRequest(data, "weather")
        msg1 = "\nThank you for talking with me :) if you want anything else simply type"
        msg = msg + msg1
    elif type == 51:
        msg = twitter_api.get_tweets("dubai traffic jam @waze")
        msg1 = "\nThank you for talking with me :) if you want anything else simply type"
        msg = msg + msg1
    elif type == 91:
        msg = "See you soon Buddy, bye!"
    elif type == 61:
        msg = "Sorry Buddy but I currently do not support flight info :( but I'm learning now that skills!"
    
    else:
        msg = "Wait wait, I am not so smart I coudn't understand you but I am learning ;)"
    
    return msg