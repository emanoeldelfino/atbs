import requests

# res is the Response object.
# requests.get is responsible for downloading the webpage given the URL argument.
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')

# res.raise_for_status()

# Invalid URL
# requests.exceptions.HTTPError: 404 Client Error: Not Found for url:
# https://inventwithpython.com/page_that_does_not_exist

# With no connection to the internet
# Failed to establish a new connection: [Errno -2] Name or service not known'))


# If a failed download isn't big deal for your program you can wrap it in a try except
# statement, so your program won't crash because of that.

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
