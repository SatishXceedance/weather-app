from datetime import datetime
import time
import json


def prep_response(api_response):
    required_response = {}
    required_response['location_name'] = api_response.get('name', '') + ', ' + \
                                         api_response.get('sys', {}).get('country', '')
    required_response['temperature'] = convert_kelvin_into_celsius(api_response.get('main', {}).get('temp', 273.15))
    required_response['wind'] = api_response.get('base', '') + ', ' +\
                                str(api_response.get('wind', {}).get('speed')) + ' m/s'
    required_response['cloudiness'] = api_response.get('clouds', {}).get('all')
    required_response['pressure'] =  str(api_response.get('main', {}).get('pressure')) + ' hpa'
    required_response['humidity'] = str(api_response.get('main', {}).get('humidity')) + ' %'
    sunrise_time = api_response.get('sys', {'sunrise': time.time()}).get('sunrise')
    sunset_time = api_response.get('sys', {'sunset': time.time()}).get('sunset')
    required_response['sunrise'] = datetime.fromtimestamp(sunrise_time).strftime('%H:%M')
    required_response['sunset'] = datetime.fromtimestamp(sunset_time).strftime('%H:%M')
    required_response['geo_coordinates'] = str(list(api_response.get('coord', {}).values()))
    now = datetime.now()
    required_response['requested_time'] = now.strftime("%Y-%m-%d %H:%M:%S")
    required_response['forecast'] = api_response.get('forecast', {})
    return required_response

def convert_kelvin_into_celsius(kelvin_tem):
    temp_in_c = kelvin_tem - 273.15
    return "{0:.2f}".format(temp_in_c) + '°C'

def read_write_from_cache_file(query_string, response_data=[], read_operation=True):
    with open("weather_app/api_response_cache.json", "r+") as file:
        try:
            data = json.load(file)
        except:
            data = {}
        if read_operation:
            cache_resp = data.get(query_string, False)
            if cache_resp:
                if is_cache_valid(cache_resp.get('requested_time')):
                    return cache_resp
            return None
        else:
            new_data = {query_string: response_data}
            data.update(new_data)
            file.seek(0)
            json.dump(data, file, indent=4)

def is_cache_valid(cache_time):
    try:
        cache_time = datetime.strptime(cache_time, '%Y-%m-%d %H:%M:%S')
        current_time = datetime.now()
        time_diff = current_time - cache_time
        minutes_diff = time_diff.total_seconds()/60
        return minutes_diff < 2
    except:
        return False