import urllib.request
from datetime import datetime, timezone
import json


class JSONData:
    def __init__(self, url='https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson'):
        self.json_data_src = url
        self.print_data_from_url()

    def print_data_from_url(self):
        response = (
            urllib.request.urlopen(self.json_data_src))
        print('result code:', str(response.getcode()))
        if(response.getcode() == 200):
            data = response.read()
            self.print_json_data(data)
        else:
            print('Error: cannot parse results')

    def print_json_data(self, data):
        json_data = json.loads(data)
        if 'title' in json_data['metadata']:
            print(json_data['metadata']['title'])
            print('Total number of earthquakes:',
                  json_data['metadata']['count'])

            for i in json_data['features']:
                print(i['properties']['place'])
                print('—————————————\n')


if(__name__ == '__main__'):
    JSONData()
