# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (the Fulfillment Policy, Payment Policy, and Return Policy), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.6.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FulfillmentPolicyResponse(object):
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
        'fulfillment_policies': 'list[FulfillmentPolicy]',
        'href': 'str',
        'limit': 'int',
        'next': 'str',
        'offset': 'int',
        'prev': 'str',
        'total': 'int'
    }

    attribute_map = {
        'fulfillment_policies': 'fulfillmentPolicies',
        'href': 'href',
        'limit': 'limit',
        'next': 'next',
        'offset': 'offset',
        'prev': 'prev',
        'total': 'total'
    }

    def __init__(self, fulfillment_policies=None, href=None, limit=None, next=None, offset=None, prev=None, total=None):  # noqa: E501
        """FulfillmentPolicyResponse - a model defined in Swagger"""  # noqa: E501
        self._fulfillment_policies = None
        self._href = None
        self._limit = None
        self._next = None
        self._offset = None
        self._prev = None
        self._total = None
        self.discriminator = None
        if fulfillment_policies is not None:
            self.fulfillment_policies = fulfillment_policies
        if href is not None:
            self.href = href
        if limit is not None:
            self.limit = limit
        if next is not None:
            self.next = next
        if offset is not None:
            self.offset = offset
        if prev is not None:
            self.prev = prev
        if total is not None:
            self.total = total

    @property
    def fulfillment_policies(self):
        """Gets the fulfillment_policies of this FulfillmentPolicyResponse.  # noqa: E501

        A list of the seller's fulfillment policies.  # noqa: E501

        :return: The fulfillment_policies of this FulfillmentPolicyResponse.  # noqa: E501
        :rtype: list[FulfillmentPolicy]
        """
        return self._fulfillment_policies

    @fulfillment_policies.setter
    def fulfillment_policies(self, fulfillment_policies):
        """Sets the fulfillment_policies of this FulfillmentPolicyResponse.

        A list of the seller's fulfillment policies.  # noqa: E501

        :param fulfillment_policies: The fulfillment_policies of this FulfillmentPolicyResponse.  # noqa: E501
        :type: list[FulfillmentPolicy]
        """

        self._fulfillment_policies = fulfillment_policies

    @property
    def href(self):
        """Gets the href of this FulfillmentPolicyResponse.  # noqa: E501

        The URI of the current page of results from the result set.  # noqa: E501

        :return: The href of this FulfillmentPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this FulfillmentPolicyResponse.

        The URI of the current page of results from the result set.  # noqa: E501

        :param href: The href of this FulfillmentPolicyResponse.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def limit(self):
        """Gets the limit of this FulfillmentPolicyResponse.  # noqa: E501

        The number of items returned on a single page from the result set.  # noqa: E501

        :return: The limit of this FulfillmentPolicyResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this FulfillmentPolicyResponse.

        The number of items returned on a single page from the result set.  # noqa: E501

        :param limit: The limit of this FulfillmentPolicyResponse.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this FulfillmentPolicyResponse.  # noqa: E501

        The URI for the following page of results. This value is returned only if there is an additional page of results to display from the result set. Max length: 2048  # noqa: E501

        :return: The next of this FulfillmentPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this FulfillmentPolicyResponse.

        The URI for the following page of results. This value is returned only if there is an additional page of results to display from the result set. Max length: 2048  # noqa: E501

        :param next: The next of this FulfillmentPolicyResponse.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def offset(self):
        """Gets the offset of this FulfillmentPolicyResponse.  # noqa: E501

        The number of results skipped in the result set before listing the first returned result. Note: The items in a paginated result set use a zero-based list where the first item in the list has an offset of 0.  # noqa: E501

        :return: The offset of this FulfillmentPolicyResponse.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this FulfillmentPolicyResponse.

        The number of results skipped in the result set before listing the first returned result. Note: The items in a paginated result set use a zero-based list where the first item in the list has an offset of 0.  # noqa: E501

        :param offset: The offset of this FulfillmentPolicyResponse.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def prev(self):
        """Gets the prev of this FulfillmentPolicyResponse.  # noqa: E501

        The URI for the preceding page of results. This value is returned only if there is a previous page of results to display from the result set. Max length: 2048  # noqa: E501

        :return: The prev of this FulfillmentPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this FulfillmentPolicyResponse.

        The URI for the preceding page of results. This value is returned only if there is a previous page of results to display from the result set. Max length: 2048  # noqa: E501

        :param prev: The prev of this FulfillmentPolicyResponse.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def total(self):
        """Gets the total of this FulfillmentPolicyResponse.  # noqa: E501

        The total number of items retrieved in the result set. If no items are found, this field is returned with a value of 0.  # noqa: E501

        :return: The total of this FulfillmentPolicyResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this FulfillmentPolicyResponse.

        The total number of items retrieved in the result set. If no items are found, this field is returned with a value of 0.  # noqa: E501

        :param total: The total of this FulfillmentPolicyResponse.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(FulfillmentPolicyResponse, dict):
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
        if not isinstance(other, FulfillmentPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
