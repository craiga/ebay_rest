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

class SetReturnPolicyResponse(object):
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
        'extended_holiday_returns_offered': 'bool',
        'international_override': 'InternationalReturnOverrideType',
        'marketplace_id': 'str',
        'name': 'str',
        'refund_method': 'str',
        'restocking_fee_percentage': 'str',
        'return_instructions': 'str',
        'return_method': 'str',
        'return_period': 'TimeDuration',
        'return_policy_id': 'str',
        'return_shipping_cost_payer': 'str',
        'returns_accepted': 'bool',
        'warnings': 'list[Error]'
    }

    attribute_map = {
        'category_types': 'categoryTypes',
        'description': 'description',
        'extended_holiday_returns_offered': 'extendedHolidayReturnsOffered',
        'international_override': 'internationalOverride',
        'marketplace_id': 'marketplaceId',
        'name': 'name',
        'refund_method': 'refundMethod',
        'restocking_fee_percentage': 'restockingFeePercentage',
        'return_instructions': 'returnInstructions',
        'return_method': 'returnMethod',
        'return_period': 'returnPeriod',
        'return_policy_id': 'returnPolicyId',
        'return_shipping_cost_payer': 'returnShippingCostPayer',
        'returns_accepted': 'returnsAccepted',
        'warnings': 'warnings'
    }

    def __init__(self, category_types=None, description=None, extended_holiday_returns_offered=None, international_override=None, marketplace_id=None, name=None, refund_method=None, restocking_fee_percentage=None, return_instructions=None, return_method=None, return_period=None, return_policy_id=None, return_shipping_cost_payer=None, returns_accepted=None, warnings=None):  # noqa: E501
        """SetReturnPolicyResponse - a model defined in Swagger"""  # noqa: E501
        self._category_types = None
        self._description = None
        self._extended_holiday_returns_offered = None
        self._international_override = None
        self._marketplace_id = None
        self._name = None
        self._refund_method = None
        self._restocking_fee_percentage = None
        self._return_instructions = None
        self._return_method = None
        self._return_period = None
        self._return_policy_id = None
        self._return_shipping_cost_payer = None
        self._returns_accepted = None
        self._warnings = None
        self.discriminator = None
        if category_types is not None:
            self.category_types = category_types
        if description is not None:
            self.description = description
        if extended_holiday_returns_offered is not None:
            self.extended_holiday_returns_offered = extended_holiday_returns_offered
        if international_override is not None:
            self.international_override = international_override
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if name is not None:
            self.name = name
        if refund_method is not None:
            self.refund_method = refund_method
        if restocking_fee_percentage is not None:
            self.restocking_fee_percentage = restocking_fee_percentage
        if return_instructions is not None:
            self.return_instructions = return_instructions
        if return_method is not None:
            self.return_method = return_method
        if return_period is not None:
            self.return_period = return_period
        if return_policy_id is not None:
            self.return_policy_id = return_policy_id
        if return_shipping_cost_payer is not None:
            self.return_shipping_cost_payer = return_shipping_cost_payer
        if returns_accepted is not None:
            self.returns_accepted = returns_accepted
        if warnings is not None:
            self.warnings = warnings

    @property
    def category_types(self):
        """Gets the category_types of this SetReturnPolicyResponse.  # noqa: E501

        For return policies, this field always returns ALL_EXCLUDING_MOTORS_VEHICLES (returns on motor vehicles are not processed through eBay flows.) Default: ALL_EXCLUDING_MOTORS_VEHICLES (for return policies only)  # noqa: E501

        :return: The category_types of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: list[CategoryType]
        """
        return self._category_types

    @category_types.setter
    def category_types(self, category_types):
        """Sets the category_types of this SetReturnPolicyResponse.

        For return policies, this field always returns ALL_EXCLUDING_MOTORS_VEHICLES (returns on motor vehicles are not processed through eBay flows.) Default: ALL_EXCLUDING_MOTORS_VEHICLES (for return policies only)  # noqa: E501

        :param category_types: The category_types of this SetReturnPolicyResponse.  # noqa: E501
        :type: list[CategoryType]
        """

        self._category_types = category_types

    @property
    def description(self):
        """Gets the description of this SetReturnPolicyResponse.  # noqa: E501

        An optional seller-defined description of the return policy for internal use (this value is not displayed to end users).  # noqa: E501

        :return: The description of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SetReturnPolicyResponse.

        An optional seller-defined description of the return policy for internal use (this value is not displayed to end users).  # noqa: E501

        :param description: The description of this SetReturnPolicyResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def extended_holiday_returns_offered(self):
        """Gets the extended_holiday_returns_offered of this SetReturnPolicyResponse.  # noqa: E501

        Important! This field has been deprecated as of version 1.2.0, released on May 31, 2018. Any value supplied in this field is ignored, it is neither read nor returned. If set to true, the seller offers an Extended Holiday Returns policy for their listings. IMPORTANT: Extended Holiday Returns is a seasonally available feature that is offered on some eBay marketplaces. To see if the feature is enabled in any given year, check the eBay Seller Center Returns on eBay page of before the holiday season begins.  # noqa: E501

        :return: The extended_holiday_returns_offered of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._extended_holiday_returns_offered

    @extended_holiday_returns_offered.setter
    def extended_holiday_returns_offered(self, extended_holiday_returns_offered):
        """Sets the extended_holiday_returns_offered of this SetReturnPolicyResponse.

        Important! This field has been deprecated as of version 1.2.0, released on May 31, 2018. Any value supplied in this field is ignored, it is neither read nor returned. If set to true, the seller offers an Extended Holiday Returns policy for their listings. IMPORTANT: Extended Holiday Returns is a seasonally available feature that is offered on some eBay marketplaces. To see if the feature is enabled in any given year, check the eBay Seller Center Returns on eBay page of before the holiday season begins.  # noqa: E501

        :param extended_holiday_returns_offered: The extended_holiday_returns_offered of this SetReturnPolicyResponse.  # noqa: E501
        :type: bool
        """

        self._extended_holiday_returns_offered = extended_holiday_returns_offered

    @property
    def international_override(self):
        """Gets the international_override of this SetReturnPolicyResponse.  # noqa: E501


        :return: The international_override of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: InternationalReturnOverrideType
        """
        return self._international_override

    @international_override.setter
    def international_override(self, international_override):
        """Sets the international_override of this SetReturnPolicyResponse.


        :param international_override: The international_override of this SetReturnPolicyResponse.  # noqa: E501
        :type: InternationalReturnOverrideType
        """

        self._international_override = international_override

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this SetReturnPolicyResponse.  # noqa: E501

        The ID of the eBay marketplace to which this return policy applies. If this value is not specified, value defaults to the seller's eBay registration site. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this SetReturnPolicyResponse.

        The ID of the eBay marketplace to which this return policy applies. If this value is not specified, value defaults to the seller's eBay registration site. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this SetReturnPolicyResponse.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def name(self):
        """Gets the name of this SetReturnPolicyResponse.  # noqa: E501

        A user-defined name for this return policy. Names must be unique for policies assigned to the same marketplace. Max length: 64  # noqa: E501

        :return: The name of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SetReturnPolicyResponse.

        A user-defined name for this return policy. Names must be unique for policies assigned to the same marketplace. Max length: 64  # noqa: E501

        :param name: The name of this SetReturnPolicyResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def refund_method(self):
        """Gets the refund_method of this SetReturnPolicyResponse.  # noqa: E501

        Important! This field has been deprecated as of version 1.2.0, released on May 31, 2018. Any value other than MONEY_BACK will be treated as MONEY_BACK (although for a period of time, eBay will store and return the legacy values to preserve backwards compatibility). Indicates the method the seller uses to compensate the buyer for returned items. The return method specified applies only to remorse returns. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:RefundMethodEnum'>eBay API documentation</a>  # noqa: E501

        :return: The refund_method of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._refund_method

    @refund_method.setter
    def refund_method(self, refund_method):
        """Sets the refund_method of this SetReturnPolicyResponse.

        Important! This field has been deprecated as of version 1.2.0, released on May 31, 2018. Any value other than MONEY_BACK will be treated as MONEY_BACK (although for a period of time, eBay will store and return the legacy values to preserve backwards compatibility). Indicates the method the seller uses to compensate the buyer for returned items. The return method specified applies only to remorse returns. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:RefundMethodEnum'>eBay API documentation</a>  # noqa: E501

        :param refund_method: The refund_method of this SetReturnPolicyResponse.  # noqa: E501
        :type: str
        """

        self._refund_method = refund_method

    @property
    def restocking_fee_percentage(self):
        """Gets the restocking_fee_percentage of this SetReturnPolicyResponse.  # noqa: E501

        Important! This field has been deprecated as of version 1.2.0, released on May 31, 2018. Any value supplied in this field is ignored, it is neither read nor returned. Optionally set by the seller, the percentage charged if the seller charges buyers a a restocking fee when items are returned due to buyer remorse and/or a purchasing mistake. The total amount charged to the buyer is the cost of the item multiplied by the percentage indicated in this field.  # noqa: E501

        :return: The restocking_fee_percentage of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._restocking_fee_percentage

    @restocking_fee_percentage.setter
    def restocking_fee_percentage(self, restocking_fee_percentage):
        """Sets the restocking_fee_percentage of this SetReturnPolicyResponse.

        Important! This field has been deprecated as of version 1.2.0, released on May 31, 2018. Any value supplied in this field is ignored, it is neither read nor returned. Optionally set by the seller, the percentage charged if the seller charges buyers a a restocking fee when items are returned due to buyer remorse and/or a purchasing mistake. The total amount charged to the buyer is the cost of the item multiplied by the percentage indicated in this field.  # noqa: E501

        :param restocking_fee_percentage: The restocking_fee_percentage of this SetReturnPolicyResponse.  # noqa: E501
        :type: str
        """

        self._restocking_fee_percentage = restocking_fee_percentage

    @property
    def return_instructions(self):
        """Gets the return_instructions of this SetReturnPolicyResponse.  # noqa: E501

        This field contains the seller's detailed explanation for their return policy and is displayed in the Return Policy section of the View Item page. This field is valid in only the following marketplaces (the field is otherwise ignored): Germany (DE) Spain (ES) France (FR) Italy (IT)  # noqa: E501

        :return: The return_instructions of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_instructions

    @return_instructions.setter
    def return_instructions(self, return_instructions):
        """Sets the return_instructions of this SetReturnPolicyResponse.

        This field contains the seller's detailed explanation for their return policy and is displayed in the Return Policy section of the View Item page. This field is valid in only the following marketplaces (the field is otherwise ignored): Germany (DE) Spain (ES) France (FR) Italy (IT)  # noqa: E501

        :param return_instructions: The return_instructions of this SetReturnPolicyResponse.  # noqa: E501
        :type: str
        """

        self._return_instructions = return_instructions

    @property
    def return_method(self):
        """Gets the return_method of this SetReturnPolicyResponse.  # noqa: E501

        This field indicates the method in which the seller handles non-money back return requests for remorse returns. This field is valid in only the US marketplace and the only valid value is REPLACEMENT. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnMethodEnum'>eBay API documentation</a>  # noqa: E501

        :return: The return_method of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_method

    @return_method.setter
    def return_method(self, return_method):
        """Sets the return_method of this SetReturnPolicyResponse.

        This field indicates the method in which the seller handles non-money back return requests for remorse returns. This field is valid in only the US marketplace and the only valid value is REPLACEMENT. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnMethodEnum'>eBay API documentation</a>  # noqa: E501

        :param return_method: The return_method of this SetReturnPolicyResponse.  # noqa: E501
        :type: str
        """

        self._return_method = return_method

    @property
    def return_period(self):
        """Gets the return_period of this SetReturnPolicyResponse.  # noqa: E501


        :return: The return_period of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: TimeDuration
        """
        return self._return_period

    @return_period.setter
    def return_period(self, return_period):
        """Sets the return_period of this SetReturnPolicyResponse.


        :param return_period: The return_period of this SetReturnPolicyResponse.  # noqa: E501
        :type: TimeDuration
        """

        self._return_period = return_period

    @property
    def return_policy_id(self):
        """Gets the return_policy_id of this SetReturnPolicyResponse.  # noqa: E501

        A unique eBay-assigned ID for a return policy. This ID is generated when the policy is created.  # noqa: E501

        :return: The return_policy_id of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_policy_id

    @return_policy_id.setter
    def return_policy_id(self, return_policy_id):
        """Sets the return_policy_id of this SetReturnPolicyResponse.

        A unique eBay-assigned ID for a return policy. This ID is generated when the policy is created.  # noqa: E501

        :param return_policy_id: The return_policy_id of this SetReturnPolicyResponse.  # noqa: E501
        :type: str
        """

        self._return_policy_id = return_policy_id

    @property
    def return_shipping_cost_payer(self):
        """Gets the return_shipping_cost_payer of this SetReturnPolicyResponse.  # noqa: E501

        This field indicates who is responsible for paying for the shipping charges for returned items. The field can be set to either BUYER or SELLER. Depending on the return policy and specifics of the return, either the buyer or the seller can be responsible for the return shipping costs. Note that the seller is always responsible for return shipping costs for SNAD-related issues. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnShippingCostPayerEnum'>eBay API documentation</a>  # noqa: E501

        :return: The return_shipping_cost_payer of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_shipping_cost_payer

    @return_shipping_cost_payer.setter
    def return_shipping_cost_payer(self, return_shipping_cost_payer):
        """Sets the return_shipping_cost_payer of this SetReturnPolicyResponse.

        This field indicates who is responsible for paying for the shipping charges for returned items. The field can be set to either BUYER or SELLER. Depending on the return policy and specifics of the return, either the buyer or the seller can be responsible for the return shipping costs. Note that the seller is always responsible for return shipping costs for SNAD-related issues. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ReturnShippingCostPayerEnum'>eBay API documentation</a>  # noqa: E501

        :param return_shipping_cost_payer: The return_shipping_cost_payer of this SetReturnPolicyResponse.  # noqa: E501
        :type: str
        """

        self._return_shipping_cost_payer = return_shipping_cost_payer

    @property
    def returns_accepted(self):
        """Gets the returns_accepted of this SetReturnPolicyResponse.  # noqa: E501

        If set to true, the seller accepts returns. If set to false, this field indicates that the seller does not accept returns.  # noqa: E501

        :return: The returns_accepted of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._returns_accepted

    @returns_accepted.setter
    def returns_accepted(self, returns_accepted):
        """Sets the returns_accepted of this SetReturnPolicyResponse.

        If set to true, the seller accepts returns. If set to false, this field indicates that the seller does not accept returns.  # noqa: E501

        :param returns_accepted: The returns_accepted of this SetReturnPolicyResponse.  # noqa: E501
        :type: bool
        """

        self._returns_accepted = returns_accepted

    @property
    def warnings(self):
        """Gets the warnings of this SetReturnPolicyResponse.  # noqa: E501

        A list of warnings related to request. This field normally returns empty, which indicates the request did not generate any warnings.  # noqa: E501

        :return: The warnings of this SetReturnPolicyResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this SetReturnPolicyResponse.

        A list of warnings related to request. This field normally returns empty, which indicates the request did not generate any warnings.  # noqa: E501

        :param warnings: The warnings of this SetReturnPolicyResponse.  # noqa: E501
        :type: list[Error]
        """

        self._warnings = warnings

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
        if issubclass(SetReturnPolicyResponse, dict):
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
        if not isinstance(other, SetReturnPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
