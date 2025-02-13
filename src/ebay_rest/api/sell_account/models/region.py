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

class Region(object):
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
        'region_name': 'str',
        'region_type': 'str'
    }

    attribute_map = {
        'region_name': 'regionName',
        'region_type': 'regionType'
    }

    def __init__(self, region_name=None, region_type=None):  # noqa: E501
        """Region - a model defined in Swagger"""  # noqa: E501
        self._region_name = None
        self._region_type = None
        self.discriminator = None
        if region_name is not None:
            self.region_name = region_name
        if region_type is not None:
            self.region_type = region_type

    @property
    def region_name(self):
        """Gets the region_name of this Region.  # noqa: E501

        A string that indicates the name of a region, as defined by eBay. A &quot;region&quot; can be either a 'world region' (e.g., the &quot;Middle East&quot; or &quot;Southeast Asia&quot;) or a country, as represented with a two-letter country code. Use GeteBayDetails to get the values accepted by this field. The values that you're allowed to use for a specific regionName field depend on the context in which you are setting the value. For details on how to set the values for this field, see The shipToLocations container.  # noqa: E501

        :return: The region_name of this Region.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this Region.

        A string that indicates the name of a region, as defined by eBay. A &quot;region&quot; can be either a 'world region' (e.g., the &quot;Middle East&quot; or &quot;Southeast Asia&quot;) or a country, as represented with a two-letter country code. Use GeteBayDetails to get the values accepted by this field. The values that you're allowed to use for a specific regionName field depend on the context in which you are setting the value. For details on how to set the values for this field, see The shipToLocations container.  # noqa: E501

        :param region_name: The region_name of this Region.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

    @property
    def region_type(self):
        """Gets the region_type of this Region.  # noqa: E501

        Reserved for future use. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:RegionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The region_type of this Region.  # noqa: E501
        :rtype: str
        """
        return self._region_type

    @region_type.setter
    def region_type(self, region_type):
        """Sets the region_type of this Region.

        Reserved for future use. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:RegionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param region_type: The region_type of this Region.  # noqa: E501
        :type: str
        """

        self._region_type = region_type

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
        if issubclass(Region, dict):
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
        if not isinstance(other, Region):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
