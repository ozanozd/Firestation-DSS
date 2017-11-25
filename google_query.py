import read_excel_trial as helper
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDH9WsOXKjDag2DhN2-9qgmY1APp1Utq7A')


now = datetime.now()
directions_result = gmaps.directions("29.490301, 41.165179",
                                     "29.633649, 41.166101",
                                     mode="driving",
                                     avoid="ferries",
                                     departure_time=now
                                    )

print(directions_result[0]['legs'][0]['distance']['text'])
print(directions_result[0]['legs'][0]['duration']['text'])
