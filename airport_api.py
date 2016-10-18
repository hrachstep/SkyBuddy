import requests
import json
import os
import sys
from pprint import pprint
#from nntplib import resp

#resp = requests.get('https://waittime-qa.api.aero/waittime/v1/current/DXB', data = {'X-apiKey', '8e2cff00ff9c6b3f448294736de5908a'})
#print resp.url

def getRequest(reqType):
    if reqType == "time":
        command = "rm -rf resp.json"
        os.system(command)
        command = "./request_time.sh"
        os.system(command)
        if os.path.isfile("resp.json"):
            with open('resp.json') as data_file:    
                data = json.load(data_file)
                if data['success']:
                    return data
                else:
                    print "Error with request"
                    return 0
        else:
            print "Error with request"
            return 0
    elif reqType == "weather":
        command = "rm -rf resp.json"
        os.system(command)
        command = "./request_weather.sh"
        os.system(command)
        if os.path.isfile("resp.json"):
            with open('resp.json') as data_file:    
                data = json.load(data_file)
                if data['success']:
                    pprint(data)
                    return data
                else:
                    print "Error with request"
                    return 0
        else:
            print "Error with request"
            return 0
    
    
    return 



def parseRequest(data, type):
    #json_input = '{"success":true,"current":[{"airportCode":"DXB","airportName":"DXB Airport","queueId":"555b3490ttt844155098f5906d518zzz","queueName":"DXB Airside North Security Checkpoint Mock Data","projectedWaitTime":3600,"projectedMinWaitMinutes":4,"projectedMaxWaitMinutes":8,"localTime":"2016-10-14T08:51:12.783Z","time":"2016-10-14T08:51:12.783Z"}]}'
    if type == "time":
        airport_name =  str(data['current'][0]['airportName'])
        queue_name = str(data['current'][0]['queueName'])
        min_wait = str(data['current'][0]['projectedMinWaitMinutes'])
        max_wait = str(data['current'][0]['projectedMaxWaitMinutes'])
        local_time = str(data['current'][0]['localTime'])
        
        queue_name = queue_name.split("Mock")[0]
        
        #constracting message
        #msg1 = "Ok, so local time in " + airport_name + " is " + local_time + "\n"
        a = max_wait
        if int(a) < 10:
            msg = "Don't worry :) queue in " + queue_name + " is bit quiet, maximum you should wait " + max_wait + " minutes, minimum " + min_wait + " minutes"
        else:
            msg = "Yea, currently there is a little queue in " + queue_name + ", maximum you should wait " + max_wait + " minutes, minimum " + min_wait + " minutes but please check later again :)"
        return msg
    elif type == "weather":
        feelT =  str(data['currentWeather']['feelsLikeTemperature'])
        state = str(data['currentWeather']['phrase'])
        humidity = str(data['currentWeather']['relativeHumidity'])
        windSpeed = str(data['currentWeather']['windSpeed'])
        windDir = str(data['currentWeather']['windDirection'])
    
        if int(feelT) > 30:
            msg = "It's pretty hot, in airport it feels like " + feelT + " and it's " + state + ",humidity is " + humidity + " % and there is a " + windDir + " wind with speed " + windSpeed
        else:
            msg = "It's OK, in airport it feels like " + feelT + " and it's " + state + ",humidity is " + humidity + " % and there is a " + windDir + " wind with speed " + windSpeed
       
        return msg
    
    
    else:
        return 0
