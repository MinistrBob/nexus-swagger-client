# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.29.2-02
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.components_api import ComponentsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestComponentsApi(unittest.TestCase):
    """ComponentsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.components_api.ComponentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_component(self):
        """Test case for delete_component

        Delete a single component  # noqa: E501
        """
        pass

    def test_get_component_by_id(self):
        """Test case for get_component_by_id

        Get a single component  # noqa: E501
        """
        pass

    def test_get_components(self):
        """Test case for get_components

        List components  # noqa: E501
        """
        pass

    def test_upload_component(self):
        """Test case for upload_component

        Upload a single component  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
