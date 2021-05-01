
import requests,json
def SERVER_MESSAGE(sender,message):
    url="http://99.79.146.226:5006/webhooks/rest/webhook"
    data = json.dumps({
        "sender": str(sender),
        "message":str(message)
    })
    data_received = requests.post(url, data=data,headers={"Content-Type":"application/json"})
    received_messages = json.dumps(" ".join([x['text'] for x in data_received.json()]))
    # print(received_messages) 
    return(received_messages)

if __name__ == "__main__":
    print(json.loads(SERVER_MESSAGE("123",str("I am a dealer"))))

 