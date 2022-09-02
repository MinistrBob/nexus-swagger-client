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


class ApiPrivilegeScriptRequest(object):
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
        'description': 'str',
        'actions': 'list[str]',
        'script_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'actions': 'actions',
        'script_name': 'scriptName'
    }

    def __init__(self, name=None, description=None, actions=None, script_name=None, _configuration=None):  # noqa: E501
        """ApiPrivilegeScriptRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._actions = None
        self._script_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if actions is not None:
            self.actions = actions
        if script_name is not None:
            self.script_name = script_name

    @property
    def name(self):
        """Gets the name of this ApiPrivilegeScriptRequest.  # noqa: E501

        The name of the privilege.  This value cannot be changed.  # noqa: E501

        :return: The name of this ApiPrivilegeScriptRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiPrivilegeScriptRequest.

        The name of the privilege.  This value cannot be changed.  # noqa: E501

        :param name: The name of this ApiPrivilegeScriptRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and not re.search(r'^[a-zA-Z0-9\\-]{1}[a-zA-Z0-9_\\-\\.]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z0-9\\-]{1}[a-zA-Z0-9_\\-\\.]*$/`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApiPrivilegeScriptRequest.  # noqa: E501


        :return: The description of this ApiPrivilegeScriptRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiPrivilegeScriptRequest.


        :param description: The description of this ApiPrivilegeScriptRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def actions(self):
        """Gets the actions of this ApiPrivilegeScriptRequest.  # noqa: E501

        A collection of actions to associate with the privilege, using BREAD syntax (browse,read,edit,add,delete,all) as well as 'run' for script privileges.  # noqa: E501

        :return: The actions of this ApiPrivilegeScriptRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ApiPrivilegeScriptRequest.

        A collection of actions to associate with the privilege, using BREAD syntax (browse,read,edit,add,delete,all) as well as 'run' for script privileges.  # noqa: E501

        :param actions: The actions of this ApiPrivilegeScriptRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["READ", "BROWSE", "EDIT", "ADD", "DELETE", "RUN", "ASSOCIATE", "DISASSOCIATE", "ALL"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(actions).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `actions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(actions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._actions = actions

    @property
    def script_name(self):
        """Gets the script_name of this ApiPrivilegeScriptRequest.  # noqa: E501

        The name of a script to give access to.  # noqa: E501

        :return: The script_name of this ApiPrivilegeScriptRequest.  # noqa: E501
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        """Sets the script_name of this ApiPrivilegeScriptRequest.

        The name of a script to give access to.  # noqa: E501

        :param script_name: The script_name of this ApiPrivilegeScriptRequest.  # noqa: E501
        :type: str
        """

        self._script_name = script_name

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
        if issubclass(ApiPrivilegeScriptRequest, dict):
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
        if not isinstance(other, ApiPrivilegeScriptRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiPrivilegeScriptRequest):
            return True

        return self.to_dict() != other.to_dict()
