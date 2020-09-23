import httplib
import urllib
import time

from sense_hat import SenseHat
from random import randint

'''
The code template was provided by Iotdesignpro:
https://iotdesignpro.com/projects/how-to-send-data-to-thingspeak-cloud-using-raspberry-pi

Paul Okenne
'''

sense=SenseHat()
sense.clear()

key = "DWWHHKJUSWXN71RK"  # Put your API Key here

def thermometer():
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C

        # temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        temp =sense.get_temperature()# Get Raspberry Pi CPU temp



        params = urllib.urlencode({'field1': temp, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(temp)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break


if __name__ == "__main__":
        while True:
                thermometer()
 