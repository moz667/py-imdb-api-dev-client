# py_imdb_api_dev_client.TitleApi

All URIs are relative to *https://rest.imdbapi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**i_mdb_api_service_batch_get_titles**](TitleApi.md#i_mdb_api_service_batch_get_titles) | **GET** /v2/titles:batch_get | Batch get titles by IDs
[**i_mdb_api_service_get_title**](TitleApi.md#i_mdb_api_service_get_title) | **GET** /v2/titles/{title_id} | Get title by ID
[**i_mdb_api_service_list_title_akas**](TitleApi.md#i_mdb_api_service_list_title_akas) | **GET** /v2/titles/{title_id}/akas | List AKAs for a title
[**i_mdb_api_service_list_title_credits**](TitleApi.md#i_mdb_api_service_list_title_credits) | **GET** /v2/titles/{title_id}/credits | List credits for a title
[**i_mdb_api_service_list_title_release_dates**](TitleApi.md#i_mdb_api_service_list_title_release_dates) | **GET** /v2/titles/{title_id}/release_dates | List release dates for a title
[**i_mdb_api_service_search_titles**](TitleApi.md#i_mdb_api_service_search_titles) | **GET** /v2/search/titles | Search titles by query


# **i_mdb_api_service_batch_get_titles**
> ImdbapiBatchGetTitlesResponse i_mdb_api_service_batch_get_titles(title_ids)

Batch get titles by IDs

Retrieve details of multiple titles using their IMDb IDs.

### Example
```python
from __future__ import print_function
import time
import py_imdb_api_dev_client
from py_imdb_api_dev_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = py_imdb_api_dev_client.TitleApi()
title_ids = ['title_ids_example'] # list[str] | List of IMDb title IDs. Maximum 10 IDs.

try:
    # Batch get titles by IDs
    api_response = api_instance.i_mdb_api_service_batch_get_titles(title_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_batch_get_titles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_ids** | [**list[str]**](str.md)| List of IMDb title IDs. Maximum 10 IDs. | 

### Return type

[**ImdbapiBatchGetTitlesResponse**](ImdbapiBatchGetTitlesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_get_title**
> ImdbapiTitle i_mdb_api_service_get_title(title_id)

Get title by ID

Retrieve a title's details using its IMDb ID.

### Example
```python
from __future__ import print_function
import time
import py_imdb_api_dev_client
from py_imdb_api_dev_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = py_imdb_api_dev_client.TitleApi()
title_id = 'title_id_example' # str | The IMDb title ID in the format 'tt1234567'.

try:
    # Get title by ID
    api_response = api_instance.i_mdb_api_service_get_title(title_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_get_title: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| The IMDb title ID in the format &#39;tt1234567&#39;. | 

### Return type

[**ImdbapiTitle**](ImdbapiTitle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_title_akas**
> ImdbapiListTitleAKAsResponse i_mdb_api_service_list_title_akas(title_id)

List AKAs for a title

Retrieve the alternative titles (AKAs) associated with a specific title.

### Example
```python
from __future__ import print_function
import time
import py_imdb_api_dev_client
from py_imdb_api_dev_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = py_imdb_api_dev_client.TitleApi()
title_id = 'title_id_example' # str | Required. IMDb title ID in the format \"tt1234567\".

try:
    # List AKAs for a title
    api_response = api_instance.i_mdb_api_service_list_title_akas(title_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_list_title_akas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| Required. IMDb title ID in the format \&quot;tt1234567\&quot;. | 

### Return type

[**ImdbapiListTitleAKAsResponse**](ImdbapiListTitleAKAsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_title_credits**
> ImdbapiListTitleCreditsResponse i_mdb_api_service_list_title_credits(title_id, categories=categories, page_size=page_size, page_token=page_token)

List credits for a title

Retrieve the credits associated with a specific title.

### Example
```python
from __future__ import print_function
import time
import py_imdb_api_dev_client
from py_imdb_api_dev_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = py_imdb_api_dev_client.TitleApi()
title_id = 'title_id_example' # str | Required. IMDb title ID in the format \"tt1234567\".
categories = ['categories_example'] # list[str] | Optional. Filter for credit categories.   - CAST: The CAST category. This enum value is used to represent both ACTOR and ACTRESS roles.  - ACTOR: The ACTOR category  - ACTRESS: The ACTRESS category  - DIRECTOR: The DIRECTOR category  - WRITER: The WRITER category (optional)
page_size = 56 # int | Optional. The maximum number of credits to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 10. (optional)
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # List credits for a title
    api_response = api_instance.i_mdb_api_service_list_title_credits(title_id, categories=categories, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_list_title_credits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| Required. IMDb title ID in the format \&quot;tt1234567\&quot;. | 
 **categories** | [**list[str]**](str.md)| Optional. Filter for credit categories.   - CAST: The CAST category. This enum value is used to represent both ACTOR and ACTRESS roles.  - ACTOR: The ACTOR category  - ACTRESS: The ACTRESS category  - DIRECTOR: The DIRECTOR category  - WRITER: The WRITER category | [optional] 
 **page_size** | **int**| Optional. The maximum number of credits to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 10. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListTitleCreditsResponse**](ImdbapiListTitleCreditsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_title_release_dates**
> ImdbapiListTitleReleaseDatesResponse i_mdb_api_service_list_title_release_dates(title_id)

List release dates for a title

Retrieve the release dates associated with a specific title.

### Example
```python
from __future__ import print_function
import time
import py_imdb_api_dev_client
from py_imdb_api_dev_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = py_imdb_api_dev_client.TitleApi()
title_id = 'title_id_example' # str | Required. IMDb title ID in the format \"tt1234567\".

try:
    # List release dates for a title
    api_response = api_instance.i_mdb_api_service_list_title_release_dates(title_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_list_title_release_dates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| Required. IMDb title ID in the format \&quot;tt1234567\&quot;. | 

### Return type

[**ImdbapiListTitleReleaseDatesResponse**](ImdbapiListTitleReleaseDatesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_search_titles**
> ImdbapiSearchTitlesResponse i_mdb_api_service_search_titles(query, page_size=page_size, page_token=page_token)

Search titles by query

Search for titles using a query string.

### Example
```python
from __future__ import print_function
import time
import py_imdb_api_dev_client
from py_imdb_api_dev_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = py_imdb_api_dev_client.TitleApi()
query = 'query_example' # str | Required. The search query for titles.
page_size = 56 # int | Optional. The maximum number of titles to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 10. (optional)
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # Search titles by query
    api_response = api_instance.i_mdb_api_service_search_titles(query, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_search_titles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Required. The search query for titles. | 
 **page_size** | **int**| Optional. The maximum number of titles to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 10. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiSearchTitlesResponse**](ImdbapiSearchTitlesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

