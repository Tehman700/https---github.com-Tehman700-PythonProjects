from geopy.geocoders import OpenCage

def get_location_by_ip(ip):
    geolocator = OpenCage(api_key='72434a3a55aa46278e0529a3e6497dd0')
    location = geolocator.geocode(ip)
    return location

ip = "192.168.1.3"  # Replace with the actual IP address
location = get_location_by_ip(ip)

if location:
    print(f"Location: {location.address}")
    print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
else:
    print("Location not found")
