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


class PullReview(object):
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
        'body': 'str',
        'comments_count': 'int',
        'commit_id': 'str',
        'dismissed': 'bool',
        'html_url': 'str',
        'id': 'int',
        'official': 'bool',
        'pull_request_url': 'str',
        'stale': 'bool',
        'state': 'ReviewStateType',
        'submitted_at': 'datetime',
        'team': 'Team',
        'updated_at': 'datetime',
        'user': 'User'
    }

    attribute_map = {
        'body': 'body',
        'comments_count': 'comments_count',
        'commit_id': 'commit_id',
        'dismissed': 'dismissed',
        'html_url': 'html_url',
        'id': 'id',
        'official': 'official',
        'pull_request_url': 'pull_request_url',
        'stale': 'stale',
        'state': 'state',
        'submitted_at': 'submitted_at',
        'team': 'team',
        'updated_at': 'updated_at',
        'user': 'user'
    }

    def __init__(self, body=None, comments_count=None, commit_id=None, dismissed=None, html_url=None, id=None, official=None, pull_request_url=None, stale=None, state=None, submitted_at=None, team=None, updated_at=None, user=None, _configuration=None):  # noqa: E501
        """PullReview - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body = None
        self._comments_count = None
        self._commit_id = None
        self._dismissed = None
        self._html_url = None
        self._id = None
        self._official = None
        self._pull_request_url = None
        self._stale = None
        self._state = None
        self._submitted_at = None
        self._team = None
        self._updated_at = None
        self._user = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if comments_count is not None:
            self.comments_count = comments_count
        if commit_id is not None:
            self.commit_id = commit_id
        if dismissed is not None:
            self.dismissed = dismissed
        if html_url is not None:
            self.html_url = html_url
        if id is not None:
            self.id = id
        if official is not None:
            self.official = official
        if pull_request_url is not None:
            self.pull_request_url = pull_request_url
        if stale is not None:
            self.stale = stale
        if state is not None:
            self.state = state
        if submitted_at is not None:
            self.submitted_at = submitted_at
        if team is not None:
            self.team = team
        if updated_at is not None:
            self.updated_at = updated_at
        if user is not None:
            self.user = user

    @property
    def body(self):
        """Gets the body of this PullReview.  # noqa: E501


        :return: The body of this PullReview.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this PullReview.


        :param body: The body of this PullReview.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def comments_count(self):
        """Gets the comments_count of this PullReview.  # noqa: E501


        :return: The comments_count of this PullReview.  # noqa: E501
        :rtype: int
        """
        return self._comments_count

    @comments_count.setter
    def comments_count(self, comments_count):
        """Sets the comments_count of this PullReview.


        :param comments_count: The comments_count of this PullReview.  # noqa: E501
        :type: int
        """

        self._comments_count = comments_count

    @property
    def commit_id(self):
        """Gets the commit_id of this PullReview.  # noqa: E501


        :return: The commit_id of this PullReview.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this PullReview.


        :param commit_id: The commit_id of this PullReview.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

    @property
    def dismissed(self):
        """Gets the dismissed of this PullReview.  # noqa: E501


        :return: The dismissed of this PullReview.  # noqa: E501
        :rtype: bool
        """
        return self._dismissed

    @dismissed.setter
    def dismissed(self, dismissed):
        """Sets the dismissed of this PullReview.


        :param dismissed: The dismissed of this PullReview.  # noqa: E501
        :type: bool
        """

        self._dismissed = dismissed

    @property
    def html_url(self):
        """Gets the html_url of this PullReview.  # noqa: E501


        :return: The html_url of this PullReview.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this PullReview.


        :param html_url: The html_url of this PullReview.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def id(self):
        """Gets the id of this PullReview.  # noqa: E501


        :return: The id of this PullReview.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PullReview.


        :param id: The id of this PullReview.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def official(self):
        """Gets the official of this PullReview.  # noqa: E501


        :return: The official of this PullReview.  # noqa: E501
        :rtype: bool
        """
        return self._official

    @official.setter
    def official(self, official):
        """Sets the official of this PullReview.


        :param official: The official of this PullReview.  # noqa: E501
        :type: bool
        """

        self._official = official

    @property
    def pull_request_url(self):
        """Gets the pull_request_url of this PullReview.  # noqa: E501


        :return: The pull_request_url of this PullReview.  # noqa: E501
        :rtype: str
        """
        return self._pull_request_url

    @pull_request_url.setter
    def pull_request_url(self, pull_request_url):
        """Sets the pull_request_url of this PullReview.


        :param pull_request_url: The pull_request_url of this PullReview.  # noqa: E501
        :type: str
        """

        self._pull_request_url = pull_request_url

    @property
    def stale(self):
        """Gets the stale of this PullReview.  # noqa: E501


        :return: The stale of this PullReview.  # noqa: E501
        :rtype: bool
        """
        return self._stale

    @stale.setter
    def stale(self, stale):
        """Sets the stale of this PullReview.


        :param stale: The stale of this PullReview.  # noqa: E501
        :type: bool
        """

        self._stale = stale

    @property
    def state(self):
        """Gets the state of this PullReview.  # noqa: E501


        :return: The state of this PullReview.  # noqa: E501
        :rtype: ReviewStateType
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PullReview.


        :param state: The state of this PullReview.  # noqa: E501
        :type: ReviewStateType
        """

        self._state = state

    @property
    def submitted_at(self):
        """Gets the submitted_at of this PullReview.  # noqa: E501


        :return: The submitted_at of this PullReview.  # noqa: E501
        :rtype: datetime
        """
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, submitted_at):
        """Sets the submitted_at of this PullReview.


        :param submitted_at: The submitted_at of this PullReview.  # noqa: E501
        :type: datetime
        """

        self._submitted_at = submitted_at

    @property
    def team(self):
        """Gets the team of this PullReview.  # noqa: E501


        :return: The team of this PullReview.  # noqa: E501
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this PullReview.


        :param team: The team of this PullReview.  # noqa: E501
        :type: Team
        """

        self._team = team

    @property
    def updated_at(self):
        """Gets the updated_at of this PullReview.  # noqa: E501


        :return: The updated_at of this PullReview.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PullReview.


        :param updated_at: The updated_at of this PullReview.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this PullReview.  # noqa: E501


        :return: The user of this PullReview.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PullReview.


        :param user: The user of this PullReview.  # noqa: E501
        :type: User
        """

        self._user = user

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
        if issubclass(PullReview, dict):
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
        if not isinstance(other, PullReview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PullReview):
            return True

        return self.to_dict() != other.to_dict()