# coding: utf-8

"""
    autoscaling

    OpenAPI spec version: 2018-06-21T02:22:22Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PutScalingPolicyRequest(object):
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
        'adjustment_type_code': 'str',
        'auto_scaling_group_name': 'str',
        'cooldown': 'int',
        'min_adjustment_step': 'int',
        'policy_name': 'str',
        'scaling_adjustment': 'int'
    }

    attribute_map = {
        'adjustment_type_code': 'adjustmentTypeCode',
        'auto_scaling_group_name': 'autoScalingGroupName',
        'cooldown': 'cooldown',
        'min_adjustment_step': 'minAdjustmentStep',
        'policy_name': 'policyName',
        'scaling_adjustment': 'scalingAdjustment'
    }

    def __init__(self, adjustment_type_code=None, auto_scaling_group_name=None, cooldown=None, min_adjustment_step=None, policy_name=None, scaling_adjustment=None):  # noqa: E501
        """PutScalingPolicyRequest - a model defined in Swagger"""  # noqa: E501

        self._adjustment_type_code = None
        self._auto_scaling_group_name = None
        self._cooldown = None
        self._min_adjustment_step = None
        self._policy_name = None
        self._scaling_adjustment = None
        self.discriminator = None

        self.adjustment_type_code = adjustment_type_code
        self.auto_scaling_group_name = auto_scaling_group_name
        if cooldown is not None:
            self.cooldown = cooldown
        if min_adjustment_step is not None:
            self.min_adjustment_step = min_adjustment_step
        self.policy_name = policy_name
        self.scaling_adjustment = scaling_adjustment

    @property
    def adjustment_type_code(self):
        """Gets the adjustment_type_code of this PutScalingPolicyRequest.  # noqa: E501

        조정유형코드  # noqa: E501

        :return: The adjustment_type_code of this PutScalingPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._adjustment_type_code

    @adjustment_type_code.setter
    def adjustment_type_code(self, adjustment_type_code):
        """Sets the adjustment_type_code of this PutScalingPolicyRequest.

        조정유형코드  # noqa: E501

        :param adjustment_type_code: The adjustment_type_code of this PutScalingPolicyRequest.  # noqa: E501
        :type: str
        """
        if adjustment_type_code is None:
            raise ValueError("Invalid value for `adjustment_type_code`, must not be `None`")  # noqa: E501

        self._adjustment_type_code = adjustment_type_code

    @property
    def auto_scaling_group_name(self):
        """Gets the auto_scaling_group_name of this PutScalingPolicyRequest.  # noqa: E501

        오토스케일링그룹명  # noqa: E501

        :return: The auto_scaling_group_name of this PutScalingPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_scaling_group_name

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, auto_scaling_group_name):
        """Sets the auto_scaling_group_name of this PutScalingPolicyRequest.

        오토스케일링그룹명  # noqa: E501

        :param auto_scaling_group_name: The auto_scaling_group_name of this PutScalingPolicyRequest.  # noqa: E501
        :type: str
        """
        if auto_scaling_group_name is None:
            raise ValueError("Invalid value for `auto_scaling_group_name`, must not be `None`")  # noqa: E501

        self._auto_scaling_group_name = auto_scaling_group_name

    @property
    def cooldown(self):
        """Gets the cooldown of this PutScalingPolicyRequest.  # noqa: E501

        쿨다운타임  # noqa: E501

        :return: The cooldown of this PutScalingPolicyRequest.  # noqa: E501
        :rtype: int
        """
        return self._cooldown

    @cooldown.setter
    def cooldown(self, cooldown):
        """Sets the cooldown of this PutScalingPolicyRequest.

        쿨다운타임  # noqa: E501

        :param cooldown: The cooldown of this PutScalingPolicyRequest.  # noqa: E501
        :type: int
        """

        self._cooldown = cooldown

    @property
    def min_adjustment_step(self):
        """Gets the min_adjustment_step of this PutScalingPolicyRequest.  # noqa: E501

        최소조정스텝  # noqa: E501

        :return: The min_adjustment_step of this PutScalingPolicyRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_adjustment_step

    @min_adjustment_step.setter
    def min_adjustment_step(self, min_adjustment_step):
        """Sets the min_adjustment_step of this PutScalingPolicyRequest.

        최소조정스텝  # noqa: E501

        :param min_adjustment_step: The min_adjustment_step of this PutScalingPolicyRequest.  # noqa: E501
        :type: int
        """

        self._min_adjustment_step = min_adjustment_step

    @property
    def policy_name(self):
        """Gets the policy_name of this PutScalingPolicyRequest.  # noqa: E501

        정책명  # noqa: E501

        :return: The policy_name of this PutScalingPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this PutScalingPolicyRequest.

        정책명  # noqa: E501

        :param policy_name: The policy_name of this PutScalingPolicyRequest.  # noqa: E501
        :type: str
        """
        if policy_name is None:
            raise ValueError("Invalid value for `policy_name`, must not be `None`")  # noqa: E501

        self._policy_name = policy_name

    @property
    def scaling_adjustment(self):
        """Gets the scaling_adjustment of this PutScalingPolicyRequest.  # noqa: E501

        스케일링조정값  # noqa: E501

        :return: The scaling_adjustment of this PutScalingPolicyRequest.  # noqa: E501
        :rtype: int
        """
        return self._scaling_adjustment

    @scaling_adjustment.setter
    def scaling_adjustment(self, scaling_adjustment):
        """Sets the scaling_adjustment of this PutScalingPolicyRequest.

        스케일링조정값  # noqa: E501

        :param scaling_adjustment: The scaling_adjustment of this PutScalingPolicyRequest.  # noqa: E501
        :type: int
        """
        if scaling_adjustment is None:
            raise ValueError("Invalid value for `scaling_adjustment`, must not be `None`")  # noqa: E501

        self._scaling_adjustment = scaling_adjustment

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
        if not isinstance(other, PutScalingPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other