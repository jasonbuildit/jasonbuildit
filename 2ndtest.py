from typing import List
import requests
from bs4 import BeautifulSoup

def extract_property_info(url: str) -> List[dict]:
    """
    Extracts property information from the given URL and returns a list of dictionaries.
    Each dictionary contains the property details such as address, city, state, zip, and price.
    """
    try:
        # make request to the URL
        response = requests.get(url)
        # parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # find all the property listings
        property_listings = soup.find_all('div', class_='property-listing')
        # extract the property information from each listing
        property_info = []
        for listing in property_listings:
            data = {}
            data['address'] = listing.find('div', class_='address').text.strip()
            data['city'] = listing.find('div', class_='city').text.strip()
            data['state'] = listing.find('div', class_='state').text.strip()
            data['zip'] = listing.find('div', class_='zip').text.strip()
            data['price'] = listing.find('div', class_='price').text.strip()
            property_info.append(data)
        return property_info
    except Exception as e:
        print(f"Error occurred: {e}")
        return []