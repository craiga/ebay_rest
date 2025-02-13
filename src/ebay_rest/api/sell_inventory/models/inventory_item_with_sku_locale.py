# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InventoryItemWithSkuLocale(object):
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
        'availability': 'Availability',
        'condition': 'str',
        'condition_description': 'str',
        'locale': 'str',
        'package_weight_and_size': 'PackageWeightAndSize',
        'product': 'Product',
        'sku': 'str'
    }

    attribute_map = {
        'availability': 'availability',
        'condition': 'condition',
        'condition_description': 'conditionDescription',
        'locale': 'locale',
        'package_weight_and_size': 'packageWeightAndSize',
        'product': 'product',
        'sku': 'sku'
    }

    def __init__(self, availability=None, condition=None, condition_description=None, locale=None, package_weight_and_size=None, product=None, sku=None):  # noqa: E501
        """InventoryItemWithSkuLocale - a model defined in Swagger"""  # noqa: E501
        self._availability = None
        self._condition = None
        self._condition_description = None
        self._locale = None
        self._package_weight_and_size = None
        self._product = None
        self._sku = None
        self.discriminator = None
        if availability is not None:
            self.availability = availability
        if condition is not None:
            self.condition = condition
        if condition_description is not None:
            self.condition_description = condition_description
        if locale is not None:
            self.locale = locale
        if package_weight_and_size is not None:
            self.package_weight_and_size = package_weight_and_size
        if product is not None:
            self.product = product
        if sku is not None:
            self.sku = sku

    @property
    def availability(self):
        """Gets the availability of this InventoryItemWithSkuLocale.  # noqa: E501


        :return: The availability of this InventoryItemWithSkuLocale.  # noqa: E501
        :rtype: Availability
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this InventoryItemWithSkuLocale.


        :param availability: The availability of this InventoryItemWithSkuLocale.  # noqa: E501
        :type: Availability
        """

        self._availability = availability

    @property
    def condition(self):
        """Gets the condition of this InventoryItemWithSkuLocale.  # noqa: E501

        This enumeration value indicates the condition of the item. Supported item condition values will vary by eBay site and category. To see which item condition values that a particular eBay category supports, use the getItemConditionPolicies method of the Metadata API. This method returns condition ID values that map to the enumeration values defined in the ConditionEnum type. The Item condition ID and name values topic in the Selling Integration Guide has a table that maps condition ID values to ConditionEnum values. The getItemConditionPolicies call reference page has more information. A condition value is optional up until the seller is ready to publish an offer with the SKU, at which time it becomes required for most eBay categories. Note: The 'Manufacturer Refurbished' item condition is no longer a valid item condition on any eBay marketplace, and to reflect this change, the MANUFACTURER_REFURBISHED value is no longer applicable, and should not be used. With Version 1.13.0, the CERTIFIED_REFURBISHED enumeration value has been introduced, and CR-eligible sellers should make a note to start using CERTIFIED_REFURBISHED from this point forward. For the time being, if the MANUFACTURER_REFURBISHED enum is used for any of the SKUs in a bulkCreateOrReplaceInventoryItem method, it will be accepted but automatically converted by eBay to CERTIFIED_REFURBISHED. To list an item as 'Certified Refurbished', a seller must be pre-qualified by eBay for this feature. Any seller who is not eligible for this feature will be blocked if they try to create a new listing or revise an existing listing with this item condition. Any seller that is interested in eligibility requirements to list with 'Certified Refurbished' should see the Certified refurbished program page in Seller Center. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:ConditionEnum'>eBay API documentation</a>  # noqa: E501

        :return: The condition of this InventoryItemWithSkuLocale.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this InventoryItemWithSkuLocale.

        This enumeration value indicates the condition of the item. Supported item condition values will vary by eBay site and category. To see which item condition values that a particular eBay category supports, use the getItemConditionPolicies method of the Metadata API. This method returns condition ID values that map to the enumeration values defined in the ConditionEnum type. The Item condition ID and name values topic in the Selling Integration Guide has a table that maps condition ID values to ConditionEnum values. The getItemConditionPolicies call reference page has more information. A condition value is optional up until the seller is ready to publish an offer with the SKU, at which time it becomes required for most eBay categories. Note: The 'Manufacturer Refurbished' item condition is no longer a valid item condition on any eBay marketplace, and to reflect this change, the MANUFACTURER_REFURBISHED value is no longer applicable, and should not be used. With Version 1.13.0, the CERTIFIED_REFURBISHED enumeration value has been introduced, and CR-eligible sellers should make a note to start using CERTIFIED_REFURBISHED from this point forward. For the time being, if the MANUFACTURER_REFURBISHED enum is used for any of the SKUs in a bulkCreateOrReplaceInventoryItem method, it will be accepted but automatically converted by eBay to CERTIFIED_REFURBISHED. To list an item as 'Certified Refurbished', a seller must be pre-qualified by eBay for this feature. Any seller who is not eligible for this feature will be blocked if they try to create a new listing or revise an existing listing with this item condition. Any seller that is interested in eligibility requirements to list with 'Certified Refurbished' should see the Certified refurbished program page in Seller Center. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:ConditionEnum'>eBay API documentation</a>  # noqa: E501

        :param condition: The condition of this InventoryItemWithSkuLocale.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def condition_description(self):
        """Gets the condition_description of this InventoryItemWithSkuLocale.  # noqa: E501

        This string field is used by the seller to more clearly describe the condition of a used inventory item, or an inventory item whose condition value is not NEW, LIKE_NEW, NEW_OTHER, or NEW_WITH_DEFECTS. The conditionDescription field is available for all eBay categories. If the conditionDescription field is used with an item in one of the new conditions (mentioned in previous paragraph), eBay will simply ignore this field if included, and eBay will return a warning message to the user. This field should only be used to further clarify the condition of the used item. It should not be used for branding, promotions, shipping, returns, payment or other information unrelated to the condition of the used item. Make sure that the condition value, condition description, listing description, and the item's pictures do not contradict one another. This field is not always required, but is required if an inventory item is being updated and a condition description already exists for that inventory item. This field is returned in the getInventoryItem, bulkGetInventoryItem, and getInventoryItems calls if a condition description was provided for a used inventory item. Max Length: 1000.  # noqa: E501

        :return: The condition_description of this InventoryItemWithSkuLocale.  # noqa: E501
        :rtype: str
        """
        return self._condition_description

    @condition_description.setter
    def condition_description(self, condition_description):
        """Sets the condition_description of this InventoryItemWithSkuLocale.

        This string field is used by the seller to more clearly describe the condition of a used inventory item, or an inventory item whose condition value is not NEW, LIKE_NEW, NEW_OTHER, or NEW_WITH_DEFECTS. The conditionDescription field is available for all eBay categories. If the conditionDescription field is used with an item in one of the new conditions (mentioned in previous paragraph), eBay will simply ignore this field if included, and eBay will return a warning message to the user. This field should only be used to further clarify the condition of the used item. It should not be used for branding, promotions, shipping, returns, payment or other information unrelated to the condition of the used item. Make sure that the condition value, condition description, listing description, and the item's pictures do not contradict one another. This field is not always required, but is required if an inventory item is being updated and a condition description already exists for that inventory item. This field is returned in the getInventoryItem, bulkGetInventoryItem, and getInventoryItems calls if a condition description was provided for a used inventory item. Max Length: 1000.  # noqa: E501

        :param condition_description: The condition_description of this InventoryItemWithSkuLocale.  # noqa: E501
        :type: str
        """

        self._condition_description = condition_description

    @property
    def locale(self):
        """Gets the locale of this InventoryItemWithSkuLocale.  # noqa: E501

        This field is for future use only. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:LocaleEnum'>eBay API documentation</a>  # noqa: E501

        :return: The locale of this InventoryItemWithSkuLocale.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this InventoryItemWithSkuLocale.

        This field is for future use only. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:LocaleEnum'>eBay API documentation</a>  # noqa: E501

        :param locale: The locale of this InventoryItemWithSkuLocale.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def package_weight_and_size(self):
        """Gets the package_weight_and_size of this InventoryItemWithSkuLocale.  # noqa: E501


        :return: The package_weight_and_size of this InventoryItemWithSkuLocale.  # noqa: E501
        :rtype: PackageWeightAndSize
        """
        return self._package_weight_and_size

    @package_weight_and_size.setter
    def package_weight_and_size(self, package_weight_and_size):
        """Sets the package_weight_and_size of this InventoryItemWithSkuLocale.


        :param package_weight_and_size: The package_weight_and_size of this InventoryItemWithSkuLocale.  # noqa: E501
        :type: PackageWeightAndSize
        """

        self._package_weight_and_size = package_weight_and_size

    @property
    def product(self):
        """Gets the product of this InventoryItemWithSkuLocale.  # noqa: E501


        :return: The product of this InventoryItemWithSkuLocale.  # noqa: E501
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this InventoryItemWithSkuLocale.


        :param product: The product of this InventoryItemWithSkuLocale.  # noqa: E501
        :type: Product
        """

        self._product = product

    @property
    def sku(self):
        """Gets the sku of this InventoryItemWithSkuLocale.  # noqa: E501

        This is the seller-defined SKU value of the product that will be listed on the eBay site (specified in the marketplaceId field). Only one offer (in unpublished or published state) may exist for each sku/marketplaceId/format combination. This field is required. Max Length: 50  # noqa: E501

        :return: The sku of this InventoryItemWithSkuLocale.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this InventoryItemWithSkuLocale.

        This is the seller-defined SKU value of the product that will be listed on the eBay site (specified in the marketplaceId field). Only one offer (in unpublished or published state) may exist for each sku/marketplaceId/format combination. This field is required. Max Length: 50  # noqa: E501

        :param sku: The sku of this InventoryItemWithSkuLocale.  # noqa: E501
        :type: str
        """

        self._sku = sku

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
        if issubclass(InventoryItemWithSkuLocale, dict):
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
        if not isinstance(other, InventoryItemWithSkuLocale):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
