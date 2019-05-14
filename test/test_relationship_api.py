# coding: utf-8

"""
    SysML v2 API and Services

    REST/HTTP binding (PSM) for the SysML v2 standard API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import sysml_v2_api_client
from sysml_v2_api_client.api.relationship_api import RelationshipApi  # noqa: E501
from sysml_v2_api_client.rest import ApiException


class TestRelationshipApi(unittest.TestCase):
    """RelationshipApi unit test stubs"""

    def setUp(self):
        self.api = sysml_v2_api_client.api.relationship_api.RelationshipApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_relationship(self):
        """Test case for create_relationship

        Add a new relationship  # noqa: E501
        """
        pass

    def test_get_relationship(self):
        """Test case for get_relationship

        Get relationship by its ID  # noqa: E501
        """
        pass

    def test_get_relationships(self):
        """Test case for get_relationships

        Get all relationships  # noqa: E501
        """
        pass

    def test_get_relationships_by_element(self):
        """Test case for get_relationships_by_element

        Get all relationships with the given element as either source or target  # noqa: E501
        """
        pass

    def test_get_relationships_by_source(self):
        """Test case for get_relationships_by_source

        Get all relationships with the given element as the source  # noqa: E501
        """
        pass

    def test_get_relationships_by_target(self):
        """Test case for get_relationships_by_target

        Get all relationships with the given element as the target  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
