import os
import joblib
from src.constants import LOCATION_PATH

if __name__ == "__main__":
    print("Generating Geolocations")
    geonames = joblib.load("/tmp/local_geocode/geonames.pkl")

    places_in_switzerland = []
    for place in geonames:
        if place[1] == "CH":
            places_in_switzerland.append(place)

    swiss_places = {entry[0]: tuple(entry[1:]) for entry in places_in_switzerland}
    global_places = {entry[0]: tuple(entry[1:]) for entry in geonames}

    # Save
    joblib.dump(swiss_places, os.path.join(LOCATION_PATH, "swiss_places.pkl"))
    joblib.dump(global_places, os.path.join(LOCATION_PATH, "global_places.pkl"))
    print("Completed!")
