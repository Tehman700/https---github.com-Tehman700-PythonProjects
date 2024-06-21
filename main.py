import phonenumbers
from myphone import number  # Ensure 'number' is defined correctly in 'myphone.py'
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Parse the phone number
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(f"Location: {location}")

# Get the carrier name
service = phonenumbers.parse(number)
carrier_name = carrier.name_for_number(service, "en")
print(f"Carrier: {carrier_name}")

# Geocode the location using OpenCage
key = '72434a3a55aa46278e0529a3e6497dd0'
geocoder = OpenCageGeocode(key)
query = 'Sargodha'
results = geocoder.geocode(query)

# Ensure results are valid
if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Latitude: {lat}, Longitude: {lng}")

    # Create a map
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)
    myMap.save("myyy.html")
else:
    print("Geocoding error: No results found")
