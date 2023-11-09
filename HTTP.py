import requests

def Get(URL):
    """
    Sends an HTTP GET request to the specified URL and returns the response content as a string.

    Args:
        URL (str): The URL to send the GET request to.

    Returns:
        str: The response content as a string, or an empty string if an error occurs during decoding.
    """
    response = requests.get(URL) 

    response_string = "" 
    try:
        response_string = response.content.decode() 
    except Exception as e:
        print("Error in decoding response:", e)
    return response_string 
