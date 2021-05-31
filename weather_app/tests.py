from django.test import TestCase, RequestFactory
from . import views

import json


class WeatherViewTestCase(TestCase):

    def test_success_response(self):
        post_data = {'city': 'Delhi', 'country': 'In'}
        req = RequestFactory().get('weather/', post_data)
        resp = views.WeatherDetail.as_view()(req, *[], **{})
        resp_data = json.loads(resp.content.decode())
        expected_resp = {
            'geo_coordinates': '[77.2167, 28.6667]',
            'location_name': 'Delhi, IN',
        }
        self.assertEqual(resp_data.get('location_name'), expected_resp.get('location_name'))
        self.assertEqual(resp_data.get('geo_coordinates'), expected_resp.get('geo_coordinates'))

    def test_failure_response(self):
        post_data = {'city': 'test', 'country': 'test'}
        req = RequestFactory().get('weather/', post_data)
        resp = views.WeatherDetail.as_view()(req, *[], **{})
        resp_data = json.loads(resp.content.decode())
        expected_resp = {'cod': '404', 'message': 'city not found'}
        self.assertEqual(resp_data.get('message'), expected_resp.get('message'))
        self.assertEqual(resp_data.get('cod'), str(404))

