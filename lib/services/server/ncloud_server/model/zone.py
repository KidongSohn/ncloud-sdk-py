# coding: utf-8

"""
    server

    OpenAPI spec version: 2018-06-22T02:34:44Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Zone(object):
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
        'zone_no': 'str',
        'zone_name': 'str',
        'zone_description': 'str',
        'region_no': 'str'
    }

    attribute_map = {
        'zone_no': 'zoneNo',
        'zone_name': 'zoneName',
        'zone_description': 'zoneDescription',
        'region_no': 'regionNo'
    }

    def __init__(self, zone_no=None, zone_name=None, zone_description=None, region_no=None):  # noqa: E501
        """Zone - a model defined in Swagger"""  # noqa: E501

        self._zone_no = None
        self._zone_name = None
        self._zone_description = None
        self._region_no = None
        self.discriminator = None

        if zone_no is not None:
            self.zone_no = zone_no
        if zone_name is not None:
            self.zone_name = zone_name
        if zone_description is not None:
            self.zone_description = zone_description
        if region_no is not None:
            self.region_no = region_no

    @property
    def zone_no(self):
        """Gets the zone_no of this Zone.  # noqa: E501

        존(Zone)번호  # noqa: E501

        :return: The zone_no of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._zone_no

    @zone_no.setter
    def zone_no(self, zone_no):
        """Sets the zone_no of this Zone.

        존(Zone)번호  # noqa: E501

        :param zone_no: The zone_no of this Zone.  # noqa: E501
        :type: str
        """

        self._zone_no = zone_no

    @property
    def zone_name(self):
        """Gets the zone_name of this Zone.  # noqa: E501

        존(Zone)명  # noqa: E501

        :return: The zone_name of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this Zone.

        존(Zone)명  # noqa: E501

        :param zone_name: The zone_name of this Zone.  # noqa: E501
        :type: str
        """

        self._zone_name = zone_name

    @property
    def zone_description(self):
        """Gets the zone_description of this Zone.  # noqa: E501

        존(Zone)설명  # noqa: E501

        :return: The zone_description of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._zone_description

    @zone_description.setter
    def zone_description(self, zone_description):
        """Sets the zone_description of this Zone.

        존(Zone)설명  # noqa: E501

        :param zone_description: The zone_description of this Zone.  # noqa: E501
        :type: str
        """

        self._zone_description = zone_description

    @property
    def region_no(self):
        """Gets the region_no of this Zone.  # noqa: E501

        리전번호  # noqa: E501

        :return: The region_no of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._region_no

    @region_no.setter
    def region_no(self, region_no):
        """Sets the region_no of this Zone.

        리전번호  # noqa: E501

        :param region_no: The region_no of this Zone.  # noqa: E501
        :type: str
        """

        self._region_no = region_no

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Zone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
