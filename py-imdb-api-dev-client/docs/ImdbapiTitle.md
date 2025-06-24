# ImdbapiTitle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the title. | [optional] 
**type** | **str** | The type of the title, such as \&quot;movie\&quot;, \&quot;tvSeries\&quot;, \&quot;tvEpisode\&quot;, etc. | [optional] 
**primary_title** | **str** | The primary title of the title, which is typically the most recognized name. | [optional] 
**original_title** | **str** | The original title of the title, normally which is the title as it was originally released. | [optional] 
**primary_image** | [**ImdbapiImage**](ImdbapiImage.md) | The primary image associated with the title, such as a poster. | [optional] 
**genres** | **list[str]** | The genres field contains a list of genres associated with the title. | [optional] 
**rating** | [**ImdbapiRating**](ImdbapiRating.md) | The rating field contains the aggregate rating and the number of votes for the title. | [optional] 
**start_year** | **int** | The start_year field is used for titles that have a defined start, such as movies or TV series. | [optional] 
**end_year** | **int** | The end_year field is used for titles that have a defined end, such as TV series. | [optional] 
**runtime_minutes** | **int** | The runtime_minutes field contains the total runtime of the title in minutes. | [optional] 
**plot** | **str** | The plot field contains a brief summary or description of the title&#39;s storyline. | [optional] 
**is_adult** | **bool** | The is_adult field indicates whether the title is intended for adult audiences. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


