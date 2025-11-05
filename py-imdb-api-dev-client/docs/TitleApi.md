# py_imdb_api_dev_client.TitleApi

All URIs are relative to *https://api.imdbapi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**i_mdb_api_service_batch_get_titles**](TitleApi.md#i_mdb_api_service_batch_get_titles) | **GET** /titles:batchGet | Batch get titles by IDs
[**i_mdb_api_service_get_title**](TitleApi.md#i_mdb_api_service_get_title) | **GET** /titles/{titleId} | Get title by ID
[**i_mdb_api_service_get_title_box_office**](TitleApi.md#i_mdb_api_service_get_title_box_office) | **GET** /titles/{titleId}/boxOffice | Get box office information for a title
[**i_mdb_api_service_list_title_akas**](TitleApi.md#i_mdb_api_service_list_title_akas) | **GET** /titles/{titleId}/akas | List AKAs for a title
[**i_mdb_api_service_list_title_award_nominations**](TitleApi.md#i_mdb_api_service_list_title_award_nominations) | **GET** /titles/{titleId}/awardNominations | List award nominations for a title
[**i_mdb_api_service_list_title_certificates**](TitleApi.md#i_mdb_api_service_list_title_certificates) | **GET** /titles/{titleId}/certificates | List certificates for a title
[**i_mdb_api_service_list_title_company_credits**](TitleApi.md#i_mdb_api_service_list_title_company_credits) | **GET** /titles/{titleId}/companyCredits | List company credits for a title
[**i_mdb_api_service_list_title_credits**](TitleApi.md#i_mdb_api_service_list_title_credits) | **GET** /titles/{titleId}/credits | List credits for a title
[**i_mdb_api_service_list_title_episodes**](TitleApi.md#i_mdb_api_service_list_title_episodes) | **GET** /titles/{titleId}/episodes | List episodes for a title
[**i_mdb_api_service_list_title_images**](TitleApi.md#i_mdb_api_service_list_title_images) | **GET** /titles/{titleId}/images | List images for a title
[**i_mdb_api_service_list_title_parents_guide**](TitleApi.md#i_mdb_api_service_list_title_parents_guide) | **GET** /titles/{titleId}/parentsGuide | List parents guide for a title
[**i_mdb_api_service_list_title_release_dates**](TitleApi.md#i_mdb_api_service_list_title_release_dates) | **GET** /titles/{titleId}/releaseDates | List release dates for a title
[**i_mdb_api_service_list_title_seasons**](TitleApi.md#i_mdb_api_service_list_title_seasons) | **GET** /titles/{titleId}/seasons | List seasons for a title
[**i_mdb_api_service_list_title_videos**](TitleApi.md#i_mdb_api_service_list_title_videos) | **GET** /titles/{titleId}/videos | List videos for a title
[**i_mdb_api_service_list_titles**](TitleApi.md#i_mdb_api_service_list_titles) | **GET** /titles | List titles
[**i_mdb_api_service_search_titles**](TitleApi.md#i_mdb_api_service_search_titles) | **GET** /search/titles | Search titles by query


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
title_ids = ['title_ids_example'] # list[str] | List of IMDb title IDs. Maximum 5 IDs.

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
 **title_ids** | [**list[str]**](str.md)| List of IMDb title IDs. Maximum 5 IDs. | 

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

# **i_mdb_api_service_get_title_box_office**
> ImdbapiBoxOffice i_mdb_api_service_get_title_box_office(title_id)

Get box office information for a title

Retrieve the box office information associated with a specific title.

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
    # Get box office information for a title
    api_response = api_instance.i_mdb_api_service_get_title_box_office(title_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_get_title_box_office: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| Required. IMDb title ID in the format \&quot;tt1234567\&quot;. | 

### Return type

[**ImdbapiBoxOffice**](ImdbapiBoxOffice.md)

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

# **i_mdb_api_service_list_title_award_nominations**
> ImdbapiListTitleAwardNominationsResponse i_mdb_api_service_list_title_award_nominations(title_id, page_size=page_size, page_token=page_token)

List award nominations for a title

Retrieve the award nominations associated with a specific title.

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
page_size = 56 # int | Optional. The maximum number of award nominations to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. (optional)
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # List award nominations for a title
    api_response = api_instance.i_mdb_api_service_list_title_award_nominations(title_id, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_list_title_award_nominations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| Required. IMDb title ID in the format \&quot;tt1234567\&quot;. | 
 **page_size** | **int**| Optional. The maximum number of award nominations to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListTitleAwardNominationsResponse**](ImdbapiListTitleAwardNominationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_title_certificates**
> ImdbapiListTitleCertificatesResponse i_mdb_api_service_list_title_certificates(title_id)

List certificates for a title

Retrieve the certificates associated with a specific title.

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
    # List certificates for a title
    api_response = api_instance.i_mdb_api_service_list_title_certificates(title_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_list_title_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| Required. IMDb title ID in the format \&quot;tt1234567\&quot;. | 

### Return type

[**ImdbapiListTitleCertificatesResponse**](ImdbapiListTitleCertificatesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_title_company_credits**
> ImdbapiListTitleCompanyCreditsResponse i_mdb_api_service_list_title_company_credits(title_id, categories=categories, page_size=page_size, page_token=page_token)

List company credits for a title

Retrieve the company credits associated with a specific title.

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
categories = ['categories_example'] # list[str] | Optional. The categories of company credits to filter by. (optional)
page_size = 56 # int | Optional. The maximum number of company credits to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. (optional)
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # List company credits for a title
    api_response = api_instance.i_mdb_api_service_list_title_company_credits(title_id, categories=categories, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_list_title_company_credits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| Required. IMDb title ID in the format \&quot;tt1234567\&quot;. | 
 **categories** | [**list[str]**](str.md)| Optional. The categories of company credits to filter by. | [optional] 
 **page_size** | **int**| Optional. The maximum number of company credits to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListTitleCompanyCreditsResponse**](ImdbapiListTitleCompanyCreditsResponse.md)

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
categories = ['categories_example'] # list[str] | Optional. The categories of credits to filter by. (optional)
page_size = 56 # int | Optional. The maximum number of credits to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. (optional)
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
 **categories** | [**list[str]**](str.md)| Optional. The categories of credits to filter by. | [optional] 
 **page_size** | **int**| Optional. The maximum number of credits to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListTitleCreditsResponse**](ImdbapiListTitleCreditsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_title_episodes**
> ImdbapiListTitleEpisodesResponse i_mdb_api_service_list_title_episodes(title_id, season=season, page_size=page_size, page_token=page_token)

List episodes for a title

Retrieve the episodes associated with a specific title.

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
season = 'season_example' # str | Optional. The season number to filter episodes by. (optional)
page_size = 56 # int | Optional. The maximum number of episodes to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. (optional)
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # List episodes for a title
    api_response = api_instance.i_mdb_api_service_list_title_episodes(title_id, season=season, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_list_title_episodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| Required. IMDb title ID in the format \&quot;tt1234567\&quot;. | 
 **season** | **str**| Optional. The season number to filter episodes by. | [optional] 
 **page_size** | **int**| Optional. The maximum number of episodes to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListTitleEpisodesResponse**](ImdbapiListTitleEpisodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_title_images**
> ImdbapiListTitleImagesResponse i_mdb_api_service_list_title_images(title_id, types=types, page_size=page_size, page_token=page_token)

List images for a title

Retrieve the images associated with a specific title.

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
types = ['types_example'] # list[str] | Optional. The types of images to filter by. If not specified, all types are returned. (optional)
page_size = 56 # int | Optional. The maximum number of images to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. (optional)
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # List images for a title
    api_response = api_instance.i_mdb_api_service_list_title_images(title_id, types=types, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_list_title_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| Required. IMDb title ID in the format \&quot;tt1234567\&quot;. | 
 **types** | [**list[str]**](str.md)| Optional. The types of images to filter by. If not specified, all types are returned. | [optional] 
 **page_size** | **int**| Optional. The maximum number of images to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListTitleImagesResponse**](ImdbapiListTitleImagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_title_parents_guide**
> ImdbapiListTitleParentsGuideResponse i_mdb_api_service_list_title_parents_guide(title_id)

List parents guide for a title

Retrieve the parents guide associated with a specific title.

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
    # List parents guide for a title
    api_response = api_instance.i_mdb_api_service_list_title_parents_guide(title_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_list_title_parents_guide: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| Required. IMDb title ID in the format \&quot;tt1234567\&quot;. | 

### Return type

[**ImdbapiListTitleParentsGuideResponse**](ImdbapiListTitleParentsGuideResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_title_release_dates**
> ImdbapiListTitleReleaseDatesResponse i_mdb_api_service_list_title_release_dates(title_id, page_size=page_size, page_token=page_token)

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
page_size = 56 # int | Optional. The maximum number of credits to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. (optional)
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # List release dates for a title
    api_response = api_instance.i_mdb_api_service_list_title_release_dates(title_id, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_list_title_release_dates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| Required. IMDb title ID in the format \&quot;tt1234567\&quot;. | 
 **page_size** | **int**| Optional. The maximum number of credits to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListTitleReleaseDatesResponse**](ImdbapiListTitleReleaseDatesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_title_seasons**
> ImdbapiListTitleSeasonsResponse i_mdb_api_service_list_title_seasons(title_id)

List seasons for a title

Retrieve the seasons associated with a specific title.

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
    # List seasons for a title
    api_response = api_instance.i_mdb_api_service_list_title_seasons(title_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_list_title_seasons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| Required. IMDb title ID in the format \&quot;tt1234567\&quot;. | 

### Return type

[**ImdbapiListTitleSeasonsResponse**](ImdbapiListTitleSeasonsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_title_videos**
> ImdbapiListTitleVideosResponse i_mdb_api_service_list_title_videos(title_id, types=types, page_size=page_size, page_token=page_token)

List videos for a title

Retrieve the videos associated with a specific title.

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
types = ['types_example'] # list[str] | Optional. The types of videos to filter by. If not specified, all types are returned. (optional)
page_size = 56 # int | Optional. The maximum number of videos to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. (optional)
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # List videos for a title
    api_response = api_instance.i_mdb_api_service_list_title_videos(title_id, types=types, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_list_title_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_id** | **str**| Required. IMDb title ID in the format \&quot;tt1234567\&quot;. | 
 **types** | [**list[str]**](str.md)| Optional. The types of videos to filter by. If not specified, all types are returned. | [optional] 
 **page_size** | **int**| Optional. The maximum number of videos to return per page. If not specified, a default value will be used.  The value must be between 1 and 50. Default is 20. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListTitleVideosResponse**](ImdbapiListTitleVideosResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_list_titles**
> ImdbapiListTitlesResponse i_mdb_api_service_list_titles(types=types, genres=genres, country_codes=country_codes, language_codes=language_codes, name_ids=name_ids, interest_ids=interest_ids, start_year=start_year, end_year=end_year, min_vote_count=min_vote_count, max_vote_count=max_vote_count, min_aggregate_rating=min_aggregate_rating, max_aggregate_rating=max_aggregate_rating, sort_by=sort_by, sort_order=sort_order, page_token=page_token)

List titles

Retrieve a list of titles with optional filters.

### Example
```python
from __future__ import print_function
import time
import py_imdb_api_dev_client
from py_imdb_api_dev_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = py_imdb_api_dev_client.TitleApi()
types = ['types_example'] # list[str] | Optional. The type of titles to filter by. If not specified, all types are returned.   - MOVIE: Represents a movie title.  - TV_SERIES: Represents a TV series title.  - TV_MINI_SERIES: Represents a TV mini-series title.  - TV_SPECIAL: Represents a TV special title.  - TV_MOVIE: Represents a TV movie title.  - SHORT: Represents a short title.  - VIDEO: Represents a video title.  - VIDEO_GAME: Represents a video game title. (optional)
genres = ['genres_example'] # list[str] | Optional. The genres to filter titles by. If not specified, titles from all genres are returned. (optional)
country_codes = ['country_codes_example'] # list[str] | Optional. The ISO 3166-1 alpha-2 country codes to filter titles by. If not specified, titles from all countries are returned. Example: \"US\" for United States, \"GB\" for United Kingdom. (optional)
language_codes = ['language_codes_example'] # list[str] | Optional. The ISO 639-1 or ISO 639-2 language codes to filter titles by. If not specified, titles in all languages are returned. (optional)
name_ids = ['name_ids_example'] # list[str] | Optional. The IDs of names to filter titles by. (optional)
interest_ids = ['interest_ids_example'] # list[str] | Optional. The IDs of interests to filter titles by. If not specified, titles associated with all interests are returned. (optional)
start_year = 56 # int | Optional. The start year for filtering titles. (optional)
end_year = 56 # int | Optional. The end year for filtering titles. (optional)
min_vote_count = 56 # int | Optional. The minimum number of votes a title must have to be included. If not specified, titles with any number of votes are included. The value must be between 0 and 1,000,000,000. Default is 0. (optional)
max_vote_count = 56 # int | Optional. The maximum number of votes a title can have to be included. If not specified, titles with any number of votes are included. The value must be between 0 and 1,000,000,000. (optional)
min_aggregate_rating = 3.4 # float | Optional. The minimum rating a title must have to be included. If not specified, titles with any rating are included. The value must be between 0.0 and 10.0. (optional)
max_aggregate_rating = 3.4 # float | Optional. The maximum rating a title can have to be included. If not specified, titles with any rating are included. The value must be between 0.0 and 10.0. (optional)
sort_by = 'sort_by_example' # str | Optional. The sorting order for the titles. If not specified, titles are sorted by popularity.   - SORT_BY_POPULARITY: Sort by popularity. This is used to rank titles based on their popularity, which can be influenced by various factors such as viewership, ratings, and cultural impact.  - SORT_BY_RELEASE_DATE: Sort by release date. This is used to rank titles based on their release dates, with newer titles typically appearing before older ones.  - SORT_BY_USER_RATING: Sort by user rating. This is used to rank titles based on the average user rating, which reflects the overall audience reception.  - SORT_BY_USER_RATING_COUNT: Sort by user rating count. This is used to rank titles based on the number of user ratings they have received, which can indicate the level of engagement or popularity among viewers.  - SORT_BY_YEAR: Sort by year. This is used to rank titles based on their release year, with newer titles typically appearing before older ones. (optional)
sort_order = 'sort_order_example' # str | Optional. The sorting order for the titles. If not specified, titles are sorted in ascending order.   - ASC: Sort in ascending order.  - DESC: Sort in descending order. (optional)
page_token = 'page_token_example' # str | Optional. Token for pagination, if applicable. (optional)

try:
    # List titles
    api_response = api_instance.i_mdb_api_service_list_titles(types=types, genres=genres, country_codes=country_codes, language_codes=language_codes, name_ids=name_ids, interest_ids=interest_ids, start_year=start_year, end_year=end_year, min_vote_count=min_vote_count, max_vote_count=max_vote_count, min_aggregate_rating=min_aggregate_rating, max_aggregate_rating=max_aggregate_rating, sort_by=sort_by, sort_order=sort_order, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_list_titles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**list[str]**](str.md)| Optional. The type of titles to filter by. If not specified, all types are returned.   - MOVIE: Represents a movie title.  - TV_SERIES: Represents a TV series title.  - TV_MINI_SERIES: Represents a TV mini-series title.  - TV_SPECIAL: Represents a TV special title.  - TV_MOVIE: Represents a TV movie title.  - SHORT: Represents a short title.  - VIDEO: Represents a video title.  - VIDEO_GAME: Represents a video game title. | [optional] 
 **genres** | [**list[str]**](str.md)| Optional. The genres to filter titles by. If not specified, titles from all genres are returned. | [optional] 
 **country_codes** | [**list[str]**](str.md)| Optional. The ISO 3166-1 alpha-2 country codes to filter titles by. If not specified, titles from all countries are returned. Example: \&quot;US\&quot; for United States, \&quot;GB\&quot; for United Kingdom. | [optional] 
 **language_codes** | [**list[str]**](str.md)| Optional. The ISO 639-1 or ISO 639-2 language codes to filter titles by. If not specified, titles in all languages are returned. | [optional] 
 **name_ids** | [**list[str]**](str.md)| Optional. The IDs of names to filter titles by. | [optional] 
 **interest_ids** | [**list[str]**](str.md)| Optional. The IDs of interests to filter titles by. If not specified, titles associated with all interests are returned. | [optional] 
 **start_year** | **int**| Optional. The start year for filtering titles. | [optional] 
 **end_year** | **int**| Optional. The end year for filtering titles. | [optional] 
 **min_vote_count** | **int**| Optional. The minimum number of votes a title must have to be included. If not specified, titles with any number of votes are included. The value must be between 0 and 1,000,000,000. Default is 0. | [optional] 
 **max_vote_count** | **int**| Optional. The maximum number of votes a title can have to be included. If not specified, titles with any number of votes are included. The value must be between 0 and 1,000,000,000. | [optional] 
 **min_aggregate_rating** | **float**| Optional. The minimum rating a title must have to be included. If not specified, titles with any rating are included. The value must be between 0.0 and 10.0. | [optional] 
 **max_aggregate_rating** | **float**| Optional. The maximum rating a title can have to be included. If not specified, titles with any rating are included. The value must be between 0.0 and 10.0. | [optional] 
 **sort_by** | **str**| Optional. The sorting order for the titles. If not specified, titles are sorted by popularity.   - SORT_BY_POPULARITY: Sort by popularity. This is used to rank titles based on their popularity, which can be influenced by various factors such as viewership, ratings, and cultural impact.  - SORT_BY_RELEASE_DATE: Sort by release date. This is used to rank titles based on their release dates, with newer titles typically appearing before older ones.  - SORT_BY_USER_RATING: Sort by user rating. This is used to rank titles based on the average user rating, which reflects the overall audience reception.  - SORT_BY_USER_RATING_COUNT: Sort by user rating count. This is used to rank titles based on the number of user ratings they have received, which can indicate the level of engagement or popularity among viewers.  - SORT_BY_YEAR: Sort by year. This is used to rank titles based on their release year, with newer titles typically appearing before older ones. | [optional] 
 **sort_order** | **str**| Optional. The sorting order for the titles. If not specified, titles are sorted in ascending order.   - ASC: Sort in ascending order.  - DESC: Sort in descending order. | [optional] 
 **page_token** | **str**| Optional. Token for pagination, if applicable. | [optional] 

### Return type

[**ImdbapiListTitlesResponse**](ImdbapiListTitlesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_mdb_api_service_search_titles**
> ImdbapiSearchTitlesResponse i_mdb_api_service_search_titles(query, limit=limit)

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
limit = 56 # int | Optional. Limit the number of results returned. Maximum is 50. (optional)

try:
    # Search titles by query
    api_response = api_instance.i_mdb_api_service_search_titles(query, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitleApi->i_mdb_api_service_search_titles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Required. The search query for titles. | 
 **limit** | **int**| Optional. Limit the number of results returned. Maximum is 50. | [optional] 

### Return type

[**ImdbapiSearchTitlesResponse**](ImdbapiSearchTitlesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

