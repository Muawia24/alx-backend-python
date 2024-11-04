#!/usr/bin/env python3
"""
 Parameterize and patch as decorators
"""


import unittest
from parameterized import parameterized
from utils import get_json
from client import GithubOrgClient
from unittest import mock
from unittest.mock import patch
import requests


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests client.GithubOrgClient
    """
    @parameterized.expand([
        ("google",{'login': "google"}),
        ("abc",{'login': "abc"})
        ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """
        Tests client.GithubOrgClient.org
        """
        mock_get_json.return_value = {'login': org_name}
        client = GithubOrgClient(org_name)

        result = client.org

        mock_get_json.assert_called_once_with(client.ORG_URL.format(org=org_name))
        self.assertEqual(result, expected)
