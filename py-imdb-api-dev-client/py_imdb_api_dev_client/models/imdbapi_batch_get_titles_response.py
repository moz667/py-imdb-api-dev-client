# coding: utf-8

"""
    IMDbAPI

    This is beta version of the IMDb API. It is not yet stable and may change in the future.  # noqa: E501

    OpenAPI spec version: 2.0.2-beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from py_imdb_api_dev_client.configuration import Configuration


class ImdbapiBatchGetTitlesResponse(object):
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
        'titles': 'list[ImdbapiTitle]'
    }

    attribute_map = {
        'titles': 'titles'
    }

    def __init__(self, titles=None, _configuration=None):  # noqa: E501
        """ImdbapiBatchGetTitlesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._titles = None
        self.discriminator = None

        if titles is not None:
            self.titles = titles

    @property
    def titles(self):
        """Gets the titles of this ImdbapiBatchGetTitlesResponse.  # noqa: E501

        List of titles retrieved by their IMDb IDs.  # noqa: E501

        :return: The titles of this ImdbapiBatchGetTitlesResponse.  # noqa: E501
        :rtype: list[ImdbapiTitle]
        """
        return self._titles

    @titles.setter
    def titles(self, titles):
        """Sets the titles of this ImdbapiBatchGetTitlesResponse.

        List of titles retrieved by their IMDb IDs.  # noqa: E501

        :param titles: The titles of this ImdbapiBatchGetTitlesResponse.  # noqa: E501
        :type: list[ImdbapiTitle]
        """

        self._titles = titles

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
        if issubclass(ImdbapiBatchGetTitlesResponse, dict):
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
        if not isinstance(other, ImdbapiBatchGetTitlesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImdbapiBatchGetTitlesResponse):
            return True

        return self.to_dict() != other.to_dict()
