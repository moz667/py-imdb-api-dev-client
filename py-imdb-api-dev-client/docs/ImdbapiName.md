# ImdbapiName

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the name in the IMDb database. | [optional] 
**display_name** | **str** | The display name of the person, typically their full name. | [optional] 
**primary_image** | [**ImdbapiImage**](ImdbapiImage.md) | The primary image associated with the person, such as a profile picture. | [optional] 
**alternative_names** | **list[str]** | Alternative names for the person, which may include stage names, nicknames, or other variations. | [optional] 
**primary_professions** | **list[str]** | A list of primary professions associated with the person, such as \&quot;Actor\&quot;, \&quot;Director\&quot;, \&quot;Producer\&quot;, etc. | [optional] 
**biography** | **str** | A brief biography or description of the person, which may include their career highlights, achievements, and other relevant information. | [optional] 
**birth_name** | **str** | The birth name of the person, which may differ from their display name. | [optional] 
**birth_date** | [**ImdbapiDate**](ImdbapiDate.md) | The birth date of the person, represented as a Date message. | [optional] 
**birth_location** | **str** | The birth location of the person, which may include the city and country of birth. | [optional] 
**death_date** | [**ImdbapiDate**](ImdbapiDate.md) | The death date of the person, represented as a Date message. This field may be empty if the person is still alive. | [optional] 
**death_location** | **str** | The death location of the person, which may include the city and country of death. | [optional] 
**death_reason** | **str** | The reason for the person&#39;s death, if applicable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


