# py_imdb_api_dev_client.NameApi

All URIs are relative to *https://rest.imdbapi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**i_mdb_api_service_batch_get_names**](NameApi.md#i_mdb_api_service_batch_get_names) | **GET** /v2/names:batch_get | Batch get names by IDs
[**i_mdb_api_service_get_name**](NameApi.md#i_mdb_api_service_get_name) | **GET** /v2/names/{name_id} | Get name by ID
[**i_mdb_api_service_list_name_known_for**](NameApi.md#i_mdb_api_service_list_name_known_for) | **GET** /v2/names/{name_id}/known_for | List known for credits for a name


# **i_mdb_api_service_batch_get_names**
> ImdbapiBatchGetNamesResponse i_mdb_api_service_batch_get_names(name_ids)

Batch get names by IDs

Retrieve details of multiple names using their IMDb IDs.

### Example
```python
from __future__ import print_function
import time
import py_imdb_api_dev_client
from py_imdb_api_dev_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = py_imdb_api_dev_client.NameApi()
name_ids = ['name_ids_example'] # list[str] | List of IMDb name IDs. Maximum 10 IDs.

try:
    # Batch get names by IDs
    api_response = api_instance.i_mdb_api_service_batch_get_names(name_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NameApi->i_mdb_api_service_batch_get_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_ids** | [**list[str]**](str.md)| List of IMDb name IDs. Maximum 10 IDs. | 

### Return type

[**ImdbapiBatchGetNamesResponse**](ImdbapiBatchGetNamesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_get_name**
> ImdbapiName i_mdb_api_service_get_name(name_id)

Get name by ID

Retrieve a name's details using its IMDb ID.

### Example
```python
from __future__ import print_function
import time
import py_imdb_api_dev_client
from py_imdb_api_dev_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = py_imdb_api_dev_client.NameApi()
name_id = 'name_id_example' # str | Required. IMDB name ID in the format \"nm1234567\".

try:
    # Get name by ID
    api_response = api_instance.i_mdb_api_service_get_name(name_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NameApi->i_mdb_api_service_get_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_id** | **str**| Required. IMDB name ID in the format \&quot;nm1234567\&quot;. | 

### Return type

[**ImdbapiName**](ImdbapiName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_name_known_for**
> ImdbapiListNameKnownForResponse i_mdb_api_service_list_name_known_for(name_id, page_size=page_size, page_token=page_token)

List known for credits for a name

Retrieve the 'known for' credits associated with a specific name.

### Example
```python
from __future__ import print_function
import time
import py_imdb_api_dev_client
from py_imdb_api_dev_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = py_imdb_api_dev_client.NameApi()
name_id = 'name_id_example' # str | Required. IMDB name ID in the format \"nm1234567\".
page_size = 56 # int | Optional. The maximum number of credits to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 10. (optional)
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # List known for credits for a name
    api_response = api_instance.i_mdb_api_service_list_name_known_for(name_id, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NameApi->i_mdb_api_service_list_name_known_for: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_id** | **str**| Required. IMDB name ID in the format \&quot;nm1234567\&quot;. | 
 **page_size** | **int**| Optional. The maximum number of credits to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 10. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListNameKnownForResponse**](ImdbapiListNameKnownForResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

