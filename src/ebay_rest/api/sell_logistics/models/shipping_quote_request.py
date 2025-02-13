# coding: utf-8

"""
    Logistics API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The <b>Logistics API</b> resources offer the following capabilities: <ul><li><b>shipping_quote</b> &ndash; Consolidates into a list a set of live shipping rates, or quotes, from which you can select a rate to ship a package.</li> <li><b>shipment</b> &ndash; Creates a \"shipment\" for the selected shipping rate.</li></ul> Call <b>createShippingQuote</b> to get a list of live shipping rates. The rates returned are all valid for a specific time window and all quoted prices are at eBay-negotiated rates. <br><br>Select one of the live rates and using its associated <b>rateId</b>, create a \"shipment\" for the package by calling <b>createFromShippingQuote</b>. Creating a shipment completes an agreement, and the cost of the base service and any added shipping options are summed into the returned <b>totalShippingCost</b> value. This action also generates a shipping label that you can use to ship the package.  The total cost of the shipment is incurred when the package is shipped using the supplied shipping label.  <p class=\"tablenote\"><b>Important!</b> Sellers must set up a payment method via their eBay account before they can use the methods in this API to create a shipment and the associated shipping label.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShippingQuoteRequest(object):
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
        'orders': 'list[Order]',
        'package_specification': 'PackageSpecification',
        'ship_from': 'Contact',
        'ship_to': 'Contact'
    }

    attribute_map = {
        'orders': 'orders',
        'package_specification': 'packageSpecification',
        'ship_from': 'shipFrom',
        'ship_to': 'shipTo'
    }

    def __init__(self, orders=None, package_specification=None, ship_from=None, ship_to=None):  # noqa: E501
        """ShippingQuoteRequest - a model defined in Swagger"""  # noqa: E501
        self._orders = None
        self._package_specification = None
        self._ship_from = None
        self._ship_to = None
        self.discriminator = None
        if orders is not None:
            self.orders = orders
        if package_specification is not None:
            self.package_specification = package_specification
        if ship_from is not None:
            self.ship_from = ship_from
        if ship_to is not None:
            self.ship_to = ship_to

    @property
    def orders(self):
        """Gets the orders of this ShippingQuoteRequest.  # noqa: E501

        A seller-defined list that contains information about the orders in the package. This allows sellers to include information about the line items in the package with the shipment information. A package can contain any number of line items from one or more orders, providing they all ship in the same package. Maximum list size: 10  # noqa: E501

        :return: The orders of this ShippingQuoteRequest.  # noqa: E501
        :rtype: list[Order]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this ShippingQuoteRequest.

        A seller-defined list that contains information about the orders in the package. This allows sellers to include information about the line items in the package with the shipment information. A package can contain any number of line items from one or more orders, providing they all ship in the same package. Maximum list size: 10  # noqa: E501

        :param orders: The orders of this ShippingQuoteRequest.  # noqa: E501
        :type: list[Order]
        """

        self._orders = orders

    @property
    def package_specification(self):
        """Gets the package_specification of this ShippingQuoteRequest.  # noqa: E501


        :return: The package_specification of this ShippingQuoteRequest.  # noqa: E501
        :rtype: PackageSpecification
        """
        return self._package_specification

    @package_specification.setter
    def package_specification(self, package_specification):
        """Sets the package_specification of this ShippingQuoteRequest.


        :param package_specification: The package_specification of this ShippingQuoteRequest.  # noqa: E501
        :type: PackageSpecification
        """

        self._package_specification = package_specification

    @property
    def ship_from(self):
        """Gets the ship_from of this ShippingQuoteRequest.  # noqa: E501


        :return: The ship_from of this ShippingQuoteRequest.  # noqa: E501
        :rtype: Contact
        """
        return self._ship_from

    @ship_from.setter
    def ship_from(self, ship_from):
        """Sets the ship_from of this ShippingQuoteRequest.


        :param ship_from: The ship_from of this ShippingQuoteRequest.  # noqa: E501
        :type: Contact
        """

        self._ship_from = ship_from

    @property
    def ship_to(self):
        """Gets the ship_to of this ShippingQuoteRequest.  # noqa: E501


        :return: The ship_to of this ShippingQuoteRequest.  # noqa: E501
        :rtype: Contact
        """
        return self._ship_to

    @ship_to.setter
    def ship_to(self, ship_to):
        """Sets the ship_to of this ShippingQuoteRequest.


        :param ship_to: The ship_to of this ShippingQuoteRequest.  # noqa: E501
        :type: Contact
        """

        self._ship_to = ship_to

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
        if issubclass(ShippingQuoteRequest, dict):
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
        if not isinstance(other, ShippingQuoteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
