# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.19.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Package(object):
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
        'created_at': 'datetime',
        'creator': 'User',
        'id': 'int',
        'name': 'str',
        'owner': 'User',
        'repository': 'Repository',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'creator': 'creator',
        'id': 'id',
        'name': 'name',
        'owner': 'owner',
        'repository': 'repository',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, created_at=None, creator=None, id=None, name=None, owner=None, repository=None, type=None, version=None, _configuration=None):  # noqa: E501
        """Package - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at = None
        self._creator = None
        self._id = None
        self._name = None
        self._owner = None
        self._repository = None
        self._type = None
        self._version = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if creator is not None:
            self.creator = creator
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if repository is not None:
            self.repository = repository
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def created_at(self):
        """Gets the created_at of this Package.  # noqa: E501


        :return: The created_at of this Package.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Package.


        :param created_at: The created_at of this Package.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def creator(self):
        """Gets the creator of this Package.  # noqa: E501


        :return: The creator of this Package.  # noqa: E501
        :rtype: User
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Package.


        :param creator: The creator of this Package.  # noqa: E501
        :type: User
        """

        self._creator = creator

    @property
    def id(self):
        """Gets the id of this Package.  # noqa: E501


        :return: The id of this Package.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Package.


        :param id: The id of this Package.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Package.  # noqa: E501


        :return: The name of this Package.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Package.


        :param name: The name of this Package.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this Package.  # noqa: E501


        :return: The owner of this Package.  # noqa: E501
        :rtype: User
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Package.


        :param owner: The owner of this Package.  # noqa: E501
        :type: User
        """

        self._owner = owner

    @property
    def repository(self):
        """Gets the repository of this Package.  # noqa: E501


        :return: The repository of this Package.  # noqa: E501
        :rtype: Repository
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this Package.


        :param repository: The repository of this Package.  # noqa: E501
        :type: Repository
        """

        self._repository = repository

    @property
    def type(self):
        """Gets the type of this Package.  # noqa: E501


        :return: The type of this Package.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Package.


        :param type: The type of this Package.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this Package.  # noqa: E501


        :return: The version of this Package.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Package.


        :param version: The version of this Package.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(Package, dict):
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
        if not isinstance(other, Package):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Package):
            return True

        return self.to_dict() != other.to_dict()
