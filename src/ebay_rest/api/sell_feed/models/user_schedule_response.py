# coding: utf-8

"""
    Feed API

    <p>The <strong>Feed API</strong> lets sellers upload input files, download reports and files including their status, filter reports using URI parameters, and retrieve customer service metrics task details.</p>  # noqa: E501

    OpenAPI spec version: v1.3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserScheduleResponse(object):
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
        'feed_type': 'str',
        'last_modified_date': 'str',
        'preferred_trigger_day_of_month': 'int',
        'preferred_trigger_day_of_week': 'str',
        'preferred_trigger_hour': 'str',
        'schedule_end_date': 'str',
        'schedule_id': 'str',
        'schedule_name': 'str',
        'schedule_start_date': 'str',
        'schedule_template_id': 'str',
        'schema_version': 'str',
        'status': 'str',
        'status_reason': 'str'
    }

    attribute_map = {
        'creation_date': 'creationDate',
        'feed_type': 'feedType',
        'last_modified_date': 'lastModifiedDate',
        'preferred_trigger_day_of_month': 'preferredTriggerDayOfMonth',
        'preferred_trigger_day_of_week': 'preferredTriggerDayOfWeek',
        'preferred_trigger_hour': 'preferredTriggerHour',
        'schedule_end_date': 'scheduleEndDate',
        'schedule_id': 'scheduleId',
        'schedule_name': 'scheduleName',
        'schedule_start_date': 'scheduleStartDate',
        'schedule_template_id': 'scheduleTemplateId',
        'schema_version': 'schemaVersion',
        'status': 'status',
        'status_reason': 'statusReason'
    }

    def __init__(self, creation_date=None, feed_type=None, last_modified_date=None, preferred_trigger_day_of_month=None, preferred_trigger_day_of_week=None, preferred_trigger_hour=None, schedule_end_date=None, schedule_id=None, schedule_name=None, schedule_start_date=None, schedule_template_id=None, schema_version=None, status=None, status_reason=None):  # noqa: E501
        """UserScheduleResponse - a model defined in Swagger"""  # noqa: E501
        self._creation_date = None
        self._feed_type = None
        self._last_modified_date = None
        self._preferred_trigger_day_of_month = None
        self._preferred_trigger_day_of_week = None
        self._preferred_trigger_hour = None
        self._schedule_end_date = None
        self._schedule_id = None
        self._schedule_name = None
        self._schedule_start_date = None
        self._schedule_template_id = None
        self._schema_version = None
        self._status = None
        self._status_reason = None
        self.discriminator = None
        if creation_date is not None:
            self.creation_date = creation_date
        if feed_type is not None:
            self.feed_type = feed_type
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if preferred_trigger_day_of_month is not None:
            self.preferred_trigger_day_of_month = preferred_trigger_day_of_month
        if preferred_trigger_day_of_week is not None:
            self.preferred_trigger_day_of_week = preferred_trigger_day_of_week
        if preferred_trigger_hour is not None:
            self.preferred_trigger_hour = preferred_trigger_hour
        if schedule_end_date is not None:
            self.schedule_end_date = schedule_end_date
        if schedule_id is not None:
            self.schedule_id = schedule_id
        if schedule_name is not None:
            self.schedule_name = schedule_name
        if schedule_start_date is not None:
            self.schedule_start_date = schedule_start_date
        if schedule_template_id is not None:
            self.schedule_template_id = schedule_template_id
        if schema_version is not None:
            self.schema_version = schema_version
        if status is not None:
            self.status = status
        if status_reason is not None:
            self.status_reason = status_reason

    @property
    def creation_date(self):
        """Gets the creation_date of this UserScheduleResponse.  # noqa: E501

        The creation date of the schedule in hours based on the 24-hour Coordinated Universal Time (UTC) clock.  # noqa: E501

        :return: The creation_date of this UserScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this UserScheduleResponse.

        The creation date of the schedule in hours based on the 24-hour Coordinated Universal Time (UTC) clock.  # noqa: E501

        :param creation_date: The creation_date of this UserScheduleResponse.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

    @property
    def feed_type(self):
        """Gets the feed_type of this UserScheduleResponse.  # noqa: E501

        The feedType associated with the schedule.  # noqa: E501

        :return: The feed_type of this UserScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._feed_type

    @feed_type.setter
    def feed_type(self, feed_type):
        """Sets the feed_type of this UserScheduleResponse.

        The feedType associated with the schedule.  # noqa: E501

        :param feed_type: The feed_type of this UserScheduleResponse.  # noqa: E501
        :type: str
        """

        self._feed_type = feed_type

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this UserScheduleResponse.  # noqa: E501

        The date the schedule was last modified.  # noqa: E501

        :return: The last_modified_date of this UserScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this UserScheduleResponse.

        The date the schedule was last modified.  # noqa: E501

        :param last_modified_date: The last_modified_date of this UserScheduleResponse.  # noqa: E501
        :type: str
        """

        self._last_modified_date = last_modified_date

    @property
    def preferred_trigger_day_of_month(self):
        """Gets the preferred_trigger_day_of_month of this UserScheduleResponse.  # noqa: E501

        The preferred day of the month to trigger the schedule. This field can be used with preferredTriggerHour for monthly schedules. The last day of the month is used for numbers larger than the number of days in the month.  # noqa: E501

        :return: The preferred_trigger_day_of_month of this UserScheduleResponse.  # noqa: E501
        :rtype: int
        """
        return self._preferred_trigger_day_of_month

    @preferred_trigger_day_of_month.setter
    def preferred_trigger_day_of_month(self, preferred_trigger_day_of_month):
        """Sets the preferred_trigger_day_of_month of this UserScheduleResponse.

        The preferred day of the month to trigger the schedule. This field can be used with preferredTriggerHour for monthly schedules. The last day of the month is used for numbers larger than the number of days in the month.  # noqa: E501

        :param preferred_trigger_day_of_month: The preferred_trigger_day_of_month of this UserScheduleResponse.  # noqa: E501
        :type: int
        """

        self._preferred_trigger_day_of_month = preferred_trigger_day_of_month

    @property
    def preferred_trigger_day_of_week(self):
        """Gets the preferred_trigger_day_of_week of this UserScheduleResponse.  # noqa: E501

        The preferred day of the week to trigger the schedule. This field can be used with preferredTriggerHour for weekly schedules. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/feed/types/api:DayOfWeekEnum'>eBay API documentation</a>  # noqa: E501

        :return: The preferred_trigger_day_of_week of this UserScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._preferred_trigger_day_of_week

    @preferred_trigger_day_of_week.setter
    def preferred_trigger_day_of_week(self, preferred_trigger_day_of_week):
        """Sets the preferred_trigger_day_of_week of this UserScheduleResponse.

        The preferred day of the week to trigger the schedule. This field can be used with preferredTriggerHour for weekly schedules. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/feed/types/api:DayOfWeekEnum'>eBay API documentation</a>  # noqa: E501

        :param preferred_trigger_day_of_week: The preferred_trigger_day_of_week of this UserScheduleResponse.  # noqa: E501
        :type: str
        """

        self._preferred_trigger_day_of_week = preferred_trigger_day_of_week

    @property
    def preferred_trigger_hour(self):
        """Gets the preferred_trigger_hour of this UserScheduleResponse.  # noqa: E501

        The preferred two-digit hour of the day to trigger the schedule. Format: UTC hhZ For example, the following represents 11:00 am UTC: 11Z  # noqa: E501

        :return: The preferred_trigger_hour of this UserScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._preferred_trigger_hour

    @preferred_trigger_hour.setter
    def preferred_trigger_hour(self, preferred_trigger_hour):
        """Sets the preferred_trigger_hour of this UserScheduleResponse.

        The preferred two-digit hour of the day to trigger the schedule. Format: UTC hhZ For example, the following represents 11:00 am UTC: 11Z  # noqa: E501

        :param preferred_trigger_hour: The preferred_trigger_hour of this UserScheduleResponse.  # noqa: E501
        :type: str
        """

        self._preferred_trigger_hour = preferred_trigger_hour

    @property
    def schedule_end_date(self):
        """Gets the schedule_end_date of this UserScheduleResponse.  # noqa: E501

        The timestamp on which the report generation (subscription) ends. After this date, the schedule status becomes INACTIVE.  # noqa: E501

        :return: The schedule_end_date of this UserScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._schedule_end_date

    @schedule_end_date.setter
    def schedule_end_date(self, schedule_end_date):
        """Sets the schedule_end_date of this UserScheduleResponse.

        The timestamp on which the report generation (subscription) ends. After this date, the schedule status becomes INACTIVE.  # noqa: E501

        :param schedule_end_date: The schedule_end_date of this UserScheduleResponse.  # noqa: E501
        :type: str
        """

        self._schedule_end_date = schedule_end_date

    @property
    def schedule_id(self):
        """Gets the schedule_id of this UserScheduleResponse.  # noqa: E501

        The ID of the schedule. This ID is generated when the schedule was created by the createSchedule method.  # noqa: E501

        :return: The schedule_id of this UserScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        """Sets the schedule_id of this UserScheduleResponse.

        The ID of the schedule. This ID is generated when the schedule was created by the createSchedule method.  # noqa: E501

        :param schedule_id: The schedule_id of this UserScheduleResponse.  # noqa: E501
        :type: str
        """

        self._schedule_id = schedule_id

    @property
    def schedule_name(self):
        """Gets the schedule_name of this UserScheduleResponse.  # noqa: E501

        The schedule name assigned by the user for the created schedule. Users assign this name for their reference.  # noqa: E501

        :return: The schedule_name of this UserScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._schedule_name

    @schedule_name.setter
    def schedule_name(self, schedule_name):
        """Sets the schedule_name of this UserScheduleResponse.

        The schedule name assigned by the user for the created schedule. Users assign this name for their reference.  # noqa: E501

        :param schedule_name: The schedule_name of this UserScheduleResponse.  # noqa: E501
        :type: str
        """

        self._schedule_name = schedule_name

    @property
    def schedule_start_date(self):
        """Gets the schedule_start_date of this UserScheduleResponse.  # noqa: E501

        The timestamp that indicates the start of the report generation.  # noqa: E501

        :return: The schedule_start_date of this UserScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._schedule_start_date

    @schedule_start_date.setter
    def schedule_start_date(self, schedule_start_date):
        """Sets the schedule_start_date of this UserScheduleResponse.

        The timestamp that indicates the start of the report generation.  # noqa: E501

        :param schedule_start_date: The schedule_start_date of this UserScheduleResponse.  # noqa: E501
        :type: str
        """

        self._schedule_start_date = schedule_start_date

    @property
    def schedule_template_id(self):
        """Gets the schedule_template_id of this UserScheduleResponse.  # noqa: E501

        The ID of the template used to create this schedule.  # noqa: E501

        :return: The schedule_template_id of this UserScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._schedule_template_id

    @schedule_template_id.setter
    def schedule_template_id(self, schedule_template_id):
        """Sets the schedule_template_id of this UserScheduleResponse.

        The ID of the template used to create this schedule.  # noqa: E501

        :param schedule_template_id: The schedule_template_id of this UserScheduleResponse.  # noqa: E501
        :type: str
        """

        self._schedule_template_id = schedule_template_id

    @property
    def schema_version(self):
        """Gets the schema_version of this UserScheduleResponse.  # noqa: E501

        The schema version of the feedType for the schedule.  # noqa: E501

        :return: The schema_version of this UserScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this UserScheduleResponse.

        The schema version of the feedType for the schedule.  # noqa: E501

        :param schema_version: The schema_version of this UserScheduleResponse.  # noqa: E501
        :type: str
        """

        self._schema_version = schema_version

    @property
    def status(self):
        """Gets the status of this UserScheduleResponse.  # noqa: E501

        The enumeration value that indicates the state of the schedule. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/feed/types/api:StatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The status of this UserScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserScheduleResponse.

        The enumeration value that indicates the state of the schedule. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/feed/types/api:StatusEnum'>eBay API documentation</a>  # noqa: E501

        :param status: The status of this UserScheduleResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_reason(self):
        """Gets the status_reason of this UserScheduleResponse.  # noqa: E501

        The reason the schedule is inactive. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/feed/types/api:StatusReasonEnum'>eBay API documentation</a>  # noqa: E501

        :return: The status_reason of this UserScheduleResponse.  # noqa: E501
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this UserScheduleResponse.

        The reason the schedule is inactive. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/feed/types/api:StatusReasonEnum'>eBay API documentation</a>  # noqa: E501

        :param status_reason: The status_reason of this UserScheduleResponse.  # noqa: E501
        :type: str
        """

        self._status_reason = status_reason

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
        if issubclass(UserScheduleResponse, dict):
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
        if not isinstance(other, UserScheduleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
