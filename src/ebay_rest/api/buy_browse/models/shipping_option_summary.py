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

class ShippingOptionSummary(object):
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
        'guaranteed_delivery': 'bool',
        'max_estimated_delivery_date': 'str',
        'min_estimated_delivery_date': 'str',
        'shipping_cost': 'ConvertedAmount',
        'shipping_cost_type': 'str'
    }

    attribute_map = {
        'guaranteed_delivery': 'guaranteedDelivery',
        'max_estimated_delivery_date': 'maxEstimatedDeliveryDate',
        'min_estimated_delivery_date': 'minEstimatedDeliveryDate',
        'shipping_cost': 'shippingCost',
        'shipping_cost_type': 'shippingCostType'
    }

    def __init__(self, guaranteed_delivery=None, max_estimated_delivery_date=None, min_estimated_delivery_date=None, shipping_cost=None, shipping_cost_type=None):  # noqa: E501
        """ShippingOptionSummary - a model defined in Swagger"""  # noqa: E501
        self._guaranteed_delivery = None
        self._max_estimated_delivery_date = None
        self._min_estimated_delivery_date = None
        self._shipping_cost = None
        self._shipping_cost_type = None
        self.discriminator = None
        if guaranteed_delivery is not None:
            self.guaranteed_delivery = guaranteed_delivery
        if max_estimated_delivery_date is not None:
            self.max_estimated_delivery_date = max_estimated_delivery_date
        if min_estimated_delivery_date is not None:
            self.min_estimated_delivery_date = min_estimated_delivery_date
        if shipping_cost is not None:
            self.shipping_cost = shipping_cost
        if shipping_cost_type is not None:
            self.shipping_cost_type = shipping_cost_type

    @property
    def guaranteed_delivery(self):
        """Gets the guaranteed_delivery of this ShippingOptionSummary.  # noqa: E501

        Indicates if the seller has committed to shipping the item with eBay Guaranteed Delivery. With eBay Guaranteed Delivery, the seller is committed to getting the line item to the buyer within 4 business days or less. See the Buying items with eBay Guaranteed Delivery help topic for more details about eBay Guaranteed Delivery.  # noqa: E501

        :return: The guaranteed_delivery of this ShippingOptionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._guaranteed_delivery

    @guaranteed_delivery.setter
    def guaranteed_delivery(self, guaranteed_delivery):
        """Sets the guaranteed_delivery of this ShippingOptionSummary.

        Indicates if the seller has committed to shipping the item with eBay Guaranteed Delivery. With eBay Guaranteed Delivery, the seller is committed to getting the line item to the buyer within 4 business days or less. See the Buying items with eBay Guaranteed Delivery help topic for more details about eBay Guaranteed Delivery.  # noqa: E501

        :param guaranteed_delivery: The guaranteed_delivery of this ShippingOptionSummary.  # noqa: E501
        :type: bool
        """

        self._guaranteed_delivery = guaranteed_delivery

    @property
    def max_estimated_delivery_date(self):
        """Gets the max_estimated_delivery_date of this ShippingOptionSummary.  # noqa: E501

        The end date of the delivery window (latest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer. Note: For the best accuracy, always include the contextualLocation values in the X-EBAY-C-ENDUSERCTX request header.  # noqa: E501

        :return: The max_estimated_delivery_date of this ShippingOptionSummary.  # noqa: E501
        :rtype: str
        """
        return self._max_estimated_delivery_date

    @max_estimated_delivery_date.setter
    def max_estimated_delivery_date(self, max_estimated_delivery_date):
        """Sets the max_estimated_delivery_date of this ShippingOptionSummary.

        The end date of the delivery window (latest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer. Note: For the best accuracy, always include the contextualLocation values in the X-EBAY-C-ENDUSERCTX request header.  # noqa: E501

        :param max_estimated_delivery_date: The max_estimated_delivery_date of this ShippingOptionSummary.  # noqa: E501
        :type: str
        """

        self._max_estimated_delivery_date = max_estimated_delivery_date

    @property
    def min_estimated_delivery_date(self):
        """Gets the min_estimated_delivery_date of this ShippingOptionSummary.  # noqa: E501

        The start date of the delivery window (earliest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer. Note: For the best accuracy, always include the contextualLocation values in the X-EBAY-C-ENDUSERCTX request header.  # noqa: E501

        :return: The min_estimated_delivery_date of this ShippingOptionSummary.  # noqa: E501
        :rtype: str
        """
        return self._min_estimated_delivery_date

    @min_estimated_delivery_date.setter
    def min_estimated_delivery_date(self, min_estimated_delivery_date):
        """Sets the min_estimated_delivery_date of this ShippingOptionSummary.

        The start date of the delivery window (earliest projected delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer. Note: For the best accuracy, always include the contextualLocation values in the X-EBAY-C-ENDUSERCTX request header.  # noqa: E501

        :param min_estimated_delivery_date: The min_estimated_delivery_date of this ShippingOptionSummary.  # noqa: E501
        :type: str
        """

        self._min_estimated_delivery_date = min_estimated_delivery_date

    @property
    def shipping_cost(self):
        """Gets the shipping_cost of this ShippingOptionSummary.  # noqa: E501


        :return: The shipping_cost of this ShippingOptionSummary.  # noqa: E501
        :rtype: ConvertedAmount
        """
        return self._shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, shipping_cost):
        """Sets the shipping_cost of this ShippingOptionSummary.


        :param shipping_cost: The shipping_cost of this ShippingOptionSummary.  # noqa: E501
        :type: ConvertedAmount
        """

        self._shipping_cost = shipping_cost

    @property
    def shipping_cost_type(self):
        """Gets the shipping_cost_type of this ShippingOptionSummary.  # noqa: E501

        Indicates the type of shipping used to ship the item. Possible values are FIXED (flat-rate shipping) and CALCULATED (shipping cost calculated based on item and buyer location).  # noqa: E501

        :return: The shipping_cost_type of this ShippingOptionSummary.  # noqa: E501
        :rtype: str
        """
        return self._shipping_cost_type

    @shipping_cost_type.setter
    def shipping_cost_type(self, shipping_cost_type):
        """Sets the shipping_cost_type of this ShippingOptionSummary.

        Indicates the type of shipping used to ship the item. Possible values are FIXED (flat-rate shipping) and CALCULATED (shipping cost calculated based on item and buyer location).  # noqa: E501

        :param shipping_cost_type: The shipping_cost_type of this ShippingOptionSummary.  # noqa: E501
        :type: str
        """

        self._shipping_cost_type = shipping_cost_type

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
        if issubclass(ShippingOptionSummary, dict):
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
        if not isinstance(other, ShippingOptionSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
