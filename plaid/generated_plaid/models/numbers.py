# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.0.10
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class Numbers(object):
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
        'account': 'str',
        'ach_routing': 'str',
        'ach_wire_routing': 'str',
        'eft_institution': 'str',
        'eft_branch': 'str',
        'international_bic': 'str',
        'international_iban': 'str',
        'bacs_sort_code': 'str'
    }

    attribute_map = {
        'account': 'account',
        'ach_routing': 'ach_routing',
        'ach_wire_routing': 'ach_wire_routing',
        'eft_institution': 'eft_institution',
        'eft_branch': 'eft_branch',
        'international_bic': 'international_bic',
        'international_iban': 'international_iban',
        'bacs_sort_code': 'bacs_sort_code'
    }

    def __init__(self, account=None, ach_routing=None, ach_wire_routing=None, eft_institution=None, eft_branch=None, international_bic=None, international_iban=None, bacs_sort_code=None, local_vars_configuration=None):  # noqa: E501
        """Numbers - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account = None
        self._ach_routing = None
        self._ach_wire_routing = None
        self._eft_institution = None
        self._eft_branch = None
        self._international_bic = None
        self._international_iban = None
        self._bacs_sort_code = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if ach_routing is not None:
            self.ach_routing = ach_routing
        if ach_wire_routing is not None:
            self.ach_wire_routing = ach_wire_routing
        if eft_institution is not None:
            self.eft_institution = eft_institution
        if eft_branch is not None:
            self.eft_branch = eft_branch
        if international_bic is not None:
            self.international_bic = international_bic
        if international_iban is not None:
            self.international_iban = international_iban
        if bacs_sort_code is not None:
            self.bacs_sort_code = bacs_sort_code

    @property
    def account(self):
        """Gets the account of this Numbers.  # noqa: E501

        Will be used for the account number.  # noqa: E501

        :return: The account of this Numbers.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Numbers.

        Will be used for the account number.  # noqa: E501

        :param account: The account of this Numbers.  # noqa: E501
        :type account: str
        """

        self._account = account

    @property
    def ach_routing(self):
        """Gets the ach_routing of this Numbers.  # noqa: E501

        Must be a valid ACH routing number.  # noqa: E501

        :return: The ach_routing of this Numbers.  # noqa: E501
        :rtype: str
        """
        return self._ach_routing

    @ach_routing.setter
    def ach_routing(self, ach_routing):
        """Sets the ach_routing of this Numbers.

        Must be a valid ACH routing number.  # noqa: E501

        :param ach_routing: The ach_routing of this Numbers.  # noqa: E501
        :type ach_routing: str
        """

        self._ach_routing = ach_routing

    @property
    def ach_wire_routing(self):
        """Gets the ach_wire_routing of this Numbers.  # noqa: E501

        Must be a valid wire transfer routing number.  # noqa: E501

        :return: The ach_wire_routing of this Numbers.  # noqa: E501
        :rtype: str
        """
        return self._ach_wire_routing

    @ach_wire_routing.setter
    def ach_wire_routing(self, ach_wire_routing):
        """Sets the ach_wire_routing of this Numbers.

        Must be a valid wire transfer routing number.  # noqa: E501

        :param ach_wire_routing: The ach_wire_routing of this Numbers.  # noqa: E501
        :type ach_wire_routing: str
        """

        self._ach_wire_routing = ach_wire_routing

    @property
    def eft_institution(self):
        """Gets the eft_institution of this Numbers.  # noqa: E501

        EFT institution number. Must be specified alongside `eft_branch`.  # noqa: E501

        :return: The eft_institution of this Numbers.  # noqa: E501
        :rtype: str
        """
        return self._eft_institution

    @eft_institution.setter
    def eft_institution(self, eft_institution):
        """Sets the eft_institution of this Numbers.

        EFT institution number. Must be specified alongside `eft_branch`.  # noqa: E501

        :param eft_institution: The eft_institution of this Numbers.  # noqa: E501
        :type eft_institution: str
        """

        self._eft_institution = eft_institution

    @property
    def eft_branch(self):
        """Gets the eft_branch of this Numbers.  # noqa: E501

        EFT branch number. Must be specified alongside `eft_institution`.  # noqa: E501

        :return: The eft_branch of this Numbers.  # noqa: E501
        :rtype: str
        """
        return self._eft_branch

    @eft_branch.setter
    def eft_branch(self, eft_branch):
        """Sets the eft_branch of this Numbers.

        EFT branch number. Must be specified alongside `eft_institution`.  # noqa: E501

        :param eft_branch: The eft_branch of this Numbers.  # noqa: E501
        :type eft_branch: str
        """

        self._eft_branch = eft_branch

    @property
    def international_bic(self):
        """Gets the international_bic of this Numbers.  # noqa: E501

        Bank identifier code (BIC). Must be specified alongside `international_iban`.  # noqa: E501

        :return: The international_bic of this Numbers.  # noqa: E501
        :rtype: str
        """
        return self._international_bic

    @international_bic.setter
    def international_bic(self, international_bic):
        """Sets the international_bic of this Numbers.

        Bank identifier code (BIC). Must be specified alongside `international_iban`.  # noqa: E501

        :param international_bic: The international_bic of this Numbers.  # noqa: E501
        :type international_bic: str
        """

        self._international_bic = international_bic

    @property
    def international_iban(self):
        """Gets the international_iban of this Numbers.  # noqa: E501

        International bank account number (IBAN). If no account number is specified via `account`, will also be used as the account number by default. Must be specified alongside `international_bic`.  # noqa: E501

        :return: The international_iban of this Numbers.  # noqa: E501
        :rtype: str
        """
        return self._international_iban

    @international_iban.setter
    def international_iban(self, international_iban):
        """Sets the international_iban of this Numbers.

        International bank account number (IBAN). If no account number is specified via `account`, will also be used as the account number by default. Must be specified alongside `international_bic`.  # noqa: E501

        :param international_iban: The international_iban of this Numbers.  # noqa: E501
        :type international_iban: str
        """

        self._international_iban = international_iban

    @property
    def bacs_sort_code(self):
        """Gets the bacs_sort_code of this Numbers.  # noqa: E501

        BACS sort code  # noqa: E501

        :return: The bacs_sort_code of this Numbers.  # noqa: E501
        :rtype: str
        """
        return self._bacs_sort_code

    @bacs_sort_code.setter
    def bacs_sort_code(self, bacs_sort_code):
        """Sets the bacs_sort_code of this Numbers.

        BACS sort code  # noqa: E501

        :param bacs_sort_code: The bacs_sort_code of this Numbers.  # noqa: E501
        :type bacs_sort_code: str
        """

        self._bacs_sort_code = bacs_sort_code

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
        if not isinstance(other, Numbers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Numbers):
            return True

        return self.to_dict() != other.to_dict()