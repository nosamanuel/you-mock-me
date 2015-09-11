"""
mock an external web request
"""
from unittest import TestCase

from shims import mock

from example.thing import get_that_thing, get_that_json


class ExcerciseTests(TestCase):
    @mock.patch('example.thing.requests')
    def test_1_thing(self, mock_requests):
        # BEGIN
        # END

        self.assertEqual(get_that_thing(), 'xyzzy')
        self.assertTrue(mock_requests.get.called)

    @mock.patch('example.thing.requests')
    def test_json_response(self, mock_requests):
        # BEGIN
        # END

        self.assertEqual(get_that_json(), 'xyzzy')
