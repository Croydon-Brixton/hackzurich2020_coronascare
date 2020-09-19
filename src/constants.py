"""File to save project-wide constants"""
import os

# PATHS
DATA_PATH = "/mnt/data"
CASES_PATH = os.path.join(DATA_PATH, "Bing-COVID-19-Data", "data")
TWITTER_PATH = os.path.join(DATA_PATH, "srf_data", "Twitter")
SMD_PATH = os.path.join(DATA_PATH, "srf_data", "SMD")
LOCATION_PATH = os.path.join(DATA_PATH, "location_data")

# API Keys
TWITTER_AUTH = {  # Keys for twitter API
    "API_KEY": "uhiTDzZBuv96kLZVVXFMkfCYh",
    "API_SECRET": "XepYPEH1mKSpv0QrWyvZt6a64dXCKelAo6cPVCTnONnpS641Oj",
    "BEARER_TOKEN": "AAAAAAAAAAAAAAAAAAAAAHhhHwEAAAAA0AHrU5ks3gu2cgiht5CqvFr3Sx8%3DB0orQFLuiclY4HWiHWPWCtYLXfXL71HGxAg9SiwyM92m5regRa",
    "ACCESS_TOKEN": "1255778628614475777-KG9ijrN1oO7R5treIJFr7X9GMQiAPH",
    "ACCESS_TOKEN_SECRET": "A6edZOelCakLWtDST0bf5JfADeNI1ONQe3Ke2rymuIy5a",
}
MS_TEXTANALYSIS = {"API_KEY": "e9d6bb4aaf3c41c3ba2fd90227c1d8bf"}
MAPBOX_TOKEN = "pk.eyJ1IjoidGlnZXJmbHlzdHVkaW8iLCJhIjoiY2tmOW94a3kzMG83ZTJybWFqc28ydDI1NyJ9.uoRh84Gv3y9J397hMz-BDw"
