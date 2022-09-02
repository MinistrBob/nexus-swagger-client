# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.29.2-02
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class AnonymousAccessSettingsXO(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enabled': 'bool',
        'user_id': 'str',
        'realm_name': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'user_id': 'userId',
        'realm_name': 'realmName'
    }

    def __init__(self, enabled=None, user_id=None, realm_name=None, _configuration=None):  # noqa: E501
        """AnonymousAccessSettingsXO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enabled = None
        self._user_id = None
        self._realm_name = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if user_id is not None:
            self.user_id = user_id
        if realm_name is not None:
            self.realm_name = realm_name

    @property
    def enabled(self):
        """Gets the enabled of this AnonymousAccessSettingsXO.  # noqa: E501

        Whether or not Anonymous Access is enabled  # noqa: E501

        :return: The enabled of this AnonymousAccessSettingsXO.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AnonymousAccessSettingsXO.

        Whether or not Anonymous Access is enabled  # noqa: E501

        :param enabled: The enabled of this AnonymousAccessSettingsXO.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def user_id(self):
        """Gets the user_id of this AnonymousAccessSettingsXO.  # noqa: E501

        The username of the anonymous account  # noqa: E501

        :return: The user_id of this AnonymousAccessSettingsXO.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AnonymousAccessSettingsXO.

        The username of the anonymous account  # noqa: E501

        :param user_id: The user_id of this AnonymousAccessSettingsXO.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def realm_name(self):
        """Gets the realm_name of this AnonymousAccessSettingsXO.  # noqa: E501

        The name of the authentication realm for the anonymous account  # noqa: E501

        :return: The realm_name of this AnonymousAccessSettingsXO.  # noqa: E501
        :rtype: str
        """
        return self._realm_name

    @realm_name.setter
    def realm_name(self, realm_name):
        """Sets the realm_name of this AnonymousAccessSettingsXO.

        The name of the authentication realm for the anonymous account  # noqa: E501

        :param realm_name: The realm_name of this AnonymousAccessSettingsXO.  # noqa: E501
        :type: str
        """

        self._realm_name = realm_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AnonymousAccessSettingsXO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnonymousAccessSettingsXO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnonymousAccessSettingsXO):
            return True

        return self.to_dict() != other.to_dict()
