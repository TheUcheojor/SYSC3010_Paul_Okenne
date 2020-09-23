import requests

def read_data_thingspeak():
    URL='https://api.thingspeak.com/channels/1153154/fields/1.json?api_key='
    KEY='8P5NU6Y7O4Z1OSOC'
    HEADER='&result=2'

    NEW_URL=URL+KEY+HEADER

    get_data=requests.get(NEW_URL).json()
    # print("get_data: "+ str(get_data) )

    channel_id=get_data['channel']['id']

    feeds=get_data['feeds']

    fields=[]
    for feed in feeds:
        fields.append(feed['field1'])
    # print("field1: "+ str(field1) )

    print(fields)


read_data_thingspeak()

   