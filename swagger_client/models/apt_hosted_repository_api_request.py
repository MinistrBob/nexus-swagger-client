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


class AptHostedRepositoryApiRequest(object):
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
        'name': 'str',
        'online': 'bool',
        'storage': 'HostedStorageAttributes',
        'cleanup': 'CleanupPolicyAttributes',
        'apt': 'AptHostedRepositoriesAttributes',
        'apt_signing': 'AptSigningRepositoriesAttributes'
    }

    attribute_map = {
        'name': 'name',
        'online': 'online',
        'storage': 'storage',
        'cleanup': 'cleanup',
        'apt': 'apt',
        'apt_signing': 'aptSigning'
    }

    def __init__(self, name=None, online=None, storage=None, cleanup=None, apt=None, apt_signing=None, _configuration=None):  # noqa: E501
        """AptHostedRepositoryApiRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._online = None
        self._storage = None
        self._cleanup = None
        self._apt = None
        self._apt_signing = None
        self.discriminator = None

        self.name = name
        self.online = online
        self.storage = storage
        if cleanup is not None:
            self.cleanup = cleanup
        self.apt = apt
        self.apt_signing = apt_signing

    @property
    def name(self):
        """Gets the name of this AptHostedRepositoryApiRequest.  # noqa: E501

        A unique identifier for this repository  # noqa: E501

        :return: The name of this AptHostedRepositoryApiRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AptHostedRepositoryApiRequest.

        A unique identifier for this repository  # noqa: E501

        :param name: The name of this AptHostedRepositoryApiRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and not re.search(r'^[a-zA-Z0-9\\-]{1}[a-zA-Z0-9_\\-\\.]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z0-9\\-]{1}[a-zA-Z0-9_\\-\\.]*$/`")  # noqa: E501

        self._name = name

    @property
    def online(self):
        """Gets the online of this AptHostedRepositoryApiRequest.  # noqa: E501

        Whether this repository accepts incoming requests  # noqa: E501

        :return: The online of this AptHostedRepositoryApiRequest.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this AptHostedRepositoryApiRequest.

        Whether this repository accepts incoming requests  # noqa: E501

        :param online: The online of this AptHostedRepositoryApiRequest.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and online is None:
            raise ValueError("Invalid value for `online`, must not be `None`")  # noqa: E501

        self._online = online

    @property
    def storage(self):
        """Gets the storage of this AptHostedRepositoryApiRequest.  # noqa: E501


        :return: The storage of this AptHostedRepositoryApiRequest.  # noqa: E501
        :rtype: HostedStorageAttributes
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this AptHostedRepositoryApiRequest.


        :param storage: The storage of this AptHostedRepositoryApiRequest.  # noqa: E501
        :type: HostedStorageAttributes
        """
        if self._configuration.client_side_validation and storage is None:
            raise ValueError("Invalid value for `storage`, must not be `None`")  # noqa: E501

        self._storage = storage

    @property
    def cleanup(self):
        """Gets the cleanup of this AptHostedRepositoryApiRequest.  # noqa: E501


        :return: The cleanup of this AptHostedRepositoryApiRequest.  # noqa: E501
        :rtype: CleanupPolicyAttributes
        """
        return self._cleanup

    @cleanup.setter
    def cleanup(self, cleanup):
        """Sets the cleanup of this AptHostedRepositoryApiRequest.


        :param cleanup: The cleanup of this AptHostedRepositoryApiRequest.  # noqa: E501
        :type: CleanupPolicyAttributes
        """

        self._cleanup = cleanup

    @property
    def apt(self):
        """Gets the apt of this AptHostedRepositoryApiRequest.  # noqa: E501


        :return: The apt of this AptHostedRepositoryApiRequest.  # noqa: E501
        :rtype: AptHostedRepositoriesAttributes
        """
        return self._apt

    @apt.setter
    def apt(self, apt):
        """Sets the apt of this AptHostedRepositoryApiRequest.


        :param apt: The apt of this AptHostedRepositoryApiRequest.  # noqa: E501
        :type: AptHostedRepositoriesAttributes
        """
        if self._configuration.client_side_validation and apt is None:
            raise ValueError("Invalid value for `apt`, must not be `None`")  # noqa: E501

        self._apt = apt

    @property
    def apt_signing(self):
        """Gets the apt_signing of this AptHostedRepositoryApiRequest.  # noqa: E501


        :return: The apt_signing of this AptHostedRepositoryApiRequest.  # noqa: E501
        :rtype: AptSigningRepositoriesAttributes
        """
        return self._apt_signing

    @apt_signing.setter
    def apt_signing(self, apt_signing):
        """Sets the apt_signing of this AptHostedRepositoryApiRequest.


        :param apt_signing: The apt_signing of this AptHostedRepositoryApiRequest.  # noqa: E501
        :type: AptSigningRepositoriesAttributes
        """
        if self._configuration.client_side_validation and apt_signing is None:
            raise ValueError("Invalid value for `apt_signing`, must not be `None`")  # noqa: E501

        self._apt_signing = apt_signing

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
        if issubclass(AptHostedRepositoryApiRequest, dict):
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
        if not isinstance(other, AptHostedRepositoryApiRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AptHostedRepositoryApiRequest):
            return True

        return self.to_dict() != other.to_dict()