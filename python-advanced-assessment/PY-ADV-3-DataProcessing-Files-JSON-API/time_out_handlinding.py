import requests

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    print("Fetching user details...")
    response = requests.get(url, timeout=5)

    response.raise_for_status()

    data = response.json()

    print("Request successful!")
    print("Name:", data["name"])
    print("Email:", data["email"])
    print("City:", data["address"]["city"])

except requests.exceptions.Timeout:
    print("Error: The request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Failed to establish a network connection.")

except requests.exceptions.RequestException as error:
    print("API Request Error:", error)