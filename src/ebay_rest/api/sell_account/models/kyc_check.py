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

class KycCheck(object):
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
        'alert': 'str',
        'data_required': 'str',
        'detail_message': 'str',
        'due_date': 'str',
        'remedy_url': 'str'
    }

    attribute_map = {
        'alert': 'alert',
        'data_required': 'dataRequired',
        'detail_message': 'detailMessage',
        'due_date': 'dueDate',
        'remedy_url': 'remedyUrl'
    }

    def __init__(self, alert=None, data_required=None, detail_message=None, due_date=None, remedy_url=None):  # noqa: E501
        """KycCheck - a model defined in Swagger"""  # noqa: E501
        self._alert = None
        self._data_required = None
        self._detail_message = None
        self._due_date = None
        self._remedy_url = None
        self.discriminator = None
        if alert is not None:
            self.alert = alert
        if data_required is not None:
            self.data_required = data_required
        if detail_message is not None:
            self.detail_message = detail_message
        if due_date is not None:
            self.due_date = due_date
        if remedy_url is not None:
            self.remedy_url = remedy_url

    @property
    def alert(self):
        """Gets the alert of this KycCheck.  # noqa: E501

        This field gives a short summary of what is required from the seller. An example might be, 'Upload bank document now.'. The detailMessage field will often provide more details on what is required of the seller.  # noqa: E501

        :return: The alert of this KycCheck.  # noqa: E501
        :rtype: str
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        """Sets the alert of this KycCheck.

        This field gives a short summary of what is required from the seller. An example might be, 'Upload bank document now.'. The detailMessage field will often provide more details on what is required of the seller.  # noqa: E501

        :param alert: The alert of this KycCheck.  # noqa: E501
        :type: str
        """

        self._alert = alert

    @property
    def data_required(self):
        """Gets the data_required of this KycCheck.  # noqa: E501

        The enumeration value returned in this field categorizes the type of details needed for the KYC check. More information about the check is shown in the detailMessage and other applicable, corresponding fields. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/kyc:DetailsType'>eBay API documentation</a>  # noqa: E501

        :return: The data_required of this KycCheck.  # noqa: E501
        :rtype: str
        """
        return self._data_required

    @data_required.setter
    def data_required(self, data_required):
        """Sets the data_required of this KycCheck.

        The enumeration value returned in this field categorizes the type of details needed for the KYC check. More information about the check is shown in the detailMessage and other applicable, corresponding fields. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/kyc:DetailsType'>eBay API documentation</a>  # noqa: E501

        :param data_required: The data_required of this KycCheck.  # noqa: E501
        :type: str
        """

        self._data_required = data_required

    @property
    def detail_message(self):
        """Gets the detail_message of this KycCheck.  # noqa: E501

        This field gives a detailed message about what is required from the seller. An example might be, 'Please upload a bank document by 2020-08-01 to get your account back in good standing.'.  # noqa: E501

        :return: The detail_message of this KycCheck.  # noqa: E501
        :rtype: str
        """
        return self._detail_message

    @detail_message.setter
    def detail_message(self, detail_message):
        """Sets the detail_message of this KycCheck.

        This field gives a detailed message about what is required from the seller. An example might be, 'Please upload a bank document by 2020-08-01 to get your account back in good standing.'.  # noqa: E501

        :param detail_message: The detail_message of this KycCheck.  # noqa: E501
        :type: str
        """

        self._detail_message = detail_message

    @property
    def due_date(self):
        """Gets the due_date of this KycCheck.  # noqa: E501

        The timestamp in this field indicates the date by which the seller should resolve the KYC requirement. The timestamp in this field uses the UTC date and time format described in the ISO 8601 Standard. See below for this format and an example: MM-DD-YYYY HH:MM:SS 06-05-2020 10:34:18  # noqa: E501

        :return: The due_date of this KycCheck.  # noqa: E501
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this KycCheck.

        The timestamp in this field indicates the date by which the seller should resolve the KYC requirement. The timestamp in this field uses the UTC date and time format described in the ISO 8601 Standard. See below for this format and an example: MM-DD-YYYY HH:MM:SS 06-05-2020 10:34:18  # noqa: E501

        :param due_date: The due_date of this KycCheck.  # noqa: E501
        :type: str
        """

        self._due_date = due_date

    @property
    def remedy_url(self):
        """Gets the remedy_url of this KycCheck.  # noqa: E501

        If applicable and available, a URL will be returned in this field, and the link will take the seller to an eBay page where they can provide the requested information.  # noqa: E501

        :return: The remedy_url of this KycCheck.  # noqa: E501
        :rtype: str
        """
        return self._remedy_url

    @remedy_url.setter
    def remedy_url(self, remedy_url):
        """Sets the remedy_url of this KycCheck.

        If applicable and available, a URL will be returned in this field, and the link will take the seller to an eBay page where they can provide the requested information.  # noqa: E501

        :param remedy_url: The remedy_url of this KycCheck.  # noqa: E501
        :type: str
        """

        self._remedy_url = remedy_url

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
        if issubclass(KycCheck, dict):
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
        if not isinstance(other, KycCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
