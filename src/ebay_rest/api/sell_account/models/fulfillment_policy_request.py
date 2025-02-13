# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (the Fulfillment Policy, Payment Policy, and Return Policy), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FulfillmentPolicyRequest(object):
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
        'category_types': 'list[CategoryType]',
        'description': 'str',
        'freight_shipping': 'bool',
        'global_shipping': 'bool',
        'handling_time': 'TimeDuration',
        'local_pickup': 'bool',
        'marketplace_id': 'str',
        'name': 'str',
        'pickup_drop_off': 'bool',
        'ship_to_locations': 'RegionSet',
        'shipping_options': 'list[ShippingOption]'
    }

    attribute_map = {
        'category_types': 'categoryTypes',
        'description': 'description',
        'freight_shipping': 'freightShipping',
        'global_shipping': 'globalShipping',
        'handling_time': 'handlingTime',
        'local_pickup': 'localPickup',
        'marketplace_id': 'marketplaceId',
        'name': 'name',
        'pickup_drop_off': 'pickupDropOff',
        'ship_to_locations': 'shipToLocations',
        'shipping_options': 'shippingOptions'
    }

    def __init__(self, category_types=None, description=None, freight_shipping=None, global_shipping=None, handling_time=None, local_pickup=None, marketplace_id=None, name=None, pickup_drop_off=None, ship_to_locations=None, shipping_options=None):  # noqa: E501
        """FulfillmentPolicyRequest - a model defined in Swagger"""  # noqa: E501
        self._category_types = None
        self._description = None
        self._freight_shipping = None
        self._global_shipping = None
        self._handling_time = None
        self._local_pickup = None
        self._marketplace_id = None
        self._name = None
        self._pickup_drop_off = None
        self._ship_to_locations = None
        self._shipping_options = None
        self.discriminator = None
        if category_types is not None:
            self.category_types = category_types
        if description is not None:
            self.description = description
        if freight_shipping is not None:
            self.freight_shipping = freight_shipping
        if global_shipping is not None:
            self.global_shipping = global_shipping
        if handling_time is not None:
            self.handling_time = handling_time
        if local_pickup is not None:
            self.local_pickup = local_pickup
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if name is not None:
            self.name = name
        if pickup_drop_off is not None:
            self.pickup_drop_off = pickup_drop_off
        if ship_to_locations is not None:
            self.ship_to_locations = ship_to_locations
        if shipping_options is not None:
            self.shipping_options = shipping_options

    @property
    def category_types(self):
        """Gets the category_types of this FulfillmentPolicyRequest.  # noqa: E501

        The CategoryTypeEnum value to which this policy applies. Used to discern accounts that sell motor vehicles from those that don't. (Currently, each policy can be set to only one categoryTypes value at a time.)  # noqa: E501

        :return: The category_types of this FulfillmentPolicyRequest.  # noqa: E501
        :rtype: list[CategoryType]
        """
        return self._category_types

    @category_types.setter
    def category_types(self, category_types):
        """Sets the category_types of this FulfillmentPolicyRequest.

        The CategoryTypeEnum value to which this policy applies. Used to discern accounts that sell motor vehicles from those that don't. (Currently, each policy can be set to only one categoryTypes value at a time.)  # noqa: E501

        :param category_types: The category_types of this FulfillmentPolicyRequest.  # noqa: E501
        :type: list[CategoryType]
        """

        self._category_types = category_types

    @property
    def description(self):
        """Gets the description of this FulfillmentPolicyRequest.  # noqa: E501

        An optional seller-defined description of the fulfillment policy for internal use (this value is not displayed to end users). Max length: 250  # noqa: E501

        :return: The description of this FulfillmentPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FulfillmentPolicyRequest.

        An optional seller-defined description of the fulfillment policy for internal use (this value is not displayed to end users). Max length: 250  # noqa: E501

        :param description: The description of this FulfillmentPolicyRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def freight_shipping(self):
        """Gets the freight_shipping of this FulfillmentPolicyRequest.  # noqa: E501

        If set to true, the seller offers freight shipping. Freight shipping can be used for large items over 150 lbs. Default: false  # noqa: E501

        :return: The freight_shipping of this FulfillmentPolicyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._freight_shipping

    @freight_shipping.setter
    def freight_shipping(self, freight_shipping):
        """Sets the freight_shipping of this FulfillmentPolicyRequest.

        If set to true, the seller offers freight shipping. Freight shipping can be used for large items over 150 lbs. Default: false  # noqa: E501

        :param freight_shipping: The freight_shipping of this FulfillmentPolicyRequest.  # noqa: E501
        :type: bool
        """

        self._freight_shipping = freight_shipping

    @property
    def global_shipping(self):
        """Gets the global_shipping of this FulfillmentPolicyRequest.  # noqa: E501

        If set to true, the seller has opted-in to the eBay Global Shipping Program and that they use that service for their international shipments. Setting this value automatically sets the international shipping service for the policy to International Priority Shipping and the buyer does not need to set any other shipping services for their INTERNATIONAL shipping options (unless they sell items not covered by the Global Shipping Program). If this value is set to false, the seller is responsible for manually specifying the international shipping services, as described in Setting up worldwide shipping. To opt-in to the Global Shipping Program, log in to eBay and navigate to My Account &gt; Site Preferences &gt; Shipping preferences. Default: false  # noqa: E501

        :return: The global_shipping of this FulfillmentPolicyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._global_shipping

    @global_shipping.setter
    def global_shipping(self, global_shipping):
        """Sets the global_shipping of this FulfillmentPolicyRequest.

        If set to true, the seller has opted-in to the eBay Global Shipping Program and that they use that service for their international shipments. Setting this value automatically sets the international shipping service for the policy to International Priority Shipping and the buyer does not need to set any other shipping services for their INTERNATIONAL shipping options (unless they sell items not covered by the Global Shipping Program). If this value is set to false, the seller is responsible for manually specifying the international shipping services, as described in Setting up worldwide shipping. To opt-in to the Global Shipping Program, log in to eBay and navigate to My Account &gt; Site Preferences &gt; Shipping preferences. Default: false  # noqa: E501

        :param global_shipping: The global_shipping of this FulfillmentPolicyRequest.  # noqa: E501
        :type: bool
        """

        self._global_shipping = global_shipping

    @property
    def handling_time(self):
        """Gets the handling_time of this FulfillmentPolicyRequest.  # noqa: E501


        :return: The handling_time of this FulfillmentPolicyRequest.  # noqa: E501
        :rtype: TimeDuration
        """
        return self._handling_time

    @handling_time.setter
    def handling_time(self, handling_time):
        """Sets the handling_time of this FulfillmentPolicyRequest.


        :param handling_time: The handling_time of this FulfillmentPolicyRequest.  # noqa: E501
        :type: TimeDuration
        """

        self._handling_time = handling_time

    @property
    def local_pickup(self):
        """Gets the local_pickup of this FulfillmentPolicyRequest.  # noqa: E501

        If set to true, no shipping is offered by this policy and the seller offers only local pickup of the item (normally from a non-business location). This option is most often used for customer-to-customer sales and if set, costType should be set to NOT_SPECIFIED. Default: false  # noqa: E501

        :return: The local_pickup of this FulfillmentPolicyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._local_pickup

    @local_pickup.setter
    def local_pickup(self, local_pickup):
        """Sets the local_pickup of this FulfillmentPolicyRequest.

        If set to true, no shipping is offered by this policy and the seller offers only local pickup of the item (normally from a non-business location). This option is most often used for customer-to-customer sales and if set, costType should be set to NOT_SPECIFIED. Default: false  # noqa: E501

        :param local_pickup: The local_pickup of this FulfillmentPolicyRequest.  # noqa: E501
        :type: bool
        """

        self._local_pickup = local_pickup

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this FulfillmentPolicyRequest.  # noqa: E501

        The ID of the eBay marketplace to which this fulfillment policy applies. If this value is not specified, value defaults to the seller's eBay registration site. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this FulfillmentPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this FulfillmentPolicyRequest.

        The ID of the eBay marketplace to which this fulfillment policy applies. If this value is not specified, value defaults to the seller's eBay registration site. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this FulfillmentPolicyRequest.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def name(self):
        """Gets the name of this FulfillmentPolicyRequest.  # noqa: E501

        A user-defined name for this fulfillment policy. Names must be unique for policies assigned to the same marketplace. Max length: 64  # noqa: E501

        :return: The name of this FulfillmentPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FulfillmentPolicyRequest.

        A user-defined name for this fulfillment policy. Names must be unique for policies assigned to the same marketplace. Max length: 64  # noqa: E501

        :param name: The name of this FulfillmentPolicyRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pickup_drop_off(self):
        """Gets the pickup_drop_off of this FulfillmentPolicyRequest.  # noqa: E501

        If set to true, the seller offers the &quot;Click and Collect&quot; feature. Click and Collect is supported by the Inventory API, and it can be used with Add/Revise/Relist calls. To enable &quot;Click and Collect&quot;, a seller (1) must be eligible for Click and Collect and (2) must set this boolean field to 'true'. Currently, Click and Collect is available to only large retail merchants selling in the eBay AU and UK marketplaces. In addition to setting this field, the merchant must also do the following to enable the &quot;Click and Collect&quot; option on a listing: Have inventory for the product at one or more physical stores tied to the merchant's account. Sellers can use the createInventoryLocaion method in the Inventory API to associate physical stores to their account and they can then can add inventory to specific store locations. Set an immediate payment requirement on the item. The immediate payment feature requires the seller to: Set the immediatePay flag in the payment policy to 'true'. Include only one paymentMethods field in the payment policy and set its value to PAYPAL. Include a valid PayPal contact in the recipientAccountReference.referenceId field of the payment policy. Have a valid store location with a complete street address. When a UK merchant successfully lists an item with Click and Collect, prospective buyers within a reasonable distance from one of the merchant's stores (that has stock available) will see the &quot;Available for Click and Collect&quot; option on the listing, along with information on the closest store that has the item.Default: false  # noqa: E501

        :return: The pickup_drop_off of this FulfillmentPolicyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._pickup_drop_off

    @pickup_drop_off.setter
    def pickup_drop_off(self, pickup_drop_off):
        """Sets the pickup_drop_off of this FulfillmentPolicyRequest.

        If set to true, the seller offers the &quot;Click and Collect&quot; feature. Click and Collect is supported by the Inventory API, and it can be used with Add/Revise/Relist calls. To enable &quot;Click and Collect&quot;, a seller (1) must be eligible for Click and Collect and (2) must set this boolean field to 'true'. Currently, Click and Collect is available to only large retail merchants selling in the eBay AU and UK marketplaces. In addition to setting this field, the merchant must also do the following to enable the &quot;Click and Collect&quot; option on a listing: Have inventory for the product at one or more physical stores tied to the merchant's account. Sellers can use the createInventoryLocaion method in the Inventory API to associate physical stores to their account and they can then can add inventory to specific store locations. Set an immediate payment requirement on the item. The immediate payment feature requires the seller to: Set the immediatePay flag in the payment policy to 'true'. Include only one paymentMethods field in the payment policy and set its value to PAYPAL. Include a valid PayPal contact in the recipientAccountReference.referenceId field of the payment policy. Have a valid store location with a complete street address. When a UK merchant successfully lists an item with Click and Collect, prospective buyers within a reasonable distance from one of the merchant's stores (that has stock available) will see the &quot;Available for Click and Collect&quot; option on the listing, along with information on the closest store that has the item.Default: false  # noqa: E501

        :param pickup_drop_off: The pickup_drop_off of this FulfillmentPolicyRequest.  # noqa: E501
        :type: bool
        """

        self._pickup_drop_off = pickup_drop_off

    @property
    def ship_to_locations(self):
        """Gets the ship_to_locations of this FulfillmentPolicyRequest.  # noqa: E501


        :return: The ship_to_locations of this FulfillmentPolicyRequest.  # noqa: E501
        :rtype: RegionSet
        """
        return self._ship_to_locations

    @ship_to_locations.setter
    def ship_to_locations(self, ship_to_locations):
        """Sets the ship_to_locations of this FulfillmentPolicyRequest.


        :param ship_to_locations: The ship_to_locations of this FulfillmentPolicyRequest.  # noqa: E501
        :type: RegionSet
        """

        self._ship_to_locations = ship_to_locations

    @property
    def shipping_options(self):
        """Gets the shipping_options of this FulfillmentPolicyRequest.  # noqa: E501

        A list that defines the seller's shipping configurations for DOMESTIC and INTERNATIONAL order shipments. shippingOptions is a list with a single element if the seller ships to only domestic locations. If the seller also ships internationally, the list contains a second element that defines their international shipping options. Shipping options configure the high-level shipping settings that apply to orders, such as flat-rate or calculated shipping, any rate tables the seller wants to associate with the shipping services, plus other details (such as the shippingServices offered for domestic or international shipments).  # noqa: E501

        :return: The shipping_options of this FulfillmentPolicyRequest.  # noqa: E501
        :rtype: list[ShippingOption]
        """
        return self._shipping_options

    @shipping_options.setter
    def shipping_options(self, shipping_options):
        """Sets the shipping_options of this FulfillmentPolicyRequest.

        A list that defines the seller's shipping configurations for DOMESTIC and INTERNATIONAL order shipments. shippingOptions is a list with a single element if the seller ships to only domestic locations. If the seller also ships internationally, the list contains a second element that defines their international shipping options. Shipping options configure the high-level shipping settings that apply to orders, such as flat-rate or calculated shipping, any rate tables the seller wants to associate with the shipping services, plus other details (such as the shippingServices offered for domestic or international shipments).  # noqa: E501

        :param shipping_options: The shipping_options of this FulfillmentPolicyRequest.  # noqa: E501
        :type: list[ShippingOption]
        """

        self._shipping_options = shipping_options

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
        if issubclass(FulfillmentPolicyRequest, dict):
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
        if not isinstance(other, FulfillmentPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
