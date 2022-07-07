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

class Branch(object):
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
        'commit': 'PayloadCommit',
        'effective_branch_protection_name': 'str',
        'enable_status_check': 'bool',
        'name': 'str',
        'protected': 'bool',
        'required_approvals': 'int',
        'status_check_contexts': 'list[str]',
        'user_can_merge': 'bool',
        'user_can_push': 'bool'
    }

    attribute_map = {
        'commit': 'commit',
        'effective_branch_protection_name': 'effective_branch_protection_name',
        'enable_status_check': 'enable_status_check',
        'name': 'name',
        'protected': 'protected',
        'required_approvals': 'required_approvals',
        'status_check_contexts': 'status_check_contexts',
        'user_can_merge': 'user_can_merge',
        'user_can_push': 'user_can_push'
    }

    def __init__(self, commit=None, effective_branch_protection_name=None, enable_status_check=None, name=None, protected=None, required_approvals=None, status_check_contexts=None, user_can_merge=None, user_can_push=None):  # noqa: E501
        """Branch - a model defined in Swagger"""  # noqa: E501
        self._commit = None
        self._effective_branch_protection_name = None
        self._enable_status_check = None
        self._name = None
        self._protected = None
        self._required_approvals = None
        self._status_check_contexts = None
        self._user_can_merge = None
        self._user_can_push = None
        self.discriminator = None
        if commit is not None:
            self.commit = commit
        if effective_branch_protection_name is not None:
            self.effective_branch_protection_name = effective_branch_protection_name
        if enable_status_check is not None:
            self.enable_status_check = enable_status_check
        if name is not None:
            self.name = name
        if protected is not None:
            self.protected = protected
        if required_approvals is not None:
            self.required_approvals = required_approvals
        if status_check_contexts is not None:
            self.status_check_contexts = status_check_contexts
        if user_can_merge is not None:
            self.user_can_merge = user_can_merge
        if user_can_push is not None:
            self.user_can_push = user_can_push

    @property
    def commit(self):
        """Gets the commit of this Branch.  # noqa: E501


        :return: The commit of this Branch.  # noqa: E501
        :rtype: PayloadCommit
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this Branch.


        :param commit: The commit of this Branch.  # noqa: E501
        :type: PayloadCommit
        """

        self._commit = commit

    @property
    def effective_branch_protection_name(self):
        """Gets the effective_branch_protection_name of this Branch.  # noqa: E501


        :return: The effective_branch_protection_name of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._effective_branch_protection_name

    @effective_branch_protection_name.setter
    def effective_branch_protection_name(self, effective_branch_protection_name):
        """Sets the effective_branch_protection_name of this Branch.


        :param effective_branch_protection_name: The effective_branch_protection_name of this Branch.  # noqa: E501
        :type: str
        """

        self._effective_branch_protection_name = effective_branch_protection_name

    @property
    def enable_status_check(self):
        """Gets the enable_status_check of this Branch.  # noqa: E501


        :return: The enable_status_check of this Branch.  # noqa: E501
        :rtype: bool
        """
        return self._enable_status_check

    @enable_status_check.setter
    def enable_status_check(self, enable_status_check):
        """Sets the enable_status_check of this Branch.


        :param enable_status_check: The enable_status_check of this Branch.  # noqa: E501
        :type: bool
        """

        self._enable_status_check = enable_status_check

    @property
    def name(self):
        """Gets the name of this Branch.  # noqa: E501


        :return: The name of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Branch.


        :param name: The name of this Branch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def protected(self):
        """Gets the protected of this Branch.  # noqa: E501


        :return: The protected of this Branch.  # noqa: E501
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this Branch.


        :param protected: The protected of this Branch.  # noqa: E501
        :type: bool
        """

        self._protected = protected

    @property
    def required_approvals(self):
        """Gets the required_approvals of this Branch.  # noqa: E501


        :return: The required_approvals of this Branch.  # noqa: E501
        :rtype: int
        """
        return self._required_approvals

    @required_approvals.setter
    def required_approvals(self, required_approvals):
        """Sets the required_approvals of this Branch.


        :param required_approvals: The required_approvals of this Branch.  # noqa: E501
        :type: int
        """

        self._required_approvals = required_approvals

    @property
    def status_check_contexts(self):
        """Gets the status_check_contexts of this Branch.  # noqa: E501


        :return: The status_check_contexts of this Branch.  # noqa: E501
        :rtype: list[str]
        """
        return self._status_check_contexts

    @status_check_contexts.setter
    def status_check_contexts(self, status_check_contexts):
        """Sets the status_check_contexts of this Branch.


        :param status_check_contexts: The status_check_contexts of this Branch.  # noqa: E501
        :type: list[str]
        """

        self._status_check_contexts = status_check_contexts

    @property
    def user_can_merge(self):
        """Gets the user_can_merge of this Branch.  # noqa: E501


        :return: The user_can_merge of this Branch.  # noqa: E501
        :rtype: bool
        """
        return self._user_can_merge

    @user_can_merge.setter
    def user_can_merge(self, user_can_merge):
        """Sets the user_can_merge of this Branch.


        :param user_can_merge: The user_can_merge of this Branch.  # noqa: E501
        :type: bool
        """

        self._user_can_merge = user_can_merge

    @property
    def user_can_push(self):
        """Gets the user_can_push of this Branch.  # noqa: E501


        :return: The user_can_push of this Branch.  # noqa: E501
        :rtype: bool
        """
        return self._user_can_push

    @user_can_push.setter
    def user_can_push(self, user_can_push):
        """Sets the user_can_push of this Branch.


        :param user_can_push: The user_can_push of this Branch.  # noqa: E501
        :type: bool
        """

        self._user_can_push = user_can_push

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
        if issubclass(Branch, dict):
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
        if not isinstance(other, Branch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
