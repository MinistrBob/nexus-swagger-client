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


class BlobStoreQuotaResultXO(object):
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
        'is_violation': 'bool',
        'message': 'str',
        'blob_store_name': 'str'
    }

    attribute_map = {
        'is_violation': 'isViolation',
        'message': 'message',
        'blob_store_name': 'blobStoreName'
    }

    def __init__(self, is_violation=None, message=None, blob_store_name=None, _configuration=None):  # noqa: E501
        """BlobStoreQuotaResultXO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_violation = None
        self._message = None
        self._blob_store_name = None
        self.discriminator = None

        if is_violation is not None:
            self.is_violation = is_violation
        if message is not None:
            self.message = message
        if blob_store_name is not None:
            self.blob_store_name = blob_store_name

    @property
    def is_violation(self):
        """Gets the is_violation of this BlobStoreQuotaResultXO.  # noqa: E501


        :return: The is_violation of this BlobStoreQuotaResultXO.  # noqa: E501
        :rtype: bool
        """
        return self._is_violation

    @is_violation.setter
    def is_violation(self, is_violation):
        """Sets the is_violation of this BlobStoreQuotaResultXO.


        :param is_violation: The is_violation of this BlobStoreQuotaResultXO.  # noqa: E501
        :type: bool
        """

        self._is_violation = is_violation

    @property
    def message(self):
        """Gets the message of this BlobStoreQuotaResultXO.  # noqa: E501


        :return: The message of this BlobStoreQuotaResultXO.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BlobStoreQuotaResultXO.


        :param message: The message of this BlobStoreQuotaResultXO.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def blob_store_name(self):
        """Gets the blob_store_name of this BlobStoreQuotaResultXO.  # noqa: E501


        :return: The blob_store_name of this BlobStoreQuotaResultXO.  # noqa: E501
        :rtype: str
        """
        return self._blob_store_name

    @blob_store_name.setter
    def blob_store_name(self, blob_store_name):
        """Sets the blob_store_name of this BlobStoreQuotaResultXO.


        :param blob_store_name: The blob_store_name of this BlobStoreQuotaResultXO.  # noqa: E501
        :type: str
        """

        self._blob_store_name = blob_store_name

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
        if issubclass(BlobStoreQuotaResultXO, dict):
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
        if not isinstance(other, BlobStoreQuotaResultXO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlobStoreQuotaResultXO):
            return True

        return self.to_dict() != other.to_dict()
