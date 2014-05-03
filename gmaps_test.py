import simplejson, urllib

GEOCODE_BASE_URL = 'http://maps.google.com/maps/api/geocode/json'

def geocode(address="New+York,+NY",sensor="false", **geo_args):
    geo_args.update({
        'address': address,
        'sensor': sensor  
    })

    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args)
    print url
	#http://maps.google.com/maps/api/geocode/json?sensor=false&address=vijayawada
    result = simplejson.load(urllib.urlopen(url))
    print result   
    print simplejson.dumps([s['formatted_address'] for s in result['results']], indent=2)

if __name__ == '__main__':
    geocode(address="vijayawada",sensor="false")
