import random, vk, os
def getCToken():
    return os.environ.get("confirm_token")

def getToken():
    return os.environ.get("api_token")

api = vk.API(access_token=getToken(), v='5.110')


def send_message(peer_id, message, attachment=""):
    api.messages.send(access_token=getToken(), 
            peer_id=str(peer_id), message=message, attachment=attachment, random_id=random.getrandbits(64))


def process_command(data):
    send_message(data["peer_id"], "Hello")