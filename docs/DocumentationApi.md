# pysbml4j.DocumentationApi

All URIs are relative to *https://virtserver.swaggerhub.com/tiede/sbml4j/1.1.4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_base_documentation**](DocumentationApi.md#get_base_documentation) | **GET** /help | Show the API help
[**get_db_status**](DocumentationApi.md#get_db_status) | **GET** /dbStatus | Get the status of the connected database
[**get_profile**](DocumentationApi.md#get_profile) | **GET** /profile | Get the active profile of sbml4j running
[**get_version**](DocumentationApi.md#get_version) | **GET** /version | Get the version of sbml4j running

# **get_base_documentation**
> object get_base_documentation()

Show the API help

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.DocumentationApi()

try:
    # Show the API help
    api_response = api_instance.get_base_documentation()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentationApi->get_base_documentation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_db_status**
> str get_db_status()

Get the status of the connected database

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.DocumentationApi()

try:
    # Get the status of the connected database
    api_response = api_instance.get_db_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentationApi->get_db_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> list[str] get_profile()

Get the active profile of sbml4j running

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.DocumentationApi()

try:
    # Get the active profile of sbml4j running
    api_response = api_instance.get_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentationApi->get_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> str get_version()

Get the version of sbml4j running

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.DocumentationApi()

try:
    # Get the version of sbml4j running
    api_response = api_instance.get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentationApi->get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

