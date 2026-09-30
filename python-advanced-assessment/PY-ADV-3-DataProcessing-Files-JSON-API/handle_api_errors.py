import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=5)

    response.raise_for_status()

    data = response.json()

    print("Data received successfully:")
    print(data)

except requests.exceptions.Timeout:
    print("Error: API request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the API.")

except requests.exceptions.HTTPError as error:
    print("Error: API returned an error:", error)

except requests.exceptions.RequestException as error:
    print("Error:", error)