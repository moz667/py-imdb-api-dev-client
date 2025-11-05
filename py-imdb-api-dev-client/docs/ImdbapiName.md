# ImdbapiName

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the name in the IMDb database. | [optional] 
**display_name** | **str** | The display name of the person, typically their full name. | [optional] 
**alternative_names** | **list[str]** | Alternative names for the person, which may include stage names, nicknames, or other variations. | [optional] 
**primary_image** | [**ImdbapiImage**](ImdbapiImage.md) | The primary image associated with the person, such as a profile picture. | [optional] 
**primary_professions** | **list[str]** | A list of primary professions associated with the person, such as \&quot;Actor\&quot;, \&quot;Director\&quot;, \&quot;Producer\&quot;, etc. | [optional] 
**biography** | **str** | A brief biography or description of the person, which may include their career highlights, achievements, and other relevant information. | [optional] 
**height_cm** | **int** | The height of the person in centimeters. | [optional] 
**birth_name** | **str** | The birth name of the person, which may differ from their display name. | [optional] 
**birth_date** | [**ImdbapiPrecisionDate**](ImdbapiPrecisionDate.md) | The birth date of the person, represented as a Date message. | [optional] 
**birth_location** | **str** | The birth location of the person, which may include the city and country of birth. | [optional] 
**death_date** | [**ImdbapiPrecisionDate**](ImdbapiPrecisionDate.md) | The death date of the person, represented as a Date message. This field may be empty if the person is still alive. | [optional] 
**death_location** | **str** | The death location of the person, which may include the city and country of death. | [optional] 
**death_reason** | **str** | The reason for the person&#39;s death, if applicable. | [optional] 
**meter_ranking** | [**ImdbapiNameMeterRanking**](ImdbapiNameMeterRanking.md) | The IMDb popularity meter ranking for the person, which includes their current rank, change direction, and difference from the previous measurement. This field is optional and may not be present for all names. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


