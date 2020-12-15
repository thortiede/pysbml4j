# pysbml4j.MydrugApi

All URIs are relative to *https://virtserver.swaggerhub.com/tiede/sbml4j/1.1.5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_my_drug_relations**](MydrugApi.md#add_my_drug_relations) | **POST** /networks/{UUID}/myDrug | Provide a URL to a MyDrug Neo4j Database and add Drug nodes and Drug-targets-&gt;Gene Relationships to a network

# **add_my_drug_relations**
> NetworkInventoryItem add_my_drug_relations(user, uuid, my_drug_url)

Provide a URL to a MyDrug Neo4j Database and add Drug nodes and Drug-targets->Gene Relationships to a network

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.MydrugApi()
user = 'user_example' # str | The user which requests the creation
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The UUID of the network that the myDrug Data should be added to. A copy will be created.
my_drug_url = 'my_drug_url_example' # str | A base url of a MyDrug Database including the port number

try:
    # Provide a URL to a MyDrug Neo4j Database and add Drug nodes and Drug-targets->Gene Relationships to a network
    api_response = api_instance.add_my_drug_relations(user, uuid, my_drug_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MydrugApi->add_my_drug_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user which requests the creation | 
 **uuid** | [**str**](.md)| The UUID of the network that the myDrug Data should be added to. A copy will be created. | 
 **my_drug_url** | **str**| A base url of a MyDrug Database including the port number | 

### Return type

[**NetworkInventoryItem**](NetworkInventoryItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

