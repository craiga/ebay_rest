# coding: utf-8

"""
    Notification API

    The eBay Notification API enables management of the entire end-to-end eBay notification experience by allowing users to:<ul><li>Browse for supported notification topics and retrieve topic details</li><li>Create, configure, and manage notification destination endpionts</li><li>Configure, manage, and test notification subscriptions</li><li>Process eBay notifications and verify the integrity of the message payload</li></ul>  # noqa: E501

    OpenAPI spec version: v1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Subscription(object):
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
        'creation_date': 'str',
        'destination_id': 'str',
        'payload': 'SubscriptionPayloadDetail',
        'status': 'str',
        'subscription_id': 'str',
        'topic_id': 'str'
    }

    attribute_map = {
        'creation_date': 'creationDate',
        'destination_id': 'destinationId',
        'payload': 'payload',
        'status': 'status',
        'subscription_id': 'subscriptionId',
        'topic_id': 'topicId'
    }

    def __init__(self, creation_date=None, destination_id=None, payload=None, status=None, subscription_id=None, topic_id=None):  # noqa: E501
        """Subscription - a model defined in Swagger"""  # noqa: E501
        self._creation_date = None
        self._destination_id = None
        self._payload = None
        self._status = None
        self._subscription_id = None
        self._topic_id = None
        self.discriminator = None
        if creation_date is not None:
            self.creation_date = creation_date
        if destination_id is not None:
            self.destination_id = destination_id
        if payload is not None:
            self.payload = payload
        if status is not None:
            self.status = status
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if topic_id is not None:
            self.topic_id = topic_id

    @property
    def creation_date(self):
        """Gets the creation_date of this Subscription.  # noqa: E501

        The creation date for this subscription.  # noqa: E501

        :return: The creation_date of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Subscription.

        The creation date for this subscription.  # noqa: E501

        :param creation_date: The creation_date of this Subscription.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

    @property
    def destination_id(self):
        """Gets the destination_id of this Subscription.  # noqa: E501

        The unique identifier for the destination associated with this subscription.  # noqa: E501

        :return: The destination_id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._destination_id

    @destination_id.setter
    def destination_id(self, destination_id):
        """Sets the destination_id of this Subscription.

        The unique identifier for the destination associated with this subscription.  # noqa: E501

        :param destination_id: The destination_id of this Subscription.  # noqa: E501
        :type: str
        """

        self._destination_id = destination_id

    @property
    def payload(self):
        """Gets the payload of this Subscription.  # noqa: E501


        :return: The payload of this Subscription.  # noqa: E501
        :rtype: SubscriptionPayloadDetail
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this Subscription.


        :param payload: The payload of this Subscription.  # noqa: E501
        :type: SubscriptionPayloadDetail
        """

        self._payload = payload

    @property
    def status(self):
        """Gets the status of this Subscription.  # noqa: E501

        The status of this subscription. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/commerce/notification/types/api:SubscriptionStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The status of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Subscription.

        The status of this subscription. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/commerce/notification/types/api:SubscriptionStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param status: The status of this Subscription.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subscription_id(self):
        """Gets the subscription_id of this Subscription.  # noqa: E501

        The unique identifier for the subscription.  # noqa: E501

        :return: The subscription_id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this Subscription.

        The unique identifier for the subscription.  # noqa: E501

        :param subscription_id: The subscription_id of this Subscription.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def topic_id(self):
        """Gets the topic_id of this Subscription.  # noqa: E501

        The unique identifier for the topic associated with this subscription.  # noqa: E501

        :return: The topic_id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """Sets the topic_id of this Subscription.

        The unique identifier for the topic associated with this subscription.  # noqa: E501

        :param topic_id: The topic_id of this Subscription.  # noqa: E501
        :type: str
        """

        self._topic_id = topic_id

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
        if issubclass(Subscription, dict):
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
        if not isinstance(other, Subscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
