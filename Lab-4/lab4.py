import requests


URL='https://api.thingspeak.com/update?api_key='
KEY='54CDA6FJF4RCJ92C'
EMAIL = '&field1=paulokenne@cmail.carleton.ca'
PROJECT_GROUP='&field2=L2-M-8'
MEMBER_ID='&field3=b'

NEW_URL=URL+KEY+EMAIL+PROJECT_GROUP+MEMBER_ID

# Update Channel 
get_data=requests.post(NEW_URL)

print("post response: "+ str(get_data) +"\n")
