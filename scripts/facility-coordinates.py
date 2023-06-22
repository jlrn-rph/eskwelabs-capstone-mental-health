import pandas as pd
from geopy.geocoders import Nominatim

def geocode_address(address):
    geolocator = Nominatim(user_agent="hospital_geocoder")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    return None, None

def add_coordinates_to_hospitals(input_file, output_file):
    # Read the hospital data from the Excel file
    hospital_data = pd.read_excel(input_file)

    # Geocode the addresses and add latitude and longitude columns
    hospital_data['LAT'], hospital_data['LONG'] = zip(*hospital_data['ADDRESS'].apply(geocode_address))

    # Save the updated data to a new Excel file
    hospital_data.to_excel(output_file, index=False)

# Example usage
input_file = 'MH_PH_Facility.xlsx'
output_file = 'MH_PH_Facility_with_Coordinates.xlsx'

add_coordinates_to_hospitals(input_file, output_file)
