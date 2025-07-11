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


class ImdbapiRating(object):
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
        'aggregate_rating': 'float',
        'votes_count': 'int'
    }

    attribute_map = {
        'aggregate_rating': 'aggregate_rating',
        'votes_count': 'votes_count'
    }

    def __init__(self, aggregate_rating=None, votes_count=None, _configuration=None):  # noqa: E501
        """ImdbapiRating - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._aggregate_rating = None
        self._votes_count = None
        self.discriminator = None

        if aggregate_rating is not None:
            self.aggregate_rating = aggregate_rating
        if votes_count is not None:
            self.votes_count = votes_count

    @property
    def aggregate_rating(self):
        """Gets the aggregate_rating of this ImdbapiRating.  # noqa: E501

        The aggregate_rating field contains the average rating of the title, typically on a scale from 1 to 10.  # noqa: E501

        :return: The aggregate_rating of this ImdbapiRating.  # noqa: E501
        :rtype: float
        """
        return self._aggregate_rating

    @aggregate_rating.setter
    def aggregate_rating(self, aggregate_rating):
        """Sets the aggregate_rating of this ImdbapiRating.

        The aggregate_rating field contains the average rating of the title, typically on a scale from 1 to 10.  # noqa: E501

        :param aggregate_rating: The aggregate_rating of this ImdbapiRating.  # noqa: E501
        :type: float
        """

        self._aggregate_rating = aggregate_rating

    @property
    def votes_count(self):
        """Gets the votes_count of this ImdbapiRating.  # noqa: E501

        The votes_count field contains the total number of votes cast for the title.  # noqa: E501

        :return: The votes_count of this ImdbapiRating.  # noqa: E501
        :rtype: int
        """
        return self._votes_count

    @votes_count.setter
    def votes_count(self, votes_count):
        """Sets the votes_count of this ImdbapiRating.

        The votes_count field contains the total number of votes cast for the title.  # noqa: E501

        :param votes_count: The votes_count of this ImdbapiRating.  # noqa: E501
        :type: int
        """

        self._votes_count = votes_count

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
        if issubclass(ImdbapiRating, dict):
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
        if not isinstance(other, ImdbapiRating):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImdbapiRating):
            return True

        return self.to_dict() != other.to_dict()
