import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# Errors that might happen because there is no internet connection:
# Max retries exceeded
# Failed to establish a new connection

print(type(res))
print(res.status_code == requests.codes.ok)  # requests.codes.ok == 200
print(len(res.text))
print(res.text[:250])
