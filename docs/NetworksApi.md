# pysbml4j.NetworksApi

All URIs are relative to *https://virtserver.swaggerhub.com/tiede/sbml4j/1.1.4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_annotation_to_network**](NetworksApi.md#add_annotation_to_network) | **POST** /networks/{UUID}/annotation | Add annotation to network nodes and/or relationships. Results in the creation of a new network entity, keeping the entity with UUID unchanged. 
[**add_my_drug_relations**](NetworksApi.md#add_my_drug_relations) | **POST** /networks/{UUID}/myDrug | Provide a URL to a MyDrug Neo4j Database and add Drug nodes and Drug-targets-&gt;Gene Relationships to a network
[**copy_network**](NetworksApi.md#copy_network) | **POST** /networks/{UUID} | Create a copy of the network with uuid UUID
[**delete_network**](NetworksApi.md#delete_network) | **DELETE** /networks/{UUID} | Request the deletion of a network
[**filter_network**](NetworksApi.md#filter_network) | **POST** /networks/{UUID}/filter | Filter a network according to the request body options. Results in the creation of a new network entity, keeping the entity with UUID unchanged.
[**get_context**](NetworksApi.md#get_context) | **GET** /networks/{UUID}/context | Get network context of one or multiple genes in the network with uuid {UUID}
[**get_network**](NetworksApi.md#get_network) | **GET** /networks/{UUID} | Retrieve the contents of a network
[**get_network_options**](NetworksApi.md#get_network_options) | **GET** /networks/{UUID}/options | Get available options for network
[**list_all_networks**](NetworksApi.md#list_all_networks) | **GET** /networks | List available networks
[**post_context**](NetworksApi.md#post_context) | **POST** /networks/{UUID}/context | Create network context of one or multiple genes in the network with uuid {UUID}

# **add_annotation_to_network**
> NetworkInventoryItem add_annotation_to_network(body, user, uuid, derive=derive)

Add annotation to network nodes and/or relationships. Results in the creation of a new network entity, keeping the entity with UUID unchanged. 

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
api_instance = pysbml4j.NetworksApi(pysbml4j.ApiClient(configuration))
body = pysbml4j.AnnotationItem() # AnnotationItem | The fields of the AnnotationItem are used to create annotations in a network as follows:

Must provide 
- either all fields associated with nodes (nodeAnnotation, nodeAnnotationName, nodeAnnotationType)
- or all fields associated wth relations (relationAnnotation, relationAnnotationName, relationAnnotationType) 
- or both.

Fields related to nodes:
- nodeAnnotationName denotes the name under which the annotations in the nodeAnnotation field of the request body are attached to nodes
 
- nodeAnnotationType is used as type with which the annotations in the nodeAnnotation field of the request body are attached to nodes. Is also used to read out the annotation in said format when extracting network
 
- nodeAnnotation is a dictionary of "node-symbol": "annotation" - pairs where node-symbol must match one of the node symbols in the network (see field nodeSymbols in FilterOptions); the annotation is added to the node under the name defined in nodeAnnotationName using the type in nodeAnnotationType
 

 
Fields related to relations:
- relationAnnotationName denotes the name under which the annotations in the relationAnnotation field of the request body are attached to relations
 
- relationAnnotationType is used as type with which the annotations in the relationAnnotation field of the request body are attached to relations. Is also used to read out the annotation in said format when extracting network
- relationAnnotation is a dictionary of "relation-symbol": "annotation" - pairs where realation-symbol must match one of the relation symbols in the network (see field relationSymbols in FilterOptions); the annotation is added to the relation under the name defined in relationAnnotationName using the type in relationAnnotationType

user = 'user_example' # str | The user which requests the creation
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The UUID of the parent network to derive a new network from
derive = true # bool | Flag whether to derive a new network and add annotation to it (true) or add annotation to existing network without deriving subnetwork (false) (optional) (default to true)

try:
    # Add annotation to network nodes and/or relationships. Results in the creation of a new network entity, keeping the entity with UUID unchanged. 
    api_response = api_instance.add_annotation_to_network(body, user, uuid, derive=derive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->add_annotation_to_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnnotationItem**](AnnotationItem.md)| The fields of the AnnotationItem are used to create annotations in a network as follows:

Must provide 
- either all fields associated with nodes (nodeAnnotation, nodeAnnotationName, nodeAnnotationType)
- or all fields associated wth relations (relationAnnotation, relationAnnotationName, relationAnnotationType) 
- or both.

Fields related to nodes:
- nodeAnnotationName denotes the name under which the annotations in the nodeAnnotation field of the request body are attached to nodes
 
- nodeAnnotationType is used as type with which the annotations in the nodeAnnotation field of the request body are attached to nodes. Is also used to read out the annotation in said format when extracting network
 
- nodeAnnotation is a dictionary of &quot;node-symbol&quot;: &quot;annotation&quot; - pairs where node-symbol must match one of the node symbols in the network (see field nodeSymbols in FilterOptions); the annotation is added to the node under the name defined in nodeAnnotationName using the type in nodeAnnotationType
 

 
Fields related to relations:
- relationAnnotationName denotes the name under which the annotations in the relationAnnotation field of the request body are attached to relations
 
- relationAnnotationType is used as type with which the annotations in the relationAnnotation field of the request body are attached to relations. Is also used to read out the annotation in said format when extracting network
- relationAnnotation is a dictionary of &quot;relation-symbol&quot;: &quot;annotation&quot; - pairs where realation-symbol must match one of the relation symbols in the network (see field relationSymbols in FilterOptions); the annotation is added to the relation under the name defined in relationAnnotationName using the type in relationAnnotationType
 | 
 **user** | **str**| The user which requests the creation | 
 **uuid** | [**str**](.md)| The UUID of the parent network to derive a new network from | 
 **derive** | **bool**| Flag whether to derive a new network and add annotation to it (true) or add annotation to existing network without deriving subnetwork (false) | [optional] [default to true]

### Return type

[**NetworkInventoryItem**](NetworkInventoryItem.md)

### Authorization

[network_auth](../README.md#network_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = pysbml4j.NetworksApi()
user = 'user_example' # str | The user which requests the creation
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The UUID of the network that the myDrug Data should be added to. A copy will be created.
my_drug_url = 'my_drug_url_example' # str | A base url of a MyDrug Database including the port number

try:
    # Provide a URL to a MyDrug Neo4j Database and add Drug nodes and Drug-targets->Gene Relationships to a network
    api_response = api_instance.add_my_drug_relations(user, uuid, my_drug_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->add_my_drug_relations: %s\n" % e)
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

# **copy_network**
> NetworkInventoryItem copy_network(user, uuid)

Create a copy of the network with uuid UUID

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
api_instance = pysbml4j.NetworksApi(pysbml4j.ApiClient(configuration))
user = 'user_example' # str | The user which requests the creation
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The UUID of the parent network to be copied

try:
    # Create a copy of the network with uuid UUID
    api_response = api_instance.copy_network(user, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->copy_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user which requests the creation | 
 **uuid** | [**str**](.md)| The UUID of the parent network to be copied | 

### Return type

[**NetworkInventoryItem**](NetworkInventoryItem.md)

### Authorization

[network_auth](../README.md#network_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network**
> delete_network(user, uuid)

Request the deletion of a network

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
api_instance = pysbml4j.NetworksApi(pysbml4j.ApiClient(configuration))
user = 'user_example' # str | The user which requests deletion of their network
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The UUID of the network to delete

try:
    # Request the deletion of a network
    api_instance.delete_network(user, uuid)
except ApiException as e:
    print("Exception when calling NetworksApi->delete_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user which requests deletion of their network | 
 **uuid** | [**str**](.md)| The UUID of the network to delete | 

### Return type

void (empty response body)

### Authorization

[network_auth](../README.md#network_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_network**
> NetworkInventoryItem filter_network(body, user, uuid)

Filter a network according to the request body options. Results in the creation of a new network entity, keeping the entity with UUID unchanged.

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
api_instance = pysbml4j.NetworksApi(pysbml4j.ApiClient(configuration))
body = pysbml4j.FilterOptions() # FilterOptions | The filterOptions to be used in the step upon creation.

- NodeSymbols: Only nodes listed here can be part of the network (and if they match given nodeTypes)
 
- NodeTypes: Only nodes having one of the listed nodesTypes here can be part of the network (and if they are contained in NodeSymbols)
 
- RelationSymbols: Only relations listed here can be part of the network (and if they match given relationTypes)
 
- RelationTypes: Only edges having one of the listed relationTypes here can be part of the network

  

user = 'user_example' # str | The user which requests the creation
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The UUID of the parent network to derive a new network from

try:
    # Filter a network according to the request body options. Results in the creation of a new network entity, keeping the entity with UUID unchanged.
    api_response = api_instance.filter_network(body, user, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->filter_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilterOptions**](FilterOptions.md)| The filterOptions to be used in the step upon creation.

- NodeSymbols: Only nodes listed here can be part of the network (and if they match given nodeTypes)
 
- NodeTypes: Only nodes having one of the listed nodesTypes here can be part of the network (and if they are contained in NodeSymbols)
 
- RelationSymbols: Only relations listed here can be part of the network (and if they match given relationTypes)
 
- RelationTypes: Only edges having one of the listed relationTypes here can be part of the network

  
 | 
 **user** | **str**| The user which requests the creation | 
 **uuid** | [**str**](.md)| The UUID of the parent network to derive a new network from | 

### Return type

[**NetworkInventoryItem**](NetworkInventoryItem.md)

### Authorization

[network_auth](../README.md#network_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_context**
> str get_context(user, uuid, genes, min_size=min_size, max_size=max_size, terminate_at_drug=terminate_at_drug, direction=direction, directed=directed)

Get network context of one or multiple genes in the network with uuid {UUID}

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
api_instance = pysbml4j.NetworksApi(pysbml4j.ApiClient(configuration))
user = 'user_example' # str | 
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The UUID of the network that serves as a basis for this context
genes = 'genes_example' # str | 
min_size = 1 # int | The minimum depth of the context search (optional) (default to 1)
max_size = 3 # int | The maximum depth of the context search (optional) (default to 3)
terminate_at_drug = false # bool | allows to restrict the context search to only show paths that end in a drug node (MyDrug annotations are required for this) (optional) (default to false)
direction = 'both' # str | The direction of the context expansion (upstream, downstream, both) (optional) (default to both)
directed = false # bool | Denotes whether the return network graph is directed (optional) (default to false)

try:
    # Get network context of one or multiple genes in the network with uuid {UUID}
    api_response = api_instance.get_context(user, uuid, genes, min_size=min_size, max_size=max_size, terminate_at_drug=terminate_at_drug, direction=direction, directed=directed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->get_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**|  | 
 **uuid** | [**str**](.md)| The UUID of the network that serves as a basis for this context | 
 **genes** | **str**|  | 
 **min_size** | **int**| The minimum depth of the context search | [optional] [default to 1]
 **max_size** | **int**| The maximum depth of the context search | [optional] [default to 3]
 **terminate_at_drug** | **bool**| allows to restrict the context search to only show paths that end in a drug node (MyDrug annotations are required for this) | [optional] [default to false]
 **direction** | **str**| The direction of the context expansion (upstream, downstream, both) | [optional] [default to both]
 **directed** | **bool**| Denotes whether the return network graph is directed | [optional] [default to false]

### Return type

**str**

### Authorization

[network_auth](../README.md#network_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network**
> str get_network(user, uuid, directed=directed)

Retrieve the contents of a network

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
api_instance = pysbml4j.NetworksApi(pysbml4j.ApiClient(configuration))
user = 'user_example' # str | The user which requests the creation
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The UUID of the network to get
directed = false # bool | Boolean flag wether the resulting network-graph should be directed  (optional) (default to false)

try:
    # Retrieve the contents of a network
    api_response = api_instance.get_network(user, uuid, directed=directed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->get_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user which requests the creation | 
 **uuid** | [**str**](.md)| The UUID of the network to get | 
 **directed** | **bool**| Boolean flag wether the resulting network-graph should be directed  | [optional] [default to false]

### Return type

**str**

### Authorization

[network_auth](../README.md#network_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_options**
> NetworkOptions get_network_options(user, uuid)

Get available options for network

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
api_instance = pysbml4j.NetworksApi(pysbml4j.ApiClient(configuration))
user = 'user_example' # str | 
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The network UUID for which the networkOptions are to be fetched

try:
    # Get available options for network
    api_response = api_instance.get_network_options(user, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->get_network_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**|  | 
 **uuid** | [**str**](.md)| The network UUID for which the networkOptions are to be fetched | 

### Return type

[**NetworkOptions**](NetworkOptions.md)

### Authorization

[network_auth](../README.md#network_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_networks**
> list[NetworkInventoryItem] list_all_networks(user)

List available networks

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
api_instance = pysbml4j.NetworksApi(pysbml4j.ApiClient(configuration))
user = 'user_example' # str | The user which requests listing of their networks

try:
    # List available networks
    api_response = api_instance.list_all_networks(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->list_all_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user which requests listing of their networks | 

### Return type

[**list[NetworkInventoryItem]**](NetworkInventoryItem.md)

### Authorization

[network_auth](../README.md#network_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_context**
> NetworkInventoryItem post_context(body, user, uuid, min_size=min_size, max_size=max_size, terminate_at_drug=terminate_at_drug, direction=direction)

Create network context of one or multiple genes in the network with uuid {UUID}

### Example
```python
from __future__ import print_function
import time
import pysbml4j
from pysbml4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pysbml4j.NetworksApi()
body = pysbml4j.NodeList() # NodeList | The genes for which the context should be generated

user = 'user_example' # str | 
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The UUID of the network that serves as a basis for this context
min_size = 1 # int | The minimum depth of the context search (optional) (default to 1)
max_size = 3 # int | The maximum depth of the context search (optional) (default to 3)
terminate_at_drug = false # bool | allows to restrict the context search to only show paths that end in a drug node (MyDrug annotations are required for this) (optional) (default to false)
direction = 'both' # str | The direction of the context expansion (upstream, downstream, both) (optional) (default to both)

try:
    # Create network context of one or multiple genes in the network with uuid {UUID}
    api_response = api_instance.post_context(body, user, uuid, min_size=min_size, max_size=max_size, terminate_at_drug=terminate_at_drug, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->post_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeList**](NodeList.md)| The genes for which the context should be generated
 | 
 **user** | **str**|  | 
 **uuid** | [**str**](.md)| The UUID of the network that serves as a basis for this context | 
 **min_size** | **int**| The minimum depth of the context search | [optional] [default to 1]
 **max_size** | **int**| The maximum depth of the context search | [optional] [default to 3]
 **terminate_at_drug** | **bool**| allows to restrict the context search to only show paths that end in a drug node (MyDrug annotations are required for this) | [optional] [default to false]
 **direction** | **str**| The direction of the context expansion (upstream, downstream, both) | [optional] [default to both]

### Return type

[**NetworkInventoryItem**](NetworkInventoryItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

