# py_imdb_api_dev_client.NameApi

All URIs are relative to *https://api.imdbapi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**i_mdb_api_service_batch_get_names**](NameApi.md#i_mdb_api_service_batch_get_names) | **GET** /names:batchGet | Batch get names by IDs
[**i_mdb_api_service_get_name**](NameApi.md#i_mdb_api_service_get_name) | **GET** /names/{nameId} | Get name by ID
[**i_mdb_api_service_list_name_filmography**](NameApi.md#i_mdb_api_service_list_name_filmography) | **GET** /names/{nameId}/filmography | List filmography for a name
[**i_mdb_api_service_list_name_images**](NameApi.md#i_mdb_api_service_list_name_images) | **GET** /names/{nameId}/images | List images for a name
[**i_mdb_api_service_list_name_relationships**](NameApi.md#i_mdb_api_service_list_name_relationships) | **GET** /names/{nameId}/relationships | List relationships for a name
[**i_mdb_api_service_list_name_trivia**](NameApi.md#i_mdb_api_service_list_name_trivia) | **GET** /names/{nameId}/trivia | List trivia for a name
[**i_mdb_api_service_list_star_meters**](NameApi.md#i_mdb_api_service_list_star_meters) | **GET** /chart/starmeter | List star meter rankings


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
name_ids = ['name_ids_example'] # list[str] | Required. List of IMDb name IDs in the format \"nm1234567\". The maximum number of IDs is 5.

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
 **name_ids** | [**list[str]**](str.md)| Required. List of IMDb name IDs in the format \&quot;nm1234567\&quot;. The maximum number of IDs is 5. | 

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

# **i_mdb_api_service_list_name_filmography**
> ImdbapiListNameFilmographyResponse i_mdb_api_service_list_name_filmography(name_id, categories=categories, page_size=page_size, page_token=page_token)

List filmography for a name

Retrieve the filmography associated with a specific name.

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
categories = ['categories_example'] # list[str] | Optional. The categories of credits to filter by. If not specified, all categories are returned. (optional)
page_size = 56 # int | Optional. The maximum number of credits to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. (optional)
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # List filmography for a name
    api_response = api_instance.i_mdb_api_service_list_name_filmography(name_id, categories=categories, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NameApi->i_mdb_api_service_list_name_filmography: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_id** | **str**| Required. IMDB name ID in the format \&quot;nm1234567\&quot;. | 
 **categories** | [**list[str]**](str.md)| Optional. The categories of credits to filter by. If not specified, all categories are returned. | [optional] 
 **page_size** | **int**| Optional. The maximum number of credits to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListNameFilmographyResponse**](ImdbapiListNameFilmographyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_name_images**
> ImdbapiListNameImagesResponse i_mdb_api_service_list_name_images(name_id, types=types, page_size=page_size, page_token=page_token)

List images for a name

Retrieve the images associated with a specific name.

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
types = ['types_example'] # list[str] | Optional. The types of images to filter by. If not specified, all types are returned. (optional)
page_size = 56 # int | Optional. The maximum number of images to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. (optional)
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # List images for a name
    api_response = api_instance.i_mdb_api_service_list_name_images(name_id, types=types, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NameApi->i_mdb_api_service_list_name_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_id** | **str**| Required. IMDB name ID in the format \&quot;nm1234567\&quot;. | 
 **types** | [**list[str]**](str.md)| Optional. The types of images to filter by. If not specified, all types are returned. | [optional] 
 **page_size** | **int**| Optional. The maximum number of images to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListNameImagesResponse**](ImdbapiListNameImagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_name_relationships**
> ImdbapiListNameRelationshipsResponse i_mdb_api_service_list_name_relationships(name_id)

List relationships for a name

Retrieve the relationships associated with a specific name.

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
    # List relationships for a name
    api_response = api_instance.i_mdb_api_service_list_name_relationships(name_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NameApi->i_mdb_api_service_list_name_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_id** | **str**| Required. IMDB name ID in the format \&quot;nm1234567\&quot;. | 

### Return type

[**ImdbapiListNameRelationshipsResponse**](ImdbapiListNameRelationshipsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_name_trivia**
> ImdbapiListNameTriviaResponse i_mdb_api_service_list_name_trivia(name_id, page_size=page_size, page_token=page_token)

List trivia for a name

Retrieve the trivia associated with a specific name.

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
page_size = 56 # int | Optional. The maximum number of trivia entries to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. (optional)
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # List trivia for a name
    api_response = api_instance.i_mdb_api_service_list_name_trivia(name_id, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NameApi->i_mdb_api_service_list_name_trivia: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_id** | **str**| Required. IMDB name ID in the format \&quot;nm1234567\&quot;. | 
 **page_size** | **int**| Optional. The maximum number of trivia entries to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListNameTriviaResponse**](ImdbapiListNameTriviaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_star_meters**
> ImdbapiListStarMetersResponse i_mdb_api_service_list_star_meters(page_token=page_token)

List star meter rankings

Retrieve the star meter rankings for names.

### Example
```python
from __future__ import print_function
import time
import py_imdb_api_dev_client
from py_imdb_api_dev_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = py_imdb_api_dev_client.NameApi()
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # List star meter rankings
    api_response = api_instance.i_mdb_api_service_list_star_meters(page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NameApi->i_mdb_api_service_list_star_meters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListStarMetersResponse**](ImdbapiListStarMetersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

