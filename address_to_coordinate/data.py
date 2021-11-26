import googlemaps
import pandas as pd
import json
from collections import OrderedDict

gmaps = googlemaps.Client(key="AIzaSyCm6kGkAftqRYTbdFLH7paHcnHJ31nwfXU")

garbage = pd.read_csv("쓰레기통_설치정보2.csv", thousands=',', index_col=0)
district_name = []
for name in garbage.index:
    district_name.append(name)

garbage_address, garbage_lat, garbage_lng = [],[],[]


i=0
for name in district_name:
    if i % 50 == 0: #진행상황 표시해주는 코드
        print(i)
    tmp = gmaps.geocode(name, language='ko')
    if len(tmp) != 0:
        garbage_address.append(tmp[0].get('formatted_address'))
        tmp_loc = tmp[0].get('geometry')
        garbage_lat.append(tmp_loc['location']['lat'])
        garbage_lng.append(tmp_loc['location']['lng'])
    i+=1

group_data = OrderedDict()

group_data['coordinates'] = []

for address, lat, lng in zip(garbage_address, garbage_lat, garbage_lng):
    group_data['coordinates'].append([lat, lng])
    print('위도: ' + str(lat) + ' 경도: ' + str(lng))


with open('test.json', 'w', encoding='utf-8') as make_file:
    json.dump(group_data, make_file, ensure_ascii=False, indent='\t')
