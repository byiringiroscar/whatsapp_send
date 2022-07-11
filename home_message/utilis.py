import requests
from decouple import config

api_token = config('API_TOKEN')
whatsapp_group_id = config('WHATSAPP_ID')


def send_whatsapp_message(message):
    url = "https://api.ultramsg.com/instance11652/messages/chat"

    payload = f"token={api_token}&to={whatsapp_group_id}&body={message}&priority=1&referenceId="
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    return response.text
