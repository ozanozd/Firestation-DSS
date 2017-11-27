"""
This program sends queries to google and get the answers.
NOTE THAT : It just tests it , not writing answers to any document.
"""

#Work to be done: Find a way to handle the query quota.
#Write answers to the document(txt or excel?)
#x,y coordinates are not good for queries:(

import read_excel_trial as helper
import googlemaps
from datetime import datetime

#Define API_KEY as a constant
API_KEY = 'AIzaSyBGWTZbOAUijqF5J6SwhF-nYAEzxCljLgU'

gmaps = googlemaps.Client(key=API_KEY)


now = datetime.now()
directions_result = gmaps.distance_matrix('Kurtkoy',
                                     "Balibey Mahallesi",
                                     mode="driving",
                                    )

print(directions_result)
