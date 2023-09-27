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


class ChangedFile(object):
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
        'additions': 'int',
        'changes': 'int',
        'contents_url': 'str',
        'deletions': 'int',
        'filename': 'str',
        'html_url': 'str',
        'previous_filename': 'str',
        'raw_url': 'str',
        'status': 'str'
    }

    attribute_map = {
        'additions': 'additions',
        'changes': 'changes',
        'contents_url': 'contents_url',
        'deletions': 'deletions',
        'filename': 'filename',
        'html_url': 'html_url',
        'previous_filename': 'previous_filename',
        'raw_url': 'raw_url',
        'status': 'status'
    }

    def __init__(self, additions=None, changes=None, contents_url=None, deletions=None, filename=None, html_url=None, previous_filename=None, raw_url=None, status=None, _configuration=None):  # noqa: E501
        """ChangedFile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._additions = None
        self._changes = None
        self._contents_url = None
        self._deletions = None
        self._filename = None
        self._html_url = None
        self._previous_filename = None
        self._raw_url = None
        self._status = None
        self.discriminator = None

        if additions is not None:
            self.additions = additions
        if changes is not None:
            self.changes = changes
        if contents_url is not None:
            self.contents_url = contents_url
        if deletions is not None:
            self.deletions = deletions
        if filename is not None:
            self.filename = filename
        if html_url is not None:
            self.html_url = html_url
        if previous_filename is not None:
            self.previous_filename = previous_filename
        if raw_url is not None:
            self.raw_url = raw_url
        if status is not None:
            self.status = status

    @property
    def additions(self):
        """Gets the additions of this ChangedFile.  # noqa: E501


        :return: The additions of this ChangedFile.  # noqa: E501
        :rtype: int
        """
        return self._additions

    @additions.setter
    def additions(self, additions):
        """Sets the additions of this ChangedFile.


        :param additions: The additions of this ChangedFile.  # noqa: E501
        :type: int
        """

        self._additions = additions

    @property
    def changes(self):
        """Gets the changes of this ChangedFile.  # noqa: E501


        :return: The changes of this ChangedFile.  # noqa: E501
        :rtype: int
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this ChangedFile.


        :param changes: The changes of this ChangedFile.  # noqa: E501
        :type: int
        """

        self._changes = changes

    @property
    def contents_url(self):
        """Gets the contents_url of this ChangedFile.  # noqa: E501


        :return: The contents_url of this ChangedFile.  # noqa: E501
        :rtype: str
        """
        return self._contents_url

    @contents_url.setter
    def contents_url(self, contents_url):
        """Sets the contents_url of this ChangedFile.


        :param contents_url: The contents_url of this ChangedFile.  # noqa: E501
        :type: str
        """

        self._contents_url = contents_url

    @property
    def deletions(self):
        """Gets the deletions of this ChangedFile.  # noqa: E501


        :return: The deletions of this ChangedFile.  # noqa: E501
        :rtype: int
        """
        return self._deletions

    @deletions.setter
    def deletions(self, deletions):
        """Sets the deletions of this ChangedFile.


        :param deletions: The deletions of this ChangedFile.  # noqa: E501
        :type: int
        """

        self._deletions = deletions

    @property
    def filename(self):
        """Gets the filename of this ChangedFile.  # noqa: E501


        :return: The filename of this ChangedFile.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this ChangedFile.


        :param filename: The filename of this ChangedFile.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def html_url(self):
        """Gets the html_url of this ChangedFile.  # noqa: E501


        :return: The html_url of this ChangedFile.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this ChangedFile.


        :param html_url: The html_url of this ChangedFile.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def previous_filename(self):
        """Gets the previous_filename of this ChangedFile.  # noqa: E501


        :return: The previous_filename of this ChangedFile.  # noqa: E501
        :rtype: str
        """
        return self._previous_filename

    @previous_filename.setter
    def previous_filename(self, previous_filename):
        """Sets the previous_filename of this ChangedFile.


        :param previous_filename: The previous_filename of this ChangedFile.  # noqa: E501
        :type: str
        """

        self._previous_filename = previous_filename

    @property
    def raw_url(self):
        """Gets the raw_url of this ChangedFile.  # noqa: E501


        :return: The raw_url of this ChangedFile.  # noqa: E501
        :rtype: str
        """
        return self._raw_url

    @raw_url.setter
    def raw_url(self, raw_url):
        """Sets the raw_url of this ChangedFile.


        :param raw_url: The raw_url of this ChangedFile.  # noqa: E501
        :type: str
        """

        self._raw_url = raw_url

    @property
    def status(self):
        """Gets the status of this ChangedFile.  # noqa: E501


        :return: The status of this ChangedFile.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ChangedFile.


        :param status: The status of this ChangedFile.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(ChangedFile, dict):
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
        if not isinstance(other, ChangedFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangedFile):
            return True

        return self.to_dict() != other.to_dict()
