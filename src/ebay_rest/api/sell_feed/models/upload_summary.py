# coding: utf-8

"""
    Feed API

    <p>The <strong>Feed API</strong> lets sellers upload input files, download reports and files including their status, filter reports using URI parameters, and retrieve customer service metrics task details.</p>  # noqa: E501

    OpenAPI spec version: v1.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UploadSummary(object):
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
        'failure_count': 'int',
        'success_count': 'int'
    }

    attribute_map = {
        'failure_count': 'failureCount',
        'success_count': 'successCount'
    }

    def __init__(self, failure_count=None, success_count=None):  # noqa: E501
        """UploadSummary - a model defined in Swagger"""  # noqa: E501
        self._failure_count = None
        self._success_count = None
        self.discriminator = None
        if failure_count is not None:
            self.failure_count = failure_count
        if success_count is not None:
            self.success_count = success_count

    @property
    def failure_count(self):
        """Gets the failure_count of this UploadSummary.  # noqa: E501

        The number of records, such as the number of listings created or the number of pictures uploaded to a listing, that failed to process during the upload feed. Check the response file and correct any issues mentioned. If the feed fails before processing, no response file is provided. In this case check the REST output response.  # noqa: E501

        :return: The failure_count of this UploadSummary.  # noqa: E501
        :rtype: int
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        """Sets the failure_count of this UploadSummary.

        The number of records, such as the number of listings created or the number of pictures uploaded to a listing, that failed to process during the upload feed. Check the response file and correct any issues mentioned. If the feed fails before processing, no response file is provided. In this case check the REST output response.  # noqa: E501

        :param failure_count: The failure_count of this UploadSummary.  # noqa: E501
        :type: int
        """

        self._failure_count = failure_count

    @property
    def success_count(self):
        """Gets the success_count of this UploadSummary.  # noqa: E501

        The number of records that were successfully processed during the upload feed.  # noqa: E501

        :return: The success_count of this UploadSummary.  # noqa: E501
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this UploadSummary.

        The number of records that were successfully processed during the upload feed.  # noqa: E501

        :param success_count: The success_count of this UploadSummary.  # noqa: E501
        :type: int
        """

        self._success_count = success_count

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
        if issubclass(UploadSummary, dict):
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
        if not isinstance(other, UploadSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
