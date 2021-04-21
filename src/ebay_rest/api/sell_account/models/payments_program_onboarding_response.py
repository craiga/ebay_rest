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

class PaymentsProgramOnboardingResponse(object):
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
        'onboarding_status': 'str',
        'steps': 'list[PaymentsProgramOnboardingSteps]'
    }

    attribute_map = {
        'onboarding_status': 'onboardingStatus',
        'steps': 'steps'
    }

    def __init__(self, onboarding_status=None, steps=None):  # noqa: E501
        """PaymentsProgramOnboardingResponse - a model defined in Swagger"""  # noqa: E501
        self._onboarding_status = None
        self._steps = None
        self.discriminator = None
        if onboarding_status is not None:
            self.onboarding_status = onboarding_status
        if steps is not None:
            self.steps = steps

    @property
    def onboarding_status(self):
        """Gets the onboarding_status of this PaymentsProgramOnboardingResponse.  # noqa: E501

        This enumeration value indicates the eligibility of payment onboarding for the registered site. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:PaymentsProgramOnboardingStatus'>eBay API documentation</a>  # noqa: E501

        :return: The onboarding_status of this PaymentsProgramOnboardingResponse.  # noqa: E501
        :rtype: str
        """
        return self._onboarding_status

    @onboarding_status.setter
    def onboarding_status(self, onboarding_status):
        """Sets the onboarding_status of this PaymentsProgramOnboardingResponse.

        This enumeration value indicates the eligibility of payment onboarding for the registered site. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:PaymentsProgramOnboardingStatus'>eBay API documentation</a>  # noqa: E501

        :param onboarding_status: The onboarding_status of this PaymentsProgramOnboardingResponse.  # noqa: E501
        :type: str
        """

        self._onboarding_status = onboarding_status

    @property
    def steps(self):
        """Gets the steps of this PaymentsProgramOnboardingResponse.  # noqa: E501

        An array of the active process steps for payment onboarding and the status of each step. This array includes the step name, step status, and a webUrl to the IN_PROGRESS step. The step names are returned in sequential order.  # noqa: E501

        :return: The steps of this PaymentsProgramOnboardingResponse.  # noqa: E501
        :rtype: list[PaymentsProgramOnboardingSteps]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this PaymentsProgramOnboardingResponse.

        An array of the active process steps for payment onboarding and the status of each step. This array includes the step name, step status, and a webUrl to the IN_PROGRESS step. The step names are returned in sequential order.  # noqa: E501

        :param steps: The steps of this PaymentsProgramOnboardingResponse.  # noqa: E501
        :type: list[PaymentsProgramOnboardingSteps]
        """

        self._steps = steps

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
        if issubclass(PaymentsProgramOnboardingResponse, dict):
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
        if not isinstance(other, PaymentsProgramOnboardingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
