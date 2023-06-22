import requests
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def geocode_address(address):
    geolocator = Nominatim(user_agent="mental_health_facility_geocoder")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    return None, None

def get_nearest_mental_health_facility(location):
    # Format the location query string for the Philippines
    query = f"{location}, Philippines"

    # Make a request to the Nominatim API
    response = requests.get(f"https://nominatim.openstreetmap.org/search?q={query}&format=json")

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        if data:
            # Get the latitude and longitude of the user's location
            user_latitude = float(data[0]['lat'])
            user_longitude = float(data[0]['lon'])

            # Read the mental health facility details from the Excel file
            facility_data = pd.read_excel('MH_PH_Facility_with_Coordinates.xlsx')

            # Calculate the distance to each mental health facility
            facility_data['DIST'] = facility_data.apply(lambda row: geodesic((user_latitude, user_longitude), (row['LAT'], row['LONG'])).kilometers, axis=1)

            if facility_data.empty:
                return None

            # Find the nearest mental health facility
            nearest_facility = facility_data.loc[facility_data['DIST'].idxmin()]

            # Return the nearest mental health facility information
            facility_info = {
                'name': nearest_facility['NAME OF HOSPITAL'],
                'address': nearest_facility['ADDRESS'],
                'contact': nearest_facility['CONTACT']
            }
            return facility_info

    # Return None if no mental health facility is found or there is an error
    return None

# Example usage
location_input = input("Enter your location: ")
nearest_facility = get_nearest_mental_health_facility(location_input)

if nearest_facility:
    print("Nearest Mental Health Facility:")
    print("Name:", nearest_facility['name'])
    print("Address:", nearest_facility['address'])
    print("Contact:", nearest_facility['contact'])
else:
    print("No mental health facility found for the specified location.")