# coding: utf-8

"""
    Order API

    <span class=\"tablenote\"><b>Note:</b> This version of the Order API (v2) currently only supports the guest payment flow for eBay managed payments. To view the v1_beta version of the Order API, which includes both member and guest checkout payment flows, refer to the <a href=\"/api-docs/buy/order_v1/resources/methods\">Order_v1 API</a> documentation.</span><br /><br /><span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#Limited\" target=\"_blank\"><img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\"  alt=\"Limited Release\" title=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The Order API provides interfaces that let shoppers pay for items. It also returns payment and shipping status of the order.  # noqa: E501

    OpenAPI spec version: v2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LineItem(object):
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
        'authenticity_verification': 'AuthenticityVerificationProgram',
        'base_unit_price': 'Amount',
        'fees': 'list[Fee]',
        'image': 'Image',
        'item_id': 'str',
        'line_item_id': 'str',
        'net_price': 'Amount',
        'promotions': 'list[Promotion]',
        'quantity': 'int',
        'seller': 'Seller',
        'shipping_options': 'list[ShippingOption]',
        'tax_details': 'list[TaxDetail]',
        'title': 'str'
    }

    attribute_map = {
        'authenticity_verification': 'authenticityVerification',
        'base_unit_price': 'baseUnitPrice',
        'fees': 'fees',
        'image': 'image',
        'item_id': 'itemId',
        'line_item_id': 'lineItemId',
        'net_price': 'netPrice',
        'promotions': 'promotions',
        'quantity': 'quantity',
        'seller': 'seller',
        'shipping_options': 'shippingOptions',
        'tax_details': 'taxDetails',
        'title': 'title'
    }

    def __init__(self, authenticity_verification=None, base_unit_price=None, fees=None, image=None, item_id=None, line_item_id=None, net_price=None, promotions=None, quantity=None, seller=None, shipping_options=None, tax_details=None, title=None):  # noqa: E501
        """LineItem - a model defined in Swagger"""  # noqa: E501
        self._authenticity_verification = None
        self._base_unit_price = None
        self._fees = None
        self._image = None
        self._item_id = None
        self._line_item_id = None
        self._net_price = None
        self._promotions = None
        self._quantity = None
        self._seller = None
        self._shipping_options = None
        self._tax_details = None
        self._title = None
        self.discriminator = None
        if authenticity_verification is not None:
            self.authenticity_verification = authenticity_verification
        if base_unit_price is not None:
            self.base_unit_price = base_unit_price
        if fees is not None:
            self.fees = fees
        if image is not None:
            self.image = image
        if item_id is not None:
            self.item_id = item_id
        if line_item_id is not None:
            self.line_item_id = line_item_id
        if net_price is not None:
            self.net_price = net_price
        if promotions is not None:
            self.promotions = promotions
        if quantity is not None:
            self.quantity = quantity
        if seller is not None:
            self.seller = seller
        if shipping_options is not None:
            self.shipping_options = shipping_options
        if tax_details is not None:
            self.tax_details = tax_details
        if title is not None:
            self.title = title

    @property
    def authenticity_verification(self):
        """Gets the authenticity_verification of this LineItem.  # noqa: E501


        :return: The authenticity_verification of this LineItem.  # noqa: E501
        :rtype: AuthenticityVerificationProgram
        """
        return self._authenticity_verification

    @authenticity_verification.setter
    def authenticity_verification(self, authenticity_verification):
        """Sets the authenticity_verification of this LineItem.


        :param authenticity_verification: The authenticity_verification of this LineItem.  # noqa: E501
        :type: AuthenticityVerificationProgram
        """

        self._authenticity_verification = authenticity_verification

    @property
    def base_unit_price(self):
        """Gets the base_unit_price of this LineItem.  # noqa: E501


        :return: The base_unit_price of this LineItem.  # noqa: E501
        :rtype: Amount
        """
        return self._base_unit_price

    @base_unit_price.setter
    def base_unit_price(self, base_unit_price):
        """Sets the base_unit_price of this LineItem.


        :param base_unit_price: The base_unit_price of this LineItem.  # noqa: E501
        :type: Amount
        """

        self._base_unit_price = base_unit_price

    @property
    def fees(self):
        """Gets the fees of this LineItem.  # noqa: E501

        A breakdown of the fees applicable to the line item.  # noqa: E501

        :return: The fees of this LineItem.  # noqa: E501
        :rtype: list[Fee]
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this LineItem.

        A breakdown of the fees applicable to the line item.  # noqa: E501

        :param fees: The fees of this LineItem.  # noqa: E501
        :type: list[Fee]
        """

        self._fees = fees

    @property
    def image(self):
        """Gets the image of this LineItem.  # noqa: E501


        :return: The image of this LineItem.  # noqa: E501
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this LineItem.


        :param image: The image of this LineItem.  # noqa: E501
        :type: Image
        """

        self._image = image

    @property
    def item_id(self):
        """Gets the item_id of this LineItem.  # noqa: E501

        The eBay identifier of an item. This ID is returned by the Browse and Feed API methods. The ID is in RESTful item ID format. For example: v1|2**********6|5**********4 or v1|1**********9|0. For more information about item IDs for RESTful APIs, see Legacy API compatibility.  # noqa: E501

        :return: The item_id of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this LineItem.

        The eBay identifier of an item. This ID is returned by the Browse and Feed API methods. The ID is in RESTful item ID format. For example: v1|2**********6|5**********4 or v1|1**********9|0. For more information about item IDs for RESTful APIs, see Legacy API compatibility.  # noqa: E501

        :param item_id: The item_id of this LineItem.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def line_item_id(self):
        """Gets the line_item_id of this LineItem.  # noqa: E501

        A unique eBay-assigned ID value that identifies a line item in a checkout session.  # noqa: E501

        :return: The line_item_id of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        """Sets the line_item_id of this LineItem.

        A unique eBay-assigned ID value that identifies a line item in a checkout session.  # noqa: E501

        :param line_item_id: The line_item_id of this LineItem.  # noqa: E501
        :type: str
        """

        self._line_item_id = line_item_id

    @property
    def net_price(self):
        """Gets the net_price of this LineItem.  # noqa: E501


        :return: The net_price of this LineItem.  # noqa: E501
        :rtype: Amount
        """
        return self._net_price

    @net_price.setter
    def net_price(self, net_price):
        """Sets the net_price of this LineItem.


        :param net_price: The net_price of this LineItem.  # noqa: E501
        :type: Amount
        """

        self._net_price = net_price

    @property
    def promotions(self):
        """Gets the promotions of this LineItem.  # noqa: E501

        An array of promotions applied to the line item.  # noqa: E501

        :return: The promotions of this LineItem.  # noqa: E501
        :rtype: list[Promotion]
        """
        return self._promotions

    @promotions.setter
    def promotions(self, promotions):
        """Sets the promotions of this LineItem.

        An array of promotions applied to the line item.  # noqa: E501

        :param promotions: The promotions of this LineItem.  # noqa: E501
        :type: list[Promotion]
        """

        self._promotions = promotions

    @property
    def quantity(self):
        """Gets the quantity of this LineItem.  # noqa: E501

        The quantity ordered for the line item.  # noqa: E501

        :return: The quantity of this LineItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this LineItem.

        The quantity ordered for the line item.  # noqa: E501

        :param quantity: The quantity of this LineItem.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def seller(self):
        """Gets the seller of this LineItem.  # noqa: E501


        :return: The seller of this LineItem.  # noqa: E501
        :rtype: Seller
        """
        return self._seller

    @seller.setter
    def seller(self, seller):
        """Sets the seller of this LineItem.


        :param seller: The seller of this LineItem.  # noqa: E501
        :type: Seller
        """

        self._seller = seller

    @property
    def shipping_options(self):
        """Gets the shipping_options of this LineItem.  # noqa: E501

        An array of shipping options that are available for the line item. By default, the first one will be selected. Note: The updateGuestShippingOption method can be used to change the shipping option.  # noqa: E501

        :return: The shipping_options of this LineItem.  # noqa: E501
        :rtype: list[ShippingOption]
        """
        return self._shipping_options

    @shipping_options.setter
    def shipping_options(self, shipping_options):
        """Sets the shipping_options of this LineItem.

        An array of shipping options that are available for the line item. By default, the first one will be selected. Note: The updateGuestShippingOption method can be used to change the shipping option.  # noqa: E501

        :param shipping_options: The shipping_options of this LineItem.  # noqa: E501
        :type: list[ShippingOption]
        """

        self._shipping_options = shipping_options

    @property
    def tax_details(self):
        """Gets the tax_details of this LineItem.  # noqa: E501

        A container that returns the tax information for the line item.  # noqa: E501

        :return: The tax_details of this LineItem.  # noqa: E501
        :rtype: list[TaxDetail]
        """
        return self._tax_details

    @tax_details.setter
    def tax_details(self, tax_details):
        """Sets the tax_details of this LineItem.

        A container that returns the tax information for the line item.  # noqa: E501

        :param tax_details: The tax_details of this LineItem.  # noqa: E501
        :type: list[TaxDetail]
        """

        self._tax_details = tax_details

    @property
    def title(self):
        """Gets the title of this LineItem.  # noqa: E501

        The seller-created title of the item.  # noqa: E501

        :return: The title of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LineItem.

        The seller-created title of the item.  # noqa: E501

        :param title: The title of this LineItem.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(LineItem, dict):
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
        if not isinstance(other, LineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
