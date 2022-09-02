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


class NegativeCacheAttributes(object):
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
        'time_to_live': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'time_to_live': 'timeToLive'
    }

    def __init__(self, enabled=None, time_to_live=None, _configuration=None):  # noqa: E501
        """NegativeCacheAttributes - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enabled = None
        self._time_to_live = None
        self.discriminator = None

        self.enabled = enabled
        self.time_to_live = time_to_live

    @property
    def enabled(self):
        """Gets the enabled of this NegativeCacheAttributes.  # noqa: E501

        Whether to cache responses for content not present in the proxied repository  # noqa: E501

        :return: The enabled of this NegativeCacheAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NegativeCacheAttributes.

        Whether to cache responses for content not present in the proxied repository  # noqa: E501

        :param enabled: The enabled of this NegativeCacheAttributes.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def time_to_live(self):
        """Gets the time_to_live of this NegativeCacheAttributes.  # noqa: E501

        How long to cache the fact that a file was not found in the repository (in minutes)  # noqa: E501

        :return: The time_to_live of this NegativeCacheAttributes.  # noqa: E501
        :rtype: int
        """
        return self._time_to_live

    @time_to_live.setter
    def time_to_live(self, time_to_live):
        """Sets the time_to_live of this NegativeCacheAttributes.

        How long to cache the fact that a file was not found in the repository (in minutes)  # noqa: E501

        :param time_to_live: The time_to_live of this NegativeCacheAttributes.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and time_to_live is None:
            raise ValueError("Invalid value for `time_to_live`, must not be `None`")  # noqa: E501

        self._time_to_live = time_to_live

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
        if issubclass(NegativeCacheAttributes, dict):
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
        if not isinstance(other, NegativeCacheAttributes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NegativeCacheAttributes):
            return True

        return self.to_dict() != other.to_dict()
