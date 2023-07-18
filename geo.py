import requests
from config import GEO_TOKEN
def g(lo, la):
    headers = {"Accept-Language": "ru"}
    return requests.get(f"https://eu1.locationiq.com/v1/reverse.php?key={GEO_TOKEN}&lat={la}&lon={lo}&format=json", 
                        headers=headers).json()