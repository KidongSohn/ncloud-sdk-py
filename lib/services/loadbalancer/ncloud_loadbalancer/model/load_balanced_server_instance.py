# coding: utf-8

"""
    loadbalancer

    OpenAPI spec version: 2018-06-21T02:19:18Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_loadbalancer.model.server_health_check_status import ServerHealthCheckStatus  # noqa: F401,E501
from ncloud_loadbalancer.model.server_instance import ServerInstance  # noqa: F401,E501


class LoadBalancedServerInstance(object):
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
        'server_instance': 'ServerInstance',
        'server_health_check_status_list': 'list[ServerHealthCheckStatus]'
    }

    attribute_map = {
        'server_instance': 'serverInstance',
        'server_health_check_status_list': 'serverHealthCheckStatusList'
    }

    def __init__(self, server_instance=None, server_health_check_status_list=None):  # noqa: E501
        """LoadBalancedServerInstance - a model defined in Swagger"""  # noqa: E501

        self._server_instance = None
        self._server_health_check_status_list = None
        self.discriminator = None

        if server_instance is not None:
            self.server_instance = server_instance
        if server_health_check_status_list is not None:
            self.server_health_check_status_list = server_health_check_status_list

    @property
    def server_instance(self):
        """Gets the server_instance of this LoadBalancedServerInstance.  # noqa: E501

        서버인스턴스  # noqa: E501

        :return: The server_instance of this LoadBalancedServerInstance.  # noqa: E501
        :rtype: ServerInstance
        """
        return self._server_instance

    @server_instance.setter
    def server_instance(self, server_instance):
        """Sets the server_instance of this LoadBalancedServerInstance.

        서버인스턴스  # noqa: E501

        :param server_instance: The server_instance of this LoadBalancedServerInstance.  # noqa: E501
        :type: ServerInstance
        """

        self._server_instance = server_instance

    @property
    def server_health_check_status_list(self):
        """Gets the server_health_check_status_list of this LoadBalancedServerInstance.  # noqa: E501

        서버헬스체크상태리스트  # noqa: E501

        :return: The server_health_check_status_list of this LoadBalancedServerInstance.  # noqa: E501
        :rtype: list[ServerHealthCheckStatus]
        """
        return self._server_health_check_status_list

    @server_health_check_status_list.setter
    def server_health_check_status_list(self, server_health_check_status_list):
        """Sets the server_health_check_status_list of this LoadBalancedServerInstance.

        서버헬스체크상태리스트  # noqa: E501

        :param server_health_check_status_list: The server_health_check_status_list of this LoadBalancedServerInstance.  # noqa: E501
        :type: list[ServerHealthCheckStatus]
        """

        self._server_health_check_status_list = server_health_check_status_list

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
        if not isinstance(other, LoadBalancedServerInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other