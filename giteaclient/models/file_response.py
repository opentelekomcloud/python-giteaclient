# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.16.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FileResponse(object):
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
        'commit': 'FileCommitResponse',
        'content': 'ContentsResponse',
        'verification': 'PayloadCommitVerification'
    }

    attribute_map = {
        'commit': 'commit',
        'content': 'content',
        'verification': 'verification'
    }

    def __init__(self, commit=None, content=None, verification=None):  # noqa: E501
        """FileResponse - a model defined in Swagger"""  # noqa: E501
        self._commit = None
        self._content = None
        self._verification = None
        self.discriminator = None
        if commit is not None:
            self.commit = commit
        if content is not None:
            self.content = content
        if verification is not None:
            self.verification = verification

    @property
    def commit(self):
        """Gets the commit of this FileResponse.  # noqa: E501


        :return: The commit of this FileResponse.  # noqa: E501
        :rtype: FileCommitResponse
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this FileResponse.


        :param commit: The commit of this FileResponse.  # noqa: E501
        :type: FileCommitResponse
        """

        self._commit = commit

    @property
    def content(self):
        """Gets the content of this FileResponse.  # noqa: E501


        :return: The content of this FileResponse.  # noqa: E501
        :rtype: ContentsResponse
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this FileResponse.


        :param content: The content of this FileResponse.  # noqa: E501
        :type: ContentsResponse
        """

        self._content = content

    @property
    def verification(self):
        """Gets the verification of this FileResponse.  # noqa: E501


        :return: The verification of this FileResponse.  # noqa: E501
        :rtype: PayloadCommitVerification
        """
        return self._verification

    @verification.setter
    def verification(self, verification):
        """Sets the verification of this FileResponse.


        :param verification: The verification of this FileResponse.  # noqa: E501
        :type: PayloadCommitVerification
        """

        self._verification = verification

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
        if issubclass(FileResponse, dict):
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
        if not isinstance(other, FileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
