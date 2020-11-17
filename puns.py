import requests

def get_portmanteaus(word):
    params = { 'function': 'getPortmanteaus', 'word': word }
    api_response = requests.get("http://rhymebrain.com/talk", params)

    return api_response.json()