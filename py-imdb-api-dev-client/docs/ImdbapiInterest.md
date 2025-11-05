# ImdbapiInterest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the interest. | [optional] 
**name** | **str** | The name of the interest, e.g., \&quot;Action\&quot;, \&quot;Action Epic\&quot;, \&quot;Adult Animation\&quot;, etc. | [optional] 
**primary_image** | [**ImdbapiImage**](ImdbapiImage.md) | The primary image of the interest, which can be a poster or cover image. | [optional] 
**description** | **str** | A brief description of the interest, which can include details about the genre or type. | [optional] 
**is_subgenre** | **bool** | Indicates whether the interest is a subgenre of another genre. | [optional] 
**similar_interests** | [**list[ImdbapiInterest]**](ImdbapiInterest.md) | A list of similar interests that are related to this interest. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


