
{'frc': 'FRC4', 'currentSpeed': 5, 'freeFlowSpeed': 19, 
'currentTravelTime': 455, 'freeFlowTravelTime': 119, 'confidence': 0.97, 
'coordinates': {'coordinate': [{'latitude': 40.76318662561519, 
'longitude': -73.97803225828615}, {'latitude': 40.76307819934861, 
'longitude': -73.97777255819328}, {'latitude': 40.76243445763016, 
'longitude': -73.97623298971268}, {'latitude': 40.76217211653262, 
'longitude': -73.97560468273522}, {'latitude': 40.76186028731343, 
'longitude': -73.97485418331016}, {'latitude': 40.76183730132585, 
'longitude': -73.97479828391468}, {'latitude': 40.761791637117156, 
'longitude': -73.974692572878}, {'latitude': 40.761147670996316, 
'longitude': -73.97318635609318}, {'latitude': 40.760523501913, 
'longitude': -73.97171011866205}, {'latitude': 40.76047481980789, 
'longitude': -73.97159916585734}, {'latitude': 40.76042245345445, 
'longitude': -73.9714749278917}]}, '@version': 'traffic-service 2.0.011'}


import json

r = requests.get(url)
for i in r.json()['coordinates']['coordinate']:
    print(i['latitude'], i['longitude'])