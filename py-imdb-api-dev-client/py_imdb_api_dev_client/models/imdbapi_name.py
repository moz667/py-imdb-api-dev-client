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


class ImdbapiName(object):
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
        'id': 'str',
        'display_name': 'str',
        'primary_image': 'ImdbapiImage',
        'alternative_names': 'list[str]',
        'primary_professions': 'list[str]',
        'biography': 'str',
        'birth_name': 'str',
        'birth_date': 'ImdbapiDate',
        'birth_location': 'str',
        'death_date': 'ImdbapiDate',
        'death_location': 'str',
        'death_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'display_name',
        'primary_image': 'primary_image',
        'alternative_names': 'alternative_names',
        'primary_professions': 'primary_professions',
        'biography': 'biography',
        'birth_name': 'birth_name',
        'birth_date': 'birth_date',
        'birth_location': 'birth_location',
        'death_date': 'death_date',
        'death_location': 'death_location',
        'death_reason': 'death_reason'
    }

    def __init__(self, id=None, display_name=None, primary_image=None, alternative_names=None, primary_professions=None, biography=None, birth_name=None, birth_date=None, birth_location=None, death_date=None, death_location=None, death_reason=None, _configuration=None):  # noqa: E501
        """ImdbapiName - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._display_name = None
        self._primary_image = None
        self._alternative_names = None
        self._primary_professions = None
        self._biography = None
        self._birth_name = None
        self._birth_date = None
        self._birth_location = None
        self._death_date = None
        self._death_location = None
        self._death_reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name
        if primary_image is not None:
            self.primary_image = primary_image
        if alternative_names is not None:
            self.alternative_names = alternative_names
        if primary_professions is not None:
            self.primary_professions = primary_professions
        if biography is not None:
            self.biography = biography
        if birth_name is not None:
            self.birth_name = birth_name
        if birth_date is not None:
            self.birth_date = birth_date
        if birth_location is not None:
            self.birth_location = birth_location
        if death_date is not None:
            self.death_date = death_date
        if death_location is not None:
            self.death_location = death_location
        if death_reason is not None:
            self.death_reason = death_reason

    @property
    def id(self):
        """Gets the id of this ImdbapiName.  # noqa: E501

        The unique identifier for the name in the IMDb database.  # noqa: E501

        :return: The id of this ImdbapiName.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImdbapiName.

        The unique identifier for the name in the IMDb database.  # noqa: E501

        :param id: The id of this ImdbapiName.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this ImdbapiName.  # noqa: E501

        The display name of the person, typically their full name.  # noqa: E501

        :return: The display_name of this ImdbapiName.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ImdbapiName.

        The display name of the person, typically their full name.  # noqa: E501

        :param display_name: The display_name of this ImdbapiName.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def primary_image(self):
        """Gets the primary_image of this ImdbapiName.  # noqa: E501

        The primary image associated with the person, such as a profile picture.  # noqa: E501

        :return: The primary_image of this ImdbapiName.  # noqa: E501
        :rtype: ImdbapiImage
        """
        return self._primary_image

    @primary_image.setter
    def primary_image(self, primary_image):
        """Sets the primary_image of this ImdbapiName.

        The primary image associated with the person, such as a profile picture.  # noqa: E501

        :param primary_image: The primary_image of this ImdbapiName.  # noqa: E501
        :type: ImdbapiImage
        """

        self._primary_image = primary_image

    @property
    def alternative_names(self):
        """Gets the alternative_names of this ImdbapiName.  # noqa: E501

        Alternative names for the person, which may include stage names, nicknames, or other variations.  # noqa: E501

        :return: The alternative_names of this ImdbapiName.  # noqa: E501
        :rtype: list[str]
        """
        return self._alternative_names

    @alternative_names.setter
    def alternative_names(self, alternative_names):
        """Sets the alternative_names of this ImdbapiName.

        Alternative names for the person, which may include stage names, nicknames, or other variations.  # noqa: E501

        :param alternative_names: The alternative_names of this ImdbapiName.  # noqa: E501
        :type: list[str]
        """

        self._alternative_names = alternative_names

    @property
    def primary_professions(self):
        """Gets the primary_professions of this ImdbapiName.  # noqa: E501

        A list of primary professions associated with the person, such as \"Actor\", \"Director\", \"Producer\", etc.  # noqa: E501

        :return: The primary_professions of this ImdbapiName.  # noqa: E501
        :rtype: list[str]
        """
        return self._primary_professions

    @primary_professions.setter
    def primary_professions(self, primary_professions):
        """Sets the primary_professions of this ImdbapiName.

        A list of primary professions associated with the person, such as \"Actor\", \"Director\", \"Producer\", etc.  # noqa: E501

        :param primary_professions: The primary_professions of this ImdbapiName.  # noqa: E501
        :type: list[str]
        """

        self._primary_professions = primary_professions

    @property
    def biography(self):
        """Gets the biography of this ImdbapiName.  # noqa: E501

        A brief biography or description of the person, which may include their career highlights, achievements, and other relevant information.  # noqa: E501

        :return: The biography of this ImdbapiName.  # noqa: E501
        :rtype: str
        """
        return self._biography

    @biography.setter
    def biography(self, biography):
        """Sets the biography of this ImdbapiName.

        A brief biography or description of the person, which may include their career highlights, achievements, and other relevant information.  # noqa: E501

        :param biography: The biography of this ImdbapiName.  # noqa: E501
        :type: str
        """

        self._biography = biography

    @property
    def birth_name(self):
        """Gets the birth_name of this ImdbapiName.  # noqa: E501

        The birth name of the person, which may differ from their display name.  # noqa: E501

        :return: The birth_name of this ImdbapiName.  # noqa: E501
        :rtype: str
        """
        return self._birth_name

    @birth_name.setter
    def birth_name(self, birth_name):
        """Sets the birth_name of this ImdbapiName.

        The birth name of the person, which may differ from their display name.  # noqa: E501

        :param birth_name: The birth_name of this ImdbapiName.  # noqa: E501
        :type: str
        """

        self._birth_name = birth_name

    @property
    def birth_date(self):
        """Gets the birth_date of this ImdbapiName.  # noqa: E501

        The birth date of the person, represented as a Date message.  # noqa: E501

        :return: The birth_date of this ImdbapiName.  # noqa: E501
        :rtype: ImdbapiDate
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this ImdbapiName.

        The birth date of the person, represented as a Date message.  # noqa: E501

        :param birth_date: The birth_date of this ImdbapiName.  # noqa: E501
        :type: ImdbapiDate
        """

        self._birth_date = birth_date

    @property
    def birth_location(self):
        """Gets the birth_location of this ImdbapiName.  # noqa: E501

        The birth location of the person, which may include the city and country of birth.  # noqa: E501

        :return: The birth_location of this ImdbapiName.  # noqa: E501
        :rtype: str
        """
        return self._birth_location

    @birth_location.setter
    def birth_location(self, birth_location):
        """Sets the birth_location of this ImdbapiName.

        The birth location of the person, which may include the city and country of birth.  # noqa: E501

        :param birth_location: The birth_location of this ImdbapiName.  # noqa: E501
        :type: str
        """

        self._birth_location = birth_location

    @property
    def death_date(self):
        """Gets the death_date of this ImdbapiName.  # noqa: E501

        The death date of the person, represented as a Date message. This field may be empty if the person is still alive.  # noqa: E501

        :return: The death_date of this ImdbapiName.  # noqa: E501
        :rtype: ImdbapiDate
        """
        return self._death_date

    @death_date.setter
    def death_date(self, death_date):
        """Sets the death_date of this ImdbapiName.

        The death date of the person, represented as a Date message. This field may be empty if the person is still alive.  # noqa: E501

        :param death_date: The death_date of this ImdbapiName.  # noqa: E501
        :type: ImdbapiDate
        """

        self._death_date = death_date

    @property
    def death_location(self):
        """Gets the death_location of this ImdbapiName.  # noqa: E501

        The death location of the person, which may include the city and country of death.  # noqa: E501

        :return: The death_location of this ImdbapiName.  # noqa: E501
        :rtype: str
        """
        return self._death_location

    @death_location.setter
    def death_location(self, death_location):
        """Sets the death_location of this ImdbapiName.

        The death location of the person, which may include the city and country of death.  # noqa: E501

        :param death_location: The death_location of this ImdbapiName.  # noqa: E501
        :type: str
        """

        self._death_location = death_location

    @property
    def death_reason(self):
        """Gets the death_reason of this ImdbapiName.  # noqa: E501

        The reason for the person's death, if applicable.  # noqa: E501

        :return: The death_reason of this ImdbapiName.  # noqa: E501
        :rtype: str
        """
        return self._death_reason

    @death_reason.setter
    def death_reason(self, death_reason):
        """Sets the death_reason of this ImdbapiName.

        The reason for the person's death, if applicable.  # noqa: E501

        :param death_reason: The death_reason of this ImdbapiName.  # noqa: E501
        :type: str
        """

        self._death_reason = death_reason

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
        if issubclass(ImdbapiName, dict):
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
        if not isinstance(other, ImdbapiName):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImdbapiName):
            return True

        return self.to_dict() != other.to_dict()
