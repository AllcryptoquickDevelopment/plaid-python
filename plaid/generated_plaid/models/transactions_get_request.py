# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.0.11
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class TransactionsGetRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'client_id': 'str',
        'options': 'TransactionsGetRequestOptions',
        'access_token': 'str',
        'secret': 'str',
        'start_date': 'str',
        'end_date': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'options': 'options',
        'access_token': 'access_token',
        'secret': 'secret',
        'start_date': 'start_date',
        'end_date': 'end_date'
    }

    def __init__(self, client_id=None, options=None, access_token=None, secret=None, start_date=None, end_date=None, local_vars_configuration=None):  # noqa: E501
        """TransactionsGetRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._options = None
        self._access_token = None
        self._secret = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        self.client_id = client_id
        if options is not None:
            self.options = options
        self.access_token = access_token
        self.secret = secret
        self.start_date = start_date
        self.end_date = end_date

    @property
    def client_id(self):
        """Gets the client_id of this TransactionsGetRequest.  # noqa: E501

        Your Plaid API `client_id`.  # noqa: E501

        :return: The client_id of this TransactionsGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this TransactionsGetRequest.

        Your Plaid API `client_id`.  # noqa: E501

        :param client_id: The client_id of this TransactionsGetRequest.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def options(self):
        """Gets the options of this TransactionsGetRequest.  # noqa: E501


        :return: The options of this TransactionsGetRequest.  # noqa: E501
        :rtype: TransactionsGetRequestOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this TransactionsGetRequest.


        :param options: The options of this TransactionsGetRequest.  # noqa: E501
        :type options: TransactionsGetRequestOptions
        """

        self._options = options

    @property
    def access_token(self):
        """Gets the access_token of this TransactionsGetRequest.  # noqa: E501

        The access token associated with the Item data is being requested for  # noqa: E501

        :return: The access_token of this TransactionsGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this TransactionsGetRequest.

        The access token associated with the Item data is being requested for  # noqa: E501

        :param access_token: The access_token of this TransactionsGetRequest.  # noqa: E501
        :type access_token: str
        """
        if self.local_vars_configuration.client_side_validation and access_token is None:  # noqa: E501
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def secret(self):
        """Gets the secret of this TransactionsGetRequest.  # noqa: E501

        Your Plaid API secret  # noqa: E501

        :return: The secret of this TransactionsGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this TransactionsGetRequest.

        Your Plaid API secret  # noqa: E501

        :param secret: The secret of this TransactionsGetRequest.  # noqa: E501
        :type secret: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def start_date(self):
        """Gets the start_date of this TransactionsGetRequest.  # noqa: E501

        The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD.  # noqa: E501

        :return: The start_date of this TransactionsGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TransactionsGetRequest.

        The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD.  # noqa: E501

        :param start_date: The start_date of this TransactionsGetRequest.  # noqa: E501
        :type start_date: str
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this TransactionsGetRequest.  # noqa: E501

        The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD.  # noqa: E501

        :return: The end_date of this TransactionsGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TransactionsGetRequest.

        The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD.  # noqa: E501

        :param end_date: The end_date of this TransactionsGetRequest.  # noqa: E501
        :type end_date: str
        """
        if self.local_vars_configuration.client_side_validation and end_date is None:  # noqa: E501
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransactionsGetRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionsGetRequest):
            return True

        return self.to_dict() != other.to_dict()
