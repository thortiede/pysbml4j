# pysbml4j.PathwaysApi

All URIs are relative to *https://virtserver.swaggerhub.com/tiede/sbml4j/1.1.5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pathway_collection**](PathwaysApi.md#create_pathway_collection) | **POST** /pathwayCollection | Create a collectionPathway from the submitted pathways
[**list_all_pathway_uui_ds**](PathwaysApi.md#list_all_pathway_uui_ds) | **GET** /pathwayUUIDs | List UUIDs of available pathways
[**list_all_pathways**](PathwaysApi.md#list_all_pathways) | **GET** /pathways | List available pathways
[**map_pathway**](PathwaysApi.md#map_pathway) | **POST** /mapping/{UUID} | Map pathwayContents on a new network representation

# **create_pathway_collection**
> str create_pathway_collection(body, user)

Create a collectionPathway from the submitted pathways

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.PathwaysApi()
body = pysbml4j.PathwayCollectionCreationItem() # PathwayCollectionCreationItem | List of pathwayUUIDs and a databaseUUID to create the collection for
user = 'user_example' # str | The user which requests the creation

try:
    # Create a collectionPathway from the submitted pathways
    api_response = api_instance.create_pathway_collection(body, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathwaysApi->create_pathway_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PathwayCollectionCreationItem**](PathwayCollectionCreationItem.md)| List of pathwayUUIDs and a databaseUUID to create the collection for | 
 **user** | **str**| The user which requests the creation | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_pathway_uui_ds**
> list[str] list_all_pathway_uui_ds(user, hide_collections=hide_collections)

List UUIDs of available pathways

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.PathwaysApi()
user = 'user_example' # str | The user which requests listing of their pathways
hide_collections = false # bool | Do hide Collection Pathways in the output (optional) (default to false)

try:
    # List UUIDs of available pathways
    api_response = api_instance.list_all_pathway_uui_ds(user, hide_collections=hide_collections)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathwaysApi->list_all_pathway_uui_ds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user which requests listing of their pathways | 
 **hide_collections** | **bool**| Do hide Collection Pathways in the output | [optional] [default to false]

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_pathways**
> list[PathwayInventoryItem] list_all_pathways(user, hide_collections=hide_collections)

List available pathways

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.PathwaysApi()
user = 'user_example' # str | The user which requests listing of their pathways
hide_collections = false # bool | Do hide Collection Pathways in the output (optional) (default to false)

try:
    # List available pathways
    api_response = api_instance.list_all_pathways(user, hide_collections=hide_collections)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathwaysApi->list_all_pathways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user which requests listing of their pathways | 
 **hide_collections** | **bool**| Do hide Collection Pathways in the output | [optional] [default to false]

### Return type

[**list[PathwayInventoryItem]**](PathwayInventoryItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_pathway**
> WarehouseInventoryItem map_pathway(user, uuid, mapping_type)

Map pathwayContents on a new network representation

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.PathwaysApi()
user = 'user_example' # str | The user which requests the creation
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The UUID of the pathway to be mapped
mapping_type = 'mapping_type_example' # str | The type of mapping to create

try:
    # Map pathwayContents on a new network representation
    api_response = api_instance.map_pathway(user, uuid, mapping_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathwaysApi->map_pathway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user which requests the creation | 
 **uuid** | [**str**](.md)| The UUID of the pathway to be mapped | 
 **mapping_type** | **str**| The type of mapping to create | 

### Return type

[**WarehouseInventoryItem**](WarehouseInventoryItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

