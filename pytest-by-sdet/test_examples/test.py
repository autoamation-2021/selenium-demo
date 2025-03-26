# from utilities.customLogger import LogGen


# logger = LogGen.loggen()

# logger.info("Test log entry - INFO level")
# logger.debug("Test log entry - DEBUG level")
# logger.warning("Test log entry - WARNING level")

import json

with open(r"C:\Users\SreekarS\Downloads\pet_store.json",'r') as file:
    data = json.load(file)

geojson = {
    "type": "FeatureCollection",
    "features": []
}

for place in data["results"]:
    feature = {
        "type": "Feature",
        "properties":{"name":place["name"]},
        "geometry":{
            "type":"Point",
            "coordinates": [place["geometry"]["location"]["lng"], place["geometry"]["location"]["lat"]]
        }
        }
    geojson["features"].append(feature)

# Save as GeoJSON file
with open("output.geojson", "w") as geojson_file:
    json.dump(geojson, geojson_file, indent=2)

print("GeoJSON file created: output.geojson")