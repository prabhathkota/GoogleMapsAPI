
https://code.google.com/apis/console/

The Google Maps JavaScript API lets you embed Google Maps in your own web pages with JavaScript

django google maps ?
C:\Prabhath\All Softwares\Pyhton\Django Related\Django-1.5.2\django\contrib\gis\maps\google

API Types:
###########
Static Maps API
Places API
Web Services

Static Maps
#############
Ref:
https://developers.google.com/maps/documentation/staticmaps/

No JavaScript is required. 
All we needed to do was create a URL, and place it within an <img> tag. 
You can place a Google static map anywhere on your webpage where you can place an image.

e.g.,
http://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap
&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318
&markers=color:red%7Clabel:C%7C40.718217,-73.998284&sensor=false

Generate API Key:
The Static Maps API uses an API key to identify your application. API keys are managed through the Google APIs console. To create your key:

Visit the APIs console at https://code.google.com/apis/console and log in with your Google Account.
Click the Services link from the left-hand menu in the APIs Console, then activate the Static Maps API service.
Once the service has been activated, your API key is available from the API Access page, in the Simple API Access section. 
Static Maps API applications use the Key for browser apps.

e.g.,
http://maps.googleapis.com/maps/api/staticmap?center=guntur,NY&zoom=13&size=600x300&key=API_KEY
http://maps.googleapis.com/maps/api/staticmap?center=guntur&zoom=13&size=600x300&key=XXXXX

Python API for Google Maps
###########################

Directions API
Distance Matrix API
Elevation API
Geocoding API
Time Zone API

192.168.0.100

**** Not able to generate Server Key
**** If key is not working, remove key parameter ***************
Directions API: (use server key instead of browser key)
https://maps.googleapis.com/maps/api/directions/json?origin=guntur&destination=vijayawada&sensor=false&key=XXXXX
https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&sensor=false&key=API_KEY&avoid=highways&mode=bicycling

https://maps.googleapis.com/maps/api/directions/json?origin=Toledo&destination=Madrid&region=es&sensor=false&key=XXXXX

Elevation API
##############
https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536,-104.9847034&sensor=false&key=XXXXX


Geocoding API
#############
Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway, Mountain View, CA") into geographic coordinates (like latitude 37.423021 and longitude -122.083739), which you can use to place markers or position the map.

Reverse geocoding is the process of converting geographic coordinates into a human-readable address.


---------------------------------------------------------------------------------------------------------------------------------------