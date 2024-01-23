import csv

from contextlib import contextmanager
from typing import List, Dict

@contextmanager
def open_file(filename: str):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

def get_filtered_properties(filename: str) -> List[Dict[str, str]]:
    properties = []

    with open_file(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            address = row['address']
            status = row['status']
            price = row['price']

            properties.append({'address': address, 'status': status, 'price': price})

    return properties
