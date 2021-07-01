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

class Shipment(object):
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
        'cancellation': 'ShipmentCancellation',
        'creation_date': 'str',
        'label_custom_message': 'str',
        'label_download_url': 'str',
        'label_size': 'str',
        'orders': 'list[Order]',
        'package_specification': 'PackageSpecification',
        'rate': 'PurchasedRate',
        'return_to': 'Contact',
        'ship_from': 'Contact',
        'ship_to': 'Contact',
        'shipment_id': 'str',
        'shipment_tracking_number': 'str'
    }

    attribute_map = {
        'cancellation': 'cancellation',
        'creation_date': 'creationDate',
        'label_custom_message': 'labelCustomMessage',
        'label_download_url': 'labelDownloadUrl',
        'label_size': 'labelSize',
        'orders': 'orders',
        'package_specification': 'packageSpecification',
        'rate': 'rate',
        'return_to': 'returnTo',
        'ship_from': 'shipFrom',
        'ship_to': 'shipTo',
        'shipment_id': 'shipmentId',
        'shipment_tracking_number': 'shipmentTrackingNumber'
    }

    def __init__(self, cancellation=None, creation_date=None, label_custom_message=None, label_download_url=None, label_size=None, orders=None, package_specification=None, rate=None, return_to=None, ship_from=None, ship_to=None, shipment_id=None, shipment_tracking_number=None):  # noqa: E501
        """Shipment - a model defined in Swagger"""  # noqa: E501
        self._cancellation = None
        self._creation_date = None
        self._label_custom_message = None
        self._label_download_url = None
        self._label_size = None
        self._orders = None
        self._package_specification = None
        self._rate = None
        self._return_to = None
        self._ship_from = None
        self._ship_to = None
        self._shipment_id = None
        self._shipment_tracking_number = None
        self.discriminator = None
        if cancellation is not None:
            self.cancellation = cancellation
        if creation_date is not None:
            self.creation_date = creation_date
        if label_custom_message is not None:
            self.label_custom_message = label_custom_message
        if label_download_url is not None:
            self.label_download_url = label_download_url
        if label_size is not None:
            self.label_size = label_size
        if orders is not None:
            self.orders = orders
        if package_specification is not None:
            self.package_specification = package_specification
        if rate is not None:
            self.rate = rate
        if return_to is not None:
            self.return_to = return_to
        if ship_from is not None:
            self.ship_from = ship_from
        if ship_to is not None:
            self.ship_to = ship_to
        if shipment_id is not None:
            self.shipment_id = shipment_id
        if shipment_tracking_number is not None:
            self.shipment_tracking_number = shipment_tracking_number

    @property
    def cancellation(self):
        """Gets the cancellation of this Shipment.  # noqa: E501


        :return: The cancellation of this Shipment.  # noqa: E501
        :rtype: ShipmentCancellation
        """
        return self._cancellation

    @cancellation.setter
    def cancellation(self, cancellation):
        """Sets the cancellation of this Shipment.


        :param cancellation: The cancellation of this Shipment.  # noqa: E501
        :type: ShipmentCancellation
        """

        self._cancellation = cancellation

    @property
    def creation_date(self):
        """Gets the creation_date of this Shipment.  # noqa: E501

        The date and time the shipment was created, formatted as an ISO 8601 string, which is based on the 24-hour Coordinated Universal Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS].[SSS]Z Example: 2018-08-20T07:09:00.000Z  # noqa: E501

        :return: The creation_date of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Shipment.

        The date and time the shipment was created, formatted as an ISO 8601 string, which is based on the 24-hour Coordinated Universal Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS].[SSS]Z Example: 2018-08-20T07:09:00.000Z  # noqa: E501

        :param creation_date: The creation_date of this Shipment.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

    @property
    def label_custom_message(self):
        """Gets the label_custom_message of this Shipment.  # noqa: E501

        If supported by the selected shipping carrier, this field can contain optional seller text to be printed on the shipping label.  # noqa: E501

        :return: The label_custom_message of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._label_custom_message

    @label_custom_message.setter
    def label_custom_message(self, label_custom_message):
        """Sets the label_custom_message of this Shipment.

        If supported by the selected shipping carrier, this field can contain optional seller text to be printed on the shipping label.  # noqa: E501

        :param label_custom_message: The label_custom_message of this Shipment.  # noqa: E501
        :type: str
        """

        self._label_custom_message = label_custom_message

    @property
    def label_download_url(self):
        """Gets the label_download_url of this Shipment.  # noqa: E501

        The direct URL the seller can use to download an image of the shipping label. By default, the file format is PDF. See downloadLabelFile for requesting different response file formats.  # noqa: E501

        :return: The label_download_url of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._label_download_url

    @label_download_url.setter
    def label_download_url(self, label_download_url):
        """Sets the label_download_url of this Shipment.

        The direct URL the seller can use to download an image of the shipping label. By default, the file format is PDF. See downloadLabelFile for requesting different response file formats.  # noqa: E501

        :param label_download_url: The label_download_url of this Shipment.  # noqa: E501
        :type: str
        """

        self._label_download_url = label_download_url

    @property
    def label_size(self):
        """Gets the label_size of this Shipment.  # noqa: E501

        The seller's desired label size. The support for multi-sized labels is shipping-carrier specific and if the size requested in the creaateFromShippingQuote call matches a size the carrier supports, the value will be represented here in the shipment. Currently, the only valid value is: 4&quot;x6&quot;  # noqa: E501

        :return: The label_size of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._label_size

    @label_size.setter
    def label_size(self, label_size):
        """Sets the label_size of this Shipment.

        The seller's desired label size. The support for multi-sized labels is shipping-carrier specific and if the size requested in the creaateFromShippingQuote call matches a size the carrier supports, the value will be represented here in the shipment. Currently, the only valid value is: 4&quot;x6&quot;  # noqa: E501

        :param label_size: The label_size of this Shipment.  # noqa: E501
        :type: str
        """

        self._label_size = label_size

    @property
    def orders(self):
        """Gets the orders of this Shipment.  # noqa: E501

        This list value is optionally assigned by the seller. When present, each element in the returned list contains seller-assigned information about an order (such as an order number). Because a package can contain all or part of one or more orders, this field provides a way for sellers to identify the packages that contain specific orders.  # noqa: E501

        :return: The orders of this Shipment.  # noqa: E501
        :rtype: list[Order]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this Shipment.

        This list value is optionally assigned by the seller. When present, each element in the returned list contains seller-assigned information about an order (such as an order number). Because a package can contain all or part of one or more orders, this field provides a way for sellers to identify the packages that contain specific orders.  # noqa: E501

        :param orders: The orders of this Shipment.  # noqa: E501
        :type: list[Order]
        """

        self._orders = orders

    @property
    def package_specification(self):
        """Gets the package_specification of this Shipment.  # noqa: E501


        :return: The package_specification of this Shipment.  # noqa: E501
        :rtype: PackageSpecification
        """
        return self._package_specification

    @package_specification.setter
    def package_specification(self, package_specification):
        """Sets the package_specification of this Shipment.


        :param package_specification: The package_specification of this Shipment.  # noqa: E501
        :type: PackageSpecification
        """

        self._package_specification = package_specification

    @property
    def rate(self):
        """Gets the rate of this Shipment.  # noqa: E501


        :return: The rate of this Shipment.  # noqa: E501
        :rtype: PurchasedRate
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this Shipment.


        :param rate: The rate of this Shipment.  # noqa: E501
        :type: PurchasedRate
        """

        self._rate = rate

    @property
    def return_to(self):
        """Gets the return_to of this Shipment.  # noqa: E501


        :return: The return_to of this Shipment.  # noqa: E501
        :rtype: Contact
        """
        return self._return_to

    @return_to.setter
    def return_to(self, return_to):
        """Sets the return_to of this Shipment.


        :param return_to: The return_to of this Shipment.  # noqa: E501
        :type: Contact
        """

        self._return_to = return_to

    @property
    def ship_from(self):
        """Gets the ship_from of this Shipment.  # noqa: E501


        :return: The ship_from of this Shipment.  # noqa: E501
        :rtype: Contact
        """
        return self._ship_from

    @ship_from.setter
    def ship_from(self, ship_from):
        """Sets the ship_from of this Shipment.


        :param ship_from: The ship_from of this Shipment.  # noqa: E501
        :type: Contact
        """

        self._ship_from = ship_from

    @property
    def ship_to(self):
        """Gets the ship_to of this Shipment.  # noqa: E501


        :return: The ship_to of this Shipment.  # noqa: E501
        :rtype: Contact
        """
        return self._ship_to

    @ship_to.setter
    def ship_to(self, ship_to):
        """Sets the ship_to of this Shipment.


        :param ship_to: The ship_to of this Shipment.  # noqa: E501
        :type: Contact
        """

        self._ship_to = ship_to

    @property
    def shipment_id(self):
        """Gets the shipment_id of this Shipment.  # noqa: E501

        The unique eBay-assigned ID for the shipment. The ID is generated when the shipment is created by a call to createFromShippingQuote.  # noqa: E501

        :return: The shipment_id of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._shipment_id

    @shipment_id.setter
    def shipment_id(self, shipment_id):
        """Sets the shipment_id of this Shipment.

        The unique eBay-assigned ID for the shipment. The ID is generated when the shipment is created by a call to createFromShippingQuote.  # noqa: E501

        :param shipment_id: The shipment_id of this Shipment.  # noqa: E501
        :type: str
        """

        self._shipment_id = shipment_id

    @property
    def shipment_tracking_number(self):
        """Gets the shipment_tracking_number of this Shipment.  # noqa: E501

        A unique carrier-assigned ID string that can be used to track the shipment.  # noqa: E501

        :return: The shipment_tracking_number of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._shipment_tracking_number

    @shipment_tracking_number.setter
    def shipment_tracking_number(self, shipment_tracking_number):
        """Sets the shipment_tracking_number of this Shipment.

        A unique carrier-assigned ID string that can be used to track the shipment.  # noqa: E501

        :param shipment_tracking_number: The shipment_tracking_number of this Shipment.  # noqa: E501
        :type: str
        """

        self._shipment_tracking_number = shipment_tracking_number

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
        if issubclass(Shipment, dict):
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
        if not isinstance(other, Shipment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
