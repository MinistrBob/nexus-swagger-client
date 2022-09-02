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


class ConanProxyRepositoryApiRequest(object):
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
        'storage': 'StorageAttributes',
        'cleanup': 'CleanupPolicyAttributes',
        'proxy': 'ProxyAttributes',
        'negative_cache': 'NegativeCacheAttributes',
        'http_client': 'HttpClientAttributes',
        'routing_rule': 'str'
    }

    attribute_map = {
        'name': 'name',
        'online': 'online',
        'storage': 'storage',
        'cleanup': 'cleanup',
        'proxy': 'proxy',
        'negative_cache': 'negativeCache',
        'http_client': 'httpClient',
        'routing_rule': 'routingRule'
    }

    def __init__(self, name=None, online=None, storage=None, cleanup=None, proxy=None, negative_cache=None, http_client=None, routing_rule=None, _configuration=None):  # noqa: E501
        """ConanProxyRepositoryApiRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._online = None
        self._storage = None
        self._cleanup = None
        self._proxy = None
        self._negative_cache = None
        self._http_client = None
        self._routing_rule = None
        self.discriminator = None

        self.name = name
        self.online = online
        self.storage = storage
        if cleanup is not None:
            self.cleanup = cleanup
        self.proxy = proxy
        self.negative_cache = negative_cache
        self.http_client = http_client
        if routing_rule is not None:
            self.routing_rule = routing_rule

    @property
    def name(self):
        """Gets the name of this ConanProxyRepositoryApiRequest.  # noqa: E501

        A unique identifier for this repository  # noqa: E501

        :return: The name of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConanProxyRepositoryApiRequest.

        A unique identifier for this repository  # noqa: E501

        :param name: The name of this ConanProxyRepositoryApiRequest.  # noqa: E501
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
        """Gets the online of this ConanProxyRepositoryApiRequest.  # noqa: E501

        Whether this repository accepts incoming requests  # noqa: E501

        :return: The online of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this ConanProxyRepositoryApiRequest.

        Whether this repository accepts incoming requests  # noqa: E501

        :param online: The online of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and online is None:
            raise ValueError("Invalid value for `online`, must not be `None`")  # noqa: E501

        self._online = online

    @property
    def storage(self):
        """Gets the storage of this ConanProxyRepositoryApiRequest.  # noqa: E501


        :return: The storage of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :rtype: StorageAttributes
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this ConanProxyRepositoryApiRequest.


        :param storage: The storage of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :type: StorageAttributes
        """
        if self._configuration.client_side_validation and storage is None:
            raise ValueError("Invalid value for `storage`, must not be `None`")  # noqa: E501

        self._storage = storage

    @property
    def cleanup(self):
        """Gets the cleanup of this ConanProxyRepositoryApiRequest.  # noqa: E501


        :return: The cleanup of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :rtype: CleanupPolicyAttributes
        """
        return self._cleanup

    @cleanup.setter
    def cleanup(self, cleanup):
        """Sets the cleanup of this ConanProxyRepositoryApiRequest.


        :param cleanup: The cleanup of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :type: CleanupPolicyAttributes
        """

        self._cleanup = cleanup

    @property
    def proxy(self):
        """Gets the proxy of this ConanProxyRepositoryApiRequest.  # noqa: E501


        :return: The proxy of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :rtype: ProxyAttributes
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this ConanProxyRepositoryApiRequest.


        :param proxy: The proxy of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :type: ProxyAttributes
        """
        if self._configuration.client_side_validation and proxy is None:
            raise ValueError("Invalid value for `proxy`, must not be `None`")  # noqa: E501

        self._proxy = proxy

    @property
    def negative_cache(self):
        """Gets the negative_cache of this ConanProxyRepositoryApiRequest.  # noqa: E501


        :return: The negative_cache of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :rtype: NegativeCacheAttributes
        """
        return self._negative_cache

    @negative_cache.setter
    def negative_cache(self, negative_cache):
        """Sets the negative_cache of this ConanProxyRepositoryApiRequest.


        :param negative_cache: The negative_cache of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :type: NegativeCacheAttributes
        """
        if self._configuration.client_side_validation and negative_cache is None:
            raise ValueError("Invalid value for `negative_cache`, must not be `None`")  # noqa: E501

        self._negative_cache = negative_cache

    @property
    def http_client(self):
        """Gets the http_client of this ConanProxyRepositoryApiRequest.  # noqa: E501


        :return: The http_client of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :rtype: HttpClientAttributes
        """
        return self._http_client

    @http_client.setter
    def http_client(self, http_client):
        """Sets the http_client of this ConanProxyRepositoryApiRequest.


        :param http_client: The http_client of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :type: HttpClientAttributes
        """
        if self._configuration.client_side_validation and http_client is None:
            raise ValueError("Invalid value for `http_client`, must not be `None`")  # noqa: E501

        self._http_client = http_client

    @property
    def routing_rule(self):
        """Gets the routing_rule of this ConanProxyRepositoryApiRequest.  # noqa: E501


        :return: The routing_rule of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :rtype: str
        """
        return self._routing_rule

    @routing_rule.setter
    def routing_rule(self, routing_rule):
        """Sets the routing_rule of this ConanProxyRepositoryApiRequest.


        :param routing_rule: The routing_rule of this ConanProxyRepositoryApiRequest.  # noqa: E501
        :type: str
        """

        self._routing_rule = routing_rule

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
        if issubclass(ConanProxyRepositoryApiRequest, dict):
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
        if not isinstance(other, ConanProxyRepositoryApiRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConanProxyRepositoryApiRequest):
            return True

        return self.to_dict() != other.to_dict()
