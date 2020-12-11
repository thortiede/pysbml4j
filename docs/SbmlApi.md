# pysbml4j.SbmlApi

All URIs are relative to *https://virtserver.swaggerhub.com/tiede/sbml4j/1.1.4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_sbml**](SbmlApi.md#upload_sbml) | **POST** /sbml | Upload SBML Model to create a Pathway

# **upload_sbml**
> list[InlineResponse201] upload_sbml(files, user, organism, source, version)

Upload SBML Model to create a Pathway

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.SbmlApi()
files = ['files_example'] # list[str] | 
user = 'user_example' # str | The user which requests the creation
organism = 'organism_example' # str | The three-letter organism code
source = 'source_example' # str | The name of the source this SBML originates from
version = 'version_example' # str | The version of the source this SBML originates from

try:
    # Upload SBML Model to create a Pathway
    api_response = api_instance.upload_sbml(files, user, organism, source, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SbmlApi->upload_sbml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | [**list[str]**](str.md)|  | 
 **user** | **str**| The user which requests the creation | 
 **organism** | **str**| The three-letter organism code | 
 **source** | **str**| The name of the source this SBML originates from | 
 **version** | **str**| The version of the source this SBML originates from | 

### Return type

[**list[InlineResponse201]**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

