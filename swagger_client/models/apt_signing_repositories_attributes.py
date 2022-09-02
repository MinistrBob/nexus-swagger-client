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


class AptSigningRepositoriesAttributes(object):
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
        'keypair': 'str',
        'passphrase': 'str'
    }

    attribute_map = {
        'keypair': 'keypair',
        'passphrase': 'passphrase'
    }

    def __init__(self, keypair=None, passphrase=None, _configuration=None):  # noqa: E501
        """AptSigningRepositoriesAttributes - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._keypair = None
        self._passphrase = None
        self.discriminator = None

        if keypair is not None:
            self.keypair = keypair
        if passphrase is not None:
            self.passphrase = passphrase

    @property
    def keypair(self):
        """Gets the keypair of this AptSigningRepositoriesAttributes.  # noqa: E501

        PGP signing key pair (armored private key e.g. gpg --export-secret-key --armor)  # noqa: E501

        :return: The keypair of this AptSigningRepositoriesAttributes.  # noqa: E501
        :rtype: str
        """
        return self._keypair

    @keypair.setter
    def keypair(self, keypair):
        """Sets the keypair of this AptSigningRepositoriesAttributes.

        PGP signing key pair (armored private key e.g. gpg --export-secret-key --armor)  # noqa: E501

        :param keypair: The keypair of this AptSigningRepositoriesAttributes.  # noqa: E501
        :type: str
        """

        self._keypair = keypair

    @property
    def passphrase(self):
        """Gets the passphrase of this AptSigningRepositoriesAttributes.  # noqa: E501

        Passphrase to access PGP signing key  # noqa: E501

        :return: The passphrase of this AptSigningRepositoriesAttributes.  # noqa: E501
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        """Sets the passphrase of this AptSigningRepositoriesAttributes.

        Passphrase to access PGP signing key  # noqa: E501

        :param passphrase: The passphrase of this AptSigningRepositoriesAttributes.  # noqa: E501
        :type: str
        """

        self._passphrase = passphrase

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
        if issubclass(AptSigningRepositoriesAttributes, dict):
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
        if not isinstance(other, AptSigningRepositoriesAttributes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AptSigningRepositoriesAttributes):
            return True

        return self.to_dict() != other.to_dict()
