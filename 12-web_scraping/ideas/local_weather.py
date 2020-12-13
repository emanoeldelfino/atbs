import webbrowser
import geocoder

g = geocoder.ip('me')

lat, lng = g.latlng

webbrowser.open(f'https://www.accuweather.com/en/search-locations?query={lat}, {lng}')

