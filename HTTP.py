import http.client

def Get(URL):
    connection = http.client.HTTPSConnection(URL)
    connection.request("GET", "/")
    response = connection.getresponse()
    
    response_string = ""
    try:
        response_string = response.read().decode()
    except Exception as e:
        print("Error in decoding response:", e)
    
    return response_string

# print(Get("www.example.com"))