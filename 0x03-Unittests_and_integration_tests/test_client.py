#!/usr/bin/env python3
"""
 Parameterize and patch as decorators
"""


import unittest
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from utils import get_json
from client import GithubOrgClient
from unittest import mock
from unittest.mock import patch, PropertyMock
import requests


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests client.GithubOrgClient
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"})
        ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """
        Tests client.GithubOrgClient.org
        """
        mock_get_json.return_value = {'login': org_name}
        client = GithubOrgClient(org_name)

        result = client.org

        mock_get_json.assert_called_once_with(
                client.ORG_URL.format(org=org_name))
        self.assertEqual(result, expected)

    def test_public_repos_url(self):
        """
        Mockes a readonly property with mock
        """
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock) as mock_public_repos_url:
            payload = {"repos_url": "Any_paylod"}
            mock_public_repos_url.return_value = payload
            test_class = GithubOrgClient('client_test')
            result = test_class._public_repos_url

            self.assertEqual(result, payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self,  mock_get_json):
        """
        To unit-test GithubOrgClient.public_repos.
        """
        payload = [{"name": "Linkedin"}, {"name": "ALX"}]
        mock_get_json.return_value = payload

        with patch(
                'client.GithubOrgClient._public_repos_url',
                ) as mock_public_repos:

            mock_public_repos.return_value = "url_example"

            client = GithubOrgClient('client_test')
            result = client.public_repos()
            expected = [repo["name"] for repo in payload]

            self.assertEqual(result, expected)

            mock_get_json.called_with_once()
            mock_public_repos.called_with_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, key, expected):
        """
        unit-test GithubOrgClient.has_license.
        """
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
     Integration test: fixtures
    """
    @classmethod
    def setUpClass(cls):
        """
        Setup class
        """
        config = {"return_value.json.side_effect": [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}

        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def tearDownClass(cls):
        """
        Run After test and stop patcher
        """
        cls.get_patcher.stop()
