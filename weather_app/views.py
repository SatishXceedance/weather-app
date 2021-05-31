from django.http import HttpResponse
from rest_framework.views import APIView
from . import utils
import json, requests



class WeatherDetail(APIView):
    """
        Weather Detail.
    """
    def get(self, request, format=None):
        """
            Get Weather Details
            Args:
                city (str): City Name
                country (str): Country Code
            Return:
                output (dict): Weather information
        """
        request_data = request.GET
        city = request_data.get('city', None)
        if city:
            country = request_data.get('country', None)
            third_party_url = 'http://api.openweathermap.org/data/2.5/weather?q='\
                              + city +','+ country +\
                              '&appid=1508a9a4840a5574c822d70ca2132032'
            response = utils.read_write_from_cache_file(third_party_url)
            if not response:
                response = json.loads(requests.get(third_party_url).content)
                if response.get('cod') == 200:
                    response = utils.prep_response(response)
                    utils.read_write_from_cache_file(third_party_url, response, read_operation=False)
        else:
            response = {'cod': '404', 'message': 'city not found'}
        required_res = json.dumps(response)
        return HttpResponse(required_res,
                            content_type='application/json')

