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


class AssetReportGetRequest(object):
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
        'secret': 'str',
        'asset_report_token': 'str',
        'include_insights': 'bool'
    }

    attribute_map = {
        'client_id': 'client_id',
        'secret': 'secret',
        'asset_report_token': 'asset_report_token',
        'include_insights': 'include_insights'
    }

    def __init__(self, client_id=None, secret=None, asset_report_token=None, include_insights=None, local_vars_configuration=None):  # noqa: E501
        """AssetReportGetRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._secret = None
        self._asset_report_token = None
        self._include_insights = None
        self.discriminator = None

        self.client_id = client_id
        self.secret = secret
        self.asset_report_token = asset_report_token
        if include_insights is not None:
            self.include_insights = include_insights

    @property
    def client_id(self):
        """Gets the client_id of this AssetReportGetRequest.  # noqa: E501

        Your Plaid API `client_id`.  # noqa: E501

        :return: The client_id of this AssetReportGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AssetReportGetRequest.

        Your Plaid API `client_id`.  # noqa: E501

        :param client_id: The client_id of this AssetReportGetRequest.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def secret(self):
        """Gets the secret of this AssetReportGetRequest.  # noqa: E501

        Your Plaid API `secret`.  # noqa: E501

        :return: The secret of this AssetReportGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this AssetReportGetRequest.

        Your Plaid API `secret`.  # noqa: E501

        :param secret: The secret of this AssetReportGetRequest.  # noqa: E501
        :type secret: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def asset_report_token(self):
        """Gets the asset_report_token of this AssetReportGetRequest.  # noqa: E501

        A token that can be provided to endpoints such as `/asset_report/get` or `/asset_report/pdf_get` to fetch or update an Asset Report.  # noqa: E501

        :return: The asset_report_token of this AssetReportGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_report_token

    @asset_report_token.setter
    def asset_report_token(self, asset_report_token):
        """Sets the asset_report_token of this AssetReportGetRequest.

        A token that can be provided to endpoints such as `/asset_report/get` or `/asset_report/pdf_get` to fetch or update an Asset Report.  # noqa: E501

        :param asset_report_token: The asset_report_token of this AssetReportGetRequest.  # noqa: E501
        :type asset_report_token: str
        """
        if self.local_vars_configuration.client_side_validation and asset_report_token is None:  # noqa: E501
            raise ValueError("Invalid value for `asset_report_token`, must not be `None`")  # noqa: E501

        self._asset_report_token = asset_report_token

    @property
    def include_insights(self):
        """Gets the include_insights of this AssetReportGetRequest.  # noqa: E501

        `true` if you would like to retrieve the Asset Report with Insights, `false` otherwise. This field defaults to `false` if omitted. [Contact Plaid Support](https://dashboard.plaid.com/support) to get access to this feature.  # noqa: E501

        :return: The include_insights of this AssetReportGetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_insights

    @include_insights.setter
    def include_insights(self, include_insights):
        """Sets the include_insights of this AssetReportGetRequest.

        `true` if you would like to retrieve the Asset Report with Insights, `false` otherwise. This field defaults to `false` if omitted. [Contact Plaid Support](https://dashboard.plaid.com/support) to get access to this feature.  # noqa: E501

        :param include_insights: The include_insights of this AssetReportGetRequest.  # noqa: E501
        :type include_insights: bool
        """

        self._include_insights = include_insights

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
        if not isinstance(other, AssetReportGetRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetReportGetRequest):
            return True

        return self.to_dict() != other.to_dict()
