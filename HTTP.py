import requests


def Get(URL):
    response = requests.get(URL)
    response_string = ""
    try:
        response_string = response.content.decode()
    except Exception as e:
        print("Error in decoding response:", e)
    return response_string
