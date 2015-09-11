"""
mock.patch
"""
from unittest import TestCase

from shims import mock

from example.thing import Foo


class ExcerciseTests(TestCase):
    @mock.patch('example.thing.Foo.thing')
    def test_1_thing(self, mock_thing):
        obj = Foo()

        # BEGIN
        # END

        self.assertEqual(obj.thing(), 'xyzzy')
