#!/usr/bin/env python3
"""
Parameterize a unit test
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest import mock
from unittest.mock import patch
import requests


class TestAccessNestedMap(unittest.TestCase):
    """
    Parameterize a unit test
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test that a KeyError is raised for provided inputs
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """ Mock HTTP calls """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])

    @patch('utils.requests.get')
    def test_get_json(self, url, expected, mock_get):
        """
        Tests that utils.get_json returns the expected result.
        """
        mock_get.return_value.json.return_value = expected
        result = get_json(url)

        self.assertEqual(result, expected)
        mock_get.assert_called_once_with(url)



if __name__ == '__main__':
    unittest.main()

