# coding: utf-8

"""
    server

    OpenAPI spec version: 2018-06-22T02:34:44Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RecreateServerInstanceRequest(object):
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
        'server_instance_no': 'str',
        'server_instance_name': 'str',
        'server_image_product_code': 'str',
        'user_data': 'str'
    }

    attribute_map = {
        'server_instance_no': 'serverInstanceNo',
        'server_instance_name': 'serverInstanceName',
        'server_image_product_code': 'serverImageProductCode',
        'user_data': 'userData'
    }

    def __init__(self, server_instance_no=None, server_instance_name=None, server_image_product_code=None, user_data=None):  # noqa: E501
        """RecreateServerInstanceRequest - a model defined in Swagger"""  # noqa: E501

        self._server_instance_no = None
        self._server_instance_name = None
        self._server_image_product_code = None
        self._user_data = None
        self.discriminator = None

        if server_instance_no is not None:
            self.server_instance_no = server_instance_no
        if server_instance_name is not None:
            self.server_instance_name = server_instance_name
        if server_image_product_code is not None:
            self.server_image_product_code = server_image_product_code
        if user_data is not None:
            self.user_data = user_data

    @property
    def server_instance_no(self):
        """Gets the server_instance_no of this RecreateServerInstanceRequest.  # noqa: E501

        서버인스턴스번호  # noqa: E501

        :return: The server_instance_no of this RecreateServerInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_instance_no

    @server_instance_no.setter
    def server_instance_no(self, server_instance_no):
        """Sets the server_instance_no of this RecreateServerInstanceRequest.

        서버인스턴스번호  # noqa: E501

        :param server_instance_no: The server_instance_no of this RecreateServerInstanceRequest.  # noqa: E501
        :type: str
        """

        self._server_instance_no = server_instance_no

    @property
    def server_instance_name(self):
        """Gets the server_instance_name of this RecreateServerInstanceRequest.  # noqa: E501

        서버인스턴스이름  # noqa: E501

        :return: The server_instance_name of this RecreateServerInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_instance_name

    @server_instance_name.setter
    def server_instance_name(self, server_instance_name):
        """Sets the server_instance_name of this RecreateServerInstanceRequest.

        서버인스턴스이름  # noqa: E501

        :param server_instance_name: The server_instance_name of this RecreateServerInstanceRequest.  # noqa: E501
        :type: str
        """

        self._server_instance_name = server_instance_name

    @property
    def server_image_product_code(self):
        """Gets the server_image_product_code of this RecreateServerInstanceRequest.  # noqa: E501

        서버이미지상품코드  # noqa: E501

        :return: The server_image_product_code of this RecreateServerInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_image_product_code

    @server_image_product_code.setter
    def server_image_product_code(self, server_image_product_code):
        """Sets the server_image_product_code of this RecreateServerInstanceRequest.

        서버이미지상품코드  # noqa: E501

        :param server_image_product_code: The server_image_product_code of this RecreateServerInstanceRequest.  # noqa: E501
        :type: str
        """

        self._server_image_product_code = server_image_product_code

    @property
    def user_data(self):
        """Gets the user_data of this RecreateServerInstanceRequest.  # noqa: E501

        사용자데이터  # noqa: E501

        :return: The user_data of this RecreateServerInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this RecreateServerInstanceRequest.

        사용자데이터  # noqa: E501

        :param user_data: The user_data of this RecreateServerInstanceRequest.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

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
        if not isinstance(other, RecreateServerInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
