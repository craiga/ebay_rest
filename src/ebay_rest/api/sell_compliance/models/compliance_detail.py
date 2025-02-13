# coding: utf-8

"""
    Compliance API

    Service for providing information to sellers about their listings being non-compliant, or at risk for becoming non-compliant, against eBay listing policies.  # noqa: E501

    OpenAPI spec version: 1.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ComplianceDetail(object):
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
        'compliance_state': 'str',
        'corrective_recommendations': 'CorrectiveRecommendations',
        'message': 'str',
        'reason_code': 'str',
        'variation': 'VariationDetails',
        'violation_data': 'list[NameValueList]'
    }

    attribute_map = {
        'compliance_state': 'complianceState',
        'corrective_recommendations': 'correctiveRecommendations',
        'message': 'message',
        'reason_code': 'reasonCode',
        'variation': 'variation',
        'violation_data': 'violationData'
    }

    def __init__(self, compliance_state=None, corrective_recommendations=None, message=None, reason_code=None, variation=None, violation_data=None):  # noqa: E501
        """ComplianceDetail - a model defined in Swagger"""  # noqa: E501
        self._compliance_state = None
        self._corrective_recommendations = None
        self._message = None
        self._reason_code = None
        self._variation = None
        self._violation_data = None
        self.discriminator = None
        if compliance_state is not None:
            self.compliance_state = compliance_state
        if corrective_recommendations is not None:
            self.corrective_recommendations = corrective_recommendations
        if message is not None:
            self.message = message
        if reason_code is not None:
            self.reason_code = reason_code
        if variation is not None:
            self.variation = variation
        if violation_data is not None:
            self.violation_data = violation_data

    @property
    def compliance_state(self):
        """Gets the compliance_state of this ComplianceDetail.  # noqa: E501

        The enumeration value returned in this field indicates if the listing violation is considered to be OUT_OF_COMPLIANCE with an eBay listing policy, or the listing is considered to be AT_RISK of becoming non-compliant against an eBay listing policy. Generally, OUT_OF_COMPLIANCE policy violations can prevent the seller from revising a listing until the underlying violation(s) can be remedied. When the compliance state is AT_RISK, the seller is not blocked from revising the listing, but the seller should correct the violation to prevent the listing from being blocked for revisions in the future. Note: This field is returned for most violations, but not all. In the case that this field is not returned, it can be assumed that the state of the listing violation is OUT_OF_COMPLIANCE. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/compliance/types/com:ComplianceStateEnum'>eBay API documentation</a>  # noqa: E501

        :return: The compliance_state of this ComplianceDetail.  # noqa: E501
        :rtype: str
        """
        return self._compliance_state

    @compliance_state.setter
    def compliance_state(self, compliance_state):
        """Sets the compliance_state of this ComplianceDetail.

        The enumeration value returned in this field indicates if the listing violation is considered to be OUT_OF_COMPLIANCE with an eBay listing policy, or the listing is considered to be AT_RISK of becoming non-compliant against an eBay listing policy. Generally, OUT_OF_COMPLIANCE policy violations can prevent the seller from revising a listing until the underlying violation(s) can be remedied. When the compliance state is AT_RISK, the seller is not blocked from revising the listing, but the seller should correct the violation to prevent the listing from being blocked for revisions in the future. Note: This field is returned for most violations, but not all. In the case that this field is not returned, it can be assumed that the state of the listing violation is OUT_OF_COMPLIANCE. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/compliance/types/com:ComplianceStateEnum'>eBay API documentation</a>  # noqa: E501

        :param compliance_state: The compliance_state of this ComplianceDetail.  # noqa: E501
        :type: str
        """

        self._compliance_state = compliance_state

    @property
    def corrective_recommendations(self):
        """Gets the corrective_recommendations of this ComplianceDetail.  # noqa: E501


        :return: The corrective_recommendations of this ComplianceDetail.  # noqa: E501
        :rtype: CorrectiveRecommendations
        """
        return self._corrective_recommendations

    @corrective_recommendations.setter
    def corrective_recommendations(self, corrective_recommendations):
        """Sets the corrective_recommendations of this ComplianceDetail.


        :param corrective_recommendations: The corrective_recommendations of this ComplianceDetail.  # noqa: E501
        :type: CorrectiveRecommendations
        """

        self._corrective_recommendations = corrective_recommendations

    @property
    def message(self):
        """Gets the message of this ComplianceDetail.  # noqa: E501

        This field provides a textual summary of the listing violation. A message field is returned for each listing violation. This message will vary widely based on the compliance type and corresponding reason code.  # noqa: E501

        :return: The message of this ComplianceDetail.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ComplianceDetail.

        This field provides a textual summary of the listing violation. A message field is returned for each listing violation. This message will vary widely based on the compliance type and corresponding reason code.  # noqa: E501

        :param message: The message of this ComplianceDetail.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def reason_code(self):
        """Gets the reason_code of this ComplianceDetail.  # noqa: E501

        This value states the nature of the listing violation. A reasonCode value is returned for each listing violation, and each compliance type can have several reason codes and related messages. The reasonCode values vary by compliance type. The reason codes for each compliance type are summarized below. Aspects adoption The reason codes for ASPECTS_ADOPTION compliance indicate that for the given violation, aspects listed in the violationData container are either missing from the listing or they have invalid values. The reason codes specify whether the violation is for required aspects, recommended (preferred) aspects, or soon to be required aspects. MISSING_OR_INVALID_REQUIRED_ASPECTS MISSING_OR_INVALID_PREFERRED_ASPECTS MISSING_OR_INVALID_SOON_TO_BE_REQUIRED_ASPECTS HTTPS The reason codes for HTTPS compliance identify where in the listing the violation occurs. For HTTPS policy violations, the seller will just need to remove the HTTP link (or update to HTTPS) from the listing details or product details: NON_SECURE_HTTP_LINK_IN_LISTING NON_SECURE_HTTP_LINK_IN_PRODUCT Non-eBay links The reason codes for OUTSIDE_EBAY_BUYING_AND_SELLING compliance identify the specific type of data (e.g., telephone number) that violated the policy. For each of these violations, the seller will just need to revise the listing, removing this information: UNAPPROVED_DOMAIN_WEBLINK_IN_LISTING PHONE_NUMBER_IN_LISTING EMAIL_ADDRESS_IN_LISTING Product adoption Product Adoption is not enforced at this time. Product adoption conformance Product Adoption is not enforced at this time. Returns policy The only RETURNS_POLICY reason code is UNSUPPORTED_RETURNS_PERIOD. The seller will have to revise their listing (or return business policy) with a supported return period for the site and category. The GetCategoryFeatures call of the Trading API can be used to verify the supported return periods for a particular category. For most eBay categories, the minimum return period that can be stated in a Returns Policy is 14 days for domestic and international sales, but some categories require a minimum 30-day return period.  # noqa: E501

        :return: The reason_code of this ComplianceDetail.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this ComplianceDetail.

        This value states the nature of the listing violation. A reasonCode value is returned for each listing violation, and each compliance type can have several reason codes and related messages. The reasonCode values vary by compliance type. The reason codes for each compliance type are summarized below. Aspects adoption The reason codes for ASPECTS_ADOPTION compliance indicate that for the given violation, aspects listed in the violationData container are either missing from the listing or they have invalid values. The reason codes specify whether the violation is for required aspects, recommended (preferred) aspects, or soon to be required aspects. MISSING_OR_INVALID_REQUIRED_ASPECTS MISSING_OR_INVALID_PREFERRED_ASPECTS MISSING_OR_INVALID_SOON_TO_BE_REQUIRED_ASPECTS HTTPS The reason codes for HTTPS compliance identify where in the listing the violation occurs. For HTTPS policy violations, the seller will just need to remove the HTTP link (or update to HTTPS) from the listing details or product details: NON_SECURE_HTTP_LINK_IN_LISTING NON_SECURE_HTTP_LINK_IN_PRODUCT Non-eBay links The reason codes for OUTSIDE_EBAY_BUYING_AND_SELLING compliance identify the specific type of data (e.g., telephone number) that violated the policy. For each of these violations, the seller will just need to revise the listing, removing this information: UNAPPROVED_DOMAIN_WEBLINK_IN_LISTING PHONE_NUMBER_IN_LISTING EMAIL_ADDRESS_IN_LISTING Product adoption Product Adoption is not enforced at this time. Product adoption conformance Product Adoption is not enforced at this time. Returns policy The only RETURNS_POLICY reason code is UNSUPPORTED_RETURNS_PERIOD. The seller will have to revise their listing (or return business policy) with a supported return period for the site and category. The GetCategoryFeatures call of the Trading API can be used to verify the supported return periods for a particular category. For most eBay categories, the minimum return period that can be stated in a Returns Policy is 14 days for domestic and international sales, but some categories require a minimum 30-day return period.  # noqa: E501

        :param reason_code: The reason_code of this ComplianceDetail.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def variation(self):
        """Gets the variation of this ComplianceDetail.  # noqa: E501


        :return: The variation of this ComplianceDetail.  # noqa: E501
        :rtype: VariationDetails
        """
        return self._variation

    @variation.setter
    def variation(self, variation):
        """Sets the variation of this ComplianceDetail.


        :param variation: The variation of this ComplianceDetail.  # noqa: E501
        :type: VariationDetails
        """

        self._variation = variation

    @property
    def violation_data(self):
        """Gets the violation_data of this ComplianceDetail.  # noqa: E501

        This container provides more information about the listing violation, if applicable. The type of information that appears here will vary based on the compliance type and type of violation. For example, for ASPECTS_ADOPTION violations, this container lists the missing aspect(s) or aspect(s) with invalid values.  # noqa: E501

        :return: The violation_data of this ComplianceDetail.  # noqa: E501
        :rtype: list[NameValueList]
        """
        return self._violation_data

    @violation_data.setter
    def violation_data(self, violation_data):
        """Sets the violation_data of this ComplianceDetail.

        This container provides more information about the listing violation, if applicable. The type of information that appears here will vary based on the compliance type and type of violation. For example, for ASPECTS_ADOPTION violations, this container lists the missing aspect(s) or aspect(s) with invalid values.  # noqa: E501

        :param violation_data: The violation_data of this ComplianceDetail.  # noqa: E501
        :type: list[NameValueList]
        """

        self._violation_data = violation_data

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
        if issubclass(ComplianceDetail, dict):
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
        if not isinstance(other, ComplianceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
