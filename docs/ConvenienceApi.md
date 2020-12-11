# pysbml4j.ConvenienceApi

All URIs are relative to *https://virtserver.swaggerhub.com/tiede/sbml4j/1.1.4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_overview_network**](ConvenienceApi.md#create_overview_network) | **POST** /overview | upload a set of genes and get a network connecting them
[**get_overview_network**](ConvenienceApi.md#get_overview_network) | **GET** /overview | retrieve a previously created overview network for a user by its name

# **create_overview_network**
> NetworkInventoryItem create_overview_network(body, user)

upload a set of genes and get a network connecting them

This endpoint creates an overview network that contains all available genes from the input gene list. The given genes will be annotated with  the boolean given by the field annotationName. The overview network will contain all available relationships between genes and metabolites that are part of the network. The endpoint returns a networkInventoryItem of the created network.  It can be retrieved using the UUID in the GET /network endpoint. If baseNetworkUUID is omitted, the full model will be used. 

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.ConvenienceApi()
body = pysbml4j.OverviewNetworkItem() # OverviewNetworkItem | The genes of interest for which to build an overview network. The network is based on the network with uuid 'baseNetworkUUID'. If 'baseNetworkUUID' is omitted, the default network will be used.

user = 'user_example' # str | The user which requests the creation

try:
    # upload a set of genes and get a network connecting them
    api_response = api_instance.create_overview_network(body, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvenienceApi->create_overview_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OverviewNetworkItem**](OverviewNetworkItem.md)| The genes of interest for which to build an overview network. The network is based on the network with uuid &#x27;baseNetworkUUID&#x27;. If &#x27;baseNetworkUUID&#x27; is omitted, the default network will be used.
 | 
 **user** | **str**| The user which requests the creation | 

### Return type

[**NetworkInventoryItem**](NetworkInventoryItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overview_network**
> str get_overview_network(user, name)

retrieve a previously created overview network for a user by its name

Attempts to retrieve an overview network by the network name that was  given during creation using POST /overview. If the network is available (created and active) it gets returned in  graphml format. If the network is still being created (not active yet) the endpoint returns a 404 error. If the network could not be created, the endpoint returns a 403 error. 

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: network_auth
configuration = pysbml4j.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pysbml4j.ConvenienceApi(pysbml4j.ApiClient(configuration))
user = 'user_example' # str | The user which requests the creation
name = 'name_example' # str | The network name to get

try:
    # retrieve a previously created overview network for a user by its name
    api_response = api_instance.get_overview_network(user, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvenienceApi->get_overview_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user which requests the creation | 
 **name** | **str**| The network name to get | 

### Return type

**str**

### Authorization

[network_auth](../README.md#network_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

