# pysbml4j.WarehouseApi

All URIs are relative to *https://virtserver.swaggerhub.com/tiede/sbml4j/1.1.4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_database_uuid**](WarehouseApi.md#get_database_uuid) | **GET** /databaseUUID | Get the uuid of the databasenode for source with version

# **get_database_uuid**
> str get_database_uuid(organism, source, version)

Get the uuid of the databasenode for source with version

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.WarehouseApi()
organism = 'organism_example' # str | The three-letter organism code
source = 'source_example' # str | The name of the source this SBML originates from
version = 'version_example' # str | The version of the source this SBML originates from

try:
    # Get the uuid of the databasenode for source with version
    api_response = api_instance.get_database_uuid(organism, source, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseApi->get_database_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organism** | **str**| The three-letter organism code | 
 **source** | **str**| The name of the source this SBML originates from | 
 **version** | **str**| The version of the source this SBML originates from | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

