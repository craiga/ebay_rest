# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#API\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#API\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#Limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentMethod(object):
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
        'payment_instructions': 'list[str]',
        'payment_method_brands': 'list[PaymentMethodBrand]',
        'payment_method_type': 'str',
        'seller_instructions': 'list[str]'
    }

    attribute_map = {
        'payment_instructions': 'paymentInstructions',
        'payment_method_brands': 'paymentMethodBrands',
        'payment_method_type': 'paymentMethodType',
        'seller_instructions': 'sellerInstructions'
    }

    def __init__(self, payment_instructions=None, payment_method_brands=None, payment_method_type=None, seller_instructions=None):  # noqa: E501
        """PaymentMethod - a model defined in Swagger"""  # noqa: E501
        self._payment_instructions = None
        self._payment_method_brands = None
        self._payment_method_type = None
        self._seller_instructions = None
        self.discriminator = None
        if payment_instructions is not None:
            self.payment_instructions = payment_instructions
        if payment_method_brands is not None:
            self.payment_method_brands = payment_method_brands
        if payment_method_type is not None:
            self.payment_method_type = payment_method_type
        if seller_instructions is not None:
            self.seller_instructions = seller_instructions

    @property
    def payment_instructions(self):
        """Gets the payment_instructions of this PaymentMethod.  # noqa: E501

        The payment instructions for the buyer, such as cash in person or contact seller.  # noqa: E501

        :return: The payment_instructions of this PaymentMethod.  # noqa: E501
        :rtype: list[str]
        """
        return self._payment_instructions

    @payment_instructions.setter
    def payment_instructions(self, payment_instructions):
        """Sets the payment_instructions of this PaymentMethod.

        The payment instructions for the buyer, such as cash in person or contact seller.  # noqa: E501

        :param payment_instructions: The payment_instructions of this PaymentMethod.  # noqa: E501
        :type: list[str]
        """

        self._payment_instructions = payment_instructions

    @property
    def payment_method_brands(self):
        """Gets the payment_method_brands of this PaymentMethod.  # noqa: E501

        The payment method brands, including the payment method brand type and logo image.  # noqa: E501

        :return: The payment_method_brands of this PaymentMethod.  # noqa: E501
        :rtype: list[PaymentMethodBrand]
        """
        return self._payment_method_brands

    @payment_method_brands.setter
    def payment_method_brands(self, payment_method_brands):
        """Sets the payment_method_brands of this PaymentMethod.

        The payment method brands, including the payment method brand type and logo image.  # noqa: E501

        :param payment_method_brands: The payment_method_brands of this PaymentMethod.  # noqa: E501
        :type: list[PaymentMethodBrand]
        """

        self._payment_method_brands = payment_method_brands

    @property
    def payment_method_type(self):
        """Gets the payment_method_type of this PaymentMethod.  # noqa: E501

        The payment method type, such as credit card or cash. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:PaymentMethodTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The payment_method_type of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, payment_method_type):
        """Sets the payment_method_type of this PaymentMethod.

        The payment method type, such as credit card or cash. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:PaymentMethodTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param payment_method_type: The payment_method_type of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._payment_method_type = payment_method_type

    @property
    def seller_instructions(self):
        """Gets the seller_instructions of this PaymentMethod.  # noqa: E501

        The seller instructions to the buyer, such as accepts credit cards or see description.  # noqa: E501

        :return: The seller_instructions of this PaymentMethod.  # noqa: E501
        :rtype: list[str]
        """
        return self._seller_instructions

    @seller_instructions.setter
    def seller_instructions(self, seller_instructions):
        """Sets the seller_instructions of this PaymentMethod.

        The seller instructions to the buyer, such as accepts credit cards or see description.  # noqa: E501

        :param seller_instructions: The seller_instructions of this PaymentMethod.  # noqa: E501
        :type: list[str]
        """

        self._seller_instructions = seller_instructions

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
        if issubclass(PaymentMethod, dict):
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
        if not isinstance(other, PaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
