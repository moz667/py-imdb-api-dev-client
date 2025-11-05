# py_imdb_api_dev_client.InterestApi

All URIs are relative to *https://api.imdbapi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**i_mdb_api_service_get_interest**](InterestApi.md#i_mdb_api_service_get_interest) | **GET** /interests/{interestId} | Get interest by ID
[**i_mdb_api_service_list_interest_categories**](InterestApi.md#i_mdb_api_service_list_interest_categories) | **GET** /interests | List interest categories


# **i_mdb_api_service_get_interest**
> ImdbapiInterest i_mdb_api_service_get_interest(interest_id)

Get interest by ID

Retrieve details of a specific interest using its ID.

### Example
```python
from __future__ import print_function
import time
import py_imdb_api_dev_client
from py_imdb_api_dev_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = py_imdb_api_dev_client.InterestApi()
interest_id = 'interest_id_example' # str | Required. The ID of the interest to retrieve.

try:
    # Get interest by ID
    api_response = api_instance.i_mdb_api_service_get_interest(interest_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestApi->i_mdb_api_service_get_interest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interest_id** | **str**| Required. The ID of the interest to retrieve. | 

### Return type

[**ImdbapiInterest**](ImdbapiInterest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_interest_categories**
> ImdbapiListListInterestCategoriesResponse i_mdb_api_service_list_interest_categories()

List interest categories

Retrieve all interest categories available in the IMDb API.

### Example
```python
from __future__ import print_function
import time
import py_imdb_api_dev_client
from py_imdb_api_dev_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = py_imdb_api_dev_client.InterestApi()

try:
    # List interest categories
    api_response = api_instance.i_mdb_api_service_list_interest_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestApi->i_mdb_api_service_list_interest_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ImdbapiListListInterestCategoriesResponse**](ImdbapiListListInterestCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

